def rev(sen):
return ' '.join(word[::-1] for word in sen.split(" "))
sen = input()
print(rev(sen))
