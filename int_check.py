#I made this because I wanted something that could gracefully check whether something can
#be converted to an int() or not and handle failure gracefully. 

def check(a):

    try:
        test=int(a)        
        result=True
        
    except ValueError:
        result=False
        #if the result fails, will put the message into the tuple
        test="Fail. Try again Scooter."
    
#The result from this is a tuple to be sorted out later
    return result, test
        
