from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mlibproject",
    version="0.22",
    author="Farid Ahamada",
    author_email="farid.ahamada25@gmail.com",
    description="The objective of this package is to group"
                "together a set of functions that I commonly use in ML projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FaridAhamadaGunners/ML_Librairie",
    packages=find_packages(exclude=['tests']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering"
    ],
    install_requires=[
        'pandas',
        'seaborn',
        'matplotlib',
        'scikit_learn'
    ],
    python_requires='>=3.6'
)
