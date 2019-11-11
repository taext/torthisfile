#!/home/dd/anaconda3/bin/python
""" ttf.py - Tor This File - Download file via Tor (with random IP and user-agent) """

import requests, re, time, sys, random, os, subprocess, datetime, time

installation_guide = "apt install tor"

version = "v2.01"
date = "November 10th 2019" 
author = "github/taext"
summary = "Download file via Tor (with random IP and user-agent)"
whats_new = "use easy_sudo credentials"

def about(): 
    print(summary + "\n" + version + " - " + date + " - by " + author)

wait_time = 1

def download(url, download_folder="~/Downloads/"):
    
    """Download a file using random IP and user-agent"""

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
    time.sleep(1)

    # download and print IP address check
    url_check = subprocess.check_output(['torify','wget','-q','-O','-','icanhazip.com/']).decode().rstrip()
    print('\nTor URL: ' + url_check)

    # get and print random user-agent
    random_agent = agent_strings[random.randint(0, len(agent_strings))].rstrip()
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

    if len(sys.argv) == 3:
        download(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        download(sys.argv[1])
    else:
        print('\nSyntax:   torthisfile.py   URL   [DOWNLOAD_FOLDER]\n')