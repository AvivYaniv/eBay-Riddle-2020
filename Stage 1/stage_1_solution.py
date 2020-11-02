import base64
coded_message   = 'aHR0cHM6Ly9ybmQuZWJheS5jby5pbC9yaWRkbGUvbXpmYmFiZXdjZXlxeGFsdXIv'
decoded_message = base64.b64decode(coded_message)
# https://rnd.ebay.co.il/riddle/mzfbabewceyqxalur/
print(decoded_message)