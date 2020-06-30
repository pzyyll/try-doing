import os

CUR_PATH = os.path.dirname(__file__)

def ogpath(filename):
    curdir = os.path.join(CUR_PATH, filename)
    print('@ogpath full path, ', curdir)
    return curdir