import os
import sys


def txt_importer(path_file):
    if not os.path.exists(path_file):
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
        return
    if not path_file.endswith('.txt'):
        sys.stderr.write("Formato inválido\n")
        return
    with open(path_file, 'r') as file:
        lines = file.read().split("\n")
    return lines
