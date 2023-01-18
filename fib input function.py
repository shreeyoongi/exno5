def recur_fib(n):
 if n<1 :
    return n
 else :
     return (recur_fib(n-1) +recur_fib(n-2))
    
nterms=int(input('enter terms'))
if nterms <=0 :
    print('plese enter a positive integer')
else :
    print('fibonacci sequence')
for i in range (nterms) :
    print (recur_fib(i))
  
