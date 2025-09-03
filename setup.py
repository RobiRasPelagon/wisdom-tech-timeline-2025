from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read the contents of your requirements file
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="wisdom-tech-timeline-2025",
    version="0.1.0",
    author="RobiRasPelagon and The Community",
    author_email="your-email@example.com",  # You can change this to a real contact email if you want
    description="A blueprint for a nature-aligned civilization, featuring an ethical AI companion.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RobiRasPelagon/wisdom-tech-timeline-2025",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Sociology",
    ],
    python_requires='>=3.9',
    entry_points={
        'console_scripts': [
            'stibera=main:main',
        ],
    },
)

