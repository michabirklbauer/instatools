import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="InstaTools",
    version="1.1.1",
    author="Micha Birklbauer",
    author_email="micha.birklbauer@gmail.com",
    description="A set of functions to access the public Instagram API and retrieve basic user data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/t0xic-m/instatools",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
