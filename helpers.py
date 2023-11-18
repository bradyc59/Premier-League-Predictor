import os

def make_new_directory(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)