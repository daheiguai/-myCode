import http
import os
from http import server

if __name__ == '__main__':
    os.system('python -m RangeHTTPServer 5555 --bind 0.0.0.0')
    server