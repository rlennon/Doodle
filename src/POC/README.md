# Doodle POC - Python MongoDB using Pymongo

This POC is intended to prove that python can successfully connect to a MongoDB and uncover any potential issues. Identifying these issues at this early stage in the project will minimise any development time wasted.

## Objectives

### 1. Run a Mongodb database as a service

Install and run MongoDB as a service

### 2. Create a simple collection with documents

Using Python - install Pymongo
Document fields to include:  ID, Name, Dimensions (width, height, length)

### 3. Read the collection

Test the documents were successfully created.

### 4. Test connection to the database over a network

Test the connection to MongoDB works over a LAN/running on a VM

## Instructions

### MongoDB community can be downloaded from here: https://www.mongodb.com/download-center/community

Use the default settings during installation. MongoDB compass (a program to analyse collections) can also be installed.

Install python pymongo and sys  
Edit pymongotest.py, set the ip address to either local or the ip of the mongodb server if running on another machine.

Usage from command line:  
python pymongotest.py findall  
python pymongotest.py add name width length height

To run Mongodb over a network you will need to set the ip in the mongo.conf file



