import socket
import time

TYPE_DATA = 0xD3  # level 3 DATA
TYPE_ACK = 0xA3  # level 3 ACK
START_TIME = time.time()


def print_with_time(msg: str):
    elapsed = time.time() - START_TIME
    print(f"[{elapsed:7.3f}s] {msg}", flush=True)


def build_packet(seq: int, msg: str, pkt_type: int = TYPE_DATA) -> bytes:
    return bytes([pkt_type, seq]) + msg.encode()


def parse_response(data: bytes):
    if len(data) < 2:
        return None
    pkt_type = data[0]
    seq = data[1]
    payload = data[2:]
    return pkt_type, seq, payload.decode()


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1.0)

    server = ("127.0.0.1", 5005)

    seq = 0

    for i in range(20):
        msg = f"packet {i}"
        pkt = build_packet(seq, msg, TYPE_DATA)
        acked = False

        while not acked:
            sock.sendto(pkt, server)
            print(f"Sent: packet {i}")

            try:
                data, addr = sock.recvfrom(4096)
                if data[0] == TYPE_ACK:
                    ack_seq = data[1]
                    if ack_seq == seq:
                        acked = True
                        print_with_time(f"Received ACK for seq {ack_seq}")
                        seq = (seq + 1) % 2  # toggle between 0 and 1
                    else:
                        print_with_time(
                            f"Received ACK with wrong seq {ack_seq}, expected {seq}")
                        print_with_time(f'Retransmitting packet {i} with seq {seq}')

            except socket.timeout:
                print_with_time(f"Packet {i} was lost. No ACK.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_with_time("Client interrupted. Exiting.")
