import sys
from workflow import Workflow3, ICON_WEB, ICON_WARNING
from pyicloud import PyiCloudService

login_info = None
for line in open("apidata.txt", "r").readlines():
    login_info = line.split()
api = PyiCloudService(login_info[0], login_info[1])

chosen_device = sys.argv[0]


def main(wf):
    # Check argument existance:
    if chosen_device is not None:
        log.debug("Houston, we have an argument")
    else:
        log.debug("No argument / argument is None")
        sys.exit()

    # if argument name is a string, the argument is the lost device:

    if isinstance(chosen_device, (str, object)):
        LostDevice = chosen_device
        log.debug(str(LostDevice))
        # api.devices[LostDevice].play_sound()
        sys.exit(1)


    # else if argument name is an object, the variable is the chosen 2SA device :

    elif isinstance(chosen_device, (int, object)):
        TwoFactorDevice = chosen_device
        if not api.send_verification_code(TwoFactorDevice):
            wf.add_item(title="Failed to send verification code",
                        subtitle='Please try again', valid="No", icon=ICON_WARNING)
        wf.send_feedback()
        sys.exit(1)


if __name__ == '__main__':
    wf = Workflow3()
    log = wf.logger
    wf.run(main)
