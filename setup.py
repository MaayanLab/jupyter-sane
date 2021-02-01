from setuptools import setup, find_packages

setup(
  name='jupyter-sane',
  version='0.0.1',
  url='https://github.com/maayanLab/jupyter-sane/',
  author='Daniel J. B. Clarke',
  author_email='u8sand@gmail.com',
  long_description=open('README.md', 'r').read(),
  license='CC-BY-SA-4.0',
  install_requires=list(map(str.strip, open('requirements.txt', 'r').readlines())),
  packages=find_packages(),
  include_package_data=False,
  entry_points={
    'console_scripts': ['jupyter-sane=jupyter_sane:jupyter_cli'],
  }
)
