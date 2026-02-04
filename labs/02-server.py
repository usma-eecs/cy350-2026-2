import socket


def main() -> None:
    host = "0.0.0.0"
    port = 8000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(5)
        print(f"Listening on {host}:{port}")
    except Exception as e:
        print(f"Failed to set up server: {e}")
        return

    try:
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Client connected: {addr}")
                while True:
                    data = conn.recv(4096)
                    if not data:
                        break
                    text = data.decode("utf-8")
                    response = text.upper()
                    responseBytes = response.encode("utf-8")
                    conn.sendall(responseBytes)

    # capture keyboard interrupt to gracefully shutdown the server
    except KeyboardInterrupt:
        print("Shutting down server.")
        s.close()


if __name__ == "__main__":
    main()
