#!/usr/bin/env python3

def canonicalize_tibble(X):
    # Enforce Property 1:
    var_names = sorted(X.columns)
    Y = X[var_names].copy()

    # Enforce Property 2:
    Y.sort_values(by=var_names, inplace=True)
    
    # Enforce Property 3:
    Y.reset_index(drop=True, inplace=True)
    return Y

def tibbles_are_equivalent(student_soln, B_hash):
    """Given two tidy tables ('tibbles'), returns True iff they are
    equivalent.
    """
    from pandas.util import hash_pandas_object
    return hash_pandas_object(canonicalize_tibble(student_soln)).sum() == B_hash

# eof
