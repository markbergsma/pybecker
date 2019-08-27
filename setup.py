import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pybecker",
    version="0.0.1",
    author="Nicolas Berthel",
    author_email="contact@nicolasberthel.fr",
    description="pybecker is a library to control becker RF shutters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nicolasberthel/pybecker",
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules :: Hardware'
    ],
)