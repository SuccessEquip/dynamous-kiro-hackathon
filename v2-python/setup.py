from setuptools import setup, find_packages

setup(
    name="core-framework",
    version="1.0.0",
    description="CORE Framework - Interactive Project Planning Tool (Python TUI)",
    author="CORE Framework Team",
    packages=find_packages(),
    install_requires=[
        "textual>=0.50.0",
        "rich>=13.0.0",
        "pydantic>=2.0.0",
        "click>=8.0.0",
    ],
    entry_points={
        "console_scripts": [
            "core-framework=core_framework.main:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
