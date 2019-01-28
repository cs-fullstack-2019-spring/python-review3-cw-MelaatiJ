def main():
    problem1()
    # problem2()
    # problem3()
    # problem4()


def problem1():

def int1to10(n,outside_mode):
    userInt= int(input("enter a number between 1 and 10"))
    if outside_mode==True:
        if n<=10 and n>=1:
            return ("True")
        else:
            return ("False")
    elif outside_mode==False:
        if n<=10 and n>=1:
            return ('False')
    else:
        return ("True")




    # Given a number n, return ```True``` if n is in the range 1..10, inclusive.
    # Unless outside_mode is ```True```, in which case return True if the number is less or equal to 1, or greater or equal to 10.
    # Print the result returned from your function.
    #
    # BONUS: Get the number and outside_mode flag from User input instead of hardcoding it
    #
    # ```def in1to10(n, ouuserInt= int(input("enter a number between 1 and 10"))tside_mode):```
    #
    # Examples of Expected Output:
    #
    # ```in1to10(5, False)``` → True
    #
    # ```in1to10(11, False)``` → False
    #
    # ```in1to10(11, True)``` → True
    #


def problem2():



















    if __name__ == '__main__':
        main()