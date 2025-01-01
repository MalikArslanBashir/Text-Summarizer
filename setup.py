from setuptools import setup, find_packages

# Metadata
__version__ = "0.0.0"
REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "MalikArslanBashir"
SRC_REPO = "textsummarizer"
AUTHOR_EMAIL = "malikarslaninfo575@gmail.com"

# Read long description from README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Setup configuration
setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),  # Automatically discovers packages in 'src'
    install_requires=[],  # Add dependencies if needed
)