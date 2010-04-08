from datetime import datetime
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

try:
    import parsedatetime.parsedatetime as pdt
    import parsedatetime.parsedatetime_consts as pdc
    from pytz import timezone
except ImportError:
    raise ImproperlyConfigured('Need to install parsedatetime and pytz')

TZ = timezone(getattr(settings, "TIME_ZONE", "UTC"))

def parse(s):
    """
    Parse the string using parsedatetime and format it to the current timezone
    """
    return TZ.localize(datetime(*tuple(pdt.Calendar(pdc.Constants()).parse(s)[0])[:7]))
