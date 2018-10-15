"""Military time.

Convert a time string of the format hh:mm:ssAM or hh:mm:ssPM (07:02:57AM or 10:12:09PM)
into military time (24h).
Special rules apply:
midnight: 12:00:00AM (12h) => 00:00:00 (24h)
noon: 12:00:00PM (12h) => 12:00:00 (24h)

Examples:
    militaryTime("09:12:41AM") returns "09:12:41"
    militaryTime("04:31:51PM") returns "16:31:51"

"""

# Utilities
from datetime import datetime


def militaryTime(s):
    """Problem solution."""
    time = datetime.strptime(s, "%I:%M:%S%p")
    return time.strftime("%H:%M:%S")
