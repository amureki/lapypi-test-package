import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="test_package",
    version="0.0.1",
    author="Rustem Saiargaliev",
    author_email="hi@amureki.me",
    description="Dummy package to test lapypi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amureki/lapypi-test-package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)