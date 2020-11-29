
#!/usr/bin/env python3

################################################################################
# Copyright (c) 2020, NVIDIA CORPORATION. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
################################################################################
import argparse
import sys
sys.path.append('../')
sys.path.insert(0, "../../../client_libraries/python/")
import paho.mqtt.client as mqtt
import sparkplug_b as sparkplug
import time
import time, threading
import random
import string
import gi
import configparser
gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import GObject, Gst, GstRtspServer
from gi.repository import GObject, Gst
from gi.repository import GLib
from ctypes import *
import sys
import math
import platform
from common.is_aarch_64 import is_aarch64
from common.bus_call import bus_call
from common.FPS import GETFPS
from sparkplug_b import *
import pyds


fps_streams={}

# Application Variables
serverUrl = "localhost"
myGroupId = "Sparkplug B Devices"
myNodeName = "NVIDIA"
myDeviceName = "XavierNX"
publishPeriod = 5000
myUsername = "admin"
myPassword = "changeme"
client = mqtt.Client(serverUrl, 1883, 60)
WAIT_SECONDS = 1
frame_numberx = 0
num_rectsx = 0

TOOTHBRUSH = 0
HAIR_DRYER = 0
TEDDY_BEAR = 0
SCISSORS = 0
VASE = 0
CLOCK = 0
BOOK = 0
REFRIGERATOR = 0
SINK = 0
TOASTER = 0
OVEN = 0
MICROWAVE = 0
CELL_PHONE = 0
KEYBOARD = 0
REMOTE = 0
MOUSE = 0
LAPTOP = 0
TVMONITOR = 0
TOILET = 0
DININGTABLE= 0
BED = 0
POTTEDPLANT = 0
SOFA = 0
CHAIR = 0
CAKE = 0
DONUT = 0
PIZZA = 0
HOT_DOG = 0
CARROT = 0
BROCCOLI = 0
ORANGE = 0
SANDWICH = 0
APPLE = 0
BANANA = 0
BOWL = 0
SPOON = 0
KNIFE = 0
FORK = 0
CUP = 0
WINE_GLASS = 0
BOTTLE = 0
TENNIS_RACKET = 0
SURFBOARD = 0
SKATEBOARD = 0
BASEBALL_GLOVE = 0
BASEBALL_BAT = 0
KITE = 0
SPORTS_BALL = 0
SNOWBOARD = 0
SKIS = 0
FRISBEE = 0
SUITCASE = 0
TIE = 0
HANDBAG = 0
UMBRELLA = 0
BACKPACK = 0
GIRAFFE = 0 
ZEBRA = 0
BEAR = 0
ELEPHANT = 0
COW = 0
SHEEP = 0
HORSE = 0
DOG = 0
CAT = 0
BIRD = 0
BENCH = 0
PARKING_METER = 0
STOP_SIGN = 0
FIRE_HYDRANT = 0
TRAFFIC_LIGHT = 0
BOAT = 0
TRUCK = 0
TRAIN = 0
BUS = 0
AEROPLANE = 0
MOTORBIKE = 0
VEHICLE = 0
BICYCLE = 0
PERSON = 0


class AliasMap:
    Next_Server = 0
    Rebirth = 1
    Reboot = 2
    Device_frame_numberx = 3
    Device_num_rectsx = 4
    Device_Metric0 = 5
    Device_Metric1 = 6
    Device_Metric2 = 7
    Device_Metric3 = 8
    Device_TOOTHBRUSH = 9
    Device_HAIR_DRYER = 10
    Device_TEDDY_BEAR = 11
    Device_SCISSORS = 12
    Device_VASE = 13
    Device_CLOCK = 14
    Device_BOOK = 15
    Device_REFRIGERATOR = 16
    Device_SINK = 17
    Device_TOASTER = 18
    Device_OVEN = 19
    Device_MICROWAVE = 20
    Device_CELL_PHONE = 21
    Device_KEYBOARD = 22
    Device_REMOTE = 23
    Device_MOUSE = 24
    Device_LAPTOP = 25
    Device_TVMONITOR = 26
    Device_TOILET = 27
    Device_DININGTABLE = 28
    Device_BED = 29
    Device_POTTEDPLANT = 30
    Device_SOFA = 31
    Device_CHAIR = 32
    Device_CAKE = 33
    Device_DONUT = 34
    Device_PIZZA = 35
    Device_HOT_DOG = 36
    Device_CARROT = 37
    Device_BROCCOLI = 38
    Device_ORANGE = 39
    Device_SANDWICH = 40
    Device_APPLE = 41
    Device_BANANA = 42
    Device_BOWL = 43
    Device_SPOON = 44
    Device_KNIFE = 45
    Device_FORK = 46
    Device_CUP = 47
    Device_WINE_GLASS = 48
    Device_BOTTLE = 49
    Device_TENNIS_RACKET = 50
    Device_SURFBOARD = 51
    Device_SKATEBOARD = 52
    Device_BASEBALL_GLOVE = 53
    Device_BASEBALL_BAT = 54
    Device_KITE = 55
    Device_SPORTS_BALL = 56
    Device_SNOWBOARD = 57
    Device_SKIS = 58
    Device_FRISBEE = 59
    Device_SUITCASE = 60
    Device_TIE = 61
    Device_HANDBAG = 62
    Device_UMBRELLA = 63
    Device_BACKPACK = 64
    Device_GIRAFFE = 65
    Device_ZEBRA = 66
    Device_BEAR = 67
    Device_ELEPHANT = 68
    Device_COW = 69
    Device_SHEEP = 70
    Device_HORSE = 71
    Device_DOG = 72
    Device_CAT = 73
    Device_BIRD = 74
    Device_BENCH = 75
    Device_PARKING_METER = 76
    Device_STOP_SIGN = 77
    Device_FIRE_HYDRANT = 78
    Device_BOAT = 79
    Device_TRAFFIC_LIGHT = 80
    Device_TRUCK = 81
    Device_TRAIN = 82
    Device_BUS = 83
    Device_AEROPLANE = 84
    Device_MOTORBIKE = 85
    Device_VEHICLE = 86
    Device_BICYCLE = 87
    Device_PERSON = 88
  

MAX_DISPLAY_LEN=64
PGIE_CLASS_ID_TOOTHBRUSH = 79
PGIE_CLASS_ID_HAIR_DRYER = 78
PGIE_CLASS_ID_TEDDY_BEAR = 77
PGIE_CLASS_ID_SCISSORS = 76
PGIE_CLASS_ID_VASE = 75
PGIE_CLASS_ID_CLOCK = 74
PGIE_CLASS_ID_BOOK = 73
PGIE_CLASS_ID_REFRIGERATOR = 72
PGIE_CLASS_ID_SINK = 71
PGIE_CLASS_ID_TOASTER = 70
PGIE_CLASS_ID_OVEN = 69
PGIE_CLASS_ID_MICROWAVE = 68
PGIE_CLASS_ID_CELL_PHONE = 67
PGIE_CLASS_ID_KEYBOARD = 66
PGIE_CLASS_ID_REMOTE = 65
PGIE_CLASS_ID_MOUSE = 64
PGIE_CLASS_ID_LAPTOP = 63
PGIE_CLASS_ID_TVMONITOR = 62
PGIE_CLASS_ID_TOILET = 61
PGIE_CLASS_ID_DININGTABLE= 60
PGIE_CLASS_ID_BED = 59
PGIE_CLASS_ID_POTTEDPLANT = 58
PGIE_CLASS_ID_SOFA = 57
PGIE_CLASS_ID_CHAIR = 56
PGIE_CLASS_ID_CAKE = 55
PGIE_CLASS_ID_DONUT = 54
PGIE_CLASS_ID_PIZZA = 53
PGIE_CLASS_ID_HOT_DOG = 52
PGIE_CLASS_ID_CARROT = 51
PGIE_CLASS_ID_BROCCOLI = 50
PGIE_CLASS_ID_ORANGE = 49
PGIE_CLASS_ID_SANDWICH = 48
PGIE_CLASS_ID_APPLE = 47
PGIE_CLASS_ID_BANANA = 46
PGIE_CLASS_ID_BOWL = 45
PGIE_CLASS_ID_SPOON = 44
PGIE_CLASS_ID_KNIFE = 43
PGIE_CLASS_ID_FORK = 42
PGIE_CLASS_ID_CUP = 41
PGIE_CLASS_ID_WINE_GLASS = 40
PGIE_CLASS_ID_BOTTLE = 39
PGIE_CLASS_ID_TENNIS_RACKET = 38
PGIE_CLASS_ID_SURFBOARD = 37
PGIE_CLASS_ID_SKATEBOARD = 36
PGIE_CLASS_ID_BASEBALL_GLOVE = 35
PGIE_CLASS_ID_BASEBALL_BAT = 34
PGIE_CLASS_ID_KITE = 33
PGIE_CLASS_ID_SPORTS_BALL = 32
PGIE_CLASS_ID_SNOWBOARD = 31
PGIE_CLASS_ID_SKIS = 30
PGIE_CLASS_ID_FRISBEE = 29
PGIE_CLASS_ID_SUITCASE = 28
PGIE_CLASS_ID_TIE = 27
PGIE_CLASS_ID_HANDBAG = 26
PGIE_CLASS_ID_UMBRELLA = 25
PGIE_CLASS_ID_BACKPACK = 24
PGIE_CLASS_ID_GIRAFFE = 23
PGIE_CLASS_ID_ZEBRA = 22
PGIE_CLASS_ID_BEAR = 21
PGIE_CLASS_ID_ELEPHANT = 20
PGIE_CLASS_ID_COW = 19
PGIE_CLASS_ID_SHEEP = 18
PGIE_CLASS_ID_HORSE = 17
PGIE_CLASS_ID_DOG = 16
PGIE_CLASS_ID_CAT = 15
PGIE_CLASS_ID_BIRD = 14
PGIE_CLASS_ID_BENCH = 13
PGIE_CLASS_ID_PARKING_METER = 12
PGIE_CLASS_ID_STOP_SIGN = 11
PGIE_CLASS_ID_FIRE_HYDRANT = 10
PGIE_CLASS_ID_TRAFFIC_LIGHT = 9
PGIE_CLASS_ID_BOAT = 8
PGIE_CLASS_ID_TRUCK = 7
PGIE_CLASS_ID_TRAIN = 6
PGIE_CLASS_ID_BUS = 5
PGIE_CLASS_ID_AEROPLANE = 4
PGIE_CLASS_ID_MOTORBIKE = 3
PGIE_CLASS_ID_VEHICLE = 2
PGIE_CLASS_ID_BICYCLE = 1
PGIE_CLASS_ID_PERSON = 0
MUXER_OUTPUT_WIDTH=1920
MUXER_OUTPUT_HEIGHT=1080
MUXER_BATCH_TIMEOUT_USEC=4000000
TILED_OUTPUT_WIDTH=1280
TILED_OUTPUT_HEIGHT=720
GST_CAPS_FEATURES_NVMM="memory:NVMM"
OSD_PROCESS_MODE= 0
OSD_DISPLAY_TEXT= 1
pgie_classes_str= ["Toothbrush", "Hair dryer", "Teddy bear","Scissors","Vase", "Clock", "Book","Refrigerator", "Sink", "Toaster","Oven","Microwave", "Cell phone", "Keyboard","Remote", "Mouse", "Laptop","Tvmonitor","Toilet", "Diningtable", "Bed","Pottedplant", "Sofa", "Chair","Cake","Donut", "Pizza", "Hot dog","Carrot", "Broccli", "Orange","Sandwich","Apple", "Banana", "Bowl","Spoon", "Knife", "Fork","Cup","Wine Glass", "Bottle", "Tennis racket","Surfboard", "Skateboard", "Baseball glove","Baseball bat","Kite", "Sports ball", "Snowboard","Skis", "Frisbee", "Suitcase","Tie","Handbag", "Umbrella", "Backpack","Giraffe", "Zebra", "Bear","Elephant","Cow", "Sheep", "Horse","Dog", "Cat", "Bird","Bench","Parking meter", "Stop sign", "Fire hydrant","Traffic light", "Boat", "Truck","Train","Bus", "Areoplane", "Motorbike","Car", "Bicycle", "Person"]
######################################################################
# The callback for when the client receives a CONNACK response from the server.
######################################################################
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected with result code "+str(rc))
    else:
        print("Failed to connect with result code "+str(rc))
        sys.exit()

    global myGroupId
    global myNodeName

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("spBv1.0/" + myGroupId + "/NCMD/" + myNodeName + "/#")
    client.subscribe("spBv1.0/" + myGroupId + "/DCMD/" + myNodeName + "/#")

######################################################################
# The callback for when a PUBLISH message is received from the server.
######################################################################

def on_message(client, userdata, msg):
    print("Message arrived: " + msg.topic)
    tokens = msg.topic.split("/")

    if tokens[0] == "spBv1.0" and tokens[1] == myGroupId and (tokens[2] == "NCMD" or tokens[2] == "DCMD") and tokens[3] == myNodeName:
        inboundPayload = sparkplug_b_pb2.Payload()
        inboundPayload.ParseFromString(msg.payload)
        for metric in inboundPayload.metrics:
            if metric.name == "Node Control/Next Server" or metric.alias == AliasMap.Next_Server:
                # 'Node Control/Next Server' is an NCMD used to tell the device/client application to
                # disconnect from the current MQTT server and connect to the next MQTT server in the
                # list of available servers.  This is used for clients that have a pool of MQTT servers
                # to connect to.
                print ("'Node Control/Next Server' is not implemented in this example")
            elif metric.name == "Node Control/Rebirth" or metric.alias == AliasMap.Rebirth:
                # 'Node Control/Rebirth' is an NCMD used to tell the device/client application to resend
                # its full NBIRTH and DBIRTH again.  MQTT Engine will send this NCMD to a device/client
                # application if it receives an NDATA or DDATA with a metric that was not published in the
                # original NBIRTH or DBIRTH.  This is why the application must send all known metrics in
                # its original NBIRTH and DBIRTH messages.
                publishBirth()
            elif metric.name == "Node Control/Reboot" or metric.alias == AliasMap.Reboot:
                # 'Node Control/Reboot' is an NCMD used to tell a device/client application to reboot
                # This can be used for devices that need a full application reset via a soft reboot.
                # In this case, we fake a full reboot with a republishing of the NBIRTH and DBIRTH
                # messages.
                publishBirth()
            elif metric.name == "output/Device Metric2" or metric.alias == AliasMap.Device_Metric2:
                # This is a metric we declared in our DBIRTH message and we're emulating an output.
                # So, on incoming 'writes' to the output we must publish a DDATA with the new output
                # value.  If this were a real output we'd write to the output and then read it back
                # before publishing a DDATA message.

                # We know this is an Int16 because of how we declated it in the DBIRTH
                newValue = metric.int_value
                print ("CMD message for output/Device Metric2 - New Value: {}".format(newValue))

                # Create the DDATA payload - Use the alias because this isn't the DBIRTH
                payload = sparkplug.getDdataPayload()
                addMetric(payload, None, AliasMap.Device_Metric2, MetricDataType.Int16, newValue)

                # Publish a message data
                byteArray = bytearray(payload.SerializeToString())
                client.publish("spBv1.0/" + myGroupId + "/DDATA/" + myNodeName + "/" + myDeviceName, byteArray, 0, False)
            elif metric.name == "output/Device Metric3" or metric.alias == AliasMap.Device_Metric3:
                # This is a metric we declared in our DBIRTH message and we're emulating an output.
                # So, on incoming 'writes' to the output we must publish a DDATA with the new output
                # value.  If this were a real output we'd write to the output and then read it back
                # before publishing a DDATA message.

                # We know this is an Boolean because of how we declated it in the DBIRTH
                newValue = metric.boolean_value
                print ("CMD message for output/Device Metric3 - New Value: %r" % newValue)

                # Create the DDATA payload - use the alias because this isn't the DBIRTH
                payload = sparkplug.getDdataPayload()
                addMetric(payload, None, AliasMap.Device_Metric3, MetricDataType.Boolean, newValue)

                # Publish a message data
                byteArray = bytearray(payload.SerializeToString())
                client.publish("spBv1.0/" + myGroupId + "/DDATA/" + myNodeName + "/" + myDeviceName, byteArray, 0, False)
            else:
                print ("Unknown command: " + metric.name)
    else:
        print ("Unknown command...")

    print ("Done publishing")

######################################################################
# Publish the BIRTH certificates
######################################################################
def publishBirth():
    publishNodeBirth()
    publishDeviceBirth()
######################################################################
# Publish the NBIRTH certificate
######################################################################
def publishNodeBirth():
    print ("Publishing Node Birth")

    # Create the node birth payload
    payload = sparkplug.getNodeBirthPayload()

    # Set up the Node Controls
    addMetric(payload, "Node Control/Next Server", AliasMap.Next_Server, MetricDataType.Boolean, False)
    addMetric(payload, "Node Control/Rebirth", AliasMap.Rebirth, MetricDataType.Boolean, False)
    addMetric(payload, "Node Control/Reboot", AliasMap.Reboot, MetricDataType.Boolean, False)

    # Publish the node birth certificate
    byteArray = bytearray(payload.SerializeToString())
    client.publish("spBv1.0/" + myGroupId + "/NBIRTH/" + myNodeName, byteArray, 0, False)

######################################################################
# Publish the DBIRTH certificate
######################################################################
def publishDeviceBirth():
    print ("Publishing Device Birth")

    # Get the payload
    payload = sparkplug.getDeviceBirthPayload()
 
  
    # Add some device metrics
    addMetric(payload, "input/Frame Number", AliasMap.Device_frame_numberx, MetricDataType.Int16, frame_numberx )
    addMetric(payload, "input/Device Metric0", AliasMap.Device_Metric0, MetricDataType.String, "hello device")
    addMetric(payload, "input/Device Metric1", AliasMap.Device_Metric1, MetricDataType.Boolean, True)
    addMetric(payload, "input/Number of Objects", AliasMap.Device_num_rectsx, MetricDataType.Int16, num_rectsx )
    addMetric(payload, "output/Device Metric2", AliasMap.Device_Metric2, MetricDataType.Int16, 3)
    addMetric(payload, "output/Device Metric3", AliasMap.Device_Metric3, MetricDataType.Boolean, True)
    addMetric(payload, "input/PERSON ", AliasMap.Device_PERSON, 
MetricDataType.Int16, PERSON  )
    addMetric(payload, "input/BICYCLE", AliasMap.Device_BICYCLE, 
MetricDataType.Int16, BICYCLE )
    addMetric(payload, "input/VEHICLE ", AliasMap.Device_VEHICLE  , 
MetricDataType.Int16, VEHICLE )
    addMetric(payload, "input/MOTORBIKE", AliasMap.Device_MOTORBIKE , 
MetricDataType.Int16, MOTORBIKE)
    addMetric(payload, "input/AEROPLANE", AliasMap.Device_AEROPLANE,
MetricDataType.Int16, AEROPLANE )
    addMetric(payload, "input/BUS", AliasMap.Device_BUS, 
MetricDataType.Int16, BUS )
    addMetric(payload, "input/TRAIN ", AliasMap.Device_TRAIN, 
MetricDataType.Int16, TRAIN  )
    addMetric(payload, "input/TRUCK", AliasMap.Device_TRUCK, 
MetricDataType.Int16, TRUCK )
    addMetric(payload, "input/BOAT ", AliasMap.Device_BOAT  , 
MetricDataType.Int16, BOAT )
    addMetric(payload, "input/TRAFFIC_LIGHT", AliasMap.Device_TRAFFIC_LIGHT,
MetricDataType.Int16, TRAFFIC_LIGHT )
    addMetric(payload, "input/FIRE_HYDRANT", AliasMap.Device_FIRE_HYDRANT, 
MetricDataType.Int16, FIRE_HYDRANT )
    addMetric(payload, "input/STOP_SIGN", AliasMap.Device_STOP_SIGN , 
MetricDataType.Int16, STOP_SIGN)
    addMetric(payload, "input/PARKING_METER", AliasMap.Device_PARKING_METER,
MetricDataType.Int16, PARKING_METER )
    addMetric(payload, "input/BENCH", AliasMap.Device_BENCH, 
MetricDataType.Int16, BENCH )
    addMetric(payload, "input/BIRD", AliasMap.Device_BIRD, 
MetricDataType.Int16, BIRD )
    addMetric(payload, "input/CAT", AliasMap.Device_CAT, 
MetricDataType.Int16, CAT )
    addMetric(payload, "input/DOG", AliasMap.Device_DOG , 
MetricDataType.Int16, DOG)
    addMetric(payload, "input/HORSE", AliasMap.Device_HORSE,
MetricDataType.Int16, HORSE )
    addMetric(payload, "input/SHEEP", AliasMap.Device_SHEEP, 
MetricDataType.Int16, SHEEP )
    addMetric(payload, "input/COW", AliasMap.Device_COW, 
MetricDataType.Int16, COW )
    addMetric(payload, "input/ELEPHANT", AliasMap.Device_ELEPHANT, 
MetricDataType.Int16, ELEPHANT )
    addMetric(payload, "input/BEAR", AliasMap.Device_BEAR , 
MetricDataType.Int16, BEAR)
    addMetric(payload, "input/ZEBRA", AliasMap.Device_ZEBRA,
MetricDataType.Int16, ZEBRA )
    addMetric(payload, "input/GIRAFFE", AliasMap.Device_GIRAFFE, 
MetricDataType.Int16, GIRAFFE )
    addMetric(payload, "input/BACKPACK", AliasMap.Device_BACKPACK, 
MetricDataType.Int16, BACKPACK )
    addMetric(payload, "input/UMBRELLA", AliasMap.Device_UMBRELLA, 
MetricDataType.Int16, UMBRELLA )
    addMetric(payload, "input/HANDBAG", AliasMap.Device_HANDBAG , 
MetricDataType.Int16, HANDBAG )
    addMetric(payload, "input/TIE", AliasMap.Device_TIE,
MetricDataType.Int16, TIE )
    addMetric(payload, "input/SUITCASE", AliasMap.Device_SUITCASE, 
MetricDataType.Int16, SUITCASE )
    addMetric(payload, "input/FRISBEE", AliasMap.Device_FRISBEE, 
MetricDataType.Int16, FRISBEE )
    addMetric(payload, "input/SKIS", AliasMap.Device_SKIS, 
MetricDataType.Int16, SKIS )
    addMetric(payload, "input/SNOWBOARD", AliasMap.Device_SNOWBOARD , 
MetricDataType.Int16, SNOWBOARD )
    addMetric(payload, "input/SPORTS_BALL", AliasMap.Device_SPORTS_BALL,
MetricDataType.Int16, SPORTS_BALL )
    addMetric(payload, "input/KITE", AliasMap.Device_KITE, 
MetricDataType.Int16, KITE )
    addMetric(payload, "input/BASEBALL_BAT", AliasMap.Device_BASEBALL_BAT, 
MetricDataType.Int16, BASEBALL_BAT )
    addMetric(payload, "input/BASEBALL_GLOVE", AliasMap.Device_BASEBALL_GLOVE, 
MetricDataType.Int16, BASEBALL_GLOVE )
    addMetric(payload, "input/SKATEBOARD", AliasMap.Device_SKATEBOARD , 
MetricDataType.Int16, SKATEBOARD )
    addMetric(payload, "input/SURFBOARD", AliasMap.Device_SURFBOARD,
MetricDataType.Int16, SURFBOARD )
    addMetric(payload, "input/TENNIS_RACKET", AliasMap.Device_TENNIS_RACKET, 
MetricDataType.Int16, TENNIS_RACKET)
    addMetric(payload, "input/BOTTLE", AliasMap.Device_BOTTLE, 
MetricDataType.Int16, BOTTLE )
    addMetric(payload, "input/WINE_GLASS", AliasMap.Device_WINE_GLASS, 
MetricDataType.Int16, WINE_GLASS )
    addMetric(payload, "input/CUP", AliasMap.Device_CUP, 
MetricDataType.Int16, CUP )
    addMetric(payload, "input/FORK", AliasMap.Device_FORK,
MetricDataType.Int16, FORK )
    addMetric(payload, "input/KNIFE", AliasMap.Device_KNIFE, 
MetricDataType.Int16, KNIFE )
    addMetric(payload, "input/SPOON", AliasMap.Device_SPOON, 
MetricDataType.Int16, SPOON )
    addMetric(payload, "input/BOWL", AliasMap.Device_BOWL, 
MetricDataType.Int16, BOWL )
    addMetric(payload, "input/BANANA", AliasMap.Device_BANANA,
MetricDataType.Int16, BANANA )
    addMetric(payload, "input/APPLE", AliasMap.Device_APPLE, 
MetricDataType.Int16, APPLE )
    addMetric(payload, "input/SANDWICH", AliasMap.Device_SANDWICH, 
MetricDataType.Int16, SANDWICH )
    addMetric(payload, "input/ORANGE", AliasMap.Device_ORANGE, 
MetricDataType.Int16, ORANGE )
    addMetric(payload, "input/BROCCOLI", AliasMap.Device_BROCCOLI,
MetricDataType.Int16, BROCCOLI )
    addMetric(payload, "input/CARROT", AliasMap.Device_CARROT, 
MetricDataType.Int16, CARROT )
    addMetric(payload, "input/HOT_DOG", AliasMap.Device_HOT_DOG, 
MetricDataType.Int16, HOT_DOG )
    addMetric(payload, "input/PIZZA", AliasMap.Device_PIZZA, 
MetricDataType.Int16, PIZZA )
    addMetric(payload, "input/DONUT", AliasMap.Device_DONUT,
MetricDataType.Int16, DONUT )
    addMetric(payload, "input/CAKE", AliasMap.Device_CAKE, 
MetricDataType.Int16, CAKE )
    addMetric(payload, "input/CUP", AliasMap.Device_CUP, 
MetricDataType.Int16, CUP )
    addMetric(payload, "input/CHAIR", AliasMap.Device_CHAIR, 
MetricDataType.Int16, CHAIR )
    addMetric(payload, "input/POTTEDPLANT", AliasMap.Device_POTTEDPLANT,
MetricDataType.Int16, POTTEDPLANT )
    addMetric(payload, "input/BED", AliasMap.Device_BED, 
MetricDataType.Int16, BED )
    addMetric(payload, "input/DININGTABLE", AliasMap.Device_DININGTABLE, 
MetricDataType.Int16, DININGTABLE )
    addMetric(payload, "input/TOILET", AliasMap.Device_TOILET, 
MetricDataType.Int16, TOILET )
    addMetric(payload, "input/TVMONITOR", AliasMap.Device_TVMONITOR, 
MetricDataType.Int16, TVMONITOR )
    addMetric(payload, "input/LAPTOP", AliasMap.Device_LAPTOP, 
MetricDataType.Int16, LAPTOP )
    addMetric(payload, "input/MOUSE", AliasMap.Device_MOUSE, 
MetricDataType.Int16, MOUSE )
    addMetric(payload, "input/REMOTE", AliasMap.Device_REMOTE, 
MetricDataType.Int16, REMOTE )
    addMetric(payload, "input/KEYBOARD", AliasMap.Device_KEYBOARD, 
MetricDataType.Int16, KEYBOARD )
    addMetric(payload, "input/CELL_PHONE", AliasMap.Device_CELL_PHONE, 
MetricDataType.Int16, CELL_PHONE )
    addMetric(payload, "input/MICROWAVE", AliasMap.Device_MICROWAVE, 
MetricDataType.Int16, MICROWAVE )
    addMetric(payload, "input/OVEN", AliasMap.Device_OVEN, 
MetricDataType.Int16, OVEN )
    addMetric(payload, "input/TOASTER", AliasMap.Device_TOASTER, 
MetricDataType.Int16, TOASTER )
    addMetric(payload, "input/SINK", AliasMap.Device_SINK, 
MetricDataType.Int16, SINK )
    addMetric(payload, "input/REFRIGERATOR", AliasMap.Device_REFRIGERATOR, 
MetricDataType.Int16, REFRIGERATOR )
    addMetric(payload, "input/BOOK", AliasMap.Device_BOOK, 
MetricDataType.Int16, BOOK )
    addMetric(payload, "input/CLOCK", AliasMap.Device_CLOCK, 
MetricDataType.Int16, CLOCK )
    addMetric(payload, "input/VASE", AliasMap.Device_VASE, 
MetricDataType.Int16, VASE )
    addMetric(payload, "input/SCISSORS", AliasMap.Device_SCISSORS, 
MetricDataType.Int16, SCISSORS )
    addMetric(payload, "input/TEDDY_BEAR", AliasMap.Device_TEDDY_BEAR, 
MetricDataType.Int16, TEDDY_BEAR )
    addMetric(payload, "input/HAIR_DRYER", AliasMap.Device_HAIR_DRYER, 
MetricDataType.Int16, HAIR_DRYER )
    addMetric(payload, "input/TOOTHBRUSH", AliasMap.Device_TOOTHBRUSH, MetricDataType.Int16, TOOTHBRUSH ) 

    # Publish the initial data with the Device BIRTH certificate
    totalByteArray = bytearray(payload.SerializeToString())
    client.publish("spBv1.0/" + myGroupId + "/DBIRTH/" + myNodeName + "/" + myDeviceName, totalByteArray, 0, False)
######################################################################

# tiler_sink_pad_buffer_probe  will extract metadata received on OSD sink pad
# and update params for drawing rectangle, object information etc.
def tiler_src_pad_buffer_probe(pad,info,u_data):
    global TOOTHBRUSH
    global HAIR_DRYER
    global TEDDY_BEAR 
    global SCISSORS
    global VASE
    global CLOCK
    global BOOK
    global REFRIGERATOR
    global SINK
    global TOASTER
    global OVEN
    global MICROWAVE
    global CELL_PHONE
    global KEYBOARD
    global REMOTE
    global MOUSE
    global LAPTOP
    global TVMONITOR
    global TOILET
    global DININGTABLE
    global BED
    global POTTEDPLANT
    global SOFA
    global CHAIR
    global CAKE
    global DONUT
    global PIZZA
    global HOT_DOG
    global CARROT
    global BROCCOLI
    global ORANGE
    global SANDWICH
    global APPLE
    global BANANA
    global BOWL
    global SPOON
    global KNIFE
    global FORK
    global CUP
    global GLASS
    global BOTTLE
    global TENNIS_RACKET
    global SURFBOARD
    global SKATEBOARD
    global BASEBALL_GLOVE
    global BASEBALL_BAT
    global KITE
    global SPORTS_BALL
    global SNOWBOARD
    global SKIS
    global FRISBEE
    global SUITCASE
    global TIE
    global HANDBAG
    global UMBRELLA
    global BACKPACK
    global GIRAFFE
    global ZEBRA
    global BEAR
    global ELEPHANT
    global COW
    global SHEEP
    global HORSE
    global DOG
    global CAT
    global BIRD
    global BENCH
    global PARKING_METER
    global STOP_SIGN
    global FIRE_HYDRANT
    global TRAFFIC_LIGHT
    global BOAT
    global TRUCK
    global TRAIN
    global BUS
    global AEROPLANE
    global MOTORBIKE
    global VEHICLE
    global BICYCLE
    global PERSON
    

    obj_counter = {
        PGIE_CLASS_ID_TOOTHBRUSH:0,
        PGIE_CLASS_ID_HAIR_DRYER:0,
        PGIE_CLASS_ID_TEDDY_BEAR:0,
        PGIE_CLASS_ID_SCISSORS:0,
        PGIE_CLASS_ID_VASE:0,
        PGIE_CLASS_ID_CLOCK:0,
        PGIE_CLASS_ID_BOOK:0,
        PGIE_CLASS_ID_REFRIGERATOR:0,
        PGIE_CLASS_ID_SINK:0,
        PGIE_CLASS_ID_TOASTER:0,
        PGIE_CLASS_ID_OVEN:0,
        PGIE_CLASS_ID_MICROWAVE:0,
        PGIE_CLASS_ID_CELL_PHONE:0,
        PGIE_CLASS_ID_KEYBOARD:0,
        PGIE_CLASS_ID_REMOTE:0,
        PGIE_CLASS_ID_MOUSE:0,
        PGIE_CLASS_ID_LAPTOP:0,
        PGIE_CLASS_ID_TVMONITOR:0,
        PGIE_CLASS_ID_TOILET:0,
        PGIE_CLASS_ID_DININGTABLE:0,
        PGIE_CLASS_ID_BED:0,
        PGIE_CLASS_ID_POTTEDPLANT:0,
        PGIE_CLASS_ID_SOFA:0,
        PGIE_CLASS_ID_CHAIR:0,
        PGIE_CLASS_ID_CAKE:0,
        PGIE_CLASS_ID_DONUT:0,
        PGIE_CLASS_ID_PIZZA:0,
        PGIE_CLASS_ID_HOT_DOG:0,
        PGIE_CLASS_ID_CARROT:0,
        PGIE_CLASS_ID_BROCCOLI:0,
        PGIE_CLASS_ID_ORANGE:0,
        PGIE_CLASS_ID_SANDWICH:0,
        PGIE_CLASS_ID_APPLE:0,
        PGIE_CLASS_ID_BANANA:0,
        PGIE_CLASS_ID_BOWL:0,
        PGIE_CLASS_ID_SPOON:0,
        PGIE_CLASS_ID_KNIFE:0,
        PGIE_CLASS_ID_FORK:0,
        PGIE_CLASS_ID_CUP:0,
        PGIE_CLASS_ID_WINE_GLASS:0,
        PGIE_CLASS_ID_BOTTLE:0,
        PGIE_CLASS_ID_TENNIS_RACKET:0,
        PGIE_CLASS_ID_SURFBOARD:0,
        PGIE_CLASS_ID_SKATEBOARD:0,
        PGIE_CLASS_ID_BASEBALL_GLOVE:0,
        PGIE_CLASS_ID_BASEBALL_BAT:0,
        PGIE_CLASS_ID_KITE:0,
        PGIE_CLASS_ID_SPORTS_BALL:0,
        PGIE_CLASS_ID_SNOWBOARD:0,
        PGIE_CLASS_ID_SKIS:0,
        PGIE_CLASS_ID_FRISBEE:0,
        PGIE_CLASS_ID_SUITCASE:0,
        PGIE_CLASS_ID_TIE:0,
        PGIE_CLASS_ID_HANDBAG:0,
        PGIE_CLASS_ID_UMBRELLA:0,
        PGIE_CLASS_ID_BACKPACK:0,
        PGIE_CLASS_ID_GIRAFFE:0,
        PGIE_CLASS_ID_ZEBRA:0,
        PGIE_CLASS_ID_BEAR:0,
        PGIE_CLASS_ID_ELEPHANT:0,
        PGIE_CLASS_ID_COW:0,
        PGIE_CLASS_ID_SHEEP:0,
        PGIE_CLASS_ID_HORSE:0,
        PGIE_CLASS_ID_DOG:0,
        PGIE_CLASS_ID_CAT:0,
        PGIE_CLASS_ID_BIRD:0,
        PGIE_CLASS_ID_BENCH:0,
        PGIE_CLASS_ID_PARKING_METER:0,
        PGIE_CLASS_ID_STOP_SIGN:0,
        PGIE_CLASS_ID_FIRE_HYDRANT:0,
        PGIE_CLASS_ID_TRAFFIC_LIGHT:0,
        PGIE_CLASS_ID_BOAT:0,
        PGIE_CLASS_ID_TRUCK:0,
        PGIE_CLASS_ID_TRAIN:0,
        PGIE_CLASS_ID_BUS:0,
        PGIE_CLASS_ID_AEROPLANE:0,
        PGIE_CLASS_ID_MOTORBIKE:0,
        PGIE_CLASS_ID_VEHICLE:0,
        PGIE_CLASS_ID_BICYCLE:0,
        PGIE_CLASS_ID_PERSON:0
        }
 
    frame_number=0
    num_rects=0
    gst_buffer = info.get_buffer()
    if not gst_buffer:
        print("Unable to get GstBuffer ")
        return

    # Retrieve batch metadata from the gst_buffer
    # Note that pyds.gst_buffer_get_nvds_batch_meta() expects the
    # C address of gst_buffer as input, which is obtained with hash(gst_buffer)
    batch_meta = pyds.gst_buffer_get_nvds_batch_meta(hash(gst_buffer))
    l_frame = batch_meta.frame_meta_list
    while l_frame is not None:
        try:
            # Note that l_frame.data needs a cast to pyds.NvDsFrameMeta
            # The casting is done by pyds.NvDsFrameMeta.cast()
            # The casting also keeps ownership of the underlying memory
            # in the C code, so the Python garbage collector will leave
            # it alone.
            frame_meta = pyds.NvDsFrameMeta.cast(l_frame.data)
        except StopIteration:
            break

        frame_number=frame_meta.frame_num
        frame_numberx=frame_meta.frame_num
        num_rects = frame_meta.num_obj_meta
        num_rectsx = frame_meta.num_obj_meta
        l_obj=frame_meta.obj_meta_list
       
        while l_obj is not None:
            try: 
                # Casting l_obj.data to pyds.NvDsObjectMeta
                obj_meta=pyds.NvDsObjectMeta.cast(l_obj.data)
            except StopIteration:
                break
            obj_counter[obj_meta.class_id] += 1
            try: 
                l_obj=l_obj.next
            except StopIteration:
                break
         # Acquiring a display meta object. The memory ownership remains in
        # the C code so downstream plugins can still access it. Otherwise
        # the garbage collector will claim it when this probe function exits.
        display_meta=pyds.nvds_acquire_display_meta_from_pool(batch_meta)
        display_meta.num_labels = 1
        py_nvosd_text_params = display_meta.text_params[0]
        # Setting display text to be shown on screen
        # Note that the pyds module allocates a buffer for the string, and the
        # memory will not be claimed by the garbage collector.
        # Reading the display_text field here will return the C address of the
        # allocated string. Use pyds.get_string() to get the string content.
        py_nvosd_text_params.display_text = "Frame Number={} Number of Objects={} Bird_count={} Person_count={}".format(frame_number, num_rects, obj_counter[PGIE_CLASS_ID_CUP], obj_counter[PGIE_CLASS_ID_BOTTLE])

        BOTTLE = obj_counter[PGIE_CLASS_ID_BOTTLE]
        CUP = obj_counter[PGIE_CLASS_ID_CUP]
        FORK = obj_counter[PGIE_CLASS_ID_FORK]
        TOOTHBRUSH = obj_counter[PGIE_CLASS_ID_TOOTHBRUSH]
        BANANA = obj_counter[PGIE_CLASS_ID_BANANA]
        SPOON  = obj_counter[PGIE_CLASS_ID_SPOON]
        PERSON = obj_counter[PGIE_CLASS_ID_PERSON]
        BOWL = obj_counter[PGIE_CLASS_ID_BOWL]
        TVMONITOR = obj_counter[PGIE_CLASS_ID_TVMONITOR]
        APPLE = obj_counter[PGIE_CLASS_ID_APPLE]

        # Now set the offsets where the string should appear
        py_nvosd_text_params.x_offset = 10
        py_nvosd_text_params.y_offset = 12

        # Font , font-color and font-size
        py_nvosd_text_params.font_params.font_name = "Serif"
        py_nvosd_text_params.font_params.font_size = 10
        # set(red, green, blue, alpha); set to White
        py_nvosd_text_params.font_params.font_color.set(1.0, 1.0, 1.0, 1.0)

        # Text background color
        py_nvosd_text_params.set_bg_clr = 1
        # set(red, green, blue, alpha); set to Black
        py_nvosd_text_params.text_bg_clr.set(0.0, 0.0, 0.0, 1.0)
        # Using pyds.get_string() to get display_text as string
        #print(pyds.get_string(py_nvosd_text_params.display_text))
        pyds.nvds_add_display_meta_to_frame(frame_meta, display_meta)
        fps_streams["stream{0}".format(frame_meta.pad_index)].get_fps()
        try:
            l_frame=l_frame.next
        except StopIteration:
            break

    return Gst.PadProbeReturn.OK

 ######################################################################

def cb_newpad(decodebin, decoder_src_pad,data):
    print("In cb_newpad\n")
    caps=decoder_src_pad.get_current_caps()
    gststruct=caps.get_structure(0)
    gstname=gststruct.get_name()
    source_bin=data
    features=caps.get_features(0)

    # Need to check if the pad created by the decodebin is for video and not
    # audio.
    print("gstname=",gstname)
    if(gstname.find("video")!=-1):
        # Link the decodebin pad only if decodebin has picked nvidia
        # decoder plugin nvdec_*. We do this by checking if the pad caps contain
        # NVMM memory features.
        print("features=",features)
        if features.contains("memory:NVMM"):
            # Get the source bin ghost pad
            bin_ghost_pad=source_bin.get_static_pad("src")
            if not bin_ghost_pad.set_target(decoder_src_pad):
                sys.stderr.write("Failed to link decoder src pad to source bin ghost pad\n")
        else:
            sys.stderr.write(" Error: Decodebin did not pick nvidia decoder plugin.\n")

def decodebin_child_added(child_proxy,Object,name,user_data):
    print("Decodebin child added:", name, "\n")
    if(name.find("decodebin") != -1):
        Object.connect("child-added",decodebin_child_added,user_data)   
    if(is_aarch64() and name.find("nvv4l2decoder") != -1):
        print("Seting bufapi_version\n")
        Object.set_property("bufapi-version",True)

def create_source_bin(index,uri):
    print("Creating source bin")

    # Create a source GstBin to abstract this bin's content from the rest of the
    # pipeline
    bin_name="source-bin-%02d" %index
    print(bin_name)
    nbin=Gst.Bin.new(bin_name)
    if not nbin:
        sys.stderr.write(" Unable to create source bin \n")

    # Source element for reading from the uri.
    # We will use decodebin and let it figure out the container format of the
    # stream and the codec and plug the appropriate demux and decode plugins.
    uri_decode_bin=Gst.ElementFactory.make("uridecodebin", "uri-decode-bin")
    if not uri_decode_bin:
        sys.stderr.write(" Unable to create uri decode bin \n")
    # We set the input uri to the source element
    uri_decode_bin.set_property("uri",uri)
    # Connect to the "pad-added" signal of the decodebin which generates a
    # callback once a new pad for raw data has beed created by the decodebin
    uri_decode_bin.connect("pad-added",cb_newpad,nbin)
    uri_decode_bin.connect("child-added",decodebin_child_added,nbin)

    # We need to create a ghost pad for the source bin which will act as a proxy
    # for the video decoder src pad. The ghost pad will not have a target right
    # now. Once the decode bin creates the video decoder and generates the
    # cb_newpad callback, we will set the ghost pad target to the video decoder
    # src pad.
    Gst.Bin.add(nbin,uri_decode_bin)
    bin_pad=nbin.add_pad(Gst.GhostPad.new_no_target("src",Gst.PadDirection.SRC))
    if not bin_pad:
        sys.stderr.write(" Failed to add ghost pad in source bin \n")
        return None
    return nbin

 ######################################################################

def main(args):
    # Check input arguments
    if len(args) < 2:
        sys.stderr.write("usage: %s <uri1> [uri2] ... [uriN]\n" % args[0])
        sys.exit(1)

    for i in range(0,len(args)-1):
        fps_streams["stream{0}".format(i)]=GETFPS(i)
    number_sources=len(args)-1

    # Standard GStreamer initialization
    GObject.threads_init()
    Gst.init(None)

    # Create gstreamer elements */
    # Create Pipeline element that will form a connection of other elements
    print("Creating Pipeline \n ")
    pipeline = Gst.Pipeline()
    is_live = False

    if not pipeline:
        sys.stderr.write(" Unable to create Pipeline \n")
    print("Creating streamux \n ")

    # Create nvstreammux instance to form batches from one or more sources.
    streammux = Gst.ElementFactory.make("nvstreammux", "Stream-muxer")
    if not streammux:
        sys.stderr.write(" Unable to create NvStreamMux \n")

    pipeline.add(streammux)
    for i in range(number_sources):
        print("Creating source_bin ",i," \n ")
        uri_name=args[i+1]
        if uri_name.find("rtsp://") == 0 :
            is_live = True
        source_bin=create_source_bin(i, uri_name)
        if not source_bin:
            sys.stderr.write("Unable to create source bin \n")
        pipeline.add(source_bin)
        padname="sink_%u" %i
        sinkpad= streammux.get_request_pad(padname) 
        if not sinkpad:
            sys.stderr.write("Unable to create sink pad bin \n")
        srcpad=source_bin.get_static_pad("src")
        if not srcpad:
            sys.stderr.write("Unable to create src pad bin \n")
        srcpad.link(sinkpad)
    queue1=Gst.ElementFactory.make("queue","queue1")
    queue2=Gst.ElementFactory.make("queue","queue2")
    queue3=Gst.ElementFactory.make("queue","queue3")
    queue4=Gst.ElementFactory.make("queue","queue4")
    queue5=Gst.ElementFactory.make("queue","queue5")
    pipeline.add(queue1)
    pipeline.add(queue2)
    pipeline.add(queue3)
    pipeline.add(queue4)
    pipeline.add(queue5)

    print("Creating Pgie \n ")
    pgie = Gst.ElementFactory.make("nvinfer", "primary-inference")
    if not pgie:
        sys.stderr.write(" Unable to create pgie \n")

    print("Creating tiler \n ")
    tiler=Gst.ElementFactory.make("nvmultistreamtiler", "nvtiler")
    if not tiler:
        sys.stderr.write(" Unable to create tiler \n")

    print("Creating nvvidconv \n ")
    nvvidconv = Gst.ElementFactory.make("nvvideoconvert", "convertor")  
    if not nvvidconv:
        sys.stderr.write(" Unable to create nvvidconv \n")

    print("Creating nvosd \n ")
    nvosd = Gst.ElementFactory.make("nvdsosd", "onscreendisplay")
           ###########################################
    if not nvosd:
        sys.stderr.write(" Unable to create nvosd \n")
    nvosd.set_property('process-mode',OSD_PROCESS_MODE)
    nvosd.set_property('display-text',OSD_DISPLAY_TEXT)
    #if(is_aarch64()):
        #print("Creating transform \n ")
        #transform=Gst.ElementFactory.make("nvegltransform", "nvegl-transform")
        #if not transform:
            #sys.stderr.write(" Unable to create transform \n")

    
    nvvidconv_postosd = Gst.ElementFactory.make("nvvideoconvert", "convertor_postosd")
    if not nvvidconv_postosd:
        sys.stderr.write(" Unable to create nvvidconv_postosd \n")
    

    # Create a caps filter
    caps = Gst.ElementFactory.make("capsfilter", "filter")
    caps.set_property("caps", Gst.Caps.from_string("video/x-raw(memory:NVMM), format=I420"))

     # Make the encoder
    bitrate=4000000
    codec="H264"
    if codec == "H264":
        encoder = Gst.ElementFactory.make("nvv4l2h264enc", "encoder")
        print("Creating H264 Encoder")
    elif codec == "H265":
        encoder = Gst.ElementFactory.make("nvv4l2h265enc", "encoder")
        print("Creating H265 Encoder")
    if not encoder:
        sys.stderr.write(" Unable to create encoder")
    encoder.set_property('bitrate', bitrate)
    if is_aarch64():
        encoder.set_property('preset-level', 1)
        encoder.set_property('insert-sps-pps', 1)
        encoder.set_property('bufapi-version', 1)
    
    # Make the payload-encode video into RTP packets
    if codec == "H264":
        rtppay = Gst.ElementFactory.make("rtph264pay", "rtppay")
        print("Creating H264 rtppay")
    elif codec == "H265":
        rtppay = Gst.ElementFactory.make("rtph265pay", "rtppay")
        print("Creating H265 rtppay")
    if not rtppay:
        sys.stderr.write(" Unable to create rtppay")
    if is_live:
        print("Atleast one of the sources is live")
        streammux.set_property('live-source', 1)

    # Make the UDP sink
    updsink_port_num = 5400
    sink = Gst.ElementFactory.make("udpsink", "udpsink")
    if not sink:
        sys.stderr.write(" Unable to create udpsink")
    
    sink.set_property('host', '224.224.255.255')
    sink.set_property('port', updsink_port_num)
    sink.set_property('async', False)
    sink.set_property('sync', 0)
    
    streammux.set_property('gpu-id', 0)
    streammux.set_property('enable-padding', 0)
    streammux.set_property('nvbuf-memory-type', 0)
    streammux.set_property('width', 1920)
    streammux.set_property('height', 1080)
    streammux.set_property('batch-size', 1)
    streammux.set_property('batched-push-timeout', 400000)
    pgie.set_property('config-file-path', "config_infer_primary_yoloV3.txt")
    pgie_batch_size=pgie.get_property("batch-size")
    if(pgie_batch_size != number_sources):
        print("WARNING: Overriding infer-config batch-size",pgie_batch_size," with number of sources ", number_sources," \n")
        pgie.set_property("batch-size",number_sources)

    tiler_rows=int(math.sqrt(number_sources))
    tiler_columns=int(math.ceil((1.0*number_sources)/tiler_rows))
    tiler.set_property("rows",tiler_rows)
    tiler.set_property("columns",tiler_columns)
    tiler.set_property("width", TILED_OUTPUT_WIDTH)
    tiler.set_property("height", TILED_OUTPUT_HEIGHT)
    sink.set_property("qos",0)

    print("Adding elements to Pipeline \n")
    pipeline.add(pgie)
    pipeline.add(tiler)
    pipeline.add(nvvidconv)
    pipeline.add(nvosd)
    pipeline.add(nvvidconv_postosd)
    pipeline.add(caps)
    pipeline.add(encoder)
    pipeline.add(rtppay)
    pipeline.add(sink)

    print("Linking elements in the Pipeline \n")
    streammux.link(queue1)
    queue1.link(pgie)
    pgie.link(queue2)
    queue2.link(tiler)
    tiler.link(queue3)
    queue3.link(nvvidconv)
    nvvidconv.link(queue4)
    queue4.link(nvosd)
    nvosd.link(queue5)   
    queue5.link(nvvidconv_postosd)
    nvvidconv_postosd.link(caps)
    caps.link(encoder)
    encoder.link(rtppay)
    rtppay.link(sink)  



    # create an event loop and feed gstreamer bus mesages to it
    loop = GObject.MainLoop()
    bus = pipeline.get_bus()
    bus.add_signal_watch()
    bus.connect ("message", bus_call, loop)
    tiler_src_pad=pgie.get_static_pad("src")
    if not tiler_src_pad:
        sys.stderr.write(" Unable to get src pad \n")
    else:
        tiler_src_pad.add_probe(Gst.PadProbeType.BUFFER, tiler_src_pad_buffer_probe, 0)

    # List the sources
    print("Now playing...")
    for i, source in enumerate(args):
        if (i != 0):
            print(i, ": ", source)

######################################################################

 # Start streaming
    rtsp_port_num = 8554
    
    server = GstRtspServer.RTSPServer.new()
    server.props.service = "%d" % rtsp_port_num
    server.attach(None)
    
    factory = GstRtspServer.RTSPMediaFactory.new()
    factory.set_launch( "( udpsrc name=pay0 port=%d buffer-size=5242888 caps=\"application/x-rtp, media=video, clock-rate=90000, encoding-name=(string)%s, payload=96 \" )" % (updsink_port_num, codec))
    factory.set_shared(True)
    server.get_mount_points().add_factory("/ds-test", factory)
    
    print("\n *** DeepStream: Launched RTSP Streaming at rtsp://localhost:%d/ds-test ***\n\n" % rtsp_port_num)

    # Lets add probe to get informed of the meta data generated, we add probe to
    # the sink pad of the osd element, since by that time, the buffer would have
    # had got all the metadata.
   
######################################################################
         
    # Create the node death payload
    deathPayload = sparkplug.getNodeDeathPayload()

    # Start of main program - Set up the MQTT client connection
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(myUsername, myPassword)
    deathByteArray = bytearray(deathPayload.SerializeToString())
    client.will_set("spBv1.0/" + myGroupId + "/NDEATH/" + myNodeName, deathByteArray, 0, False)
    client.connect(serverUrl, 1883, 60)

    # Publish the birth certificates
    publishBirth()
   

    def foo():
      # Periodically publish some new data
      payload = sparkplug.getDdataPayload()

       # Add some random data to the inputs
      addMetric(payload, "input/number of objects", AliasMap.Device_num_rectsx, MetricDataType.Int16, num_rectsx )
      addMetric(payload, "input/Device Metric0", AliasMap.Device_Metric0, MetricDataType.String, "hello device")
      addMetric(payload, "input/Device Metric1", AliasMap.Device_Metric1, MetricDataType.Boolean, True)
      addMetric(payload, "output/Device Metric2", AliasMap.Device_Metric2, MetricDataType.Int16, 3)
      addMetric(payload, "output/Device Metric3", AliasMap.Device_Metric3, MetricDataType.Boolean, True)
      addMetric(payload, "input/BOTTLE", AliasMap.Device_BOTTLE, 
MetricDataType.Int16, BOTTLE )
      addMetric(payload, "input/CUP", AliasMap.Device_CUP, 
MetricDataType.Int16, CUP)
      addMetric(payload, "input/FORK", AliasMap.Device_FORK,
 MetricDataType.Int16, FORK )
      addMetric(payload, "input/SPOON", AliasMap.Device_SPOON, 
MetricDataType.Int16, SPOON )
      addMetric(payload, "input/BOWL", AliasMap.Device_BOWL, 
MetricDataType.Int16, BOWL)
      addMetric(payload, "input/BANANA", AliasMap.Device_BANANA,
 MetricDataType.Int16, BANANA )
      addMetric(payload, "input/APPLE", AliasMap.Device_APPLE, 
MetricDataType.Int16, APPLE )
      addMetric(payload, "input/PERSON", AliasMap.Device_PERSON, 
MetricDataType.Int16, PERSON )
      addMetric(payload, "input/TVMONITOR", AliasMap.Device_TVMONITOR, 
MetricDataType.Int16, TVMONITOR )
      addMetric(payload, "input/TOOTHBRUSH", AliasMap.Device_TOOTHBRUSH, 
MetricDataType.Int16, TOOTHBRUSH )
    

      # Note this data we're setting to STALE via the propertyset as an example
      metric = addMetric(payload, None, AliasMap.Device_Metric1, MetricDataType.Boolean, random.choice([True, False]))
      metric.properties.keys.extend(["Quality"])
      propertyValue = metric.properties.values.add()
      propertyValue.type = ParameterDataType.Int32
      propertyValue.int_value = 500

      # Publish a message data
      byteArray = bytearray(payload.SerializeToString())
      client.publish("spBv1.0/" + myGroupId + "/DDATA/" + myNodeName + "/" + myDeviceName, byteArray, 0, False)

      threading.Timer(WAIT_SECONDS, foo).start()

    foo() 
     
######################################################################
    print("Starting pipeline \n")
    # start play back and listed to events		
    pipeline.set_state(Gst.State.PLAYING)
    try:
        loop.run()
    except:
        pass
    # cleanup
    print("Exiting app\n")
    pipeline.set_state(Gst.State.NULL)

if __name__ == '__main__':
    sys.exit(main(sys.argv))


