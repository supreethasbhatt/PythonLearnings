**Iterators**
1. Iterator vs Iterable are different --> 
    **Iterators**: an abject that can be iterated upon. i.e which can run for loop on. On object that returns data one lement at a time when next() is called on. here next() is called
    **Iterable** : An object that returns an itrator when iter() is called on it.
    "hello" ---> iterable
    iter("hello") --> returns an iterator

    for next() functio to be called, itr() should be called.

2. iter(): returns the iterator
3. next(): iters over the iterator after iter() is called on it

**Generators**:
1. They are iteraots.
2. "yield" keyword --------> Returns to a generator object.
3. Generator functions  ------> It returns more than once. 

------------------------
def count_upto(max):
    count=1
    while count <= max:
        yield count -----------> returns value of count and paus until next is called on the function again
        count = count+1
-------------------------------------------
Let's say you have 100 million domains in your MySQL table, and you would like to update Alexa rank for each domain.

First thing you need is to select your domain names from the database.

Let's say your table name is domains and column name is domain.

If you use SELECT domain FROM domains it's going to return 100 million rows which is going to consume lot of memory. So your server might crash.

So you decided to run the program in batches. Let's say our batch size is 1000.

In our first batch we will query the first 1000 rows, check Alexa rank for each domain and update the database row.

In our second batch we will work on the next 1000 rows. In our third batch it will be from 2001 to 3000 and so on.

Now we need a generator function which generates our batches.

Here is our generator function:


def ResultGenerator(cursor, batchsize=1000):
    while True:
        results = cursor.fetchmany(batchsize)
        if not results:
            break
        for result in results:
            yield result

db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="domains")
cursor = db.cursor()
cursor.execute("SELECT domain FROM domains")
for result in ResultGenerator(cursor):
    doSomethingWith(result)
db.close()

4. Memory ussage with numbers - 
    When dealing with bigvolume of data it is better to use yield than return to saveon the memory being consumed.