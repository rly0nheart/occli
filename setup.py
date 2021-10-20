import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name="occli",
    version="0.2.2",
    author="Richard Mwewa",
    packages=["occli"],
    description="Unofficial Open Corporates Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rlyonheart/occli",
    license="GNU General Public License v3 (GPLv3)",
    install_requires=["requests==2.26.0"],
    classifiers=[
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',  
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        "console_scripts": [
            "occli=occli.__main__:occli",
            ]
    }
)
