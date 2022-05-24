#!/usr/bin/env python3
import socket, os

SOCKET_FILE_NAME = "/tmp/build-process.socket"
BUFFER_SIZE = 1024

def main():
  try:
    os.remove(SOCKET_FILE_NAME)
  except OSError:
    pass

  s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
  s.bind(SOCKET_FILE_NAME)
  s.listen()
  while True:
    conn, _ = s.accept()
    with conn:
      data = conn.recv(BUFFER_SIZE)
      if data:
        print(data)


if __name__ == "__main__":
  main()