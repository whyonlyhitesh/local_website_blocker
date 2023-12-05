# Local Website Blocking
import pandas as pd
import requests
import zipfile
import io
import os
from windows_autostart_script import *

# Website
zip_file_url = "https://urlhaus.abuse.ch/downloads/csv/" 

# Downlading Zip
def download_zip() :
    r = requests.get(zip_file_url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()

# Retrieving Data
def retrieving_data():
    dataframe = pd.read_csv("csv.txt", skiprows=range(0, 8), usecols = ["url"])
    with open('block_url.txt', 'w') as f:
        df_string = dataframe.to_string(header=False, index=False)
        f.write(df_string)
    os.remove("csv.txt")
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

def program_autostart():
    autostart_program = input("Do you wish to have the list of dangerous websites updated automatically each time you power on your computer or laptop (Yes or No)?")
    if autostart_program.lower() == "yes":

        print("work under progress")


download_zip()
retrieving_data()

# Doing Part 2
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
