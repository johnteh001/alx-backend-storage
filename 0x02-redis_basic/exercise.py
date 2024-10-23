#!/usr/bin/env python3
"""Task 0"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def call_history(method: Callable) -> Callable:
    """History decorator"""
    key = method.__qualname__
    inp_lk = key + ":inputs"
    ouput_lk = key + ":outputs"
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper"""
        self._redis.rpush(inp_lk, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(ouput_lk, str(result))
        return result
    return wrapper


def count_calls(method: Callable) -> Callable:
    """Returns a callable"""
    key = method.__qualname__
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Cache class"""
    def __init__(self):
        """Initializes and instantiates Redis"""
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Creates a unique key and stores data"""
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None):
        """Get method"""
        k = self._redis.get(key)
        if k and fn:
            if fn == "str":
                return self.get_str(k)
            elif fn == "int":
                return self.get_int(k)
            else:
                return fn(k)
        return k

    def get_str(self, arg: bytes) -> str:
        """Returns string"""
        return arg.decode("utf-8")

    def get_int(self, arg: bytes) -> int:
        """Returns int"""
        return int(self.get_str(arg))

    def replay(self, method: Callable):
        """Display call history"""
        key = method.__qualname__
        inp = key + ":inputs"
        out = key + ":outputs"
        redis = method.__self__._redis
        counter = redis.get(key).decode('utf-8')
        print("{} was called {} times:".format(key, counter))
        input_list = redis.lrange(inp, 0, -1)
        output_list = redis.lrange(out, 0, -1)
        all_obj = list(zip(input_list, output_list))
        for c, d in all_obj:
            attr, res = c.decode("utf-8"), d.decode("utf-8")
            print("{}(*{}) -> {}".format(key, attr, res))
