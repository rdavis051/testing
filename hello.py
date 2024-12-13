# test of python
import os

"""
This is just a simple python program that print "Hello World"
followed by the user name  and home directory.
"""

username = os.environ['USER']
home_dir = os.environ['HOME']

print("Hello World")
print(f'{username}  home directory is: {home_dir}')
