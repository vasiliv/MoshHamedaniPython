import random
import string

print(random.random())
print(random.randint(1,10))
#masividan archevs random values
print(random.choice([1,2,1000]))
#archevs imden values ramdenic mititebulia key-shi
print(random.choices([1,2,1000,999],k=2))
#works with strings also
print(random.choices("abcdefghijklmno",k=4))
#ase ukve strings abrunebs
print("".join(random.choices("abcdefghijklmno",k=4)))
#abrunebs kvela did da patara asos
print(string.ascii_letters)
#abrunebs kvela ciprs
print(string.digits)
#random password generator
print("".join(random.choices(string.ascii_letters + string.digits,k=8)))

#ucvlis tanmimdevrobas
numbers = [1,2,3,4]
random.shuffle(numbers)
print(numbers)