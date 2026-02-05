#!/usr/bin/python3

import re
                
def calc(A,B):
        if not isinstance(A, int) or not isinstance(B, int):
                return -1

        if A < 1 or A > 999:
                return -1

        if B < 1 or B > 999:
                return -1

        return A * B
        
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
