Results of timing user/status functions:
(the SQLite3 code is the Assignment 03 answer because my Assignment 03 has not been completed yet)

Load user database from CSV file - SQLite3 - 39.03129089999999 seconds
Load user database from CSV file - MongoDB - 10.713283500000003 seconds

Load status database from CSV file - SQLite3 - 4318.1628243000005 seconds
Load status database from CSV file - Mongo DB - 119.2392716 seconds

Add a user - SQLite3 - 0.010986499999489752 seconds
Add a user - MongoDB - 0.0002926999999885993 seconds

Add a status - SQLite3 - 0.00037650000012945384 seconds
Add a status - MongoDB - 0.0006486000000052172 seconds

Update user - SQLite3 - 0.010388800000328047 seconds
Update user - MongoDB - 0.0006914999999878546 seconds

Update status - SQLite3 - 0.049130800000057206 seconds
Update status - MongoDB - 0.0006496999999967557 seconds

Search user - SQLite3 - 0.049340399999891815 seconds
Search user - MongoDB - 0.0297655999999904 seconds

Search status - SQLite3 - 0.03127339999991818 seconds
Search status - MongoDB - 0.030038100000012946 seconds

Delete user - SQLite3 - 0.019639899999674526 seconds
Delete user - MongoDB - 0.0006596999999999298 seconds

Delete status - SQLite3 - 0.010629200000039418 seconds
Delete status - MongoDB - 0.0006484000000170909 seconds

To test the performance of the SQLite3 and MongoDB code, I used the timeit module to time each user/status function. For most of the functions I timed one repetition because they can only run completely once with a given input. For instance, a certain user can only be added and deleted once. I did run 100 repetitions of the search user/status functions because they can be repeated. 

I found the MongoDB code was faster than the SQLite3 code for almost every function except the add_status() function. This is interesting because when the code loads status updates from the csv file, the MongoDB code loads the file about 4,199 seconds faster.  To investigate this further, I used cProfile to look at the load_status_updates() functions for both databases. I am not sure what most of the information from the cProfile report means, but I did notice that peewee is doing a lot more work than the MongoClient. Other processes are happening when the MongoDB code is loading data from a file. For example, topology, pool, and cursor. I am not sure what those are or if they are related to MongoDB.

Both load_status_updates() functions call the add_status() function in user_status.py file, so each is adding one row of status update information at a time. Adding one row at a time to a database does take a long time. If I am understanding correctly and peewee is doing a lot of behind the scenes work, then that extra work would add up after loading 200,000 status updates.  Besides using different databases, the other difference between the twp load_status_updates() functions is that the SQLite3 code does not use a csv reader and the MongoDB code does. I am not sure what lines in the cProfile reports show the csv reader and the stripping/splitting of the raw status update data, but it may be that the csv reader is faster than handling the formating of the csv file within the load_status_updates() function.

Based on the results of the timings and profiling, and my experience creating and using each database my recommendation is to implement MongoDB. MongoDB was faster for almost every piece of functionality, especially when adding data from a file to the database. It was also a lot easier for me to implement and use. It was simpler to set up the tables for MongoDB and connect the database to my exisiting code. For the SQLite3 database, I struggled with connecting the database to my existing code and understanding how the foreign keys work. Relating data in MongoDB is not as complex as SQLite3 and its foreign keys. With that said, if a lot of functionality with relational data is needed with the implementation of the database then SQLite3 would be a better choice. 

One way I could potentially improve the performance of each database code is to add the user and status data in batches instead of by individual rows. I implemented this functionality in assignment 04 for the SQLite3 database and that made loading the data files significantly faster. For example, timing load_users() and load_status_updates() on assignment 04 resulted in 28.226141500000004 seconds for loading the user data and 2937.2261466 seconds for loading the status data. This is about 11 and 1,381 seconds faster, respectively, than the assignment 03 code. Still not as fast as the MongoDB code, but it is an improvement.




