### 시나리오

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
