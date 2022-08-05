# setup.py for planar
#
# $Id$

import os
import sys
import shutil
from distutils.core import setup, Extension


srcdir = os.path.dirname(__file__)

def read(fname):
    return open(os.path.join(srcdir, fname)).read()

include_dirs = ['include']
extra_compile_args = []

setup(
    name='planar',
    version='0.4', # *** REMEMBER TO UPDATE __init__.py ***
    description='2D planar geometry library for Python.',
    long_description=read('README.txt'),
    provides=['planar'],
    author='Casey Duncan',
    author_email='casey.duncan@gmail.com',
    url='http://bitbucket.org/caseman/planar/',
    license='BSD',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
    ],
    platforms = 'any',

    package_dir={'planar': 'planar',
                 'planar.test': 'test'},
    packages=['planar', 'planar.test'],
    package_data={"planar": ["py.typed", "vector.pyi", "transform.pyi"]},

)
