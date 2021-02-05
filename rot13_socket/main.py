import os
import socket
import logging
from rot13 import rot13


def main():
    logging.basicConfig(format='%(asctime)s %(message)s',
                        filename=os.path.join(os.path.dirname(__file__), \
                        'info.log'), level=logging.INFO)
    hostname = socket.gethostbyname(socket.gethostname())
    port = 9998
    logging.info(f'Listening on {hostname} port {port}')   
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ss:
        ss.bind((hostname, port))
        ss.listen(10)
        conn, addr = ss.accept()
        with conn:
            logging.info(f'Connected. IP: {addr}')
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                logging.info(f'Received: {data.decode()}')
                conn.send(rot13(data.decode()).encode())


if __name__ == '__main__':
    main() 
