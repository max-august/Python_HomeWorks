import string
import random

#print(string.ascii_letters)
#print(string.digits)
#print(string.punctuation)

#site = input("사이트: ")
#count = input("입력: ")
#count = int(count)

_LENGTH = 10 #10자리
string_pool = string.ascii_letters + string.digits + string.punctuation
result = ""
for i in range(_LENGTH) :
    result += random.choice(string_pool)
print(result)

