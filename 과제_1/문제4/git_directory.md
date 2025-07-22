# 기초 git 환경 구축

- 개행문자 설정을 윈도우는 true, 맥은 input 값으로 지정한다.
    - 설정: git config --global core.autocrlf input
    - 확인: git config --global core.autocrlf

- 사용자 이름과 이메일 주소를 설정한다.
    - 이름 설정: git config --global user.name "Somin"
    - 이메일: git config --global user.email "somin@example.com"

- 기본 브랜치 이름을 main으로 변경한다.
    - git config --global init.defaultBranch main

- Git 전역 설정 목록을 명령어로 확인한다.
    - git config --global --list

- Git 전역 설정을 에디터에서 띄워서 전체 설정을 확인한다.
    - git config --global -e

- Git의 기본 에디터를 Visual Studio Code로 변경한다.
    - git config --global core.editor "code --wait"

# 버전 관리 시스템의 종류와 .git 디렉토리의 역할

## ✅ 버전 관리 시스템의 종류 3가지

1. **로컬 버전 관리 시스템 (Local VCS)**
   - 개발자의 컴퓨터에만 저장되는 방식
   - 예: RCS (Revision Control System)

2. **중앙집중식 버전 관리 시스템 (Centralized VCS)**
   - 하나의 중앙 서버에서 모든 버전을 관리
   - 개발자는 중앙 서버에서 데이터를 받아 작업
   - 예: SVN, CVS

3. **분산형 버전 관리 시스템 (Distributed VCS)**
   - 각 개발자가 전체 저장소를 복제하여 로컬에서도 버전 관리 가능
   - 중앙 서버가 없어도 작업 가능하며, 협업에 유리
   - 예: **Git**, Mercurial

---

## ✅ `.git` 디렉토리의 역할

- `.git` 디렉토리는 **Git 저장소의 핵심**입니다.
- 이 디렉토리는 Git이 프로젝트를 **버전 관리할 수 있도록 만드는 정보 저장소**입니다.
- 주요 역할:
  - 커밋 이력, 브랜치 정보, 설정 파일, 객체 데이터 등을 저장
  - `.git`이 존재하는 디렉토리는 Git이 "저장소"로 인식함
  - 내부 구조:
    - `HEAD`, `config`, `objects/`, `refs/`, `logs/` 등 핵심 요소 포함

---

## ✅ 실습: `.git` 디렉토리 삭제 및 복원 후 상태 확인

### 1. `.git` 디렉토리 삭제
```bash
rm -rf .git
```

### 2. Git 상태 확인
```bash
git status
```
**결과:**
```
fatal: not a git repository (or any of the parent directories): .git
```
→ Git이 버전 관리 저장소로 인식하지 못함

---

### 3. 휴지통에서 `.git` 복원 후 상태 확인
- `.git` 디렉토리를 다시 프로젝트 디렉토리로 복사하거나 복원

```bash
git status
```

**결과:**
```
On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean
```
→ Git 저장소로 다시 인식하며 이전 상태 그대로 복구됨
