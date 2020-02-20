import os
import platform

os.system('clear')
def banner():
    print ("""\033[1;33m


                   /$$  /$$$$$$  /$$       /$$                                  
                  |__/ /$$__  $$|__/      | $$                                  
     /$$  /$$  /$$ /$$| $$  \__/ /$$  /$$$$$$$ /$$   /$$ /$$$$$$/$$$$   /$$$$$$ 
    | $$ | $$ | $$| $$| $$$$    | $$ /$$__  $$| $$  | $$| $$_  $$_  $$ /$$__  $$
    | $$ | $$ | $$| $$| $$_/    | $$| $$  | $$| $$  | $$| $$ \ $$ \ $$| $$  \ $$
    | $$ | $$ | $$| $$| $$      | $$| $$  | $$| $$  | $$| $$ | $$ | $$| $$  | $$
    |  $$$$$/$$$$/| $$| $$      | $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/
     \_____/\___/ |__/|__/      |__/ \_______/ \______/ |__/ |__/ |__/| $$____/ 
                                                                      | $$      
                                                                      | $$      
                                                                      |__/ \033[0;37;40m \n""")

    print "\033[32m cod By :" "Abdullah Al-hajj" "| github : www.github.com/torgodly | @torgodly \n"

banner()
print "Please choose your operating system.\n"
print " 1) linux"
print " 2) Windows\n"

OS = raw_input("wifidump>>")
print ''

# linux tool
while OS == '1'  and platform.system() == "Linux":
    print 'type "scan" to scan your networks\n'
    scaner = raw_input("wifidump>>"+"\033[1;31mlinux\033[1;m"+"\033[32m>>")
    if scaner == "scan":
        os.system('clear')
        banner()
        print "#" * 40 + " - All wireless networks you have - " + "#" * 40 + '\n'
        wifilinux = os.system('ls /etc/NetworkManager/system-connections/')
        print ""
        print'#' * 80 + '\n'
        print '\033[1;34mtype your network name\n\033[1;m'
        network = raw_input("\033[32mwifidump>>"+"\033[1;31mlinux\033[1;m"+"\033[32m>>")
        print'#' * 40 + " - here you go the password is after the 'psk=' - " + '#' * 40
        password = str(os.system("egrep -h -s -A 0 --color -T 'security=|key-mgmt=|psk=' /etc/NetworkManager/system-connections/" + network))
        print'\033[32m#' * 80
    else:
        os.system(exit())
#windows tool
while OS == '2' and platform.system() == "Windows":
    print 'type "scan" to scan your networks\n'
    scanerwin = raw_input("wifidump>>"+"\033[1;31mWindows\033[1;m"+"\033[32m>>")
    if scanerwin == "scan":
        os.system('cls')
        banner()
        print "#" * 40 + " - All wireless networks you have - " + "#" * 40 + '\n'
        wifiwin = os.system('netsh wlan show profile')
        print ""
        print'#' * 80 + '\n'
        print 'type your network name\n'
        networkwin = raw_input("wifidump>>" + "\033[1;31mWindows\033[1;m" + "\033[32m>>")
        print'#' * 40 + " - here you go the password is after the 'Key Content' - " + '#' * 40
        passwordwin = os.system('netsh wlan show profile' + networkwin + 'key=clear')
        print'\033[32m#' * 80
    else:
        os.system(exit())
