from setuptools import setup

setup(name='ClearFinder',
      version='0.1.6',
      author='Philip Schleihauf',
      author_email='uniphil@gmail.com',
      license='GPLv3',
      description='Identify clear measurements from solar irradiation data',
      long_description=open('README.txt').read(),
      py_modules=['clearfinder'],
      scripts=['clearfinder.py'])
