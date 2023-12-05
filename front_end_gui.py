import customtkinter
import tkinter

customtkinter.set_ctk_parent_class(tkinter.Tk)

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("900x780")
app.title("Local Website Blocker")

def submit():
    user_system2 = user_system.get()
    choice_button1 = choice_button.get()
    check_var1 = check_var.get()
    url_variable1 = url_variable.get()
    quit()
    return url_variable1, check_var1, choice_button1, user_system2

def quit():
    app.quit()

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

title = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="Local Website Blocker")
title.pack(pady=10, padx=10)

parameter_option = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="Select the Operating System")
parameter_option.pack(pady=0, padx=10)


user_system1 = customtkinter.StringVar(value="Windows")
user_system = customtkinter.CTkComboBox(frame_1, values=["Windows", "Linux"], variable=user_system1)
user_system.pack(pady=10, padx=10)
user_system.set("Windows")

# Selecting which operation to perform

choice_button = customtkinter.IntVar(value=2)

radiobutton_1 = customtkinter.CTkRadioButton(master=frame_1, variable=choice_button, value=1, text="To only restrict access to the specific websites that you've identified")
radiobutton_1.pack(pady=10, padx=10)

radiobutton_2 = customtkinter.CTkRadioButton(master=frame_1, variable=choice_button, value=2, text="Only block harmful websites from known database")
radiobutton_2.pack(pady=10, padx=10)

radiobutton_3 = customtkinter.CTkRadioButton(master=frame_1, variable=choice_button, value=3, text="Both URLs and Database")
radiobutton_3.pack(pady=10, padx=10)

# Input the URL
url_input = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.CENTER, text="Enter the list of websites that you need to block in the box below." + "\n" + "(Websites should be seperated with spaces)" "\n" "(It will only work with 1st and 2rd option):")
url_input.pack(pady=10, padx=10)

url_variable = tkinter.StringVar()
textbox = customtkinter.CTkEntry(master=frame_1, width=200, height=20, textvariable=url_variable)
textbox.pack(pady=10, padx=10)

# Autostart checkbox
check_var = customtkinter.StringVar(value="on")
checkbox = customtkinter.CTkCheckBox(master=frame_1, variable=check_var, text= "Would you like the list of dangerous websites to update automatically when you start your Windows computer or laptop?")
checkbox.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=submit)
button_1.pack(pady=10, padx=10)

app.mainloop()
