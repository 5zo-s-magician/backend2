## 씨없는 멜론 
![661860884_7i9ZF3CS_5722828239e4aa8bba0c01eb981aa22ba4b88254](https://user-images.githubusercontent.com/51503799/190332972-9cd33c17-6002-4204-bf96-1c30dbe68278.jpeg)

### 0. Introduce
음원에서 원하는 멤버의 목소리를 원하는 타겟 목소리로 변형시켜주는 프로그램
![KakaoTalk_Photo_2022-09-15-15-19-52](https://user-images.githubusercontent.com/51503799/190329199-3ac5894d-7ffd-4998-aef2-ca6ac7d06203.png)





### 1. Program Flow
![KakaoTalk_Photo_2022-09-15-15-19-46](https://user-images.githubusercontent.com/51503799/190329054-698b4940-4a28-442e-80e8-caaa4082ece6.png)


### 2. Backend 
- **MELGAN * 폴더, pretrained_models** : 데이터를 통해 목소리 변환 머신러닝을 학습시킨 파라미터, 모델을 저장하는 폴더
- **lyricparsing.py**: 
	* <code>input</code>: 사용자가 선택한 음원 이름, 사용자가 올린 음원 파일
	* <code>output</code>: 멤버별 파트 타임스탬프
	* 가사 사이트에서 사용자가 입력한 곡의 가사와 파트별 타임스탬프를 크롤링 해온다.
	
- **audio_cut.py**: 
	* <code>input</code>: 사용자가 선택한 멤버
	* <code>output</code>: 선택된 멤버의 파트를 기준으로 자른 음원 파일들
	* 사용자가 변환하고 싶은 멤버의 파트에 해당되는 음원을 잘라 저장한다. (예시: 멤버 A의 파트가 1:00부터 1:20이면 1:00, 1:20을 기준으로 음원 파일을 잘라 3파일을 생성한 뒤 저장한다)
	
- **voice_conversion.py**
	* <code>input</code>: 멤버의 목소리가 담긴 음원 파일
	* <code>output</code>: 멤버의 목소리가 변환된 음원 파일
	*  1) audio_cut.py로 잘라진 음원 파일 중, 사용자가 변환하고 싶다고 지정한 멤버의 목소리가 담긴 파일을 목소리와 MR로 분리한다.
		2) 목소리만 담긴 파일을 input으로 해서 목소리를 변환한다. 이후 변환된 목소리 파일과 MR파일을 다시 합쳐 변환된 음원 파일을 저장한다.

- **final_mp3.py**
	* <code>input</code>: lyricparsing.py에서 저장한 멤버별 파트 타임스탬프, 잘려진 음원 파일들
	* <code>output</code>: 변환된 목소리가 담긴 완전한 음원 파일
	* 멤버별 파트 타임 스탬프를 바탕으로 잘려진 음원 파일들을 다시 이어붙여 하나의 완성된 음원 파일을 만든다.
	
- **app.py** : flask를 기반으로 만든 백엔드 파일. 위에서 언급한 함수들을 사용해 서비스를 제공한다.

### 3. 개발 파트 분배
- <code>김현주</code>: 팀장, 아이디어 제공, 목소리 데이터셋 모으기, TTS 모델 학습, code 수합, flask 백엔드 개발
- <code>이현주</code>: 목소리 데이터셋 모으기, voice conversion 모델 학습, 가사 파싱, react 프론트엔드 개발
- <code>임예린</code>: 목소리 데이터셋 모으기, spleeter 및 파트 편집 등 음원 데이터 전처리
