## Explain if __name__ == __main__:
# print("hello") 
# When you call python x.py, all the code that has indentation 0 will be run

# in python there is a built-in variable called __name__
# this variable will be assigned to a string.
# if you run this script from the terminal, __name__ will be automatically
# assigned to '__main__'

# if __name__=="__main__": # this means this line of code was run directly from python

def func():
  print("func in one.py")

print("Top level in one.py")

if __name__=="__main__":
  print("one.py is being run directly")
else:
  print("one.py is has been imported")