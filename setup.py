# read the contents of your README file
from collections import OrderedDict
from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='apiflash',
    packages=['apiflash'],
    version='0.1.2',
    url='https://apiflash.com/',
    project_urls=OrderedDict((
        ('Documentation', 'https://apiflash.com/documentation'),
        ('Code', 'https://github.com/ApiFlash/python-client'),
        ('Issue tracker', 'https://github.com/ApiFlash/python-client/issues'),
    )),
    license='MIT',
    description='The official python client of ApiFlash, website screenshot API.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Timothée Jeannin',
    author_email='tjeannin@apiflash.com',
    keywords=[
        "screenshots",
        "urlbox",
        "urlbox.io",
        "phantom",
        "phantomjs",
        "screenshot",
        "website",
        "urlbox",
        "headless",
        "chrome",
        "screenshotlayer",
        "render",
        "page",
        "webkit",
        "webkit2png",
        "url2png",
        "fullpage",
        "fullheight"
    ],
    install_requires=[],
    extras_require={
        'dev': [
            'setuptools',
            'twine',
            'wheel'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
