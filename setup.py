from setuptools import setup, find_packages

setup(
    name="topdeps",
    description="Brew top dependencies extractor",
    author="Illia Khudoshyn",
    author_email="illia.khudoshyn@gmail.com",
    packages=find_packages(),
    setup_requires=["setuptools_scm"],
    use_scm_version=True,
    include_package_data=True,
    entry_points={"console_scripts": ["topdeps=topdeps.topdeps:main"]},
)
