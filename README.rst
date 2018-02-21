ksv
===

 decodes/encodes entire Kubernetes secrets files

-  Free software: Apache Software License 2.0

Installation
------------

::

    pip install ksv
    # or pip3, ksv requires Python 3

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


Credits
-------

This package was created with
`Cookiecutter <https://github.com/audreyr/cookiecutter>`__ and the
`audreyr/cookiecutter-pypackage <https://github.com/audreyr/cookiecutter-pypackage>`__
project template.

