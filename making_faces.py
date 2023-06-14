"""
implement a function called main that prompts the user for input,
alls convert on that input, and prints the result. You’re welcome,
but not required, to prompt the user explicitly, as by passing a str
of your own as an argument to input. Be sure to call main at the bottom of your file.
"""
def main():
    message = input("Enter your special message: ")
    Message = convert_message(message).capitalize()
    print(f"Your converted message:  {Message}")
def convert_message(message):
    if ":)" in message:
        return message.replace(":)", "🙂")
    elif ":(" in message:
        return message.replace(":(", "🙁")
    else:
        return message

if __name__=="__main__":
    main()