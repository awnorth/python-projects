# Fibonacci numbers module
# https://docs.python.org/2/tutorial/modules.html

def fib(n):     # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print b
        a, b = b, a+b

def fib2(n):
    a, b = 0, 1
    result = []
    while b < n:
        result.append(b)
        a, b = b, a+b

    return result

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
