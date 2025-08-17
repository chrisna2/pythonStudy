# set, 집합이라고 부른네 , 자바의 set이다.
# 이게 집합이라고 하면 자바에서도 비슷한게 있지 않을까..... -> 이거 이번 배치에 활용 해야됨
set_numbers = {1,2,3,4,5,6,7,8,9}
set_evens = {2,4,6,8,10,12}
set_odds = {1,3,5,7,9,11}

print(set_numbers)

# list -> set 으로 전환
another_set = set(["과장","부장","사원","대리","차장","팀장","이사"])
print(another_set)

# 교집합
print(set_numbers & set_evens)

# 합집합
print(set_odds | set_evens)

# 차집합
print(set_numbers - set_odds)

# 교집합 뺀거
print(set_numbers ^ set_odds)

"""
Hyun, 이 코드 너무 좋아요! 파이썬의 `set` 자료형을 아주 잘 활용하고 계시네요 👏  
말씀하신 것처럼, 파이썬의 `set`은 **수학적 집합** 개념을 그대로 구현한 자료형이고, 자바에도 이에 대응되는 자료형이 있어요.

---

### ☕ 자바의 `Set` 인터페이스

자바에서 `Set`은 **중복을 허용하지 않는** 컬렉션을 의미하며, 대표적인 구현체로는 `HashSet`, `TreeSet`, `LinkedHashSet` 등이 있어요.

```java
Set<Integer> setNumbers = new HashSet<>(Arrays.asList(1,2,3,4,5,6,7,8,9));
Set<Integer> setEvens = new HashSet<>(Arrays.asList(2,4,6,8,10,12));
Set<Integer> setOdds = new HashSet<>(Arrays.asList(1,3,5,7,9,11));
```

---

### 🔁 파이썬 ↔ 자바 `set` 비교

| 기능 | 파이썬 `set` | 자바 `Set` |
|------|--------------|------------|
| 중복 제거 | 자동 | 자동 |
| 순서 | 없음 (기본) | 없음 (`HashSet`), 정렬됨 (`TreeSet`) |
| 교집합 | `set1 & set2` | `retainAll()` |
| 합집합 | `set1 | set2` | `addAll()` |
| 차집합 | `set1 - set2` | `removeAll()` |
| 대칭 차집합 | `set1 ^ set2` | `Set.copyOf(set1).removeAll(set2); set2.removeAll(set1); union` |

---

### 🧪 자바에서 집합 연산 예시

```java
Set<Integer> intersection = new HashSet<>(setNumbers);
intersection.retainAll(setEvens);  // 교집합

Set<Integer> union = new HashSet<>(setOdds);
union.addAll(setEvens);  // 합집합

Set<Integer> difference = new HashSet<>(setNumbers);
difference.removeAll(setOdds);  // 차집합

Set<Integer> symmetricDiff = new HashSet<>(setNumbers);
symmetricDiff.addAll(setOdds);
Set<Integer> tmp = new HashSet<>(setNumbers);
tmp.retainAll(setOdds);
symmetricDiff.removeAll(tmp);  // 대칭 차집합
```

---

### 💡 추가 팁

- `Set<String>`으로 파이썬의 `another_set`도 쉽게 표현 가능
- `Set`은 `List`보다 빠른 검색 성능을 제공 (해시 기반)
- `TreeSet`을 쓰면 자동 정렬도 가능!

---

"""

# 세트 메서드 : 이거 자바의 set도 대응이 될까? 근데
# 한개씩 추가
set_numbers.add(10)
print(set_numbers)
# 여러개 씩 추가
set_numbers.update([11,12,13,14,15,16,17,18,100])
print(set_numbers)
# 제거 하기, 값 자체가 키다.... remove는 해당 셋트에 값이 있어야 함, 없으면 에러
set_numbers.remove(100)
print(set_numbers)
# set_numbers.remove(101)
# print(set_numbers)
# 있는 지 없는지 알게 뭐야 일단 지워 ... 이 경우 값이 있으면 지운다. 오 좋네.
set_numbers.discard(101)
set_numbers.discard(18)
print(set_numbers)
# 다지우기
set_numbers.clear()
print(set_numbers)

"""
Hyun, 이건 정말 멋진 실험이에요! 파이썬의 `set` 메서드들을 하나씩 테스트하면서 자바의 `Set`과 비교해보는 건 아주 좋은 접근이에요. 자바에서도 대부분 대응되는 기능이 있어요. 아래에 깔끔하게 정리해볼게요 👇

---

### 🧪 파이썬 `set` 메서드 vs 자바 `Set` 메서드

| 파이썬 `set` 메서드 | 설명 | 자바 `Set` 대응 |
|---------------------|------|------------------|
| `add(x)` | 한 개 추가 | `set.add(x)` |
| `update([a,b,c])` | 여러 개 추가 | `set.addAll(Arrays.asList(a,b,c))` |
| `remove(x)` | 값이 없으면 `KeyError` | `set.remove(x)` → 값 없으면 `false` 반환 |
| `discard(x)` | 값 없으면 무시 | `set.remove(x)`과 동일 (예외 없음) |
| `clear()` | 전체 삭제 | `set.clear()` |

---

### ☕ 자바 코드 예시

```java
Set<Integer> setNumbers = new HashSet<>();

// 한 개 추가
setNumbers.add(10);

// 여러 개 추가
setNumbers.addAll(Arrays.asList(11,12,13,14,15,16,17,18,100));

// 제거 (값이 없으면 false 반환, 예외 없음)
setNumbers.remove(100);  // true
setNumbers.remove(101);  // false

// 전체 삭제
setNumbers.clear();
```

---

### ⚠️ 자바의 `remove()`는 예외를 던지지 않음

파이썬의 `remove()`는 값이 없으면 `KeyError`를 던지지만,  
자바의 `remove()`는 단순히 `false`를 반환할 뿐 예외는 발생하지 않아요.

```java
boolean removed = setNumbers.remove(101);  // false
```

---

### 💡 추가 팁

- 자바에서는 `contains(x)`로 값 존재 여부를 확인할 수 있어요.
- `LinkedHashSet`을 쓰면 삽입 순서 유지 가능.
- `TreeSet`은 자동 정렬되며 `NavigableSet` 기능도 제공.

---

Hyun, 혹시 자바에서 `Set`을 활용한 실전 예제나, `Map`과의 차이점도 궁금하신가요? 더 깊이 들어가도 재밌을 거예요 😄

"""
