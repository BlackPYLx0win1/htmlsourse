_authur_ = "BlackPY"
print("*******************")
print("*******************")
print("*****  BlackPY   *****")
print(" My channel in Telegram : @Termux_Tools")
print("*******************")
pip install requests 
import requests 
link = input ("Enter sitename:")
req = requests.get(link)
print(req.text)
