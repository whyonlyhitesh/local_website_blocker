'''
Developed by whyonlyhitesh
Github: https://github.com/whyonlyhitesh
'''

# Local Website Blocking
import os
import tkinter
import tkinter.messagebox
import customtkinter
import pandas as pd
import requests
import zipfile
import subprocess
import io
import sys

# Website
zip_file_url = "https://urlhaus.abuse.ch/downloads/csv/" 


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")  

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
    
def website_blocked_reading():
    file_path = '/etc/hosts'
    with open(file_path, 'r') as file:
        file_contents = file.read()
    return file_contents

# It takes the input of sites that user wants to block
def user_site_input(user_html):
    HtmlFile = user_html 
    n = HtmlFile.count(" ") + 1 
    HtmlFile = HtmlFile[0:].split(" ")
    return HtmlFile, n

# Downlading Zip
def download_zip(zip_file_url) :
    # Downloading zip 
    r = requests.get(zip_file_url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    # Extracting zip
    z.extractall()

# Retriving Data
def retrieving_data():
    # Reading the csv file
    dataframe = pd.read_csv("csv.txt", skiprows=range(0, 8), usecols = ["url"])
    # Writing the csv to block_url.txt
    with open('block_url.txt', 'w') as f:
        df_string = dataframe.to_csv(header=False, index=False)
        f.write(df_string)
    # Removing csv
    os.remove("csv.txt")
    # Removing http:// & https://
    with open("block_url.txt", "rt") as fin:
        with open("block_url0.txt", "wt") as fout:
            for line in fin:
                fout.write(line.replace('http://', '')) 
    with open("block_url0.txt", "rt") as fin:
        with open("block_url.txt", "wt") as fout:
            for line in fin:
                fout.write(line.replace('https://', ''))
    os.remove("block_url0.txt")

# to read sites from database
def reading_database():
    read_file = open("block_url.txt", 'r', encoding='utf-8', errors='ignore')
    source_code = read_file.read() 
    n = source_code.count("\n") + 1
    source_code = source_code[0:].split("\n")
    return source_code, n

# to read the host file if host is edited or not
def hosts_edited_not(user_or_database, host_file):
    with open(host_file,'r') as f:
        for (i, line) in enumerate(f):
            if user_or_database in line:
                return i
    return -1

def program_autostart_linux(auto_program):
    # Specify the command you want to execute
    command0 = 'cp ./autostartlocalwebsiteblockerlinux /usr/bin/autostartlocalwebsiteblockerlinux'
    command1 = '''BINARY_PATH="/usr/bin/autostartlocalwebsiteblockerlinux"
# Check if the binary file exists
if [ -f "$BINARY_PATH" ]; then
    # Create a new service file
    SERVICE_FILE="/etc/systemd/system/autostartlocalwebsiteblockerlinux.service"

    # Write the service file
    echo "[Unit]" > "$SERVICE_FILE"
    echo "Description=autostartlocalwebsiteblockerlinux" >> "$SERVICE_FILE"
    echo "After=network.target" >> "$SERVICE_FILE"
    echo "" >> "$SERVICE_FILE"
    echo "[Service]" >> "$SERVICE_FILE"
    echo "Type=simple" >> "$SERVICE_FILE"
    echo "ExecStart=$BINARY_PATH" >> "$SERVICE_FILE"
    echo "Group=sudo" >> "$SERVICE_FILE"
    echo "" >> "$SERVICE_FILE"
    echo "[Install]" >> "$SERVICE_FILE"
    echo "WantedBy=default.target" >> "$SERVICE_FILE"
fi
    '''
    command2 = 'systemctl daemon-reload'
    command3 = 'chown root:sudo /usr/bin/autostartlocalwebsiteblockerlinux'
    command4 = 'chmod 750 /usr/bin/autostartlocalwebsiteblockerlinux'
    command5 = 'systemctl enable autostartlocalwebsiteblockerlinux.service'
    command6 = 'systemctl start autostartlocalwebsiteblockerlinux.service'

    # Specify the path to the log file
    log_file = './log_file.txt'

    # Open the log file in append mode
    with open(log_file, 'a') as f:
        # Execute the command and redirect the output to the log file
        subprocess.call(command0, shell=True, stdout=f, stderr=subprocess.STDOUT)
        subprocess.call(command1, shell=True, stdout=f, stderr=subprocess.STDOUT)
        subprocess.call(command2, shell=True, stdout=f, stderr=subprocess.STDOUT)
        subprocess.call(command3, shell=True, stdout=f, stderr=subprocess.STDOUT)
        subprocess.call(command4, shell=True, stdout=f, stderr=subprocess.STDOUT)
        subprocess.call(command5, shell=True, stdout=f, stderr=subprocess.STDOUT)
        subprocess.call(command6, shell=True, stdout=f, stderr=subprocess.STDOUT)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Local Website Blocker")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Local Website Blocker", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))


        self.logo_label1 = customtkinter.CTkLabel(self.sidebar_frame, text="Developed by whyonlyhitesh \n https://github.com/whyonlyhitesh", font=customtkinter.CTkFont(size=10, weight="bold"))
        self.logo_label1.grid(row=12, column=0, padx=20, pady=(20, 10))

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", text= "Submit", border_width=2, text_color=("gray10", "#DCE4EE"), command= self.submit1)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Determine Your System")
        self.scrollable_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = [0]

        self.optionmenu_var = customtkinter.StringVar(value="Linux")
        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.scrollable_frame, dynamic_resizing=False, values=["Linux"], variable=self.optionmenu_var)
        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.logo_label1 = customtkinter.CTkLabel(master=self.scrollable_frame, text="Also check out the Windows release!", font=customtkinter.CTkFont(size=12, weight="normal"))
        self.logo_label1.grid(row=11, column=0, padx=20, pady=(20, 10))

        self.logo_label1 = customtkinter.CTkLabel(master=self.scrollable_frame, text="Coming soon to \n Macs & Android devices!", font=customtkinter.CTkFont(size=12, weight="normal"))
        self.logo_label1.grid(row=12, column=0, padx=20, pady=(20, 10))

        # create checkbox and switch frame
        self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")

        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Which Website you want to block:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, text="Specific websites that you've identified     ", variable=self.radio_var, value=1)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, text="Harmful websites from known database", variable=self.radio_var, value=2)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, text="Both URLs and Database                              ", variable=self.radio_var, value=3)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        # create checkbox and switch frame
        self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.check_var = customtkinter.StringVar(value="off")
        self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text= '''Would you like the list of dangerous websites to update automatically
when you start your Linux system?''', variable=self.check_var)
        self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")

        self.logo_label1 = customtkinter.CTkLabel(master=self.checkbox_slider_frame, text="We get the list of harmful websites identified by cybersecurity experts from URLhaus. \n https://urlhaus.abuse.ch/browse/", font=customtkinter.CTkFont(size=12, weight="normal"))
        self.logo_label1.grid(row=12, column=0, padx=20, pady=(20, 10))

        # set default values
        self.checkbox_1.select()
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.textbox.insert("0.0", "Hidden Gems that has blocked\n\n" + website_blocked_reading())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)


    def submit1(self):
        user_choice = self.radio_var.get()
        operating_System = self.optionmenu_var.get()
        auto_program = self.check_var.get()
        sites_by_users = 0

        if user_choice == 2:
            sites_by_users = 0
            self.quit
        elif user_choice == 1 or user_choice == 3:
            # Input the URL
            self.url_variable = customtkinter.CTkInputDialog(text="Enter the list of websites that you need to block in the box below." + "\n" + "(Websites should be seperated with spaces)", title="Local Website blocker")
            sites_by_users = self.url_variable.get_input()
            # MAN = self.url_variable.get_input()
            self.quit
        else:
            self.quit
        #################################
        
        download_zip(zip_file_url)
        retrieving_data()
        operating_System = operating_System.lower()

        if user_choice == 1:
            program_autostart_linux(auto_program)
            start = hosts_edited_not("#### Websites Blocked by USER Starts", '/etc/hosts')
            if start == -1:
                # Starting USER sites marker
                with open('/etc/hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "#### Websites Blocked by USER Starts")
                HtmlFile, n =  user_site_input(sites_by_users)
                for i in range(0,n):
                    with open('/etc/hosts', 'a', errors='ignore') as f:
                        f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
                # Ending USER sites marker
                with open('/etc/hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "#### Websites Blocked by USER Ends" + "\n")
                os.remove('block_url.txt')

            else :
                with open('/etc/hosts', 'r+') as f: #r+ does the work of rw
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if line.startswith('#### Websites Blocked by USER Starts'):
                            HtmlFile, n =  user_site_input(sites_by_users)
                            for j in range(0,n):
                                lines[i] = lines[i].strip() + '\n' + "127.0.0.1 " + f"{HtmlFile[j]}" + '\n'
                    f.seek(0)
                    for line in lines:
                        f.write(line) 
                os.remove('block_url.txt')
            self.destroy()    

        elif user_choice == 2 :
            program_autostart_linux(auto_program)
            start = hosts_edited_not("#### Websites Blocked by Database Starts", '/etc/hosts')
            end = hosts_edited_not("#### Websites Blocked by Database Ends", '/etc/hosts')
            if start == -1:
                HtmlFile, n = reading_database()
                # Starting database sites marker
                with open('/etc/hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "#### Websites Blocked by Database Starts")
                for i in range(0,n):
                    with open('/etc/hosts', 'a', errors='ignore') as f:
                        f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
                # Ending database sites marker
                with open('/etc/hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "#### Websites Blocked by Database Ends" + "\n")
                os.remove('block_url.txt')
            else :
                HtmlFile, n = reading_database()
                with open(r'/etc/hosts', 'r+') as fp:
                    # read an store all lines into list
                    lines = fp.readlines()
                    # move file pointer to the beginning of a file
                    fp.seek(0)
                    # truncate the file
                    fp.truncate()
                    # start writing lines
                    # iterate line and line number
                    for number, line in enumerate(lines):
                        # delete line number start - 1 and end + 1
                        if number not in range(start , end + 1):
                            fp.write(line)
                # Starting database sites marker
                with open('/etc/hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "#### Websites Blocked by Database Starts")
                for i in range(0,n):
                    with open('/etc/hosts', 'a', errors='ignore') as f:
                        f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
                # Ending database sites marker
                with open('/etc/hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "#### Websites Blocked by Database Ends" + "\n")
                os.remove('block_url.txt')
            self.destroy()

        else :
        # Doing part 1
            start = hosts_edited_not("#### Websites Blocked by USER Starts", '/etc/hosts')
            if start == -1:
                # Starting USER sites marker
                with open('/etc/hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "#### Websites Blocked by USER Starts")
                HtmlFile, n =  user_site_input(sites_by_users)
                for i in range(0,n):
                    with open('/etc/hosts', 'a', errors='ignore') as f:
                        f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
                # Ending USER sites marker
                with open('/etc/hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "#### Websites Blocked by USER Ends" + "\n")
            else :
                with open('/etc/hosts', 'r+') as f: #r+ does the work of rw
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if line.startswith('#### Websites Blocked by USER Starts'):
                            HtmlFile, n =  user_site_input(sites_by_users)
                            for j in range(0,n):
                                lines[i] = lines[i].strip() + '\n' + "127.0.0.1 " + f"{HtmlFile[j]}" + '\n'
                    f.seek(0)
                    for line in lines:
                        f.write(line)             
            
        # Doing Part 2
            program_autostart_linux(auto_program)
            start = hosts_edited_not("#### Websites Blocked by Database Starts", '/etc/hosts')
            end = hosts_edited_not("#### Websites Blocked by Database Ends", '/etc/hosts')
            if start == -1:
                HtmlFile, n = reading_database()
                # Starting database sites marker
                with open('/etc/hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "#### Websites Blocked by Database Starts")
                for i in range(0,n):
                    with open('/etc/hosts', 'a', errors='ignore') as f:
                        f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
                # Ending database sites marker
                with open('/etc/hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "#### Websites Blocked by Database Ends" + "\n")
                os.remove('block_url.txt')
            else :
                HtmlFile, n = reading_database()
                with open(r'/etc/hosts', 'r+') as fp:
                    # read an store all lines into list
                    lines = fp.readlines()
                    # move file pointer to the beginning of a file
                    fp.seek(0)
                    # truncate the file
                    fp.truncate()
                    # start writing lines
                    # iterate line and line number
                    for number, line in enumerate(lines):
                        # delete line number start - 1 and end + 1
                        if number not in range(start, end+1):
                            fp.write(line)
                # Starting database sites marker
                with open('/etc/hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "#### Websites Blocked by Database Starts")
                for i in range(0,n):
                    with open('/etc/hosts', 'a', errors='ignore') as f:
                        f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
                # Ending database sites marker
                with open('/etc/hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "#### Websites Blocked by Database Ends" + "\n")
                os.remove('block_url.txt')
            self.destroy()




if __name__ == "__main__":
    app = App()
    app.mainloop()
