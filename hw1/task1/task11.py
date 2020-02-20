import pytest


def fib(n):

	if n==1 or n == 2:
		return 1
	else:
		return fib(n-1)+fib(n-2)


def test_fib():

	assert fib(2) == 1
	assert fib(5) == 5
	assert fib(12) == 144

print(fib(2))
print(fib(5))
print(fib(12))