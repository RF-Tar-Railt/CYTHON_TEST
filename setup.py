from setuptools import setup, Extension, Command
from setuptools.command.build_ext import build_ext
from setuptools.command.sdist import sdist
from pathlib import Path
from Cython.Build import cythonize
import glob
import sys

example_source = "src/example/_example.pyx"
cython_sources =[example_source]
Sdist = sdist

class Clean(Command):
    description = "clean the build directory"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        for source in cython_sources:
            genc = Path(source).with_suffix(".c")
            genc.unlink(missing_ok=True)
            for compiled in sorted(glob.glob(source.replace(".pyx", ".cpython*"))):
                Path(compiled).unlink(missing_ok=True)

cmdclass = {
    "clean2": Clean,
    "sdist": Sdist,
    "build_ext": build_ext,
}

cflags = ["-Wall"]

ext = [
    Extension(
        "example._example",
        [example_source],
        extra_compile_args=cflags,
    )
]

cythonizing = (
    len(sys.argv) > 1
    and sys.argv[1] not in ("clean", "clean2", "egg_info", "--help-commands", "--version")
    and "--help" not in sys.argv[1:]
)

if cythonizing:
    cython_opts = {
        "compiler_directives": {
            "language_level": "3str",
        }
    }
    ext = cythonize(ext, **cython_opts)

setup(
    name="example",
    version="0.1.0",
    description="A test project using cython",
    package_dir={"": "src"},
    packages=["example"],
    python_requires=">=3.8",
    cmdclass=cmdclass,
    ext_modules=ext,
    include_package_data=True,
    exclude_package_data={"": ["*.c"]},
)