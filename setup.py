from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Daniella",
    author_email="danyrodriguesti@gmail.com",
    description="Image Processing Package using Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DanyJapah/Desafio-criacao-de-pacotes-de-processamento-de-imagens-em-Python.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)