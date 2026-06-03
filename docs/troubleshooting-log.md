# Git 트러블슈팅 기록

팀 과제 진행 중 수행한 Git 트러블슈팅 시나리오를 이곳에 기록합니다.

## 시나리오 기록

### 시나리오

- 종류: `git reset --hard origin/main`, `git reset --soft HEAD~1`
- 참여자: 팀원 5

### 상황

- 로컬 `main` 브랜치에서 `git pull`을 실행했을 때 pull이 되지 않는 문제가 발생했다.
- `git status` 확인 결과, 로컬 `main`과 원격 `origin/main`의 커밋 히스토리가 서로 갈라진 상태였다.
```
➜  docs git:(main) git status
On branch main
Your branch and 'origin/main' have diverged,
and have 1 and 14 different commits each, respectively.
  (use "git pull" if you want to integrate the remote branch with yours)

nothing to commit, working tree clean
```
- 이는 로컬 `main`에는 원격에 없는 커밋 1개가 있고, 원격 `origin/main`에는 로컬에 없는 커밋 14개가 있다는 의미이다.
- 처음에는 마지막 로컬 커밋 1개를 취소하기 위해 `git reset --soft HEAD~1`을 사용할 수 있을지 검토했다.
- 하지만 이 상황의 목적은 마지막 커밋을 다시 작성하는 것이 아니라, 로컬 `main`을 원격 `origin/main`과 완전히 동일한 상태로 맞추는 것이었다.
- 따라서 `git reset --soft HEAD~1`과 `git reset --hard origin/main`의 차이를 비교한 뒤, 현재 상황에는 `git reset --hard origin/main`이 더 적절하다고 판단했다.


- 추가로 `git reset --soft HEAD~1`의 동작 방식을 확인하기 위해 문서 파일을 수정한 뒤 일부러 커밋을 생성했다.
- 이후 마지막 커밋을 취소하되, 커밋에 포함된 변경사항은 삭제하지 않고 유지되는지 확인해야 했다.
- 특히 커밋 메시지를 잘못 작성했거나, 마지막 커밋을 다시 작성해야 하는 상황에서 `git reset --soft HEAD~1`을 사용할 수 있는지 확인하고자 했다.
- 예를 들어 문서 수정 작업인데 커밋 메시지를 `fix` 타입으로 작성한 경우, 마지막 커밋을 취소하고 `docs` 타입으로 다시 커밋할 수 있다.

### 수행 명령 또는 절차
**git reset --hard**
```bash
git fetch origin
git reset --hard origin/main
```

**git reset --soft**
```bash
git add docs/troubleshooting-log.md 
git commit -m "fix: reset soft 내용 추가"
```

```bash
git reset --soft HEAD~1
```

```bash
git status 
git commit -m "docs: reset soft 트러블슈팅 추가"
```

### 결과

- `git reset --hard origin/main`을 실행한 결과, 로컬 `main` 브랜치가 원격 `origin/main`과 동일한 상태로 정리되었다.
- 로컬 `main`에만 있던 불필요한 커밋 1개가 제거되었고, 원격 `main`의 최신 커밋 14개를 기준으로 로컬 브랜치가 맞춰졌다.
- 로컬 `main`이 `origin/main`과 동일해져 더 이상 diverged 상태가 아니게 되었다.
- 이후 `git reset --soft HEAD~1`은 실제 `main` 문제가 해결된 뒤, 문서 작업 브랜치인 `docs/26`에서 별도로 테스트했다.
- 별도 테스트에서 `git reset --soft HEAD~1` 실행한 결과, 마지막 커밋은 취소되었지만 변경사항은 삭제되지 않고 staged 상태로 유지되었다.
- 따라서 `git add`를 다시 하지 않고도 올바른 커밋 메시지로 다시 커밋할 수 있었다.

```
➜  B2-2 git:(docs/26) git reset --soft HEAD~1
➜  B2-2 git:(docs/26) ✗ git status             
On branch docs/26
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   docs/troubleshooting-log.md

➜  B2-2 git:(docs/26) ✗ git commit -m "docs: reset soft 트러블슈팅 추가"
[docs/26 d9bc39b] docs: reset soft 트러블슈팅 추가
 1 file changed, 3 insertions(+), 3 deletions(-)
➜  B2-2 git:(docs/26) 
```


### 배운 점

- `git reset --soft HEAD~1`과 `git reset --hard origin/main`은 모두 `reset` 명령어를 사용하지만 목적과 결과가 다르다.
- `git reset --soft HEAD~1`은 마지막 로컬 커밋 1개를 취소하되, 해당 커밋에 포함된 변경사항은 staged 상태로 유지하는 명령어이다.
- 파일 변경사항을 잃지 않고 커밋만 다시 만들 수 있기 때문에, 커밋 메시지 수정이나 누락된 파일 추가에 적합하다.
- 반면 `git reset --hard origin/main`은 로컬 브랜치를 원격 브랜치인 `origin/main`과 완전히 동일한 상태로 맞춘다.
- `git reset --soft HEAD~1`은 변경사항을 보존하는 명령어이고, `git reset --hard origin/main`은 로컬 브랜치를 원격 브랜치 상태로 강제로 맞추는 명령어이다.
- 두 명령어는 목적이 다르므로 상황에 맞게 구분해서 사용해야 한다.

| 명령어                       | 커밋 기록       | Staging Area | Working Directory |
| ------------------------- | ----------- | ------------ | ----------------- |
| `git reset --soft HEAD~1` | 최근 커밋 1개 취소 | 변경사항 유지됨     | 변경사항 유지됨          |
| `git reset --hard origin/main` | 로컬 브랜치를 `origin/main`과 동일하게 맞춤 | 변경사항 삭제됨 | 변경사항 삭제됨 |

### 정리
- 이번 pull 실패 상황에서는 로컬 `main`과 원격 `origin/main`의 히스토리가 갈라져 있었다.
- 이때 `git reset --soft HEAD~1`을 사용하면 로컬 커밋 1개는 취소되지만, 그 커밋에 포함된 변경사항이 staged 상태로 남는다.
- staged 상태로 남은 변경사항 때문에 이후 git pull 과정에서 원격 변경사항과 충돌할 수 있다.
- 즉, soft reset은 커밋을 다시 만들기 위한 방법이지, 로컬 main을 원격 main과 완전히 동일하게 맞추는 방법은 아니다.
- 현재 상황에서는 로컬 커밋을 유지할 필요가 없었고, 원격 `main`을 기준으로 로컬 `main`을 정리하는 것이 목적이었다.
- 따라서 `git reset --hard origin/main`을 사용하는 것이 적절했다.

### 주의사항
- `git reset --hard origin/main`은 로컬 브랜치를 원격 브랜치 상태로 강제로 맞추는 명령어이다.
- 이 과정에서 로컬에만 있던 커밋이나 아직 커밋하지 않은 변경사항이 삭제될 수 있으므로, 실행 전에 반드시 현재 상태를 확인해야 한다.
    ```bash
    git status
    ```
- 필요한 변경사항이 남아 있다면 `git reset --hard origin/main`을 실행하기 전에 `git stash`로 임시 저장하거나 백업 브랜치를 만들어야 한다.
    ```bash
    git stash
    git branch backup/main-local-work
    ```
- `git reset --soft HEAD~1`은 마지막 커밋을 다시 작성해야 할 때 선택하고, `git reset --hard origin/main`은 로컬 브랜치를 원격 브랜치와 완전히 동일하게 맞춰야 할 때 선택한다.
    ```
    git reset --soft HEAD~1 : 마지막 커밋은 취소하되 변경사항을 유지해야 할 때 사용 
    git reset --hard origin/main : 로컬 변경사항을 버리고 원격 브랜치 기준으로 초기화해야 할 때 사용
    ```