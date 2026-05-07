from setuptools import setup, find_packages

setup(
    name='mci506-andres',
    version='0.1.0',
    author='Andres',
    author_email='andres@example.com',
    description='Data Engineering project for MCI506',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your project dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)