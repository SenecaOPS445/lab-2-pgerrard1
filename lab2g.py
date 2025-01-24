#!/usr/bin/env python3

#Author:  Patrick Gerrard
#Author ID: pgerrard1
#Date Created: 2024/10/03

import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

# While loop that runs until timer equals 0
while timer != 0:
    print(timer)
    timer -= 1

print("blast off!")