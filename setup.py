from setuptools import setup, find_packages

with open('README.md', mode='r') as f:
    long_descr = f.read()

setup(
    name='condatest',
    version='1.3',

    package_dir={"": "src"},
    packages=find_packages(where="src"),

    url='',
    license='MIT',
    author='Markus Franke',
    author_email='test@test.de',

    description='A test on how to build a conda package',
    long_description=long_descr,
    long_description_content_type='text/markdown'
)
