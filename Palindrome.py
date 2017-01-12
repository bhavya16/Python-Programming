#Ask the user for a string and print out whether this string is a palindrome or #not. (A palindrome is a string that reads the same forwards and backwards.)

word = str(input("enter a word "))

if word[:] == word[::-1]:
  print("This is a palindrome")
else:
  print("This is not a palindrome")