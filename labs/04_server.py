#!/usr/bin/env python3
import socket
import random
import argparse
import logging
import time

# Client types
D1 = 0xD1  # Stage 1
D2 = 0xD2  # Stage 2
D3 = 0xD3  # Stage 3

# Server types
A1 = 0xA1
A2 = 0xA2
A3 = 0xA3

def build_packet(ptype, seq, payload=b""):
    return bytes([ptype, seq]) + payload

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=5005)
    parser.add_argument("--loss", type=float, default=0.3)
    parser.add_argument("--target", type=int, default=20)
    parser.add_argument("--max-delay", type=float, default=0.2, help="max delay in seconds for simulating network latency")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO,
                        format="%(asctime)s %(levelname)s: %(message)s")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((args.host, args.port))

    logging.info("Server listening on %s:%d", args.host, args.port)

    # Per-client state for Stage 3
    client_state = {}  # addr -> {expected_seq, count}

    while True:
        data, addr = sock.recvfrom(4096)

        if len(data) < 2:
            continue

        # Simulated loss
        if random.random() < args.loss:
            logging.debug("Dropped packet from %s", addr)
            continue

        # Simulated delay
        delay = random.random() * args.max_delay
        time.sleep(delay)

        ptype = data[0]
        seq = data[1]
        payload = data[2:]

        # -----------------------
        # Stage 1: Simple Echo
        # -----------------------
        if ptype == D1:
            logging.debug("Stage 1 packet from %s", addr)
            response = build_packet(A1, seq, payload.upper())
            sock.sendto(response, addr)

        # -----------------------
        # Stage 2: Echo with loss (students retransmit)
        # -----------------------
        elif ptype == D2:
            logging.debug("Stage 2 packet from %s", addr)
            response = build_packet(A2, seq)
            sock.sendto(response, addr)

        # -----------------------
        # Stage 3: Stop-and-Wait
        # -----------------------
        elif ptype == D3:
            state = client_state.get(addr)
            if state is None:
                state = {"expected_seq": 0, "count": 0}
                client_state[addr] = state

            expected = state["expected_seq"]

            if seq == expected:
                # Valid in-order packet
                ack = build_packet(A3, seq)
                sock.sendto(ack, addr)

                state["expected_seq"] ^= 1
                state["count"] += 1

                logging.debug("Accepted seq %d from %s (count=%d)",
                              seq, addr, state["count"])

                if state["count"] >= args.target:
                    flag_msg = b"FLAG{STOP_AND_WAIT_SUCCESS}"
                    sock.sendto(build_packet(A3, seq, flag_msg), addr)
                    state["count"] = 0  # reset for replay

            else:
                # Duplicate — resend last ACK
                last_ack_seq = 1 - expected
                ack = build_packet(A3, last_ack_seq)
                sock.sendto(ack, addr)

        else:
            logging.debug("Unknown packet type from %s", addr)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Server interrupted. Exiting.")
