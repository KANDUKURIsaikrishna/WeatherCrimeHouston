import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "WeatherCrimeHouston"
AUTHOR_USER_NAME = "XuanQin"
SRC_REPO = "WeatherCrimeHouston"
AUTHOR_EMAIL = "milanbeherazyx@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for WeatherCrimeHouston app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://dagshub.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://dagshub.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)