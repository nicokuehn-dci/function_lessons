def authorize(counter=3):#3 is default parameter
    username = input("username : ")
    password = input("password : ")
    if username != "admin" or password !="password":
        print("wrong credentials")
        counter -= 1
        if counter == 0:
            print("you have attemped all your tries, are you trying to hack this account ?")
            return 
        else :
            authorize(counter)
    else:
        print("welcome admin")
        return 
    
authorize()

def authorize_with_lockout(counter=3, lockout_time=10):
    """
    This function adds a lockout mechanism to the authorization process.
    If the user fails all attempts, they must wait for a specified lockout time.
    """
    import time

    username = input("username : ")
    password = input("password : ")

    if username != "admin" or password != "password":
        print("wrong credentials")
        counter -= 1
        if counter == 0:
            print(f"You have attempted all your tries. Please wait {lockout_time} seconds before trying again.")
            time.sleep(lockout_time)
            return authorize_with_lockout(counter=3, lockout_time=lockout_time)
        else:
            authorize_with_lockout(counter, lockout_time)
    else:
        print("welcome admin")
        return

# Example usage of the new function
authorize_with_lockout()

