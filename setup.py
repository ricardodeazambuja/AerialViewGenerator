VERSION = "0.0.1"

import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 7):
    sys.exit('Sorry, Python < 3.7 is not supported.')

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name="aerialviewgenerator",
    packages=[package for package in find_packages()],
    version=VERSION,
    license="GPL",
    description="Aerial View Generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Ricardo de Azambuja",
    author_email="ricardo.azambuja@gmail.com",
    url="https://github.com/ricardodeazambuja/AerialViewGenerator",
    download_url=f"https://github.com/ricardodeazambuja/AerialViewGenerator/archive/refs/tags/v{VERSION}.tar.gz",
    keywords=['UAV', 'aerial images'],
    install_requires=['requests', 'pillow', 'quad_sim_python'],
    classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Information Technology',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3)',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Framework :: Robot Framework :: Library',
          'Topic :: Education',
          'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ]
)