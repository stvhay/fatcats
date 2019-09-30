"""setup.py"""
import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="fatcats",
    version="0.0.1",
    author="Steve Hay",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tablador/fatcats",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4'
)
