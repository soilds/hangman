
filename = 'guest_book.txt'


	


mes = ''

while True:
	mes = input("Enter you like resone,or Enter'q' to quiet  ")

	if mes =='quite':
		
		break
	
	
		
	else:
		with open(filename,'a') as file_object:
			
	
	
			file_object.write(mes+'\n')
	

		
		

