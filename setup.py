from setuptools import setup, find_packages

import sys, os

setup(
    name='paginate_cloudstore',
    version='0.1.0',
    description="Extension to paginate.Page that supports Google Cloud Store.",
    long_description="""
        This module helps divide up large result sets into pages or chunks.
        The user gets displayed one page at a time and can navigate to other pages.
        It is especially useful when developing web interfaces and showing the
        users only a selection of information at a time.

        This module uses and extends the functionality of the paginate module to
        support Cloud Store Iterator
        """,

    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    keywords='pagination paginate google cloud store',
    author='Ji-Ho Lee',
    author_email='search5@gmail.com',
    maintainer='Ji-Ho Lee',
    maintainer_email='search5@gmail.com',
    install_requires=[
        "google-cloud-datastore==1.7.2",
        "paginate>=0.4"
        ],
    url='https://github.com/search5/paginate_cloudstore',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points=""" """,
)

