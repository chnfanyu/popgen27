#!/usr/bin/env python

import os
import sys

from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

#
readme_path = os.path.join(os.path.dirname(__file__), 'README.rst')
if not os.path.exists(readme_path):
    readme_content = "PopGen\n======\n\nSynthetic Population Generator 2.0"
    with open(readme_path, 'w') as f:
        f.write(readme_content)

readme = open(readme_path).read()
doclink = """
Documentation
-------------

The full documentation is at http://popgen.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='popgen',
    version='2.0',
    description='Synthetic Population Generator 2.0',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Karthik Konduri',
    author_email='karthik.charan@gmail.com',
    url='https://github.com/chnfanyu/popgen27',
    packages=[
        'popgen',
    ],
    package_data={'popgen': [
        '../tutorials/1_basic_popgen_setup/*.csv',
        '../tutorials/1_basic_popgen_setup/*.yaml']},
    scripts=['bin/popgen_run'],
    include_package_data=True,
    license='Apache License 2.0',
    zip_safe=False,
    keywords='popgen',
    classifiers=[
        'Development Status :: 2 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent'
    ],
)
