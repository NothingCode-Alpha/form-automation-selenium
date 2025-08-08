import input_validation

name_input = input("name: ")
while input_validation.name_validation(name_input) == False:
    print("didgits and symbols arent validiate/name must be at least 3 chars")
    name_input = input("name: ")

email_input = input("email: ")
while input_validation.email_validation(email_input) == False:
    print("enter a valid email")
    email_input = input("email: ")


message_input = input("your message: ")