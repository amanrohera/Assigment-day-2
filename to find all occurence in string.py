test_str = 'python is  great tha python java'
test_sub = "python"
print("The original string is : " + test_str) 
print("The substring to find : " + test_sub) 
res = [i for i in range(len(test_str)) if test_str.startswith(test_sub, i)] 
  
# printing result  
print("The start indices of the substrings are : " + str(res)) 
