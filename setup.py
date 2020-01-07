import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytoexe", 
    version="0.0.1",
    author="Wardopdem",
    author_email="wardopdem@gmail.com",
    description="Creating windows executable  that calling python interpretter from Pyton's script.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages('src'),
    package_dir={'':'src'},
    package_data={'pytoexe': ['exe_mods/*.exe']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'pytoexe = pytoexe.__main__:main',
        ],
    },
)