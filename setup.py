__version__ = '3.1b1'

from setuptools import setup, Extension, find_packages
import sys, os
import textwrap


setup(
    name="SchevoZodb",

    version=__version__,

    description="ZODB3 storage backend for Schevo",

    long_description=textwrap.dedent("""
    SchevoZodb provides integration between the ZODB3_ object database
    for Python and the Schevo_ DBMS.

    You can also get the `latest development version
    <http://getschevo.org/hg/repos.cgi/schevozodb-dev/archive/tip.tar.gz#egg=SchevoZodb-dev>`__.

    .. _Schevo: http://schevo.org/

    .. _ZODB3: http://www.zope.org/Products/ZODB3
    """),

    classifiers=[
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Database :: Database Engines/Servers',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],

    keywords='database dbms',

    author='ElevenCraft Inc.',
    author_email='schevo@googlegroups.com',

    url='http://www.schevo.org/',

    license='MIT',

    platforms=['UNIX', 'Windows'],

    packages=find_packages(exclude=['doc', 'tests']),

    include_package_data=True,

    zip_safe=False,

    install_requires=[
        'ZODB3 >= 3.8.0',
    ],

    tests_require=[
        'nose >= 0.11.0',
        'Schevo == dev, >= 3.1b1dev-20090507',
    ],
    test_suite='nose.collector',

    extras_require={
    },

    dependency_links = [
    ],

    entry_points = """
    [schevo.backend]
    zodb = schevozodb.backend:ZodbBackend
    """,
    )
