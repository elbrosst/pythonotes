def hola(kirbi):
    
    num = 1
    while num < kirbi:
        yield num * 2
        num = num  + 1 
ramdom = hola(10)

print(next(ramdom))
print("this is an example")
print(next(ramdom))
print("this is another example")
print(next(ramdom))
#for i in ramdom:
 #   print(i)