# Git 트러블슈팅 기록

팀 과제 진행 중 수행한 Git 트러블슈팅 시나리오를 이곳에 기록합니다.

## 시나리오 기록

### 시나리오: git revert 1 - 윤대영

- 종류: `git revert`
- 참여자: 윤대영

### 상황

- Git 트러블슈팅 실습 중 `docs/conflict-resolution.md` 파일에 이름을 추가하고 커밋했다.
- 커밋 후 현재 브랜치가 해당 작업을 진행해야 하는 브랜치가 아니라는 것을 확인했다.
- 이미 커밋이 생성된 상태였기 때문에, 커밋 기록을 삭제하지 않고 변경사항만 되돌리기 위해 `git revert`를 사용했다.

### 수행 명령 또는 절차

```bash
git add docs/conflict-resolution.md

git commit -m "docs: 충돌 해결 문서에 이름 추가"

git log --oneline

git revert 185b6fd
```

### 결과

- `docs/conflict-resolution.md`에 잘못 추가했던 이름이 제거되었다.
- 기존 커밋 `185b6fd`는 삭제되지 않고 유지되었다.
- 해당 커밋의 변경사항을 취소하는 새로운 revert 커밋이 생성되었다.

#### revert 이전

![revert 이전](../images/trouble-shooting/revert%20이전_윤대영.png)

#### revert 이후

![revert 이후](../images/trouble-shooting/revert%20이후_윤대영.png)

### 배운 점

- 이미 커밋한 변경사항은 `git revert`를 사용해 안전하게 되돌릴 수 있다.
- `git revert`는 기존 커밋을 삭제하는 것이 아니라, 반대 변경사항을 담은 새 커밋을 만든다.
- 협업 중 공유될 수 있는 커밋은 `reset`으로 기록을 지우기보다 `revert`로 되돌리는 것이 더 안전하다.
- 작업 전 현재 브랜치를 확인하는 습관이 중요하다.

---

## 시나리오: git stash / git stash pop

### 참여자
- bangahee

### 상황
- 작업 브랜치에서 문서 내용을 수정하던 중, 아직 커밋하기에는 완성되지 않은 상태였다.
- 하지만 최신 main 브랜치 내용을 먼저 확인하거나 다른 브랜치로 이동해야 하는 상황이 발생했다.
- 작업 중인 변경 사항을 잃지 않기 위해 `git stash`를 사용해 임시 저장했다.


### 시도한 명령/절차

```bash
git status
git stash
git status
git switch main
git pull origin main
git switch docs/25
git stash pop
```

### 결과
- 커밋하지 않은 작업 내용을 `git stash`로 임시 저장했다.
- 작업 디렉터리가 clean 상태가 되어 `main` 브랜치로 이동하고 최신 내용을 확인할 수 있었다.
- 다시 `docs/25` 브랜치로 돌아온 뒤 `git stash pop`을 사용하여 임시 저장했던 내용을 복원했다.

### 왜 이 방법을 선택했는가
- 아직 완성되지 않은 변경 사항을 불필요하게 커밋하지 않기 위해 사용했다.
- 작업 내용을 잃지 않으면서도 브랜치 이동과 최신 내용 확인을 진행할 수 있었기 때문이다.

### 주의할 점
- `git stash`는 기본적으로 추적 중인 파일의 변경 사항만 저장한다.
- 새로 생성된 untracked 파일까지 함께 저장하려면 `git stash -u`를 사용해야 한다.
- `git stash pop` 이후 충돌이 발생할 수 있으므로 반드시 `git status`로 상태를 확인해야 한다.
