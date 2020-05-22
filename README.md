# kor2num
Change korean text num to 
한글로 구성된 숫자를 아라비안 숫자로 바꿔주는 코드
### Installation
* pypi: ```pip install knum```
* source code:
  ```bash
  git clone https://github.com/study-ai-data/knum.git
  cd knum
  python setup.py install
  ```
### Getting Started
* pypi
  ```python
  from knum.chgFormat import kor2num
  
  
  text = "맛있는 포카칩이 구천팔백칠십육억오천사백삼십이만천백십일원!"
  result = kor2num(text)
  print(result) # 맛있는 포카칩이 987654321111원!
  ```
* source code:
  ```python run.py```
