# logging_example.py

import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def divide(a, b):
    logging.debug(f"Dividing {a} by {b}")
    try:
        result = a / b
    except ZeroDivisionError as e:
        logging.error(f"Error occurred: {e}")
        return None
    logging.info(f"Division result: {result}")
    return result

divide(10, 0)
