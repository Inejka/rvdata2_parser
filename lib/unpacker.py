from rubymarshal.reader import loads, load
from rubymarshal.classes import RubyObject, registry
from rubymarshal.writer import writes, write
import zlib


def unpack(path):
    with open(path, 'rb') as file:
        print(path)
        contest = load(file)
        #print(contest)
        #for i in contest:
        #    print(i)
        # temp = "asdf"
        # print(content[7])
        # print(zlib.decompress(content[10][2].encode("latin1")).decode("utf-8"))
        # print(content[3][2])
