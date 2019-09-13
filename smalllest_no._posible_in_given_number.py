def smallest(lst): 
	for i,n in enumerate(lst): 
		if n != '0': 
			tmp = lst.pop(i) 
			break
	return str(tmp) + ''.join(lst) 
if __name__ == '__main__': 
	lst = list(str(input())) 
	lst.sort() 
	print (smallest(lst))
