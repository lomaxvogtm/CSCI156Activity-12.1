__author__ = 'Madeleine'


def splitemail(email):
    a = [".com", ".gov", ".edu", ".org", ".mil", ".net"]
    try:
        username, domain = email.split("@")
        domain, gTLD = domain.split(".")
        print(username,domain,gTLD)
        if gTLD in a:
            print(domain)
            print(gTLD)
            print(username)
        else:
            print("Please recheck your email address.")
    except ValueError:
        print("Please enter a valid email address.")



# inputemail('.edu', '.org',)

emailaddress = input("Type in an email address, don't screw it up Bowers whannabe.")
splitemail(emailaddress)

