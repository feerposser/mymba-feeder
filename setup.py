from setuptools import find_packages, setup, version

setup(
    name="mymba-feeder",
    author="Fernando Posser Pinheiro",
    url="https://github.com/feerposser/mymba-feeder",
    version="0.0.1",
    packages=find_packages(
        include=[
            "mymba-feeder",
            "tests"],
        exclude=[
            "*.__pycache__"
        ]),
    include_package_data=True,
    zip_file=False,
    install_requires=[
        "Flask==1.1.2",
        "requests==2.25.0",
        "flask-mongoengine==1.0.0",
        "flask-cors"
    ],
    extras_require={
        "dev_tools": [
            "pytest",
            "pytest-flask",
            "flask-shell-ipython",
            "faker"
        ]
    }
)