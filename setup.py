from setuptools import setup

setup(
    name="pytalibstream",
    version="0.0.4",
    description="QS private package",
    url="git@github.com:QuantSatoshi/py-talib-stream.git",
    author="Hao Wang",
    author_email="hao@quantsatoshi.com",
    license="unlicense",
    packages=["pytalibstream"],
    zip_safe=False,
    install_requires=[
        "pyslidingwindow @ git+https://git@github.com/quantsatoshi/py-sliding-window#main",
    ],
)
