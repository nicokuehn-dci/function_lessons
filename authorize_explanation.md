# Explanation of Authorization Methods in Python

This document explains the different authorization methods implemented in the `authorize.py` file. The script demonstrates two approaches: a basic authorization mechanism and an enhanced version with a lockout feature.

## 1. Basic Authorization

This method, implemented in the `authorize` function, allows a user to attempt login with a username and password. The user has a limited number of attempts (default is 3). If the user fails all attempts, the function terminates with a warning message.

### How It Works:
- The function takes an optional parameter `counter` to track the remaining attempts.
- If the username or password is incorrect, the counter is decremented.
- If the counter reaches 0, the function terminates with a warning message.
- If the credentials are correct, the user is granted access.

### When to Use:
- For simple applications where a basic login mechanism is sufficient.
- When no additional security measures, such as lockout, are required.

```python
# Basic Authorization
def authorize(counter=3):
    username = input("username : ")
    password = input("password : ")
    if username != "admin" or password != "password":
        print("wrong credentials")
        counter -= 1
        if counter == 0:
            print("you have attempted all your tries, are you trying to hack this account ?")
            return 
        else:
            authorize(counter)
    else:
        print("welcome admin")
        return 

authorize()
```

## 2. Authorization with Lockout

This method, implemented in the `authorize_with_lockout` function, enhances the basic authorization mechanism by introducing a lockout feature. If the user fails all attempts, they are temporarily locked out for a specified duration (default is 10 seconds).

### How It Works:
- The function takes two optional parameters: `counter` (default is 3) and `lockout_time` (default is 10 seconds).
- If the username or password is incorrect, the counter is decremented.
- If the counter reaches 0, the user is locked out for the specified duration.
- After the lockout period, the function resets the counter and allows the user to try again.
- If the credentials are correct, the user is granted access.

### When to Use:
- For applications where additional security is required to prevent brute-force attacks.
- When a temporary lockout mechanism is needed to deter unauthorized access attempts.

```python
# Authorization with Lockout
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

authorize_with_lockout()
```

## Summary

Both methods provide a way to handle user authentication. The basic authorization method is suitable for simple use cases, while the lockout mechanism adds an extra layer of security for more sensitive applications. Choose the method that best fits your application's requirements.