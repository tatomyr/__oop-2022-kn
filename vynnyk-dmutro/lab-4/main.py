#Functions
def my_function():
  print("Hello from a function")
my_function()


#Arguments
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")


#Callbacks
def callbackFunc1(s):
    print('Callback Function 1: Length of the text file is : ', s)
def callbackFunc2(s):
    print('Callback Function 2: Length of the text file is : ', s)
def printFileLength(path, callback):
    f = open(path, "r")
    length = len(f.read())
    f.close()
    callback(length)
if __name__ == '__main__':
    printFileLength("sample.txt", callbackFunc1)
    printFileLength("sample.txt", callbackFunc2)