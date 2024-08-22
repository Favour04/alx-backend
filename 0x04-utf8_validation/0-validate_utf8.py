#!/usr/bin/python3
"""
validate if givin character is utf-8
complying
"""


def validUTF8(data):
    """
        Simple implementation
    """
    real_len = len(data)
    i = 0
    for num in range(real_len):
        if data[i] <= 127:
            data.pop(i)
        else:
            i = i + 1

    if len(data) > 0:
        return False
    else:
        return True
        
