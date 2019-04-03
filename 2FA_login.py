import sys, argparse
from workflow import Workflow3, ICON_WEB, ICON_WARNING, web
from pyicloud import PyiCloudService
import click

trusted_devices = api.trusted_devices
for i, trusted_device in enumerate(trusted_devices):
    print "  %s: %s" % (i, trusted_device.get('deviceName',
    "SMS to %s" % trusted_device.get('phoneNumber')))
    wf.add_item(title= trusted_device.get('deviceName'),
    subtitle= 'Send iCloud verification code to this device', valid="Yes",
    arg= trusted_device)
wf.send_feedback()

trusted_device = trusted_devices[trusted_device]
# Have to change this to have selected device argument passed to trusted_device
if not api.send_verification_code(trusted_device):
    print "Failed to send verification code"
    sys.exit(1)

code = click.prompt('Please enter validation code')
if not api.validate_verification_code(trusted_device, code):
    print "Failed to verify verification code"
    sys.exit(1)



parser = argparse.ArgumentParser()
parser.add_argument('--setcode', dest='two_factor_code', nargs='?', default=None)
parser.add_argument('query', nargs='?', default=None)
args = parser.parse_args(wf.args)



# decide what to do based on arguments
if args.apikey:  # Script was passed an API key
    # save the key
    wf.settings['api_key'] = args.apikey
    return 0  # 0 means script exited cleanly


two_factor_code = wf.settings.get('two_factor_code', None)

if not api_key:  # iCloud code has not yet been set
    wf.add_item('Need to verify iCloud login with two factor authentication',
            "Please choose which iCloud device you'd like to send your two factor authentication code to",
            valid=False,
            icon=ICON_WARNING)
wf.send_feedback()
return 0


 query = args.query
 # Retrieve posts from cache if available and no more than 600
 # seconds old

 def wrapper():
     """`cached_data` can only take a bare callable (no args),
     so we need to wrap callables needing arguments in a function
     that needs none.
     """
     return get_recent_posts(api_key)

 posts = wf.cached_data('posts', wrapper, max_age=600)
