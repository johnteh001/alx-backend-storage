## Redis Basic
This is the introduction to Redis
Learning objectives:
* Learn how to use redis for basic operations
* Learn how to use redis as a simple cache

### Resources
* [Redis commands](https://redis.io/commands/)
* [Redis python client](https://redis-py.readthedocs.io/en/stable/)
* [How to use Redis with Python](https://realpython.com/python-redis/)
* [Redis crash course tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)

### Tasks
* **Task 0:**  Writing strings to Redis. Creating Cache class with `store` method
* **Task 1: Reading from Redis and recovering original type**
Redis only allows to store string, bytes and numbers (and lists thereof). Whatever you store as single elements, it will be returned as a byte string. Hence if you store "a" as a UTF-8 string, it will be returned as b"a" when retrieved from the server.

In this exercise we will create a `get` method that take a `key` string argument and an optional `Callable` argument named `fn`. This callable will be used to convert the data back to the desired format.

Remember to conserve the original `Redis.get` behavior if the key does not exist.
Also, implement 2 new methods: `get_str` and `get_int` that will automatically parametrize `Cache.get` with the correct conversion function.
* **Task 2: Incrementing values**
Familiarize yourself with the `INCR` command and its python equivalent.
In this task, we will implement a system to count how many times methods of the `Cache` class are called.
Above `Cache` define a `count_calls` decorator that takes a single `method Callable` argument and returns a `Callable`.
As a key, use the qualified name of method using the `__qualname__` dunder method.
Create and return function that increments the count for that key every time the method is called and returns the value returned by the original method.
Remember that the first argument of the wrapped function will be `self` which is the instance itself, which lets you access the Redis instance.
Protip: when defining a decorator it is useful to use functool.wraps to conserve the original function’s name, docstring, etc. Make sure you use it as described here.
Decorate `Cache.store` with `count_calls`.
* **Task 3: Storing lists**
Familiarize yourself with redis commands `RPUSH`, `LPUSH`, `LRANGE`, etc.
In this task, we will define a `call_history` decorator to store the history of inputs and outputs for a particular function.
Everytime the original function will be called, we will add its input parameters to one list in redis, and store its output into another list.
In `call_history`, use the decorated function’s qualified name and append ":inputs" and ":outputs" to create input and output list keys, respectively.
`call_history` has a single parameter named `method` that is a `Callable` and returns a `Callable`.
In the new function that the decorator will return, use `rpush` to append the input arguments. Remember that Redis can only store strings, bytes and numbers. Therefore, we can simply use `str(args)` to normalize. We can ignore potential `kwargs` for now.
Execute the wrapped function to retrieve the output. Store the output using `rpush` in the `"...:outputs"` list, then return the output.
Decorate `Cache.store` with `call_history.`
* **Task 4: Retrieving lists**
In this tasks, we will implement a `replay` function to display the history of calls of a particular function.
