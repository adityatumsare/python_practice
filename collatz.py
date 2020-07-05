#!/usr/bin/python
#Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1.
#
#Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1. (Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)
#
#Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a string value.

n = int(input("Type the number: "))

def collatz(num):
  if (num%2==0):
    y=num//2
    print(y)
    return y
  elif (num%2==1):
    y=(3*num)+1
    print(y)
    return y

res=collatz(n)
while(res!=1):
  res=collatz(res)
  #print (res)
