import sys
from setuptools import setup, find_packages

setup(
    name="panda.py",
    version="1.0.0",
    author="Santiago Serrano",
    author_email="sant.serrano@icloud.com",
    description="Tkinter Framework",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/santserrano/panda",
    packages=find_packages(),
    install_requires=[
        "customtkinter",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "panda-dev=panda.engine.run:main",
        ],
    },
)
