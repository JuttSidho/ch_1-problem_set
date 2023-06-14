"""
implement a program in Python that prompts the user for mass as an integer (in kilograms) 
and then outputs the equivalent number of Joules as an integer. Assume that the user 
will input an integer.
"""
def Calculate_energy ():
    m = int(input("enter the mass in kilogram: "))
    c = (3 * 10**8)**2
    E = m*c
    print("Energy in joules:",E)
Calculate_energy()