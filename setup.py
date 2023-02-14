from setuptools import setup, find_packages

setup(
    name='database-demo',
    description='',
    author='Dan Fornika',
    author_email='dan.fornika@bccdc.ca',
    url='https://github.com/dfornika/database-demo',
    packages=find_packages(exclude=('tests', 'tests.*')),
    python_requires='>=3.10',
        install_requires=[
        "sqlalchemy==1.4.44",
        "alembic==1.8.1",
    ],
    setup_requires=['pytest-runner', 'flake8'],
    tests_require=[],
    entry_points = {
        'console_scripts': [],
    }
)
