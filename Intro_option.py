# OPTIONS 딕셔너리 참조
from options import OPTIONS

def intro_option():
        print("Available options : ")
        for key in OPTIONS:
            print(" - ", key)
        print("\n")
