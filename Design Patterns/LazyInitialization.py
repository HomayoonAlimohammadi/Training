def later(p):
    def covered(*args, **kwargs):
        if hasattr(covered, '_cached_val'):
            return covered._cached_val
        outcome = p(*args, **kwargs)
        covered._cached_val = outcome
        return outcome
    return covered
#driver code


@later
def costly():
    print ("Processing costly function:")
    import time
    time.sleep(2)
    return 177
print (costly())
print (costly())
print (costly())