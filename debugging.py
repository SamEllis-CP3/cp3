import logging

logging.basicConfig(level=logging.DEBUG)

def buggy_function(a , b):
    result = a * b
    logging.debug(f"A: {a} b: {b} result: {result}")
    return result

# We could use assert here
print(buggy_function("2",3)) #expected output 9