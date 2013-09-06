import os
import setuptools
from distutils.core import setup

def find_packages():
    packages = []
    for dir,subdirs,files in os.walk('trrackspace_gevent'):
        package = dir.replace(os.path.sep, '.')
        if '__init__.py' not in files:
            # not a package
            continue
        packages.append(package)
    return packages

setup(
    name='trrackspace_gevent',
    version = '0.4-SNAPSHOT',
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
        'trpycore>=0.11.0',
        'trhttp>=0.5.0',
        'trhttp_gevent>=0.5.0',
        'trrackspace>=0.3.0',
    ]
)
