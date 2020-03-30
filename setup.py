import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="verizon-spider-man",
    version="0.0.1",
    author="Example Author",
    author_email="spiderman@spiderverse.com",
    description="A package which generates random number",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['verizon',],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)