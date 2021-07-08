import string
import random
import pyperclip
letters = string.ascii_letters
nums = string.digits
chars = string.punctuation
password = ''

password+=letters
password+=nums    
password+=chars


z = random.sample(password, 10)
new_password = "".join(z)
pyperclip.copy(new_password)

with open('./password.txt', 'a') as f:
    f.write(new_password+"\n")

print(new_password)