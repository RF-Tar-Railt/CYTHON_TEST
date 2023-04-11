from setuptools import setup, Extension


extensions = [
    Extension("example._example", ["src/example/_example.c"])
]

setup(ext_modules=extensions)