import random

words = ("skillfactory", "testing", "blackbox", "pytest", "unittest", "coverage")

secret_word = random.choice(words)

gamer_word = ['_ '] * len(secret_word)
print(''.join(gamer_word))

pov = []
error = 0 
def visel_testing():
	error = 0
	while True:
	    letter = input('\nвведите одну английскую букву: ')
	    if letter in pov:
	    	print("Будьте внимательнее вы уже вводили эту букву")
	    pov.append(letter)
	    if len(letter) != 1 or not letter.isalpha():
	        print("ВВЕДИТЕ ОДНУ БУКВУ!!!")
	        continue
	
	    if letter in secret_word:
	    	for index, simbol in enumerate(secret_word):
	    		if simbol == letter:
	    			gamer_word[index] = simbol
	    	if '_ ' not in gamer_word:
	    		print("Поздравляю, вы выиграли!!! \nВы отгадали слово: " + secret_word.upper())
	    		break
	    else:
	    	error += 1
	    	print('ошибок допущенно: ' + str(error) + '!')
	    	if error == 4:
	    		print("Вы не отгадали загаданное слово попробуйте еще")
	    		#following = input("Играть еще? введи да или нет:")
	    		break
	
	    print(''.join(gamer_word))
#visel_testing()	 
