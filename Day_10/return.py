#return meaning is end of the func

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
         return "output is invalid"   
    
    f_name_print = f_name.title()
    l_name_print = l_name.title()

    return f"result:{f_name_print} and {l_name_print}"

print(format_name(input("What is your first name:"), input("What is your last name:")))

