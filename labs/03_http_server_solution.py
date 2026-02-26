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
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # TODO bind the socket
            HOST = self.server_ip
            PORT = self.server_port
            self.sock.bind((HOST, PORT))

            # TODO start listening
            self.sock.listen(1)

            self.listening = True
            print(f"Listening on {self.server_ip}:{self.server_port}")

        except Exception as e:
            print(f"Error setting up socket: {e}")
            self.listening = False

    def acceptConnection(self) -> None:

        print('Ready to accept a connection...')

        # TODO accept a connection
        conn, addr = self.sock.accept()
        print(f'Accepted connection from {addr}')

        self.conn = conn

        # TODO store the request data somewhere
        received = b''
        data = b''

        # TODO in a loop, receive data until the full request is obtained
        while not data.endswith(b'\r\n\r\n'):
            # TODO use the connection to receive data
            data = conn.recv(1024)
            # TODO append the received data somewhere
            received += data

        print(f'Received data: {len(received)} bytes')

        receivedStr = received.decode()

        print(f'======= REQUEST =======\n{receivedStr}\n=======================')

        # TODO once the request is received, parse it
        method, resource = self.parse_request(receivedStr)

        print(f'Method: {method}, Resource: {resource}')

        # TODO build the response using build_http_response()
        response = self.build_http_response(method, resource)

        print(f'======= RESPONSE =======\n{response}\n=======================')

        # TODO send the response using send_response()
        # print(...)
        self.send_response(response)

        # TODO close the connection
        self.conn.close()
        self.conn = None

        print(f'Connection closed: {addr}')
        # print(...)

    def parse_request(self, request: str) -> tuple[str | None, str | None]:
        method = None
        resource = None

        # TODO parse the request string and extract the method and resource
        items = request.split()
        method = items[0]
        resource = items[1]

        return method, resource

    def build_http_response(self, method: str, resource: str) -> str:
        responseCode = 500
        responseMsg = "Internal Server Error"
        responseBody = "Sadness ensues. Something did not go as planned. All hope is lost."

        # TODO parse the resource and create the corresponding message
        # TODO 200 OK
        # TODO 404 Not Found
        # TODO 400 Bad Request

        if method != "GET":
            responseCode = 400
            responseMsg = "BAD REQUEST"
            responseBody = "Only GET method is supported."

        elif not resource in self.resources:
            responseCode = 404
            responseMsg = "NOT FOUND"

        else:
            responseCode = 200
            responseMsg = "OK"
            responseBody = self.resources[resource]

        responseBody += '\r\n'
        header = f'Content-Length: {len(responseBody)}'

        http_response = f'HTTP/1.1 {responseCode} {responseMsg}\r\n{header}\r\n\r\n{responseBody}'
        return http_response

    def send_response(self, response) -> None:
        # TODO send the response through the connection
        bytes = response.encode()
        self.conn.sendall(bytes)
        print(f'Sent: {len(bytes)} bytes')

    def close_connection(self) -> None:
        if self.conn:
            self.conn.close()
        self.sock.close()
        print("Listening socket closed.")


if __name__ == "__main__":
    server = TCPServer()
    try:
        while server.listening:
            server.acceptConnection()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down server...")
    finally:
        server.listening = False
        server.close_connection()
