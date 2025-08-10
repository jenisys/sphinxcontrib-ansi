# -*- coding: utf-8 -*-
# Copyright (c)2010, 2011 Sebastian Wiesner <lunaryorn@googlemail.com>
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


from setuptools import setup, find_packages, find_namespace_packages

with open('README.rst') as stream:
    long_desc = stream.read()

setup(
    name='sphinxcontrib-ansi',
    version='0.7.2',
    url='https://github.com/sphinx-contrib/ansi',
    download_url='http://pypi.org/project/sphinxcontrib-ansi',
    license="BSD-2-Clause",
    author='Sebastian Wiesner',
    author_email='lunaryorn@googlemail.com',
    description='Sphinx extension ansi',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    # packages=find_packages(),
    packages=find_namespace_packages(where="./", include=["sphinxcontrib.ansi"]),
    # namespace_packages=["sphinxcontrib"],
    include_package_data=True,
    setup_requires=[
        "setuptools",
        "setuptools_scm",
    ],
    install_requires=[
        "sphinx >= 2.0",
        "docutils >= 0.21.2",
    ],
    tests_require = [
        "pytest < 5.0; python_version < '3.0'",  # >= 4.2
        "pytest >= 5.0; python_version >= '3.0'",
        "pytest-html >= 1.19.0, < 2.0; python_version < '3.0'",
        "pytest-html >= 2.0; python_version >= '3.0'",
    ],
)
