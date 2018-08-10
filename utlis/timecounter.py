from time import time, clock, perf_counter


def timecounter(f):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = f(*args, **kwargs)
        time_used = time() - start_time
        print("time用时 %.4f s" % time_used)
        return result
    return wrapper


def clockCounter(f):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result  = f(*args, **kwargs)
        time_used = perf_counter() - start_time
        print("clock用时 %.4f s" % time_used)
        return result

    return wrapper

