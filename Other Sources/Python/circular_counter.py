import sys

"""
There are people sitting in a circular fashion,
print every third member while removing them,
the next counter starts immediately after the member is removed.
Print till all the members are exhausted.

For example:
Input: consider 123456789 members sitting in a circular fashion,
Output: 369485271

123456789
124578 - 369
1257   - 48
127    - 5
"""

def main(args):
	input = raw_input()
	print input

if (__name__ == '__main__'):
	main(sys.argv)

