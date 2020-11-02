import gzip
from math import sqrt
from itertools import count, islice
import os
import glob

import re
from functools import lru_cache

# Constants Section
IS_UNZIP            = False

CURRENT_PATH        = os.getcwd()
ZIPPED_FILE_PATH    = os.path.join(CURRENT_PATH, 'ZIP')
EXTRACTED_FILE_PATH = os.path.join(CURRENT_PATH, 'XML')

# Code Section
# Extract Zipped files
if IS_UNZIP:
    for zipped_file_path in glob.glob(f'{ZIPPED_FILE_PATH}/*'):
         zipped_file_name_no_extension   = os.path.splitext(os.path.basename(zipped_file_path))[0]
         extracted_file_path             = os.path.join(EXTRACTED_FILE_PATH, zipped_file_name_no_extension)
         if os.path.isfile(extracted_file_path):
             continue
         with gzip.open(zipped_file_path, mode="rb") as f_in:
             with open(extracted_file_path, mode='wb') as f_out:
                 f_out.write(f_in.read())

@lru_cache(maxsize=None)
def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))

starts_ends_with_same_digit = lambda s : s[0] == s[-1]

# Find maximal valid product id
max_n = float('-inf')
for extracted_file_path in glob.glob(f'{EXTRACTED_FILE_PATH}/*'):
    with open(extracted_file_path, mode="r") as f:
        matches = re.findall('p/(\d+)', f.read())
        if matches:
            product_ids             = list(map(str,                             matches))
            filtered_product_ids    = list(filter(starts_ends_with_same_digit,  product_ids))
            filtered_product_ids    = list(map(int,                             filtered_product_ids))
            filtered_product_ids.sort(reverse=True)
            for pid in filtered_product_ids:
                if is_prime(pid):
                    if max_n < pid:
                        max_n = pid
                        print(f'Maximal N : | {max_n} | = {len(str(max_n))} @ {os.path.splitext(os.path.basename(extracted_file_path))[0]}')
                    break
