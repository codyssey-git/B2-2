# Git 트러블슈팅 기록

팀 과제 진행 중 수행한 Git 트러블슈팅 시나리오를 이곳에 기록합니다.

## 시나리오 기록

### 시나리오

* 종류: `git revert`
* 참여자: 팀원 3

### 상황

* `validate_length()` 함수에 음수 길이 검증 로직을 추가하는 과정에서 잘못된 조건 처리가 포함된 커밋을 생성하였다.
* 해당 커밋이 원격 저장소에 push된 이후 오류를 발견하였다.
* 이미 공유된 커밋이므로 `git reset` 대신 `git revert`를 사용하여 변경 사항을 취소하였다.
## 실수로 커밋한 코드
```python
if min_length < 0:
    return False
```

## 정상 코드 (수정본)
```python
if min_length < 0:
    raise ValueError("min_length는 0 이상이어야 합니다.")
```
### 수행 명령 또는 절차

```bash
git log --oneline
9cfeacf (origin/main, origin/docs/26, origin/HEAD,
14ab263 (origin/feat/19) Merge branch
'main' into
main) Merge pull request #23 from
codyssey-git/feat/19
feat/19
05db6e7 Merge pull request #18 from codyssey-git/feat/15
2697723 (origin/feat/15, feat/15) Merge branch
'main' into feat/15

git revert 9cfeacf

git log --oneline

vnkers948441@c6r6s5 B2-2 % git log --oneline
Idf150c Revert "Merge pull request #23 from codyssey-git/feat/19'
434dd75 refactor: 문자열 업데이트
9cfeacf (origin/main, origin/docs/26, origin/HEAD, main) Merge pull request #23 from codyssey-git/feat/19
```

### 결과

* 잘못된 변경 사항을 취소하는 새로운 커밋이 생성되었다.
* 기존 커밋 이력은 유지되었다.
* 협업 중인 저장소의 히스토리를 안전하게 보존하면서 문제를 해결할 수 있었다.

### 배운 점

* 이미 원격 저장소에 공유된 커밋은 `git reset`보다 `git revert`를 사용하는 것이 안전하다.
* `git revert`는 기존 커밋을 삭제하지 않고 취소 이력을 남기므로 협업 환경에 적합하다.
* 커밋을 되돌려야 하는 상황에서도 Git 히스토리를 보존할 수 있다.
-

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
