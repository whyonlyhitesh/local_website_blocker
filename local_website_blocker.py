# Local Website Blocking
import pandas as pd
import requests
import zipfile
import io
import os
import getpass
import shutil
import front_end_gui


user_html, auto_program, user_choice, Operating_System = front_end_gui.submit1()

# Website
zip_file_url = "https://urlhaus.abuse.ch/downloads/csv/" 

# Getting information about the user
USER_NAME = getpass.getuser()

# It takes the input of sites that user wants to block
def user_site_input():
    HtmlFile = user_html 
    n = HtmlFile.count(" ") + 1 
    HtmlFile = HtmlFile[0:].split(" ")
    return HtmlFile, n

# Downlading Zip
def download_zip() :
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

def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" "%s"' % file_path)

def program_autostart_windows():
        if int(auto_program) == 1:
            os.mkdir("C:\Windows\Program Files\local_website_blocking")
            shutil.copy("windows_autostart_application.py", "C:\Windows\Program Files\local_website_blocking\windows_autostart_application.py")
            add_to_startup("C:\Windows\Program Files\local_website_blocking\windows_autostart_application.py")


download_zip()
retrieving_data()

user_preference = user_choice
Operating_System = Operating_System.lower()

if Operating_System == "linux" :

    if user_preference == 1:
        start = hosts_edited_not("#### Websites Blocked by USER Starts", 'hosts')
        if start == -1:
            # Starting USER sites marker
            with open('hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by USER Starts")
            HtmlFile, n = user_site_input()
            for i in range(0,n):
                with open('hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
            # Ending USER sites marker
            with open('hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by USER Ends" + "\n")

        else :
            with open('hosts', 'r+') as f: #r+ does the work of rw
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith('#### Websites Blocked by USER Starts'):
                        HtmlFile, n = user_site_input()
                        for j in range(0,n):
                            lines[i] = lines[i].strip() + '\n' + "127.0.0.1 " + f"{HtmlFile[j]}" + '\n'
                f.seek(0)
                for line in lines:
                    f.write(line)          

    elif user_preference == 2 :
        start = hosts_edited_not("#### Websites Blocked by Database Starts", 'hosts')
        end = hosts_edited_not("#### Websites Blocked by Database Ends", 'hosts')
        if start == -1:
            HtmlFile, n = reading_database()
            # Starting database sites marker
            with open('hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Starts")
            for i in range(0,n):
                with open('hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
            # Ending database sites marker
            with open('hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Ends" + "\n")
        else :
            HtmlFile, n = reading_database()
            with open(r'hosts', 'r+') as fp:
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
            with open('hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Starts")
            for i in range(0,n):
                with open('hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
            # Ending database sites marker
            with open('hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Ends" + "\n")

    else :
    # Doing part 1
        start = hosts_edited_not("#### Websites Blocked by USER Starts", 'hosts')
        if start == -1:
            # Starting USER sites marker
            with open('hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by USER Starts")
            HtmlFile, n = user_site_input()
            for i in range(0,n):
                with open('hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
            # Ending USER sites marker
            with open('hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by USER Ends" + "\n")
        else :
            with open('hosts', 'r+') as f: #r+ does the work of rw
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith('#### Websites Blocked by USER Starts'):
                        HtmlFile, n = user_site_input()
                        for j in range(0,n):
                            lines[i] = lines[i].strip() + '\n' + "127.0.0.1 " + f"{HtmlFile[j]}" + '\n'
                f.seek(0)
                for line in lines:
                    f.write(line)
        
    # Doing Part 2
        start = hosts_edited_not("#### Websites Blocked by Database Starts", 'hosts')
        end = hosts_edited_not("#### Websites Blocked by Database Ends", 'hosts')
        if start == -1:
            HtmlFile, n = reading_database()
            # Starting database sites marker
            with open('hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Starts")
            for i in range(0,n):
                with open('hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
            # Ending database sites marker
            with open('hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Ends" + "\n")
        else :
            HtmlFile, n = reading_database()
            with open(r'hosts', 'r+') as fp:
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
            with open('hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Starts")
            for i in range(0,n):
                with open('hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
            # Ending database sites marker
            with open('hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Ends" + "\n")
                


else:
    if user_preference == 1:
        program_autostart_windows()
        start = hosts_edited_not("#### Websites Blocked by USER Starts", 'C:\Windows\System32\drivers\etc\hosts')
        if start == -1:
            # Starting USER sites marker
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by USER Starts")
            HtmlFile, n = user_site_input()
            for i in range(0,n):
                with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
            # Ending USER sites marker
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by USER Ends" + "\n")

        else :
            with open('C:\Windows\System32\drivers\etc\hosts', 'r+') as f: #r+ does the work of rw
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith('#### Websites Blocked by USER Starts'):
                        HtmlFile, n = user_site_input()
                        for j in range(0,n):
                            lines[i] = lines[i].strip() + '\n' + "127.0.0.1 " + f"{HtmlFile[j]}" + '\n'
                f.seek(0)
                for line in lines:
                    f.write(line)          

    elif user_preference == 2 :
        program_autostart_windows()
        start = hosts_edited_not("#### Websites Blocked by Database Starts", 'C:\Windows\System32\drivers\etc\hosts')
        end = hosts_edited_not("#### Websites Blocked by Database Ends", 'C:\Windows\System32\drivers\etc\hosts')
        if start == -1:
            HtmlFile, n = reading_database()
            # Starting database sites marker
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Starts")
            for i in range(0,n):
                with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
            # Ending database sites marker
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Ends" + "\n")
        else :
            HtmlFile, n = reading_database()
            with open(r'C:\Windows\System32\drivers\etc\hosts', 'r+') as fp:
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
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Starts")
            for i in range(0,n):
                with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
            # Ending database sites marker
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Ends" + "\n")

    else :
    # Doing part 1
        start = hosts_edited_not("#### Websites Blocked by USER Starts", 'C:\Windows\System32\drivers\etc\hosts')
        if start == -1:
            # Starting USER sites marker
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by USER Starts")
            HtmlFile, n = user_site_input()
            for i in range(0,n):
                with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
            # Ending USER sites marker
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by USER Ends" + "\n")
        else :
            with open('C:\Windows\System32\drivers\etc\hosts', 'r+') as f: #r+ does the work of rw
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith('#### Websites Blocked by USER Starts'):
                        HtmlFile, n = user_site_input()
                        for j in range(0,n):
                            lines[i] = lines[i].strip() + '\n' + "127.0.0.1 " + f"{HtmlFile[j]}" + '\n'
                f.seek(0)
                for line in lines:
                    f.write(line)
        
    # Doing Part 2
        program_autostart_windows()
        start = hosts_edited_not("#### Websites Blocked by Database Starts", 'C:\Windows\System32\drivers\etc\hosts')
        end = hosts_edited_not("#### Websites Blocked by Database Ends", 'C:\Windows\System32\drivers\etc\hosts')
        if start == -1:
            HtmlFile, n = reading_database()
            # Starting database sites marker
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Starts")
            for i in range(0,n):
                with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
            # Ending database sites marker
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Ends" + "\n")
        else :
            HtmlFile, n = reading_database()
            with open(r'C:\Windows\System32\drivers\etc\hosts', 'r+') as fp:
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
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Starts")
            for i in range(0,n):
                with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
            # Ending database sites marker
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Ends" + "\n")
os.remove('block_url.txt')
