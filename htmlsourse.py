_authur_ = "BlackPY"
print ("                    
| __ )| | __ _  ___| | _|  _ \ \ / /
|  _ \| |/ _` |/ __| |/ / |_) \ V /
| |_) | | (_| | (__|   <|  __/ | |
|____/|_|\__,_|\___|_|\_\_|    |_|    
  ")
import os
import requests 
os.system ("pip install requests")
link = input ("Enter sitename:")
req = requests.get(link)
print(req.text)
