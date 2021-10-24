# CHANGELOG
**Improvements**:
* can now get information on an individual company, including company officer's information	
* added flag  <code>-n/--company-number</code> ;used for specifying which company to get information on
* added flag  <code>-j/--jurisdiction-code</code> ;used for specifying which jurisdiction code to check (recommended: should be used with <code>-n/--company-number</code>)
* bug fixes

# Unofficial Open Corporates CLI

![occli](https://user-images.githubusercontent.com/74001397/137996387-d7f23e1b-395e-499e-8d4d-250d25cca115.jpg)
![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=flat&logo=linux)
![GitHub](https://img.shields.io/github/license/rlyonheart/occli?style=flat&logo=github)
![CodeFactor](https://www.codefactor.io/repository/github/rlyonheart/occli/badge)
![Lines of code](https://img.shields.io/tokei/lines/github/rlyonheart/occli?style=flat&logo=github)
![PyPI](https://img.shields.io/pypi/v/occli?style=flat&logo=pypi)
[![Downloads](https://static.pepy.tech/personalized-badge/occli?period=total&units=none&left_color=grey&right_color=yellowgreen&left_text=pypi%20downloads)](https://pepy.tech/project/occli)
![GitHub repo size](https://img.shields.io/github/repo-size/rlyonheart/occli?style=flat&logo=github)

[Open Corporates](https://opencorporates.com) *is a website that shares data on corporations under the copyleft Open Database License. 
This is an unofficial open corporates command line client.*

# Installation
**Clone From Github**:
```
$ git clone https://github.com/rlyonheart/occli.git

$ cd occli
```

**Install From PyPI**:
```
$ pip install occli
```

**Upgrade to latest version**:
```
$ python -m pip install --upgrade occli
```


# Usage
**Github Clone**:
```
$ python occli -c COMPANY-NAME
```

**Viewing API version information**:
```
$ python occli --versions
```

**Getting information on an individual company**:
```
$ python occli -n COMPANY-NUMBER -j JURISDICTION-CODE
```


**PyPI Package**:
```
$ occli -c COMPANY-NAME
```

**Viewing version information**
```
$ occli --versions
```

**Getting information on an individual company**:
```
$ occli -n COMPANY-NUMBER -j JURISDICTION-CODE
```

# Optional Arguments
| Flag         | MetaVar | Usage|
| ------------- |:----------------------:|:---------:|
| <code>-c/--company</code> | **COMPANYNAME** |  *name of company*  |
| <code>-j/--jurisdiction-code</code> | **JURISDICTION-CODE** |  *company jurisdiction code*  |
| <code>-n/--company-number</code> | **COMPANYNUMBER** |  *company number*  |
| <code>--versions</code>  |    |  *get latest Open Corporates API version information*  |
| <code>-o/--output</code>      |   **FILENAME** |  *output filename*  |
| <code>-r/--raw</code>  |    |  *return results in raw json format*  |
| <code>-v/--verbosity</code>  |    |  *run program in verbose mode*  |



# LICENSE
![license](https://user-images.githubusercontent.com/74001397/137917929-2f2cdb0c-4d1d-4e4b-9f0d-e01589e027b5.png)

# About author
* [About.me](https://about.me/rlyonheart)

# Contact author
* [Github](https://github.com/rlyonheart)

* [Twitter](https://twitter.com/rly0nheart)
