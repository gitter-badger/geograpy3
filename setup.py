from setuptools import setup
from collections import OrderedDict

try:
    long_description = ""
    with open('README.md', encoding='utf-8') as f:
        long_description = f.read()

except (IOError, ImportError):
    long_description = open('README.md').read()

setup(name='geograpy3',
      version='0.1.6',
      description='Extract countries, regions and cities from a URL or text',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/somnathrakshit/geograpy3',
      download_url='https://github.com/somnathrakshit/geograpy3',
      author='Somnath Rakshit',
      author_email='somnath52@gmail.com',
      license='Apache',
      project_urls=OrderedDict(
        (
            ("Documentation", "https://geograpy3.netlify.app"),
            ("Code", "https://github.com/somnathrakshit/geograpy3"),
            ("Issue tracker", "https://github.com/somnathrakshit/geograpy3/issues"),
        )
      ),
      classifiers=[
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8'
      ],
      packages=['geograpy'],
      install_requires=[
          'numpy',
          'nltk',
          'newspaper3k',
          'jellyfish',
          'pycountry'
      ],
      scripts=['geograpy/bin/geograpy-nltk'],
      package_data={
          'geograpy': ['data/*.csv'],
      },
      zip_safe=False)
