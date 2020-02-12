import passw
import paho.mqtt.client as mqtt
import os, urlparse

# Define event callbacks
def publish(msg):
	print (msg)
	mqttc.publish(topic, msg)

def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def on_message(client, obj, msg):
    print(str(msg.payload));

def on_publish(client, obj, mid):
    pass
    #print("mid_: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
#mqttc.on_log = on_log


# Connect
mqttc.username_pw_set(passw.user, passw.psw)
mqttc.connect(passw.server, passw.port)
topic='test'
# Start subscribe, with QoS level 0
mqttc.subscribe('topic_rx', 0)

# Publish a message
mqttc.publish(topic, 'test')
#mqttc.publish(topic,topic)
# Continue the network loop, exit when an error occurs
rc = 0
import time
i=0
while rc == 0:
	time.sleep(2)
	i=i+1
	mqttc.publish(topic, 'i='+str(i))
	rc=mqttc.loop()
print("rc: " + str(rc))






