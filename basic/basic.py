'''
Author: JSH
Date: 2020-09-01 10:56:49
LastEditTime: 2021-02-24 18:03:49
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \py\basic\basic.py
'''

def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError: # not iterable
        return False

print(isiterable('a string'))

print(isiterable([1,2,3]))

print(isiterable(5))
