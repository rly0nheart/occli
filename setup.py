from setuptools import setup

setup(
    name='opencorps',
    version='0.1.0',    
    description='An unofficial Open Corporates CLI tool',
    url='https://github.com/rlyonheart/opencorps:',
    author='Richard Mwewa',
    author_email='r1chardmw3wa@gmail.com',
    license='GPL-3.0 License',
    packages=['opencorps'],
    install_requires=['requests>=2.26.0',
    ],

    classifiers=[
        'Intended Audience :: Cybersecurity/Research',
        'License :: OSI Approved :: GPL-3.0 License',  
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.9',
    ],
)
