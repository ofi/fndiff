"""
    setup.py -- Package setup to fndiff
    See LICENSE for copyright information.
"""
from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='fndiff',
      version='0.1',
      description='List unpaired files in directories acc. to name patterns',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Environment :: Console',
        'Operating System :: POSIX',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'Topic :: Desktop Environment :: File Managers',
      ],
      keywords='filenames diff shell tools',
      url='http://github.com/ofi/fndiff',
      author='Olaf Fiedler',
      author_email='software@olaf-fiedler.de',
      license='MIT',
      packages=['fndiff'],
    #   install_requires=[
    #       'markdown',
    #   ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['fndiff=fndiff.fndiff_cli:main'],
      },
      include_package_data=True,
      zip_safe=False)