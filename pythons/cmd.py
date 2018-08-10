#!/bin/python
import sys
import paramiko

rpi = {"username": "pi",
       "hostname": "172.16.0.141"}
command = " ".join(sys.argv[1:])

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(**rpi)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
