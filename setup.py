from setuptools import setup, find_packages

setup(
    name="webserver",
    platforms="all",
    packages=find_packages(exclude=["tests"]),
    install_requires=["aiohttp", "pytest"],
    entry_points={"console_scripts": ["webserver-api = webserver:main"]},
)
