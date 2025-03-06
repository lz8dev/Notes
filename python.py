
## See usedLines file, python section

#print("first")
#f1 = 'SamplE'
#print (f1)
#print(f1.lower())
#print(f1.upper())
#print('first','second','third') 
#print('first'+'second'+'third') 
#print('first','second','third',sep=' - ') 
#print('one \'two\'') 

#n1 = 'one'
#n2 = 'two'
#print(f'first: {n1} , \ - second:{n2}')

#list_1 = ['a', 'b', 3, True, 'last']   
#print(list_1)
#print(list_1[0]  )
#print(list_1[:2])
#print(list_1[2:])
#rint(list_1[-1])
#print(len(list_1))
#list_1.append('X')
#list_1.insert(2, 'item1')
#del list_1[1:3]
#print(list_1)

#m1 = [[1, 2, 3],
#      [4, 5, 6],
#      [7, [8.1, 8.2, 8.3], 9]]

#for row in m1:
#    for element in row:
#        print(element)
#print(m1)
#print(m1[2][1][1])


## INPUTS
#name = input('Type Name: ')
#age = int(input('Type Age: '))
#height = float(input('Type Height: '))
#print(type(name))
#print(type(age))
#print(type(height))
#print(name)
#print(age)
#print(height)

## DICTIONARIES
#dic_1 = {1:'one', 2:'two', 3:'three'}
#dic_2 = {'numbers':{1:'one', 2:'two', 3:'three'},
#         'chars':{'a':'A', 'b':'B', 'c':'C'},
#         'specs':{'s1':'@', 's2':'#', 's3':'$'}}
#print(dic_1)
#print(dic_2)

#print(dic_1.keys())
#print(dic_1.values())
#print(dic_1.items())

#print(dic_2.keys())
#print(dic_2.values())
#print(dic_2.items())

#print(dic_1[2])
#print(dic_2['specs']['s3'])
#rint(dic_2['specs'].values())

## IF EXERCISE
#print('Yankenpo')
#i1 = input('P1 Type b, l, or s: ')
#i2 = input('P2 Type b, l, or s: ')
#if i1 == 'b':
#    if i2 == 'l':
#        print('P1 wins')
#    elif i2 =='s':
#        print('P2 wins')
#    else:
#        print('Tie')
#elif i1 == 'l':
#    if i2 == 'l':
#        print('Tie')
#   elif i2 =='s':
#       print('P1 wins')
#    else:
#       print('P2 wins')
#elif i1 == 's':
#    if i2 == 'l':
#        print('P2 wins')
#    elif i2 =='s':
#        print('Tie')
#    else:
#        print('P1 wins') 
#else:
#   print('Invalid input.')


## FOR
#num = [1,2,3,4,5,6,7,8,9,0]
#for x in num:
#    if x == 9:
#        break
#    elif x == 5:
#        continue
#    print(f' -> x = {x}')


#for m in range(5, 10):        
#    print(m)


#x = 0   
#while x < 5:
#   print(x)
#   x += 1 


#def count():        
#    for i in range(55): 
#        print(i)       
#        yield i 
#for num in count():
#    print(num)

#Odd numbers
#lim = 20
#odd = iter(range(1, lim + 1, 2))

#for num in odd:
#    print(num)


#Fibonacci

#def fib(lim):
#    a, b = 0, 1
#    while a < lim:
#        yield a
#        a, b = b, a + b   

#for num in fib(20):        
#    print(num)     

mult = lambda x, y : x * y 
print(mult(5, 4))        

nums = list(range(10,20))
pot_1 = list(map(lambda x : x ** 2, nums))
print(pot_1)

even_1 = list(filter(lambda x : x % 2 == 0, nums))
print(even_1)