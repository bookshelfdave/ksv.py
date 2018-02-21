ksv
===

|image|

|image|

|Documentation Status|

ksv decodes/encodes entire Kubernetes secrets files

-  Free software: Apache Software License 2.0
-  Documentation: https://ksv.readthedocs.io.

Installation
------------

::

    pip install ksv

Usage
-----

Decoding all secret values:

::

    ksv < some_secrets_file_with_base64_encoded_data_values.yaml

Encoding all secret values:

::

    ksv --encode < some_secrets_file_with_plaintext_data_values.yaml

Round trip:

::

    ksv < test.yaml | ksv --encode

Features
--------

-  TODO

Credits
-------

This package was created with
`Cookiecutter <https://github.com/audreyr/cookiecutter>`__ and the
`audreyr/cookiecutter-pypackage <https://github.com/audreyr/cookiecutter-pypackage>`__
project template.

.. |image| image:: https://img.shields.io/pypi/v/ksv.svg
   :target: https://pypi.python.org/pypi/ksv
.. |image| image:: https://img.shields.io/travis/metadave/ksv.svg
   :target: https://travis-ci.org/metadave/ksv
.. |Documentation Status| image:: https://readthedocs.org/projects/ksv/badge/?version=latest
   :target: https://ksv.readthedocs.io/en/latest/?badge=latest
