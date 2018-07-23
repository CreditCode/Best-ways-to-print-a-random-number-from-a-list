# You are here to see the best ways to output texts in a list?
# Here we go!

# Oh ye, we need this to import. 
import random

# Here is the first Method. We are just making a list, and print a random choice of the list.

happy = [1, 2, 3]
print(random.choice(happy))

# In the second method, we register the numbers again in a list. After that, we make a SystemRandom. And finally, we print the SystemRandom with the list.
numme = [1, 2, 3]
secure_random = random.SystemRandom()
print(secure_random.choice(numme))

# In the third method, we have a again a small list. Now we use the range thing to print a number from 0-1. I know thats stupid, but it still works. 
# And again, we make a random Choice and print that.

numbers = [1,2,3,4,5]

for i in range(0, 1): #If you want to print more numbers, just change the number 1 to 2,3,4,5 and so on.
	letter = random.choice(numbers)
	print(letter)

# Finally finished. 
# I hope you learned something and can use it again.
# hAvE a niCe dAy!!!!111elf!!!