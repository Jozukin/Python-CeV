from random import randint
b = ()
for c in range(0, 5):
    a = (randint(0, 50),)
    b = b + a
print(f'Os números gerados foram {b}')
print(f'O maior número é {max(b)}')
print(f'O menor número é {min(b)}')
