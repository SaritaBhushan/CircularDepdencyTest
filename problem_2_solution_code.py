# Fibonacci sequence intial values with 1 and 2
print("Fibonacci Sequence:")
f1, f2 = 1, 2
print(f1, end=' ')

# set Fibonacci sequence range
n= 4000000 # four million
# Intalize the evensum vriable by 0
evensum = 0
while f2 <= n:
    print(f2, end=' ')
    if f2 % 2 == 0:
        evensum += f2
    f1, f2 = f2, f1+f2  # the real formula for Fibonacci sequence

print("\nSum of Even term of the above series is ",evensum)