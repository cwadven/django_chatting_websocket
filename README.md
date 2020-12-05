<code><img src="https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white"/></code>
<code><img src="https://img.shields.io/badge/redis%20-%23CC342D.svg?&style=for-the-badge&logo=redis&logoColor=white"/></code>

# 구축 방법

1. 가상환경 생성
> python -m venv 가상환경이름

2. 가상환경 실행
> source 가상환경이름/bin/activate (가상환경 실행)
(Windows : source 가상환경이름/Script/activate)

3. 필요한 모듈 가상환경에 설치 
> pip install -r requirements.txt

4. Redis 서버 설치
> 설치 방법

(https://redis.io/topics/quickstart)
(Linux)
(https://github.com/tporadowski/redis/releases)
(Windows)

5. Redis 실행
> redis-server

(Linux)

Redis 설치한 곳 Programfiles의 Redis에서 파일 실행

> redis-server.exe

(Windows)

6. WAS 테스트 서버 실행
> python manage.py runserver 0.0.0.0:8000

7. 홈페이지
> http://my.computer.host.ip/chat/

<img alt="outside" src="https://github.com/cwadven/django_chatting_websocket/blob/master/assets/chat_room.PNG" />

8. 채팅방들어가서 채팅하기
> http://my.computer.host.ip/chat/채팅방이름/

<img alt="inside" src="https://github.com/cwadven/django_chatting_websocket/blob/master/assets/chat_home.PNG" />