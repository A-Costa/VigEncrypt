from setuptools import setup, find_packages

setup(
    name='VigEncrypt',
    version='0.0.1',
    description='Vigenere cipher web application',
    author='Alberto Costa',
    author_email='alberto.costa05@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'}
)
