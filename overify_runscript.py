import sys
from workflow import Workflow3, ICON_WEB, ICON_WARNING, web
from pyicloud import PyiCloudService

# Check workflow variable existance:
if wf.getvar() is not None:
    print "Houston, we have a workflow variable"
else:
    print "No variable to get / wf.getvar() is None"
    sys.exit()

# if workflow variable name is a string, the variable is the lost device:

if isinstance(wf.getvar(), (str, object)):
    LostDevice = sys.argv[1]
    print str(LostDevice)
    api.devices[LostDevice].play_sound()
    sys.exit(1)


# else if workflow variable name = str, the variable is the chosen 2SA device :

elif isinstance(sys.argv[1], (int, object)):
    TwoFactorDevice = sys.argv[1]
    if not api.send_verification_code(TwoFactorDevice):
        wf.add_item(title="Failed to send verification code",
                    subtitle='Please try again', valid="No", icon=ICON_WARNING)
    wf.send_feedback()
    sys.exit(1)

    print "The object is either not the correct "

    # two_factor_code = wf.settings.get('two_factor_code', None)
    # query = args.query
    #
    # def wrapper():
    #     """`cached_data` can only take a bare callable (no args),
    #     so we need to wrap callables needing arguments in a function
    #     that needs none.
    #     """
    #     return get_recent_posts(api_key)
