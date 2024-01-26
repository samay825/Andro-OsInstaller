# ----- Simple adb connect 
# ----- coded by samay 
# ----- Script chori krke fayda nahi tum yeh code se kuch siklo 
# ----- dont be script kiddie just learn something from this code 

import os ,sys
import subprocess
try:
    import colorama
    import requests
except ImportError:
    _ = os.system('pip install colorama' if os.name=='nt' else 'pip3 install colorama')
    _ = os.system('pip install requests' if os.name=='nt' else 'pip3 install requests')

from time import sleep
import requests
from colorama import Fore

os.system('pkg install android-tools')

# ------- colors
red = Fore.RED
green = Fore.GREEN
white = Fore.WHITE
yellow = Fore.YELLOW
blue = Fore.BLUE

# ---- banner 

logo = Fore.GREEN+''' █████╗ ██████╗ ██████╗ 
'''+Fore.MAGENTA+'''██╔══██╗██╔══██╗██╔══██╗
███████║██║  ██║██████╔╝
'''+Fore.YELLOW+'''██╔══██║██║  ██║██╔══██╗
'''+Fore.BLUE+'''██║  ██║██████╔╝██████╔╝
╚═╝  ╚═╝╚═════╝ ╚═════╝ '''


def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def backlash():
    print('\n')


def banner():
    print(logo)

def cleanscreen():
    clear()
    banner()
    backlash()

def STart():
    clear()
    banner()
    print(Fore.RED+'[ '+Fore.GREEN+'Disable Phantom process '+Fore.RED+']')


class SamayFun:

    def __init__(self):
        for i in os.listdir():
            if not 'adblatest' in i:
                return False
        self.path1 = os.path.expanduser('~') + '/'
        self.path2 = os.getcwd() + '/'
        self.path3 = os.getcwd() + '/adblatest/'

    def AdbDevicePair(self,ipport,ports,code):
        sdk_path = os.getcwd() + '/adblatest/'
        env = os.environ.copy()
        env["PATH"] = f"{env['PATH']}:{sdk_path}"
        self.command_1 = f'adb pair {ipport}:{ports} {code}'
        backlash()
        subprocess.run(self.command_1,env=env,shell=True)

    def AdbDeviceConnect(self,ipport,mainport):
        sdk_path = os.getcwd() + '/adblatest/'
        env = os.environ.copy()
        env["PATH"] = f"{env['PATH']}:{sdk_path}"
        self.command_2 = f'adb connect {ipport}:{mainport}'
        self.command_3 = 'adb devices'
        subprocess.run(self.command_2,env=env,shell=True)
        sleep(3)
        subprocess.run(self.command_3,env=env,shell=True)
        backlash()
        cleanscreen()
        print('Removing Phantom Process')
        backlash()
        self.command_4 = 'adb shell "/system/bin/device_config set_sync_disabled_for_tests persistent"'
        self.command_5 = 'adb shell "/system/bin/device_config put activity_manager max_phantom_processes 2147483647"'
        self.command_6 = 'adb shell settings put global settings_enable_monitor_phantom_procs false'
        subprocess.run(self.command_4,env=env,shell=True)
        sleep(1)
        subprocess.run(self.command_5,env=env,shell=True)
        sleep(1)
        subprocess.run(self.command_6,env=env,shell=True)
        print('Phantom Process Disabled Successfully !!')



    
    def Condition1(self,name1):
        if ':' in name1:
            pass
        else:
            return False
        
    def ErrorFIx(self,text):
        print(Fore.GREEN+f'{text}')
        backlash()
        print(Fore.RED+'Returning home ...')
        sleep(3)
        os.system('python Disable_Phantom.py' if os.name=='nt' else 'python3 Disable_Phantom.py')
        sys.exit()
        return True
        



class Main(SamayFun):

    def __init__(self):
        STart()
        backlash()
        self.samaybhai = input(Fore.WHITE+'Enter the ip & Port '+Fore.RED+'>>> '+Fore.GREEN).strip()
        self.recievedata = super().Condition1(self.samaybhai)
        if self.recievedata == False:
            cleanscreen()
            self.excuterror = super().ErrorFIx('Enter the Correct Format ex: 193.543.6.1:87654')
        self.splitedtext = self.samaybhai.split(':')[0]
        self.data2 = self.samaybhai.split(':')[1]
        self.savediplocal = self.splitedtext
        self.main_assigned_port = self.data2


    def Mainscl(self):
        super().__init__()
        cleanscreen()
        self.ports_names = input(Fore.WHITE+'Enter the Pair Port '+Fore.RED+'>>> '+Fore.GREEN).strip()
        self.codesname_rec = input(Fore.WHITE+'Enter the Wifi Paring Code '+Fore.RED+'>>> '+Fore.GREEN).strip()
        super().AdbDevicePair(self.savediplocal,self.ports_names,self.codesname_rec)
        sleep(3)
        cleanscreen()
        super().AdbDeviceConnect(self.savediplocal,self.main_assigned_port)

        



if __name__ == '__main__':
    samay = Main()
    samay.Mainscl()


