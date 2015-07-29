from setuptools import setup

setup(
    name='xtralien',
    version='0.0.1',
    description='A connector to implement connecting to CLOI-based instruments',
    author='Xtralien',
    author_email='jack@xtralien.com',
    url='https://github.com/Xtralien/pyxtralien.git',
    packages=['xtralien'],
    install_requires=['cloi'],
    license='GPLv3'
)
