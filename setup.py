from setuptools import setup, find_packages

setup (
    name='dbus_webapi',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'pydbus',
        'json-rpc'
    ],
)

