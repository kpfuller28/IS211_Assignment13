def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

def gcd(a, b):
  if (b==0):
    return a
  return gcd(b, a%b)

def compareTo(s1, s2):
  if len(s1) <= 1 or len(s2) <= 1:
    return ord(s1[0]) - ord(s2[0])

  return (ord(s1[0]) - ord(s2[0])) + compareTo(s1[1:], s2[1:])

def main():
  print (fibonacci(6))
  print(gcd(538, 8))
  print(compareTo('test', 'test'))

main()