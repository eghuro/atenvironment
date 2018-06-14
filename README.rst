============
@environment
============


.. image:: https://img.shields.io/pypi/v/atenvironment.svg
        :target: https://pypi.python.org/pypi/atenvironment

.. image:: https://img.shields.io/travis/eghuro/atenvironment.svg
        :target: https://travis-ci.org/eghuro/atenvironment

.. image:: https://readthedocs.org/projects/atenvironment/badge/?version=latest
        :target: https://atenvironment.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/eghuro/atenvironment/shield.svg
     :target: https://pyup.io/repos/github/eghuro/atenvironment/
     :alt: Updates


.. image:: https://codecov.io/gh/eghuro/atenvironment/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/eghuro/atenvironment



Decorator for convenient loading of environment variables


* Free software: MIT license
* Documentation: https://atenvironment.readthedocs.io.


Usage
--------

Usage
--------
Using @environment is as simple as::

  from atenvironment.atenvironment import environment

  @environment('API_KEY')
  @environment('TOKEN')
  def check(a, b, c, key, token):
      # API_KEY is in key
      # TOKEN is in token


