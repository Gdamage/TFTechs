from os import path
import sys

def resource_path(relative_path):
    """Returns the absolute file path given a relative one"""
    base_path = getattr(sys, '_MEIPASS', path.dirname(path.abspath(__file__)))
    return path.join(base_path, relative_path)

def string_starts_with(string, substring) -> bool:
    if(string.find(substring) == 0):
        return True
    return False