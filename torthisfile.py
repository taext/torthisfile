#!/home/dd/anaconda3/bin/python
import requests, re, time, sys, random, os, subprocess, datetime, time

# ttf.py - Tor This File Downloader v1.98
# Download file using random IPs and user-agents
# november 10th 2019 by gh/taext
# what's new: update for single-use downloading


def download_w_tor(url, download_folder="~/Downloads/"):
    
    """Download a file using random IP and user-agent"""

    # get user-agent strings from file
    f = open('user-agents.txt', 'r')
    agent_strings = f.readlines()

    # get filename from URL
    m = re.search(r'/([^/]+)$', url)
    filename = m.group(1)
    
    #restart Tor service to get new IP address
    subprocess.Popen(['sudo','service','tor','restart']).wait()
    print('\nRestarted Tor service')

    # pause for Tor restart to take effect
    print('Waiting 1 seconds for Tor service restart to take effect...')
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

    # # random delay in specified range
    # randinteger = random.randint(time_delay_from, time_delay_to)
    # randintstr = str(datetime.timedelta(seconds=randinteger))
    # print('sleeping randomly for ' + randintstr)
    # time.sleep(randinteger)


if __name__ == '__main__':

    if len(sys.argv) == 3:
        download_w_tor(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        download_w_tor(sys.argv[1])
    else:
        print('\nSyntax:   run.py URL\n')