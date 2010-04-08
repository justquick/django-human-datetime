Django Human DateTime Parsing
==============================

:Authors:
   Justin Quick <justquick@gmail.com>
:Version: 0.1

This tool uses the `parsedatetime package <http://code.google.com/p/parsedatetime/`_ to turn human readable form input (like 'tomorrow 7PM') into ``datetime`` objects (like datetime.datetime(2010, 4, 9, 19, ...)).
This app requires ``parsedatetime`` and ``pytz``. 
The app comes with a set of fields to replace Django's own DateTimeField, DateField, and TimeField. Get them by using::

    from humandt.fields import HumanDateTimeField, HumanTimeField, HumanDateField
    
Then use them however you like as form fields in your own Django Forms::

    from django.forms import Form
    
    class ExampleForm(Form):
        datetime = HumanDateTimeField(required=False)
        time = HumanTimeField(required=False)
        date = HumanDateField(required=False)

Example Project
================

Download the most recent sourcecode and start up the development server. Make sure you have the most recent version of django::

    git clone git://github.com/justquick/django-human-datetime.git
    cd django-human-datetime
    python setup.py install # sudo this
    pip install django # and this
    cd example_project
    python manage.py runserver
    
If all goes well it will be available at http://127.0.0.1:8000/. There is an example form up there that just spits out the parsed date/time input. Look at the example_project.views for useage example.
To test the humandt app, stop the server and run this::

    python manage.py test humandt
    