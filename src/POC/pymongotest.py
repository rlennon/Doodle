import pymongo
import sys


def add(name, width, length, height):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["doodletestDB"]
    col = db["requirement"]
    requirement = {"name": name, "width": width, "length": length, "height": height}
    x = col.insert_one(requirement)
    print(x)


def findall():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["doodletestDB"]
    col = db["requirement"]

    for x in col.find():
        print(x)


# add(*sys.argv[1:])
# findall()
def main(args):
    if args[1] == "add":
        add(*args[2:])
    if args[1] == "findall":
        findall()


main(sys.argv)

