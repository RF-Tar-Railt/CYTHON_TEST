PYXS = $(wildcard src/example/*.pyx)


src/example/%.c: src/example/%.pyx
	python -m cython -3 -o $@ $< -I src/example


cythonize: $(PYXS:.pyx=.c)