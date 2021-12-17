import os
import lib.unpacker as unp
from rubymarshal.reader import loads, load
from rubymarshal.writer import writes, write

# with open("another_examples/Actors.rvdata2", 'rb') as file:
#    test = load(file)
# with open("repacked/test.rvdata2", 'wb') as file:
#    write(file,test)

for i in os.listdir("another_examples"):
    with open("another_examples/" + i, 'rb') as file:
        test = load(file)
    with open("repacked/" + i, 'wb') as file:
        write(file, test)
# CommontEvents )0)
