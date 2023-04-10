from setuptools import setup, Extension

ext = [
    Extension(
        "example._example",
        ["src/example/_example.c"]
    )
]

setup(
    name="example",
    version="0.1.0",
    description="A test project using cython",
    package_dir={"": "src"},
    packages=["example"],
    python_requires=">=3.8",
    ext_modules=ext,
    include_package_data=True,
    exclude_package_data={"": ["*.c"]},
)