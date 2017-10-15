from setuptools import setup

setup(
    name='chess-web',
    packages=['chess-web'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-redis',
    ],
)
