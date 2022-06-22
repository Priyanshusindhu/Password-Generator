import random
lc= "abcdeffghijklmnopqrstuvwxyz"
up= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num= "0123456789"
symbol="@#$%^&*\/?"

use_for = lc+up+num+symbol
length_for_pass= 8
password= "".join(random.sample(use_for, length_for_pass))
print("Your Generated Password is:", password)
