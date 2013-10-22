import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'pyramid_beaker',
    'zope.sqlalchemy',
    'waitress',
    'markdown',
    'bitcoin-python',
    ]

setup(name='ccvpn',
      version='0.0',
      description='ccvpn',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='ccvpn',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = ccvpn:main
      [console_scripts]
      initialize_ccvpn_db = ccvpn.scripts.initializedb:main
      ccvpn_checkbtcorders = ccvpn.scripts.checkbtcorders:main
      """,
      )
