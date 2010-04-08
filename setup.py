from distutils.core import setup
from humandt import __version__

setup(name='django-human-datetime',
    version=__version__,
    description='Uses the parsedatetime package to parse human readable date/time expressions into Django fields',
    long_description=open('README.rst').read(),
    author='Justin Quick',
    author_email='justquick@gmail.com',
    url='http://github.com/justquick/django-human-datetime',
    packages=['humandt'],
    requires=['parsedatetime','pytz',],
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Utilities'],
    )
