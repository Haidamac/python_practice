def guest_list(guests):
    for guest in guests:
        name, age, occupation = guest
        print("{} is {} years old and works as {}".format(name, age, occupation))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""