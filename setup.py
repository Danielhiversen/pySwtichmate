from setuptools import setup

setup(
    name = 'PySwitchmate',
    packages = ['switchmate'],
    install_requires=['bluepy'],
    version = '0.4.6',
    description = 'A library to communicate with Switchmate',
    author='Daniel Hjelseth Hoyer',
    url='https://github.com/Danielhiversen/pySwitchmate/',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Home Automation',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ]
)
