from setuptools import setup

with open("README.md", "r") as fh:
      long_description = fh.read()

setup(name='meshtasTAK',
      version='0.1.1',
      description='Python library for using Meshtastic with TAK servers',
      url='http://github.com/DeltaBravo15/meshtasTAK',
      author='DeltaBravo15',
      license='GPLv3+',
      packages=setuptools.find_packages(),
      zip_safe=True,
      python_requires='>=3.6',
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
      ]
      )
