import random
passlen = int(input('Enter lenght of password'))
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#%&"
p = "".join(random.sample(s,passlen ))
print(p)