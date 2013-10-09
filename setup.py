from setuptools import setup, find_packages

version = '0.1.1'

with open('README.md', 'r') as f:
    long_desc = f.readlines()

setup(name='pyinter',
      version=version,
      description="An interval package which deals with open, closed or half open intervals.",
      long_description=long_desc,
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Development Status :: 3 - Alpha',
                   'License :: OSI Approved :: MIT License'],
      keywords='interval range discontinous-range union intersection',
      author='Inti Ocean',
      author_email='intiocean@gmail.com',
      url='intiocean.com',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
