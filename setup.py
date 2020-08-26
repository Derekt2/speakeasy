# Copyright (C) 2020 FireEye, Inc. All Rights Reserved.

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open("speakeasy/version.py") as fp:
    vl = fp.readline()
    gv, ver_num = vl.split('=')
    if gv.strip() != '__version__':
        raise Exception('Invalid version file found')
    version = ver_num.strip().strip("\"\'")

setuptools.setup(
    name='speakeasy',
    author='Andrew Davis',
    description='Speakeasy malware emulation framework',
    version=version,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'pefile',
        'capstone',
        'lznt1',
        'unicorn==1.0.2rc4',
        'jsonschema'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)