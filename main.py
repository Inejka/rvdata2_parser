import os
import lib.unpacker as unp
from rubymarshal.reader import loads, load
from rubymarshal.writer import writes, write

# with open("another_examples/Actors.rvdata2", 'rb') as file:
#    test = load(file)
# with open("repacked/test.rvdata2", 'wb') as file:
#    write(file,test)

for i in os.listdir("examples"):
    # with open("examples/" + i, 'rb') as file:
    unp.unpack("examples/" + i)
# with open("repacked/" + i, 'wb') as file:
#     write(file, test)
# CommontEvents )0)
