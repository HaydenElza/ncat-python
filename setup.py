from setuptools import find_packages, setup

setup(
    name='ncat',
    packages=find_packages(include=['ncat']),
    version='0.1.0',
    description='Python Bindings for NGS Coordinate Conversion and Transformation Tool (NCAT)',
    author='Hayden Elza',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==5.3.1'],
    test_suite='tests',
)