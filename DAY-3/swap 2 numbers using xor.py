#swap 2 numbers using xor
a=100
b=200
a=a^b
b=a^b
a=a^b
print(f"After swap a={a} b={b}")