import time

from pydroid_ipcam import *
import aiohttp
import asyncio
import sys
from thingin.thingin_requests import *
import uuid
import platform
import os
import json

update_frequency = 5


hue_url= "https://192.168.1.47/api/75WMpeSrs1ogZ6kxD79ez-fseyPxaCNkt-r8YL1z/lights/1/state"

print("###########################")
print("Program arguemnts : ")
for arg in sys.argv:
    print(arg)

token = sys.argv[1]
domain_to_insert = sys.argv[2]
name = sys.argv[3]
ip_local = sys.argv[4]
camuser = sys.argv[5]
campwd = sys.argv[6]
print("###########################")
my_uuid = uuid.uuid3(namespace=uuid.NAMESPACE_DNS, name=name)


if platform.system() == "Windows":
    thingindir = os.getcwd()+"\\thingin\\"
else:
    thingindir = os.getcwd()+"/thingin/"

boostrap_data_file = open(thingindir+'boostrap_result.json', 'r')
boostrap_data = json.load(boostrap_data_file)
print("Updating existing data :")
print(boostrap_data)
luminance_uuid = ""
motion_uuid = ""


async def main():
    async with aiohttp.ClientSession() as client:
        cam = PyDroidIPCam(websession=client, host=ip_local, username=camuser, password=campwd, port=8080, ssl=False)

        while(True):
            time.sleep(update_frequency)
            await cam.update()
            try:
                print_data(cam)
                update_data(cam)
            except Exception as e:
                print(e)


def print_data(cam):
    print("Camera availability ", cam.available)
    print("Enabled sensors ", cam.enabled_sensors)
    print("Motion events ", cam.sensor_data["motion_event"])
    print("Luminance Value ", cam.sensor_data["light"])
    print("Torch status ", cam.status_data["curvals"]["torch"])


def update_data(cam):
    motion_update_result = put_motion_event_thingin(uuid=motion_uuid, iri=motion_iri, motion_data=cam.sensor_data["motion_event"], access_token=token)
    luminance_update_result = put_luminance_thingin(uuid=luminance_uuid, iri=luminance_iri, luminance_data=cam.sensor_data["light"], access_token=token)
    print("Motion data update", motion_update_result.text)
    print("Luminance data update",luminance_update_result.text)


# ##BOOTSTRAP DATA UUIDS LOADING FROM THINGIN RESPONSE"
luminance_iri = domain_to_insert+"androidIPCam.luminance-"+str(my_uuid)
motion_iri = domain_to_insert+"androidIPCam.movementDetection-"+str(my_uuid)
for node in boostrap_data:
    if node["iri"] == luminance_iri:
        luminance_uuid = node["uuid"]
    if node["iri"] == motion_iri:
        motion_uuid = node["uuid"]

# MAIN LOOP
loop = asyncio.get_event_loop()
loop.run_until_complete(main())


