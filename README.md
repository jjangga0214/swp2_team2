Software Project Team 2
==========================

멤버
---------
* 고지원
* 길병찬
* 김규리
* 김수진



발표 현황
-----------
* 고지원
	* 아직 없음
* 길병찬
	* 아직 없음
* 김규리
	* 아직 없음
* 김수진
	* factorial  :  2017.09.07.목



리뷰 반영 현황 [반영 여부 간단 체크]
-----------------------------------
#### 리뷰 1  :  factorial [2017.09.07.목]

* 고지원 
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ###### 아직 없음
* 길병찬
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ###### 구조 개선
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * `try except` 범위 좁힘
* 김규리
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ###### 의미 부여
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * 함수명 수정 : `fun` ==> `factorial`
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * 변수명 수정 : `x` ==> `result`
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ###### 역할 분리
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * `factorial` 함수는 계산을 전담하고 더 이상 `print` 하지 않는다
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ###### 중복 제거, 구조 개선
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * `input`과 `factorial` 함수를 2번씩 호출  ==>  각각 1번씩만 호출 
* 김수진
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ###### 불필요한 코드 조정
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * 불필요한 continue문 삭제 
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 	* [참고 : `try except` 범위 조정시 `continue`문이 다시 필요 ]
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * 중복되는 `if`문 필터링 조정 *[MINOR]* 
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 	* `if n <= 1 : return 0`  ==>  `if n == 0 : return 0`



의미 참고
-----------

#### 코드 개선
* *[MINOR]*  :  호불호에 따라 갈릴 수도 있는 선택이나 아주 작은 성능 향상과 같이 말 그대로 마이너한 개선을 나타낸다. 
 

