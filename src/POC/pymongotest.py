# Doodle PoC Pythin - MongoDB
# Usage from command line:
# python pymongotest.py findall
# python pymongotest.py add name width length height

import pymongo
import sys


def dbinfo(collection):
    # Basic db connection
    client = pymongo.MongoClient("mongodb://192.168.1.125:27017/")
    db = client["doodletestDB"]
    col = db[collection]
    return col


def add(name, width, length, height):
    # Create a new document
    col = dbinfo("requirement")
    requirement = {"name": name, "width": width, "length": length, "height": height}
    x = col.insert_one(requirement)
    print(x)


def findall():
    # Print all documents
    col = dbinfo("requirement")

    for x in col.find():
        print(x)


def main(args):
    # Command line arguments
    if args[1] == "add":
        add(*args[2:])
    if args[1] == "findall":
        findall()


main(sys.argv)

