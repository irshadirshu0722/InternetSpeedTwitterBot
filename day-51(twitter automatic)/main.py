from InternetSpeedTwitterBot import InternetSpeedTwitterBot
username = ""
password = ""
ob = InternetSpeedTwitterBot(username,password)
ob.get_internet_speed()
message = f"hey internet provider , why is my internet speed {ob.download}down/{ob.upload}up when i pay for 150down/10up"
if int(ob.download)<100:
    ob.send_tweet(message)