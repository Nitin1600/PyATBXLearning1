class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg
        # self.name = name
        # self.las_name = last_name

    def login_confirm(self):
        if self.email == "amith@gmail.com" and self.password == "Abc@123":
            print("You are allowed")
        else:
            print("You are not allowed")

vwo_obj = VWOLoginPage("email", "password")
vwo_obj.login_confirm()

Akash = VWOLoginPage("Niketh@gmail.com", "Cba@321")
Akash.login_confirm()

Amith = VWOLoginPage("amith@gmail.com", "Abc@123")
Amith.login_confirm()


