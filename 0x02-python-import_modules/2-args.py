#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    print(n-1, "argument:")
    for i in range(1 , n):
        print(i,":", sys.argv[i])
