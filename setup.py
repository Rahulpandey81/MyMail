import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MyMail",
    version="0.0.2",
    author="Rahul Pandey",
    author_email="rahulpandey.rp1996@gmail.com",
    description="A small example package By Rahul Pandey",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rahulpandey81/MyMail",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)