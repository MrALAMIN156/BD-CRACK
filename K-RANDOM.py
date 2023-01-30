import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
bit = platform.architecture()[0]
 
if bit == "64bit":
        os.system('xdg-open https://facebook.com/groups/651079003382136/')
 
        from RANDOM import boss
 
        menu()
 
 
 
elif bit == "32bit":
 
        os.system('xdg-open https://facebook.com/groups/651079003382136/')
 
        os.system('python RANDOM.py')
