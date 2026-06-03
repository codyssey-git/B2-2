# Git 트러블슈팅 기록

팀 과제 진행 중 수행한 Git 트러블슈팅 시나리오를 이곳에 기록합니다.

## 시나리오 기록

### 시나리오 1 - 윤대영

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
