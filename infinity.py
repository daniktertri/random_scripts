import random
while True:
 l = ['1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
 line =1000
 a = 0
 code = ['a','b','c','d','e','f','g','h','i','j','1','2','3','4','5','6','7','8','9','0']
 m =[]
 while a < line:
   a += 1
   m+=random.choice(l)
   str_a = ''.join(m)

 f=open("C:/Users/tertr/Documents/math/test.txt",'a')
 f.write(str_a)
