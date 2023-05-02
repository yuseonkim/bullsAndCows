def bulls(user, answer) :
	bull = 0

	for i in user :
		if i in answer :
			if user.index(i) == answer.index(i) :
				bull += 1
	
	return bull
