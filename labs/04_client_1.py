import socket
import time

TYPE_DATA = 0xD1  # level 1 DATA
TYPE_ACK = 0xA1  # level 1 ACK
START_TIME = time.time()


def print_with_time(msg: str):
    elapsed = time.time() - START_TIME
    print(f"[{elapsed:7.3f}s] {msg}", flush=True)


def build_packet(seq: int, msg: str, pkt_type: int = TYPE_DATA) -> bytes:
    return bytes([pkt_type, seq]) + msg.encode()


def get_payload(data: bytes):
    if len(data) < 2:
        return False
    payload = data[2:]
    return payload.decode()


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1.0)

    server = ("127.0.0.1", 5005)

    for i in range(20):
        msg = f"packet {i}"
        pkt = build_packet(i, msg)
        sock.sendto(pkt, server)
        print_with_time(f"Sent: packet {i}")
        try:
            data, addr = sock.recvfrom(4096)
            payload = get_payload(data)
            print_with_time(f"Received: {payload}")
        except socket.timeout:
            print_with_time(f"Packet {i} was lost. No ACK.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_with_time("Client interrupted. Exiting.")
