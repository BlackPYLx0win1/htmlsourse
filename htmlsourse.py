_authur_ = "BlackPY"
print("*******************")
print("*******************")
print("*****  BlackPY   *****")
print(" My channel in Telegram : @Termux_Tools")
print("*******************")
import requests 
link = input("Enter sitename:")
req = requests.get(link)
print(req.text)
