# korNum
Change **[Korean number text -> Arabic number]** or<br>
**[Arabic number -> Korean number text]**

### Installation
* pypi: ```pip install korNum```
* source code:
  ```bash
  git clone https://github.com/study-ai-data/korNum.git
  cd knum
  python setup.py install
  ```

### Getting Started
* pypi
  ```python
  from korNum.chgFormat import kor2num
  
  
  text = "맛있는 포카칩이 구천팔백칠십육억오천사백삼십이만천백십일원!"
  result = kor2num(text)
  print(result) # 맛있는 포카칩이 987654321111원!
  ```
* source code:
  ```python run.py```

### Note
You can see more information here: [Description.md](https://github.com/study-ai-data/korNum/blob/master/Description.md)
