import socket
import time


class TCPServer:
    def __init__(self, server_ip='127.0.0.1', server_port=8080):
        print("Initializing TCP Server...")
        self.server_ip = server_ip
        self.server_port = server_port
        self.listening = False
        self.setup_socket()

        self.resources = {
            "/": "Welcome to the TCP Server!",
            "/hello": "Hello, TCP Client!",
            "/goodbye": "Goodbye from the TCP Server!",
            "/joke": "Why do programmers prefer dark mode? Because light attracts bugs!"
        }

    def setup_socket(self) -> None:
        try:
            print(f"Creating TCP socket")

            # TODO create a TCP listening socket
            # TODO bind the socket
            # TODO start listening

            self.listening = True
            # print(...)

        except Exception as e:
            print(f"Error setting up socket: {e}")
            self.listening = False

        print('NOT IMPLEMENTED')

    def acceptConnection(self) -> None:

        print('Accepting connections...')

        # TODO accept a connection
        # print(...)

        # TODO store the request data somewhere
        # TODO in a loop, receive data until the full request is obtained

        # TODO use the connection to receive data
        # TODO append the received data somewhere

        # print(...)
        # TODO once the request is received, parse it

        # TODO build the response using build_http_response()
        # print(...)
        # TODO send the response using send_response()
        # print(...)
        # TODO close the connection
        # print(...)

    def parse_request(self, request: str) -> tuple[str | None, str | None]:
        method = None
        resource = None

        # TODO parse the request string and extract the method and resource

        return method, resource

    def build_http_response(self, method: str, resource: str) -> str:
        responseCode = 500
        responseMsg = "Internal Server Error"
        responseBody = "Sadness ensues. Something did not go as planned. All hope is lost."

        # TODO parse the resource and create the corresponding message
        # TODO 200 OK
        # TODO 404 Not Found
        # TODO 400 Bad Request

        http_response = None
        return http_response

    def send_response(self, response) -> None:
        print('NOT IMPLEMENTED')
        # TODO send the response through the connection

    def close_connection(self) -> None:
        self.sock.close()
        print("Listening socket closed.")


if __name__ == "__main__":
    server = TCPServer()
    server.listening = True
    try:
        while server.listening:
            server.acceptConnection()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down server...")
        server.listening = False
    finally:
        server.close_connection()
