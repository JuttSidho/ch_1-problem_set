"""
In the United States, it’s customary to leave a tip for your 
server after dining in a restaurant, typically an amount equal 
to 15% or more of your meal’s cost. Not to worry, though,
we’ve written a tip calculator for you, below!
"""
def main():
    dollars = float(input("How much was the meal? "))
    percent = float(input("What percentage would you like to tip? "))
    tip = dollars * ((percent) / 100)
    print(f"Leave ${tip:.2f}")
main()