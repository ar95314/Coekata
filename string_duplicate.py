def toMutable(string): 
	temp = [] 
	for x in string: 
		temp.append(x) 
	return temp 
def toString(List): 
	return ''.join(List) 
def removeDupsSorted(List): 
	res_ind = 1
	ip_ind = 1
	while ip_ind != len(List): 
		if List[ip_ind] != List[ip_ind-1]: 
			List[res_ind] = List[ip_ind] 
			res_ind += 1
		ip_ind+=1
	string = toString(List[0:res_ind]) 

	return string  
def removeDups(string):  
	List = toMutable(string) 
	List.sort() 
	return removeDupsSorted(List) 


string = input()
print (removeDups(string))
