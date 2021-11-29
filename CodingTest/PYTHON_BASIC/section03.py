# Section03
# 파이썬 가상환경 개념, 설정 및 pip 사용법, vscode 연동

#외부 설치 패키지 테스트
import simplejson as json

test_dict = {'1': 95, '4': 77, '3': 65, '5': 100, '2': 88}

#simplejson 실행
print(json.dumps(test_dict, sort_keys=True, indent=4 * ' '))


'''
** 가상환경은 왜 쓰는 가?
:   서로 다른 버전의 여러 모듈을 사용하여, 여러 프로젝트를 진행하더라도
	별개의 가상환경을 통해 프로젝트를 위한 환경을 깔끔하게 구성하고 관리할 수 있다.
 
** 가상환경에 pip 명령어를 활용하여, 패키지를 설치하고 관리해준다.
 
python -m venv 가상환경명
	Script\activate.bat
	Script\deactivate.bat
	pip 명령어 : search , install, uninstall, [list], freeze, show, upgrade
 
	pip install search simplejson , simple*
	pip install install simplejson
	pip install install simplejson==버전
	pip install --upgrade simplejson
 
	pip show simplejson
	pip show -f simplejson
 
	pip freeze > packages.txt
	pip freeze --all > packages.txt
 
	pip install -r packages.txt


	python -m venv /path/to/venv : 윈도우, 맥, 리눅스 동일

	윈도우 : Script
	맥 : bin

	윈도우 

	activate.bat : 가상환경 진입
	deactivate.bat : 가상환경 해제

	맥
	source ./activate : 가상환경 진입
	source ./deactivate : 가상환경 해제

	command : code 실행
'''