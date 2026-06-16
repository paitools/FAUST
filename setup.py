from pathlib import Path
from setuptools import setup

BASE_DIR = Path(__file__).parent

README = ""
readme_path = BASE_DIR / "README.md"
if readme_path.exists():
    README = readme_path.read_text(encoding="utf-8")

setup(
    name="faust-obda",
    version="1.0.0",
    description="Fine-tuning Automation System for LLM-driven Semantic Data Analysis",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Ivanovic, Hranisavljevic, and Maleshkova",
    url="https://github.com/paitools/FAUST",
    py_modules=[
        "main",
        "kg_maker",
        "kg_reader",
        "module_a",
        "module_d",
        "module_g",
    ],
    python_requires=">=3.9",
    install_requires=[
        "pandas>=2.0",
        "PyYAML>=6.0",
        "rdflib>=7.0",
        "scikit-learn>=1.3",
        "openpyxl>=3.1",
    ],
    extras_require={
        "moa": [
            "customtkinter>=5.2",
            "requests>=2.31",
            "ollama>=0.3",
        ],
    },
    entry_points={
        "console_scripts": [
            "faust=main:main",
        ],
    },
    include_package_data=True,
    data_files=[
        ("faust", ["config.yaml", "units_table.csv"]),
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Database",
    ],
)
