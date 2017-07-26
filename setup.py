from setuptools import setup

def readme():
    with open('README') as f:
        return f.read()


setup(name='2fassassin',
      version='2.0',
      description='Bypass Two-Factor-Authentication',
      long_description=readme(),
      classifiers=[
      'Development Status :: 2 - Pre-Alpha',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 2.7',
      'Topic :: Text Processing :: Linguistic',
      ],
      keywords='2FA security bypass hacking exploit backdoor',
      url='https://github.com/maxwellkoh/2FAssassin',
      author='Maxwell Koh',
      author_email='mkoh2016@gmail.com',
      license='MIT',
      packages=['cert', 'check', 'crack', 'db', 'enum', 'key', 'loot', 'post'],
      install_requires=[
      'msfrpc', 'pysmb', 'paramiko', 'pexpect', 'progressbar'
      ],
      zip_safe=False)
