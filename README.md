# ✨workspace-fastapi

🎉 FastAPI를 공부하면 Youtubu Clone 및 실전 Project에 적용하기 위한 테스트

🎉 주로 Python 3.10.x 이상에서 실행 가능

## 🎁 1. package 관리

### 1-1. Poetry를 이용하여 Python Package 관리.

- windows pc 에서의 poetry 설치

    - Python 설치
    - pip install virtualenv 설치
    - virtualenv .venv
    - .venv\script\active
    - pip install poetry

### 2-1 poetyr 간단 명령어

- 신규 프로젝트 생성

> poetry new <project_name>

- python package add

> poetry add <package_name>

- python package delete

> poetry remove <package_name>

- poetry export requirements

> poetry export --without-hashes --format=requirements.txt > requirements.txt

- poetry를 이용한 python package 설치

> poetry install

## 🆚 2. vscode Extention 관리

> code --list-extensions | xargs -L 1 echo code --install-extension > vscode-extensions.txt