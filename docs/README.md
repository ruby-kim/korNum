# Project Description
## Installation
* pypi: ```pip install korNum```
* source code:
  ```bash
  git clone https://github.com/study-ai-data/korNum.git
  cd korNum
  python setup.py install
  ```

## Getting Started
* pypi
  ```python
  >>> from korNum.chgFormat import kor2num
  >>> text1 = "맛있는 포카칩이 구천팔백칠십육억오천사백삼십이만천백십일원!"
  >>> print(kor2num(text1))
  맛있는 포카칩이 987654321111원!
  >>> text2 = "맛있는 포카칩이 구천팔백칠십육억오천사백삼십이만천백십일원에서 오백십만육십구원, 만사천칠백원을 거쳐 이제는 천오백원으로!"
  >>> print(kor2num(text2))
  맛있는 포카칩이 987654321111원에서 5100069원, 14700원을 거쳐 이제는 1500원으로!
  ```
* source code:
  ```python run.py```

## File Structure
```
.
├─ docs
│  ├─ contri_guide.md
│  └─ READMD.md
├─ korNum
│  ├─ __init__.py
│  ├─ chgFormat.py
│  └─ chgList.py
├─ .gitignore
├─ LICENSE
├─ README.md
├─ run.py  
├─ setup.cfg  
└─ setup.py
```

## File description
File description except for docs files

### ```./run.py```
* test script: input your text in ```line 5```

### ```knum/chgFormat.py```
* change format: the process of kor2num(only cardinal num), num2kor(Not Yet)
* Judgement Algorithm: When units appear, determine whether they are numbers by looking at the status of the words immediately preceding them.
  ```bash
  나에게는 구멍난 원이 있어.
  ```
  * 여기서 ```원```은 금액의 단위 또는 도형 등 다양한 의미를 가짐
  * 하지만 ```원```의 앞에는 ```구멍난```이라는,<br>정확히 말해서 ```난```은 숫자단위가 아님
  * 따라서 여기에는 숫자로 구성된 텍스트가 없는 것으로 판단
  ```bash
  나 오늘 포카칩 샀는데 행사해서 하나 가격으로 다섯개 샀어!!
  ``` 
  * 여기서 ```포```는 인삼이나 자루 등을 세는 단위 또는 포카칩이라는 명사의 일부분,<br>```개```는 물건을 세는 단위 또는 동물 등 다양한 의미를 가짐
  * ```포```앞의 ```늘```은 숫자를 세는 단위가 아님<br>```개```앞의 ```다섯```은 숫자를 세는 단위
  * 따라서 해당 문장에서는 숫자로 구성된 텍스트가 존재하고, 그 부분이 바로 다섯이라는 것을 알 수 있음

### ```knum/chgList.py```
* change list: [**cardinal** "text" & "real num"] list + [**ordinal** "text" & "real num"] list + [**unit** about cardinal & ordinal] list
