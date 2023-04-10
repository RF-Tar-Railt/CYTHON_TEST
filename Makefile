PYXS = $(wildcard src/example/*.pyx)
SRC = src/example setup.py


.install-cython: requirements/cython.txt
	pip install -r requirements/cython.txt
	touch .install-cython


src/example/%.c: yarl/%.pyx
	python -m cython -3 -o $@ $< -I src/example


.cythonize: .install-cython $(PYXS:.pyx=.c)


cythonize: .cythonize
