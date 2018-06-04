#!/usr/local/bin/python2

from netmiko import ConnectHandler
from colors import *
from ale_devices import all_devices
from ale_commands import all_commands

for a_device in all_devices:
  try:
    net_connect = ConnectHandler(**a_device)
    print ("\n\n{0}{1} Device {2} {3}{4}"
      .format(SUCCESS, ">"*10, a_device["ip"], "<"*10, NORMAL))
    for a_command in all_commands:
      output = net_connect.send_command(a_command["command"])
      print ("\nCommand: {0}{1}{2} \n"
        .format(INFO, a_command["command"], NORMAL))
      try:
        a_command["search"]
        for single_line in output.splitlines():
          if a_command["search"] in single_line:
            print (single_line)
      except:
        print (output)
      print ("\n")
    net_connect.disconnect()
  except:
    print ("\n\n{0}{1} Device {2} {3}{4}"
      .format(ERROR, ">"*10, a_device["ip"], "<"*10, NORMAL))
