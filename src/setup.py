# setup.py
from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        "s21_list",
        sources=["python/bindings/list.pyx"],
        language="c++",
        include_dirs=["cpp/list"]
    ),
    Extension(
        "s21_queue",
        sources=["python/bindings/queue.pyx"],
        language="c++",
        include_dirs=["cpp/queue"]
    ),
    Extension(
        "s21_stack",
        sources=["python/bindings/stack.pyx"],
        language="c++",
        include_dirs=["cpp/stack"]
    )

]

setup(
    name="cpp_libs",
    ext_modules=cythonize(extensions),
)
