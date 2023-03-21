def rand_name():
	import random
	names = ['Ibrahim','Hashim','Kim','Gonzalez','Ali','Vinko','Dragomir','Roberto','Felix','Edgar','Patrick','Talal','Mario',
							'Carlos','Sergei','Omar','Jong','Richard','Sohrab','Chan','Francisco','Valencia','Ashraf','Sultan','Charles']
	rand_name = names[random.randrange(1,25)]
	
	return rand_name