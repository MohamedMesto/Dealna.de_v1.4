import os

# DEBUG is True if DEVELOPMENT=1, False otherwise
DEBUG = os.environ.get('DEVELOPMENT', '0') in ['1', 'True', 'true']

print("DEBUG 999999999999999999 =", DEBUG)
