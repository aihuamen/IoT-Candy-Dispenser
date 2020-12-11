from dotenv import load_dotenv
load_dotenv()

import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
from datetime import datetime
import time
import json
import random
import ssl
import os

port = 1883 # default port
Server_ip = os.getenv("SERVER_IP")

Update_Topic = "@shadow/data/get"
Subscribe_Topic = "@private/shadow/data/get/response"
Publish_Topic = "@shadow/data/update"

Client_ID = os.getenv("CLIENT_ID")
Token = os.getenv("TOKEN")
Secret = os.getenv("SECRET")


MqttUser_Pass = {"username":Token,"password":Secret}
candy_data = {
    "Guest": 0, 
    "Reject": 0, 
    "Admin": 0,
    "Weight": 0,
    "Log": []
}

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("MQTT connect!")
    client.subscribe(Subscribe_Topic)

def on_message(client, userdata, msg):
    global candy_data

    data_receive = msg.payload.decode("UTF-8")
    update = json.loads(data_receive)

    candy_data["Guest"] = update["data"]["Guest"]
    candy_data["Admin"] = update["data"]["Admin"]
    candy_data["Reject"] = update["data"]["Reject"]
    candy_data["Weight"] = update["data"]["Weight"]
    candy_data["Log"] = update["data"]["Log"]

client = mqtt.Client(protocol=mqtt.MQTTv311,client_id=Client_ID, clean_session=True)
client.on_connect = on_connect
client.on_message = on_message

client.subscribe(Subscribe_Topic)
client.username_pw_set(Token,Secret)
client.connect(Server_ip, port)
client.loop_start()

def mqtt_update():
    client.publish(Update_Topic, retain=True)
    print('MQTTUpdateData')

def mqtt_guest(amt):
    global candy_data
    timen = datetime.now()
    timef = str(datetime.timestamp(timen))
    timec = timen.strftime("%c")

    candy_data["Weight"] += amt
    candy_data["Guest"] += 1
    candy_data["Log"].append({"type": "guest","weight": amt, "time": timec})
    data_out = json.dumps({"data": candy_data})
    client.publish(Publish_Topic, data_out, retain=True)
    print("MQTTGuest")

def mqtt_admin(name,amt):
    global candy_data
    timen = datetime.now()
    timef = str(datetime.timestamp(timen))
    timec = timen.strftime("%c")

    candy_data["Weight"] += amt
    candy_data["Admin"] += 1
    candy_data["Log"].append({"type": "admin","name":name, "weight": amt, "time": timec})
    data_out = json.dumps({"data": candy_data})
    client.publish(Publish_Topic, data_out, retain=True)
    print("MQTTAdmin")

def mqtt_reject():
    global candy_data
    timen = datetime.now()
    timef = str(datetime.timestamp(timen))
    timec = timen.strftime("%c")

    candy_data["Reject"] += 1
    candy_data["Log"].append({"type":"reject","time": timec})
    data_out = json.dumps({"data": candy_data})
    client.publish(Publish_Topic, data_out, retain=True)
    print("MQTTReject")

def mqtt_reset(name):
    global candy_data
    timen = datetime.now()
    timef = str(datetime.timestamp(timen))
    timec = timen.strftime("%c")

    candy_data["Admin"] = 0
    candy_data["Reject"] = 0
    candy_data["Weight"] = 0
    candy_data["Guest"] = 0
    candy_data["Log"].append({"type": "reset","name": name,"time": timec})
    data_out = json.dumps({"data": candy_data})
    client.publish(Publish_Topic, data_out, retain=True)
    print("MQTTReset")



