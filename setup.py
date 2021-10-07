import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name="occli",
    version="0.1.3",
    author="Richard Mwewa",
    packages=["occli"],
    description="An unofficial Open Corporates python CLI tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rlyonheart/occli",
    classifiers=[
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',  
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.9',
    ],
)
