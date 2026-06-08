"""
TasteGuard - Setup Configuration
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="taste-guard",
    version="1.0.0",
    author="AI Agent",
    author_email="agent@example.com",
    description="AI Content Quality Guardian - Evaluate and optimize AI-generated content",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/taste-guard",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Content Creators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "click>=8.0.0",
        "rich>=13.0.0",
        "requests>=2.28.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "taste-guard=taste_guard.cli:cli",
            "tg=taste_guard.cli:cli",
        ],
    },
    keywords="ai content quality analysis optimization nlp text",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/taste-guard/issues",
        "Source": "https://github.com/yourusername/taste-guard",
    },
)
