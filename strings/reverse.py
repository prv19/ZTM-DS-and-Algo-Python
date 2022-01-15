# Reverse a string 
  
inputString = "Hello World"
def reverse(str):
  tmpString = ""
  for i in str:
    tmpString = i + tmpString
  return tmpString
  
print ("The reversed string is : ", reverse(inputString))