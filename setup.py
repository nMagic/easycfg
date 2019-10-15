import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easycfg",
    version="1.0.1",
    author="Dmitriy Glebenkov",
    author_email="dvg1995@gmail.com",
    description="A simple package for easy work with cfg files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nMagic/easycfg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
    install_requires=['PyYAML==5.1.2', ]
)
