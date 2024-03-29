# Local Website Blocker
## Why website Blocking ?
To ensure children's online safety in the digital age, it's crucial to block certain websites. The internet, while beneficial, poses risks like addiction & exposure to adult content. These can disrupt children's development & expose them to inappropriate material. By blocking specific sites, we create a safer, age-appropriate online environment, protecting them from harmful content & addiction. This isn't censorship, but a way to promote healthy growth. Blocking harmful websites also protects devices & personal information from malware.
## Why Local website blocking ?
Local website blocking is increasingly vital due to risks like data breaches, child profiling, & harmful app influences. Children's online activities can be exploited for targeted advertising, affecting their self-perception & consumer habits. Certain apps can also negatively shape their thinking. By locally blocking specific websites & apps, we can ensure a safer digital environment for children, protecting them from harm & promoting positive growth.

![alt text](local_website_blocker_light.png)


## Prerequisites
### Running with python script (For Linux & Windows)
Before you begin, ensure you have met the following requirements:

* You have installed Python 3.x
* No need of prior knowledge of Python.
* Admin Permissions
* Stable internet connection.
* Install python libraries by

        pip install requests
        pip install pandas
        pip install customtkinter
        pip install tkinter
        pip  install shutils

### Running with Graphical binary release
Before you begin, ensure you have met the following requirements:

* Admin Permissions
* Stable internet connection.

## Usage
### Running with python script (For Linux & Windows)
To use the script, follow these steps:

* Run the script using the comm& with root/admin privilege:

        python local_website_blocker.py
* Enter the operating system you are using
* Do you want to block harmful websites from the database URLhaus Database (https://urlhaus.abuse.ch/browse/). Depending on your use case type 1, 2 or 3.
* While entering websites that you have identified. Enter the domain of sites which you want to block (one after another with space in between).
Example:
www.social_media.com www.addictive_site.com abc.com
NOTE: If website starts with http or https, then ignore both the prefixes & directly write the name of website.
Example: Website = https://abc.com, so you will only write abc.com
* After running the script, disconnect you internet connection & then connect again.

### Running with Graphical binary release (For both Windows & Linux)
To use the local_website_blocking-v0.6 release Graphical binary follow these steps:

* Run the release with root/admin privilege.
* Select the operating system you are using.
* Select the option you want.
* While entering websites that you have identified. Enter the domain of sites which you want to block (one after another with space in between).
Example:
www.social_media.com www.addictive_site.com abc.com
NOTE: If website starts with http or https, then ignore both the prefixes & directly write the name of website.
Example: Website = https://abc.com, so you will only write abc.com
* After running the script, disconnect you internet connection & then connect again.

## URLhaus Database
* URLhaus Database (https://urlhaus.abuse.ch/browse/) is a valuable resource for online security & protection. It is a comprehensive collection of known malicious URLs that have been reported & identified by a community of cybersecurity experts.

## License
This project uses the following license: MIT License (https://opensource.org/license/mit/)

## Articles of data breaches
### From Apps
* Child Tracker App uKnowkids Data Leak Exposed Weak Database (https://www.trendmicro.com/vinfo/us/security/news/mobile-safety/child-tracker-app-uknowkids-data-leak-exposed-weak-database)
* Parental control app with 5 million downloads vulnerable to attacks (https://www.bleepingcomputer.com/news/security/parental-control-app-with-5-million-downloads-vulnerable-to-attacks/)
* This top parental control app has a serious security flaw (https://www.techradar.com/news/this-top-parental-control-app-found-to-have-a-serious-security-flaw)
* These parental control apps could expose your kids’ private data — what you need to know (https://www.laptopmag.com/news/child-monitoring-apps-are-tracking-parents-too-here-are-the-bad-apples)

### From Web Browser Extensions
* 1.3 million users encountered browser extension threats in the first half of 2022 (https://www.kaspersky.com/about/press-releases/2022_13-million-users-encountered-browser-extension-threats-in-the-first-half-of-2022)
* Websites can steal browser data via extensions APIs (https://www.zdnet.com/article/websites-can-steal-browser-data-via-extensions-apis/)
*  The cybersecurity threat of browser extensions (https://cybernews.com/security/the-cybersecurity-threat-of-browser-extensions/)
