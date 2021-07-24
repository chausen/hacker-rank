#!/bin/python3

import math
import os
import random
import re
import sys

n,a = input(),sorted(map(int, input().split()))
print(min(abs(x-y) for x,y in zip(a,a[1:])))
