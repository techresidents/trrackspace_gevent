import os
from setuptools import setup, find_packages, Extension

import ez_setup
ez_setup.use_setuptools()

setup(
    name='trrackspace_gevent',
    version = '0.6-SNAPSHOT',
    author = 'Tech Residents, Inc.',
    packages = find_packages(),
    license = open('LICENSE').read(),
    description = 'Tech Residents Rackspace GEvent Library',
    long_description = open('README').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Distributed Computing',
        'Topic :: Utilities',
        ],
    install_requires=[
        'trpycore>=0.12.0',
        'trhttp_gevent>=0.7.0',
        'trrackspace>=0.5.0',
    ],
    dependency_links=[
        'git+ssh://dev.techresidents.com/tr/repos/techresidents/lib/python/trpycore.git@0.12.0#egg=trpycore-0.12.0',
        'git+ssh://dev.techresidents.com/tr/repos/techresidents/lib/python/trhttp_gevent.git@0.7.0#egg=trhttp_gevent-0.7.0',
        'git+ssh://dev.techresidents.com/tr/repos/techresidents/lib/python/trrackspace.git@0.5.0#egg=trrackspace-0.5.0'
    ],
)
