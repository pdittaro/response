#!/usr/bin/env python3
import socket, threading
from time import sleep
from subprocess import Popen, PIPE

SOCKET_FILE_NAME = "/tmp/build-process.socket"
BUFFER_SIZE = 1024

def foo(progress_callback):
  cmd = "sleep 2m && echo Done" # Replace with build script

  with Popen(cmd, shell=True) as p:

    task_running = True
    while task_running:
      sleep(1)
      try:
        if p.poll() is None:
          progress_callback("Not Done")
        else:
          progress_callback("Done")
          task_running = False
      except Exception as e:
        print(e)


def progress_status(data):
  try:
    _socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    _socket.connect(SOCKET_FILE_NAME) 
    sent = _socket.sendall(str.encode(data))
    if sent == 0:
      raise RuntimeError("socket connection broken")
  except Exception as e:
    print(e)
    pass


def main():
  task = threading.Thread(name='foo', target=foo, args=(progress_status,))
  task.start()
  print("Build process started.")
  task.join()
  print("Build process complete or failed.")

if __name__ == "__main__":
  main()