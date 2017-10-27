#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import hashlib
from uuid import getnode as get_mac
import time
import os


def get_seed():
    return str(get_mac()) + str(time.time()) + str(os.getpid())


def get_entropy(file, limit):
    return file.read(limit).hex()


def get_hash(seed, entropy):
    return hashlib.sha256((seed + entropy).encode('utf-8')).hexdigest()


def dev_random(file, start, limit):
    seed = get_seed()
    while True:
        entropy = get_entropy(file, limit)

        # Wait for more entropy
        if entropy is '':
            time.sleep(1)
        else:
            hash = get_hash(seed, entropy)
            sys.stdout.write(hash)
            start = start + limit

            # new seed
            seed = hash


def main():
    # The entropy input should ideally be
    file = sys.stdin.buffer
    start = 0
    limit = 56
    dev_random(file, start, limit)


if __name__ == '__main__':
    main()
