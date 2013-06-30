from datetime import datetime
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

try:
    import parsedatetime as pdt
    from parsedatetime import Constants as pdc
    from pytz import timezone
except ImportError:
    raise ImproperlyConfigured('Need to install parsedatetime and pytz')

TZ = timezone(getattr(settings, "TIME_ZONE", "UTC"))

def parse(s):
    """
    Parse the string using parsedatetime and format it to the current timezone
    """
    return TZ.localize(datetime(*tuple(pdt.Calendar(Constants()).parse(s)[0])[:7]))
