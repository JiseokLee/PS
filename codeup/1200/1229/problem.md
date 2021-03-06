# 1229 : 비만도 측정 2

시간 제한: 1 Sec 메모리 제한: 128 MB

## 문제 설명

앞의 브로카 공식은 사실 키가 160cm 이상일 경우에만 적용되는 식이다.

만약 키가 160cm보다 작을 때는 다음과 같은 공식을 사용한다.

- 표준몸무게

키에 따른 표준몸무게 공식
키가 150 미만일 때 (실제 키 - 100)
키가 150이상 160미만일 때 (실제 키 - 150) /2 + 50
키가 160 이상일 때 (실제 키 - 100) \* 0.9

- 비만도 계산 공식

항목 공식
비만도 =
(실제 몸무게 - 표준몸무게) \* 100 / 표준 몸무게

- 비만도에 따른 등급 판정

등급 비만도 수치
10 이하 정상
10~20 이하 과체중
20 초과 비만
예시)

키가 150Cm 이고, 몸무게는 60kg이라고 하자.

표준 몸무게 = (150 - 150) / 2 + 50 = 50 kg

비만도 = (60 - 50) \* 100 / 50 = 20

따라서 비만도가 20 이므로 "과체중"

## 입력

키와 몸무게가 공백을 기준으로 입력된다.(실수)

반드시 double형을 사용해야 함. float으로 하면 오답처리되는 케이스가 있음.

## 출력

비만도에 따른 등급을 출력한다.(설명 참조)

## 입력 예시

150 60

## 출력 예시

과체중
