#!/usr/bin/python3
"""this moule reads a file to stdout"""

def read_file(filename=""):
    """prints the content of a UFT-8 text file"""
    with open(filename, encoding="utf-8") as f
    print(f.read(), end="")
