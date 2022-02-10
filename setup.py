try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

f = open("README.rst", "r")
readme = f.read()
f.close()


setup(
    name="CalCalc",
    version="0.0.1",
    description="CalCalc: some catchy description",
    long_description=readme,
    author="Christian H. Bye",
    author_email="chbye@berkeley.edu",
    url="https://github.com/christianhbye/calcalc",
    packages=["calcalc"],
    install_requires=[
        'numpy',
        'requests'
        ],
    extras_require={'tests': 'pytest'}
    include_package_data=True,
    python_requires=">=3.6",
    license="MIT",
    classifiers=[
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
)
