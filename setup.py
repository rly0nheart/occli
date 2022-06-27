import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name="occli",
    version="0.3.5",
    author="Richard Mwewa",
    author_email="richardmwewa@duck.com",
    packages=["occli"],
    description="Open Corporates CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rly0nheart/occli",
    license="GNU General Public License v3 (GPLv3)",
    install_requires=["requests"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',  
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 3'
        ],
    entry_points={
        "console_scripts": [
            f"occli=occli.main:onSearch",
        ]
    },
)
