# Reverse a string 
  
from xml.sax.xmlreader import InputSource


inputString = "Hello World"
def reverse(str):
  tmpString = ""
  for i in str:
    tmpString = i + tmpString
  return tmpString

print('Input String: ', inputString)
print('Input String Length: ', len(inputString))
for i in range(len(inputString)):
    print(inputString[i])
print ("The reversed string is : ", reverse(inputString))