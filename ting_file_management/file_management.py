import os
import sys

def txt_importer(path_file):
    with open(path_file, 'r') as file:
        lines = file.read().split("\n")
    return lines