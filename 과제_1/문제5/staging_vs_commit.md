# 📄 Staging 영역에 추가 vs Commit의 차이

Git에서 작업을 저장하기 위한 단계는 크게 두 단계로 나뉩니다:

---

## ✅ 1. Staging 영역에 추가 (`git add`)

### 의미
- **작업 디렉토리에서 변경한 파일을 Git이 추적할 준비를 하는 단계**
- 커밋하기 전, 어떤 변경사항을 기록할지 **선택적으로 준비**하는 것

### 명령어
```bash
git add <파일명>
git add .             # 모든 변경된 파일을 스테이징에 추가
```

### 예시
```bash
git add main.py
```
> → `main.py` 파일이 스테이징 영역에 올라감

---

## ✅ 2. 커밋 (`git commit`)

### 의미
- 스테이징 영역에 있는 변경 사항을 **하나의 버전(스냅샷)** 으로 저장하는 것
- 로컬 저장소에 **히스토리로 남음**

### 명령어
```bash
git commit -m "메시지"
```

### 예시
```bash
git commit -m "Fix login bug"
```
> → 스테이징에 올라간 모든 변경사항이 저장되고, 커밋 메시지가 붙음

---

## 🔁 정리: Staging vs Commit

| 구분             | Staging (`git add`)                      | Commit (`git commit`)                           |
|------------------|-------------------------------------------|--------------------------------------------------|
| 목적             | 커밋할 변경 사항을 **선택하고 준비**     | 준비된 변경 사항을 **저장소에 기록**             |
| 저장 위치        | Staging Area (Index)                     | 로컬 Git 저장소 (.git 디렉토리)                 |
| 실행 명령        | `git add`                                | `git commit`                                    |
| 커밋 메시지 필요 | ❌ 없음                                   | ✅ 필요                                           |
| 버전 이력에 기록 | ❌ 안 됨                                 | ✅ 기록됨                                         |

---

## 💡 비유로 이해하기

- `git add`: 📋 **장바구니에 담기**
- `git commit`: ✅ **계산하고 영수증 받기 (저장하기)**
