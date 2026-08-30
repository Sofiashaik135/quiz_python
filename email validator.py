email = input("Enter an email:")
if ( 
    "@" in email
    and "." in email
    and " " not in email
    and not email.startswith ("@")
    and not email.endswith("@")
    and not email.startswith(".")
    and not email.endswith(".")
    ):
    at_position = email.index("@")
    if at_position < len(email) - 1 :
        domain = email[at_position + 1:]
        if "." in domain and not domain.startswith(".") and not domain.endswith("."):
            print("valid email")
        else:
            print("invalid email")
    else:
        print("invalid email")
else:
    print("invalid email")
        

