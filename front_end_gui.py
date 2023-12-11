import customtkinter
import tkinter

customtkinter.set_ctk_parent_class(tkinter.Tk)

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("900x780")
app.title("Local Website Blocker")

def quit():
    app.quit()

def submit1():
    Operating_System = user_system.get()
    user_choice = choice_button.get()
    auto_program = check_var.get()

    if choice_button.get() == 2:
        user_html = 0
        quit()
    else:
        # Input the URL
        url_variable = customtkinter.CTkInputDialog(text="Enter the list of websites that you need to block in the box below." + "\n" + "(Websites should be seperated with spaces)", title="Local Website Blocker")
        user_html = url_variable.get_input()
        quit()
    
    return user_html, auto_program, user_choice, Operating_System

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

title = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="Local Website Blocker", font= ("Roboto Medium", 52), text_color="Black")
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

# Autostart checkbox
check_var = customtkinter.StringVar(value="on")
checkbox = customtkinter.CTkCheckBox(master=frame_1, variable=check_var, text= "Would you like the list of dangerous websites to update automatically when you start your Windows computer or laptop?")
checkbox.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=submit1, text="Submit")
button_1.pack(pady=10, padx=10)

app.mainloop()
