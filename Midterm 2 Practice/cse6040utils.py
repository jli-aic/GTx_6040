#!/usr/bin/env python3

#======================================================================
# Utility routines to download external datasets
#======================================================================

import requests
import os
import hashlib
import io

def download_one(filename, local_base, url_base, checksum=None):
    local_file = "{}{}".format(local_base, filename)
    if not os.path.exists(local_file):
        url = "{}{}".format(url_base, filename)
        print("Downloading: {} ...".format(url))
        r = requests.get(url)
        with open(local_file, 'wb') as f:
            f.write(r.content)
            
    if checksum is not None:
        with io.open(local_file, 'rb') as f:
            body = f.read()
            body_checksum = hashlib.md5(body).hexdigest()
            assert body_checksum == checksum, \
                "Downloaded file '{}' has incorrect checksum: '{}' instead of '{}'".format(local_file,
                                                                                           body_checksum,
                                                                                           checksum)
    print("'{}' is ready!".format(filename))

def on_vocareum():
    return os.path.exists('.voc')

if on_vocareum():
    URL_BASE = "https://cse6040.gatech.edu/datasets/"
    LOCAL_BASE = "../resource/asnlib/publicdata/"
else:
    URL_BASE = "https://github.com/cse6040/labs-fa17/raw/master/datasets/"
    LOCAL_BASE = ""

def download_all(datasets, local_base=LOCAL_BASE, local_suffix="", url_base=URL_BASE, url_suffix=""):
    local_paths = {}
    local_dir = "{}{}".format(local_base, local_suffix)
    url_dir = "{}{}".format(url_base, url_suffix)
    os.makedirs(local_dir, exist_ok=True)
    for filename, checksum in datasets.items():
        download_one(filename, local_base=local_dir, url_base=url_dir, checksum=checksum)
        local_paths[filename] = "{}{}".format(local_dir, filename)
    return local_paths
    
#======================================================================
# Tibble support
#======================================================================

from pandas import DataFrame

def canonicalize_tibble (X: DataFrame):
    """Returns a tibble in _canonical order_."""
    # Enforce Property 1:
    var_names = sorted (X.columns)
    Y = X[var_names].copy ()

    # Enforce Property 2:
    Y.sort_values (by=var_names, inplace=True)

    # Enforce Property 3:
    Y.set_index ([list (range (0, len (Y)))], inplace=True)

    return Y

def tibbles_are_equivalent (A: DataFrame, B: DataFrame):
    """Given two tidy tables ('tibbles'), returns True iff they are
    equivalent.
    """
    A_canonical = canonicalize_tibble (A)
    B_canonical = canonicalize_tibble (B)
    cmp = A_canonical.eq (B_canonical)
    return cmp.all ().all ()

# eof
