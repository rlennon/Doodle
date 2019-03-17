##      Starting mongo from command line

1.	Download MongoDB 4.0.6 ->  https://www.mongodb.com/download-center/community
                               mongodb-win32-x86_64-2008plus-ssl-4.0.6-signed.msi

2.	When Installing MongoDB, choose Complete version not custom. You can choose custom if you want a smaller/easier naming convention.

3.	Go into command prompt and cd into MongoDB

"(C:) > Program Files > MongoDB > Server > 4.0 > bin"

4.	Then type "mongod" into the command prompt. An error should appear.

5.	When this happens, just create a folder on your local disk (C drive) called data and another folder in data called db.The path should look like:

"(C:)> data > db"

6.	After you created folders, run the mongod command again and it should be successful.

7.	Open another cmd and type in "mongo".

"C:\Users\Conor Dorrian> mongo"

8.	This will open the mongo shell. From here you can create a database etc.

##      Run MongoDB Anywhere

To run mongod and mongo in any directory, follow the steps provided. 
To Run the mongod and mongo command anywhere instead of always having to go into the folder.

To do this you need to set the environmental variables up. Just type “environmental variables” in the start menu or go to system then advanced settings then environmental variables.

In system variables. Double click “path” and enter a new MongoDB bin path inside path like below. Make sure it points to bin folder.

C:\Program Files\MongoDB\Server\4.0\bin

Then close all terminals and open a new terminal/cmd and type "mongod" to run the server and in a new terminal/cmd type "mongo". Which will take you straight to mongo shell anywhere in the system.

##      Some Mongo simple commands to start off

show dbs 				                             === Shows the database
use firstDatabase		                             === Create a database named firstDatabase  
db.books.insert({“name”:” Game of Thrones book”})    === Collection Name of Books with book names in the collection
show dbs				                             === Shows the database
show collections 			                         === Shows all collections in firstDatabase
db.books.find()			                             === Shows the values in books
