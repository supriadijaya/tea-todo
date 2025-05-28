from setuptools import setup, find_packages

setup(
    name="tea-todo",
    version="0.1",
    packages=find_packages(),
    project_urls={
        "Source": "https://github.com/supriadijaya/tea-todo"
    },
    author="supriadijaya",
    description="A simple todo app to learn Tea Protocol",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

