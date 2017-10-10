## Hello Review!
---
## 타입 체크
---
```python
@tc.typecheck
def fibo_recur(n: int) -> int:
    if n < 0:
        raise ValueError("The term index 'n' have to be positive integer.")
    return n if n <= 1 else fibo_recur(n - 1) + fibo_recur(n - 2)
```
---
## @decorator
---
## 횡단 관심사
* #### 시간 체크
* #### 로깅
* #### 보안, 트랜잭션 등등..
---
## AOP
---
## 인접 n 항간 점화식
---
```python
@tc.typecheck
def fibo_iter(n: int) -> int:
    rseq = RecurrenceSeq(0, 1, calc=lambda nextidx, parts: parts[0] + parts[1], init_idx=0)
    return rseq.get(n)
```
---
## Facade Pattern
---
## Linked List
---
```python

```
---
```python

```
---
## Meta 정보 추출
---
## 타입 체크
---
## 타입 체크
---
## 타입 체크
---
## 타입 체크
---
