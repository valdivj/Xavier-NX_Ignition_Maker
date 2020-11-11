
# Nvidia Deepstream5+Ignition Maker+Metatdata+Python

Here is the items and steps you will need to run Nvidia deepstream5
extract metadata and send to Ignition maker using Python.



Here are links to video tutorials to get youre Nano
or Xavier NX setup.



1.Link to setup Ignition Maker. They have a 64 bit Ignition maker
now so that is another option.

https://youtu.be/0kvurkDSYt4



2.Link to setup MySQL database if you want a Database

https://youtu.be/_D5eCn2LCZY



3.Link to setup Sparkplug. This will be used as the MQTT
link from Deepstream to Ignition Maker

https://youtu.be/QJ4EBMoA2sw



4.Link to instruction on converting Deepstream RTSP outstream
to HTTP stream.
To use in Ignition Maker video player.

https://youtu.be/3VEvOL_32L8




5.Download Deepstream Python Bindings and install at
"/opt/nvidia/deepstream/deepstream-5.0/sources"

https://github.com/NVIDIA-AI-IOT/deepstream_python_apps




6.clone this repo and install and install at

"/opt/nvidia/deepstream/deepstream-5.0/sources/deepstream_python_apps-1.0/apps"



7.cd into "/opt/nvidia/deepstream/deepstream-5.0/sources/deepstream_python_apps-1.0/apps/deepstream-ign-rtsp-web"



8.There are 3 Python Examples in the this repo


9.This sends out a Deepstream RTSP stream from a webcam and sends Deepstream metadata to ignition Maker

$python3 deepstream_ignition_usb_rtsp.py /dev/video0 



10.This Shows the output of a Deepstream webcam and sends Deepstream metadata to ignition Maker

$python3 deepstream_ignition_usb.py /dev/video0 



11.This Shows the output of a .h264 file and sends Deepstream metadata to ignition Maker

$python3 deepstream_ignition_rtsp_out.py /opt/nvidia/deepstream/deepstream-5.0/samples/streams/sample_720p.h264



When These Scripts are ran the will automaticly generate the tags in ignition.














