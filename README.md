ksv
===

[![image](https://img.shields.io/pypi/v/ksv.svg)](https://pypi.python.org/pypi/ksv)

[![image](https://img.shields.io/travis/metadave/ksv.svg)](https://travis-ci.org/metadave/ksv)

[![Documentation Status](https://readthedocs.org/projects/ksv/badge/?version=latest)](https://ksv.readthedocs.io/en/latest/?badge=latest)

ksv decodes/encodes entire Kubernetes secrets files

-   Free software: Apache Software License 2.0
-   Documentation: <https://ksv.readthedocs.io>.

Installation
--------

```
pip install ksv
```


Usage
--------

Decoding all secret values:

```
ksv < some_secrets_file_with_base64_encoded_data_values.yaml

```

Encoding all secret values:

```
ksv --encode < some_secrets_file_with_plaintext_data_values.yaml
```

Round trip:

```
# KSV *will* resort keys automatically
ksv < test.yaml | ksv --encode
```

Features
--------

-   TODO

Credits
-------

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
project template.
