'''
 Douglas Byfield
    
'''

def hello():
    print("ECSE3038 - Engineering IoT Systems")

hello()


def validatePassword(psword):
    alnum, num = 0, 0

    if len(psword) >= 8 and psword.isalnum():
        for val in psword:
            try:
                if isinstance(int(val), int):
                    num += 1
            except:
                pass
        
        if num >= 2:
            return True
    
    return False

def sumUpToN(num):
    digit = 0

    if num > 1:
        for i in range(1, num+1):
            digit += i
    else:
        digit = -1

    return digit
