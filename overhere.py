import sys
from workflow import Workflow3, ICON_WEB, ICON_WARNING, web
from pyicloud import PyiCloudService


for line in open("apidata.txt","r").readlines():
    login_info = line.split()

api = PyiCloudService(login_info[0], login_info[1])


def main(wf):
    if api.requires_2sa:
        wf.add_item('Need to verify with iCloud two-factor authentication',
                     "Please use 'overify' keyword to choose which device you'd like to send the code to",
                     valid=False,
                     icon=ICON_WARNING)
    else:
        device_list = api.devices._devices

        for device_id, device in device_list.iteritems():
            device_name = str(device).split(":",1)[1]
            device_hardware = str(device).split(":")[0]
            it = wf.add_item(title= device_name,
            subtitle= device_hardware, valid="Yes",
            arg= device_id)
        wf.send_feedback()

if __name__ == "__main__":
    wf = Workflow3()
    sys.exit(wf.run(main))
