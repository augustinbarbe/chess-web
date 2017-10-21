from setuptools import setup

setup(
    name='chessweb',
    packages=['chessweb'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-redis',
        'requests',
    ],
)
