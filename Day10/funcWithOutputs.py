#Function with Outputs

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formate_l_name = l_name.title()

    return(f"{formated_f_name} {formate_l_name}")

formatedName = format_name("joao pedro", "ferreira")

print(formatedName)