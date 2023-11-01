import os
import requests
from werkzeug.wrappers import request


data_file = '../data/bell.txt'
fp = None


def read_line():
    global fp, data_file
    if not fp:
        fp = open(data_file, 'r', encoding='utf-8')
    line = fp.readline()
    if line is not None:
        line = line.rstrip('\n\r ')
    return line


def bell():
    watson_hots = os.environ.get('WATSON_HOST')
    watson_port = os.environ.get('WATSON_PORT')
    while True:
        line = read_line()
        if line:
            print(f"bell said: {line}")
            # finish the code here
            # use python requests module to invoke Watson's api
        else:
            break


if __name__ == '__main__':
    bell()

