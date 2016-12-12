from setuptools import find_packages
from setuptools import setup

import os


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'docs', 'CHANGES.rst')) as f:
    CHANGES = f.read()


setup(name='pyramid_supervisord_cluster_dashboard',
      version='0.1.0.dev0',
      description='A Cluster-Dashboard for supervisord',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          'License :: OSI Approved :: GPL',
          'Programming Language :: Python',
          'Operating System :: OS Independent',
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
          "Topic :: System :: Clustering",
          "Topic :: System :: Monitoring",
          "Development Status :: 2 - Pre-Alpha",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          'Natural Language :: English',
          'Natural Language :: German',
      ],
      author='Alexander Loechel',
      author_email='Alexander.Loechel@lmu.de',
      url='',
      license='GPLv2',
      keywords='web pylons pyramid supervisord cluster dashboard',
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
          'pyramid_layout',
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
