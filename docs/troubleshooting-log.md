### 시나리오: git commit --amend

* 종류: `git commit --amend`
* 참여자: 팀원 1

### 상황

* `docs/troubleshooting-log.md`에 Git 트러블슈팅 기록을 추가한 뒤, 첫 커밋 메시지를 너무 모호하게 작성한 상황을 가정했습니다.
* 처음 작성한 커밋 메시지는 `docs: 기록 추가`였는데, 이 메시지만 보면 어떤 기록을 추가했는지 명확히 알기 어렵습니다.
* 따라서 `git commit --amend`를 사용하여 최근 커밋 메시지를 더 구체적으로 수정했습니다.
* 실습 과정에서 원격 브랜치에 한 번 push한 뒤 커밋 메시지를 수정하게 되었기 때문에, 수정된 커밋을 원격 브랜치에 다시 반영하기 위해 `git push --force-with-lease`를 사용했습니다.

### 수행 명령 또는 절차

```bash
git switch main
git pull origin main
git switch docs/31

git add docs/troubleshooting-log.md
git commit -m "docs: 기록 추가"
git log --oneline -1

git push origin docs/31

git commit --amend -m "docs: git amend 트러블슈팅 기록 추가"
git log --oneline -1

git push --force-with-lease origin docs/31
```

### 결과

* 최근 커밋 메시지가 `docs: 기록 추가`에서 `docs: git amend 트러블슈팅 기록 추가`로 변경되었습니다.
* `git log --oneline -1` 명령어를 통해 amend 전후의 최근 커밋 메시지가 달라진 것을 확인했습니다.
* `git commit --amend`를 사용하면서 기존 커밋이 수정되고 커밋 해시가 변경되는 것을 확인했습니다.
* 이미 원격 브랜치에 push된 커밋을 수정했기 때문에, 원격 브랜치에는 `git push --force-with-lease origin docs/31` 명령어로 반영했습니다.
* 새로운 커밋을 하나 더 추가한 것이 아니라, 가장 최근 커밋 자체를 수정하여 Git 히스토리를 더 명확하게 정리했습니다.

### 배운 점

* `git commit --amend`는 가장 최근 커밋을 수정할 때 사용하는 명령어입니다.
* 커밋 메시지를 잘못 작성했거나, 방금 만든 커밋에 작은 수정 사항을 함께 포함하고 싶을 때 사용할 수 있습니다.
* `git commit --amend`를 사용하면 기존 커밋이 수정되면서 커밋 해시가 바뀝니다.
* 따라서 이미 원격 저장소에 push한 커밋에 사용하면 로컬 브랜치와 원격 브랜치의 커밋 이력이 달라질 수 있습니다.
* 이미 push한 커밋을 amend한 경우 일반 `git push`가 거부될 수 있으며, 이때는 원격 브랜치 상태를 확인한 뒤 `git push --force-with-lease`를 사용할 수 있습니다.
* `--force-with-lease`는 원격 브랜치가 내가 마지막으로 확인한 상태에서 바뀌지 않았을 때만 강제 push를 허용하므로, 단순 `--force`보다 안전합니다.
* 다만 공유 브랜치나 `main` 브랜치에서는 다른 팀원의 작업에 영향을 줄 수 있으므로 신중하게 사용해야 합니다.
* 협업 상황에서는 일반적으로 push하기 전의 로컬 커밋에 `git commit --amend`를 사용하는 것이 가장 안전합니다.

---

### 시나리오: git revert

* 종류: `git revert`
* 참여자: 팀원 3

### 상황

* `validate_length()` 함수에 음수 길이 검증 로직을 추가하는 과정에서 잘못된 조건 처리가 포함된 커밋을 생성했습니다.
* 해당 커밋이 원격 저장소에 push된 이후 오류를 발견했습니다.
* 이미 공유된 커밋이므로 `git reset` 대신 `git revert`를 사용하여 변경 사항을 취소했습니다.

### 수행 명령 또는 절차

```bash
git log --oneline

git revert <commit-hash>

git log --oneline
```

예시:

```bash
git revert a1b2c3d
```

### 결과

* 잘못된 변경 사항을 취소하는 새로운 커밋이 생성되었습니다.
* 기존 커밋 이력은 유지되었습니다.
* 협업 중인 저장소의 히스토리를 안전하게 보존하면서 문제를 해결할 수 있었습니다.

### 배운 점

* 이미 원격 저장소에 공유된 커밋은 `git reset`보다 `git revert`를 사용하는 것이 안전합니다.
* `git revert`는 기존 커밋을 삭제하지 않고 취소 이력을 남기므로 협업 환경에 적합합니다.
* 커밋을 되돌려야 하는 상황에서도 Git 히스토리를 보존할 수 있습니다.

---

## 시나리오: git stash / git stash pop

### 참여자

* bangahee

### 상황

* 작업 브랜치에서 문서 내용을 수정하던 중, 아직 커밋하기에는 완성되지 않은 상태였습니다.
* 하지만 최신 main 브랜치 내용을 먼저 확인하거나 다른 브랜치로 이동해야 하는 상황이 발생했습니다.
* 작업 중인 변경 사항을 잃지 않기 위해 `git stash`를 사용해 임시 저장했습니다.

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

* 커밋하지 않은 작업 내용을 `git stash`로 임시 저장했습니다.
* 작업 디렉터리가 clean 상태가 되어 `main` 브랜치로 이동하고 최신 내용을 확인할 수 있었습니다.
* 다시 `docs/25` 브랜치로 돌아온 뒤 `git stash pop`을 사용하여 임시 저장했던 내용을 복원했습니다.

### 왜 이 방법을 선택했는가

* 아직 완성되지 않은 변경 사항을 불필요하게 커밋하지 않기 위해 사용했습니다.
* 작업 내용을 잃지 않으면서도 브랜치 이동과 최신 내용 확인을 진행할 수 있었기 때문입니다.

### 주의할 점

* `git stash`는 기본적으로 추적 중인 파일의 변경 사항만 저장합니다.
* 새로 생성된 untracked 파일까지 함께 저장하려면 `git stash -u`를 사용해야 합니다.
* `git stash pop` 이후 충돌이 발생할 수 있으므로 반드시 `git status`로 상태를 확인해야 합니다.


<!-- CODEOWNERS 자동 리뷰어 지정 확인용 테스트 변경 -->
