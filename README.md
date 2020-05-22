# korNum
[![Python](https://img.shields.io/pypi/pyversions/korNum.svg?style=plastic)](https://badge.fury.io/py/korNum)
[![PyPI](https://badge.fury.io/py/korNum.svg)](https://badge.fury.io/py/korNum)  
Change **[Korean number text -> Arabic number]** or<br>
**[Arabic number -> Korean number text]**

### Installation
* pypi: ```pip install korNum```
* source code:
  ```bash
  git clone https://github.com/study-ai-data/korNum.git
  cd korNum
  python setup.py install
  ```

### Getting Started
* pypi
  ```python
  >>> from korNum.chgFormat import kor2num
  >>> text1 = "맛있는 포카칩이 구천팔백칠십육억오천사백삼십이만천백십일원!"
  >>> print(kor2num(text1))
  맛있는 포카칩이 987654321111원!
  >>> text2 = "맛있는 포카칩이 구천팔백칠십육억오천사백삼십이만천백십일원에서 오백십만육십구원, 만오천구백원을 거쳐 이제는 천오백원으로!"
  >>> print(kor2num(text2))
  맛있는 포카칩이 987654321111원에서 5100069원, 15900원을 거쳐 이제는 1500원으로!
  ```
* source code:
  ```python run.py```

### Note
* only operate about cardinal number(기수: 일, 이, 삼, 사, ...) text -> real num
* You can see more information here: [Description.md](https://github.com/study-ai-data/korNum/blob/master/Description.md)
