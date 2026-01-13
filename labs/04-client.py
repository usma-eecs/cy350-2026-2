import socket

HOST = "127.0.0.1"
PORT = 8000


def main() -> None:

    # see https://docs.python.org/3/library/socket.html
    # Example -> Echo client program

    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # TODO: connect to the server
    sock.connect((HOST, PORT))

    # ask for user input in a loop
    while True:
        message = input("> ")
        if message == "exit":
            break

        # TODO: encode user input into bytes

        # TODO: send the bytes to the server

        # TODO: receive the response from the server

        # TODO: decode the response into a string

        # TODO: print the response
        print(f"Not Server Response: {message}")

    # TODO: close the connection to the server


if __name__ == "__main__":
    main()
