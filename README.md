![occli](https://user-images.githubusercontent.com/74001397/137996387-d7f23e1b-395e-499e-8d4d-250d25cca115.jpg)

![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat&logo=python)
![GitHub](https://img.shields.io/github/license/rly0nheart/occli?style=flat)
![CodeFactor](https://www.codefactor.io/repository/github/rly0nheart/occli/badge)
![PyPI](https://img.shields.io/pypi/v/occli?style=flat&logo=pypi)
[![Downloads](https://static.pepy.tech/personalized-badge/occli?period=total&units=none&left_color=grey&right_color=yellowgreen&left_text=downloads)](https://pepy.tech/project/occli)
![GitHub repo size](https://img.shields.io/github/repo-size/rly0nheart/occli?style=flat&logo=github)

Occli is a lite command line interface for [Open Corporates](https://opencorporates.com), that queries and gets data on companies under the copyleft Open Database License.

# Installation
## Clone from Github
```
git clone https://github.com/rly0nheart/occli.git
```

```
cd occli
```

```
python setup.py sdist bdist_wheel
```

```
pip install dist/occli-[version.tag]-py3-none.whl
```

## Install from PyPI
```
pip install occli
```

# Usage
```
occli 'query'
```
## Updating
```
pip install --upgrade occli
```

# Optional Arguments
| Option         | Argument | Usage|
| ------------- |:----------------------:|:---------:|
| ``-o/--output``      |   path/to/file |  write output to a specified file  |
| ``-c/--count``  |    |  number of results to return (1-30) (default: 30) |
| ``-v/--verbose``  |    |  enable verbosity |

# Note
> Occli is in no way affiliated with Open Corporates. This project only uses their public API, therefore, user privacy policies and terms of service will be applied as provided by [Open Corporates](https://opencorporates.com/legal/user_privacy_policy) itself.

# LICENSE
![license](https://user-images.githubusercontent.com/74001397/137917929-2f2cdb0c-4d1d-4e4b-9f0d-e01589e027b5.png)
