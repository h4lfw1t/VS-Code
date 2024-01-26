def is_eligible(age, citizenship, prison):
    if (age >= 18) and (citizenship.lower() == 'canadian') and (prison.lower() == 'no'):
        return True
    else:
        return False


name = input("What is your name? ")
age = int(input("How old are you? "))
citizenship = input("What is your citizenship? ")
prison = input("Are you currently incarcerated?")

if is_eligible(age, citizenship, prison):
    print(name, ", you are eligible to vote")
else:
    print(name, ", you are ineligible to vote")
