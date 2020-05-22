from setuptools import setup, find_packages
import korNum

setup(name=korNum.__name__,
      description=korNum.__description__,
      version=korNum.__version__,
      author='Kyeongnam Kim',
      author_email='kkyy0126@naver.com',
      url=korNum.__url__,
      download_url=korNum.__download_url__,
      install_requires=korNum.__install_requires__,
      license=korNum.__license__,
      long_description=open('./README.md', 'r', encoding='utf-8').read(),
      long_description_content_type="text/markdown",
      packages=find_packages(),
      classifiers=[
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: Korean",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: MacOS",
            "Operating System :: POSIX",
      ]
      )
