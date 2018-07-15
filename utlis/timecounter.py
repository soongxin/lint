from time import time


def timecounter(f):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = f(*args, **kwargs)
        time_used = time() - start_time
        print("用时 %.4f s" % time_used)
        return result
    return wrapper