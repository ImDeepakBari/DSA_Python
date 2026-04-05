# 1. Find the longest string in a list of strings
test_data1 = ["hello", "world",'this is a string'] # output: 16

def find_long_str(s):
    longest = 0
    for item in s:
        if len(item) > longest:
            longest = len(item)
    return longest

print(find_long_str(test_data1))

        
        

