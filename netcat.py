#!/usr/bin/python3

import subprocess, socket

def netcat(hostname, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((hostname, port))
    s.listen(5)
    while True:
        c, addr = s.accept()
        c.send(core_temp())
        c.close()

def core_temp():
    return subprocess.check_output('sensors | grep "Core 0:" | cut -d"+" -f2 | cut -c 1-4', shell=True)
    #.strip()
    #.decode('ascii')
