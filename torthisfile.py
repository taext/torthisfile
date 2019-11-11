#!/home/dd/anaconda3/bin/python
""" ttf.py - Tor This File - Download file via Tor (with random IP and user-agent) """

import requests, re, time, sys, random, os, subprocess, datetime, time

installation_steps = ["apt install tor","input sudo password in easy_sudo file"]

version = "v2.06"
date = "November 11th 2019" 
author = "github/taext"
summary = "Download file via Tor (with random IP and user-agent)"
online_user_guide = "https://v1d.dk/h/ttf.htm"
online_code_highlighted = "https://v1d.dk/h/ttf.png"
whats_new = "add docstrings"

# how many seconds to wait for Tor service to restart
wait_time = 1

def about():
    """Print module information"""
    print(summary + "\n" + version + " - " + date + " - by " + author)

def installation_guide():
    """Print installation information"""
    _ = [print(str(i+1) + ".", item) for i, item in enumerate(installation_steps)]

def user_guide():
    """Open online user-guide"""
    subprocess.Popen(['xdg-open',online_user_guide]).wait()

def syntax_highlight_code(dark=True):
    """Open online .png of code with syntax highlighting, optional light version"""
    if not dark:
        online_code_highlighted.replace("ttf","ttf_light")
    subprocess.Popen(['xdg-open',online_code_highlighted]).wait()


def download(url, download_folder="~/Downloads/"):
    """Download file using random IP and user-agent"""

    # get user-agent strings from file
    f = open('user-agents.txt', 'r')
    agent_strings = f.readlines()

    # get filename from URL
    m = re.search(r'/([^/]+)$', url)
    filename = m.group(1)
    
    #restart Tor service to get new IP address
    subprocess.Popen(['./easy_sudo','sudo','service','tor','restart']).wait()
    print('\nRestarted Tor service')

    # pause for Tor restart to take effect
    report_str = 'Waiting ' + str(wait_time) + ' seconds for Tor service restart to take effect...'
    if wait_time == 1:
        report_str = report_str.replace("seconds","second")
    print(report_str)
    time.sleep(wait_time)

    # download and print IP address check
    url_check = subprocess.check_output(['torify','wget','-q','-O','-','icanhazip.com/']).decode().rstrip()
    print('\nTor URL: ' + url_check)

    # get and print random user-agent
    random_agent = agent_strings[random.randint(0, len(agent_strings)-1)].rstrip()
    print('Random User-Agent: ' + random_agent + "\n")
    
    # build wget user-agent header argument string
    user_agent_header_str = '--header="User-Agent: ' + random_agent + '"'

    # download file through torify
    os_str = 'torify wget ' + user_agent_header_str + " " + url + " -P " + download_folder
    os.system(os_str)  # user-agent header argument didn't work with subprocess
    
    # write event to log.txt
    time_str = time.strftime("%Y-%m-%d %H:%M")
    new_log_str = time_str + ' - Downloaded ' + filename + ' with URL ' \
                    + url_check + ' and user-agent ' + random_agent
    f = open('log.txt', 'a')
    f.write(new_log_str + "\n")
    f.close()


if __name__ == '__main__':
    
    if len(sys.argv) == 3:    # explicit download folder argument passed
        download(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:  # no folder argument passed (use ~/Downloads folder)
        download(sys.argv[1]) # no arguments passed, output syntax guide
    else:
        print('\nSyntax:   torthisfile.py   URL   [DOWNLOAD_FOLDER]\n')