#!/bin/python

import os
import sys
import time
import pyfiglet

def bersih():
       os.system("clear")

def menu():
       bersih()
       a = pyfiglet.figlet_format('SCP - 097')
       print (a)
       print("----------------------------------------------")
       print(" ➤Author   : AunSoePy")
       print(" ➤Github   : https://github.com/Aungsoepy37686")
       print(" ➤Facebook : Aung SoePy")
       print(" ----------------------------------------------")
       print("[ 1 ] Facebook Login")
       print("[ 0 ] Exit")
       print("----------------------------------------------")
       pil = input("Select an option: ")
       if pil =="1":
            os.system("python SCP-097.py")
       elif pil =="3":
            sys.exit()

menu()
            