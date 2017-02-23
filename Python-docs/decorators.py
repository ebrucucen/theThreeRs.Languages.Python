def stop():
        print "stop"
def return2():
        print 2
        return 2
 #decorator is a function or a class
 # wrapping a function or a method 
def decorator(func):
    return (func) 

weird= decorator(return2) #manually decorate       

@decorator        
def start():
        print "start"
