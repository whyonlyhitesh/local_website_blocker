'''
Developed by whyonlyhitesh
Github: https://github.com/whyonlyhitesh
'''

import os
import pandas as pd
import requests
import zipfile
import io
import os


# Website
zip_file_url = "https://urlhaus.abuse.ch/downloads/csv/" 

   
def website_blocked_reading():
    file_path = 'C:\Windows\System32\drivers\etc\hosts'
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


download_zip(zip_file_url)
retrieving_data()


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
    os.remove('block_url.txt')
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
    os.remove('block_url.txt')
