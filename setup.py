from setuptools import setup, find_packages
import knum

setup(name=knum.__name__,
      description=knum.__description__,
      version=knum.__version__,
      author=['Kyeongnam Kim'],
      author_email=['kkyy0126@naver.com'],
      url=knum.__url__,
      download_url=knum.__download_url__,
      install_requires=knum.__install_requires__,
      license=knum.__license__,
      long_description=open('./README.md', 'r', encoding='utf-8').read(),
      packages=find_packages(),
      classifiers=[
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
      ]
      )
