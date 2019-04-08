#!/usr/bin/env python3

import functools
strList = ["I never thought this would happen. ", "Me being stuck with another sentence? ", "This is nonsense."]
strResult = functools.reduce(lambda x, y: x+y, strList)
print(strResult)
