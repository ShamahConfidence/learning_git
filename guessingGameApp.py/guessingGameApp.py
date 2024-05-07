import random
print('Welcome to my guessing game')

guess_number = random.randrange(1,6)

guess_num = int(input('Guess the number on my mind, the number is between 1 and 5: '))

while(True):

    if guess_num == guess_number:
        print("You got it","the number is", guess_number)
        break
    else:
        print("You missed it", "the number is" ,guess_number)
        break
    
# age = 18
# if age >= 22:
#     print("You can work")
# elif age == 18:
#     print("Ask your parents  if you can work")
# else:
#     print("You can not work")
    
# print('Thanks')
