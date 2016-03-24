from setuptools import find_packages
from setuptools import setup

import os


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.rst')) as f:
    CHANGES = f.read()


setup(name='pyramid_supervisord_cluster_dashboard',
      version='0.1.0.dev0',
      description='pyramid_supervisord_cluster_dashboard',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          'License :: OSI Approved :: GPL',
          'Programming Language :: Python',
          'Natural Language :: English',
          #'Natural Language :: German',
          'Operating System :: OS Independent',
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='Alexander Loechel',
      author_email='Alexander.Loechel@lmu.de',
      url='',
      license='GPLv2',
      keywords='web pylons pyramid supervisord dashboard',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Dependencies -*-
          'setuptools',
          # -*- Extra requirements: -*-
          'pyramid',
          'pyramid_chameleon',
          'pyramid_debugtoolbar',
          'pyramid_tm',
          'pyramid_zodbconn',
          'transaction',
          'ZODB',
          'waitress',
      ],
      setup_requires=[],
      tests_require=[
          # -*- Add additional test dependencies -*-
      ],
      test_suite="pyramid_supervisord_cluster_dashboard",
      entry_points="""\
      [paste.app_factory]
      main = pyramid_supervisord_cluster_dashboard:main
      """,
      )
