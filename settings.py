from client import Client
from blessings import Terminal

""" ----------------------------------------------------------
You can edit these to your preferences. Note: anything silly
like MAX_MESSAGES=-1 will break the client. Duh.
-------------------------------------------------------------- """

# the default server which will be joined upon startup - CASE SENSITIVE!
DEFAULT_SERVER="DisKvlt"

# the default channel which will be joined upon startup - CASE SENSITIVE!
DEFAULT_CHANNEL="general"

# the leading character used for commands
prefix = '/'

# the default prompt when not in a channel
DEFAULT_PROMPT = "~"

# Margins for inside the terminal and between elements. NOTE: must be >= 2
MARGIN = 2

# the max amount of messages to be downloaded + kept
MAX_MESSAGES=100

# the max amount of entries in each channel log to be downloaded + kept
MAX_LOG_ENTRIES=150





# ----------- Internal-Use Variables Below ----------------- #

""" ----------------------------------------------------------
DO NOT EDIT THESE - SERIOUSLY, DON'T DO IT.
-------------------------------------------------------------- """
client = Client(max_messages=MAX_MESSAGES)
term = Terminal()
channel_log = []