import pathlib

from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cga2121",
    version="1.0",
    description="Technicolor CGA2121 Gateway library",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/drolano/cga2121",
    author="drolano",
    author_email="drolano@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["cga2121"],
    include_package_data=True,
    install_requires=["six", "html2text", "robobrowser", "Werkzeug==0.16.1"],
)
