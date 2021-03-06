import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="UzTranslit",
    version="0.0.7",
    author="Ulugbek Salaev, Elmurod Kuriyozov",
    author_email="ulugbek0302@gmail.com, e.kuriyozov@udc.es",
    description="UzTranslit | Transliteration tool for Uzbek language - Cyrillic<>Latin<>NewLatin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UlugbekSalaev/UzTranslit",
    project_urls={
        "Bug Tracker": "https://github.com/UlugbekSalaev/UzTranslit/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=['python', 'transliteration', 'uzbek', 'cyrillic', 'latin'],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
