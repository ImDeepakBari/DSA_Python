# check if a string is palindorme

test_data1 = "Hello World!" # false
test_data2 = "Radar" #true
test_data3 = "madaM" # true

def check_str_palindrome(st):

    # clean up string
    cleaned = ''
    for ch in st:
        if ch.isalnum():
            cleaned += ch.lower()
    print("cleaned data:", cleaned)

    l, r = 0, len(cleaned) -1
    while l < r:
        if cleaned[l] != cleaned[r]:
            return False
        else:
            l += 1
            r -= 1

    return True


  

    

print(check_str_palindrome(test_data1))
print(check_str_palindrome(test_data2))
print(check_str_palindrome(test_data3))