from pydroid_ipcam import *
import aiohttp
import asyncio
import sys

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
torchlight = sys.argv[7]

print("###########################")
async def main():
    async with aiohttp.ClientSession() as client:
        cam = PyDroidIPCam(websession=client, host=ip_local, username=camuser, password=campwd, port=8080, ssl=False)
        if torchlight == "ON":
            await cam.torch(True)
        else:
            await cam.torch(False)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())


