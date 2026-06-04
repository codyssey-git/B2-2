# 제출물 인덱스

팀 과제 진행 후 Issue, PR, 문서, 증빙 링크를 이곳에 정리합니다.

## 저장소

- GitHub 저장소: codyssey-git/B2-2

## 팀원별 제출 링크

| 팀원 | Issue | PR | 리뷰 | 비고 |
| --- | --- | --- | --- | --- |
| 팀원 1 |  |  |  |  |
| 팀원 2 |  |  |  |  |
| 팀원 3 |  |  |  |  |
| 팀원 4 | [#8 docs: 코드 리뷰 규칙 작성](https://github.com/codyssey-git/B2-2/issues/8)<br>[#24 feat: 숫자 리스트 평균 계산 함수 작성](https://github.com/codyssey-git/B2-2/issues/24)<br>[#31 docs: git commit --ammend 트러블슈팅 시나리오](https://github.com/codyssey-git/B2-2/issues/31) | [#12 docs: 코드 리뷰 규칙 작성](https://github.com/codyssey-git/B2-2/pull/12)<br>[#22 feat: 숫자 리스트 평균 계산 함수 추가](https://github.com/codyssey-git/B2-2/pull/22)<br>[#37 docs: git amend 트러블슈팅 기록 추가](https://github.com/codyssey-git/B2-2/pull/37) | [#12 리뷰 포함 PR](https://github.com/codyssey-git/B2-2/pull/12)<br>[#22 리뷰 포함 PR](https://github.com/codyssey-git/B2-2/pull/22)<br>[#37 리뷰 포함 PR](https://github.com/codyssey-git/B2-2/pull/37) | `CONTRIBUTING.md`에 코드 리뷰 규칙 작성<br>숫자 리스트 평균 계산 함수 `calculate_average` 작성<br>트러블슈팅 문서에 `git commit --amend` 트러블슈팅 작성<br>충돌 해결 기록에 `src/data_utils.py` 코드 충돌 해결 과정 작성 |
| 팀원 5 | [#3 docs: 충돌 대응 흐름 파일 작성](https://github.com/codyssey-git/B2-2/issues/3)<br>[#19 feat: 빈 값 검증 함수 작성](https://github.com/codyssey-git/B2-2/issues/19)<br>[#26 docs: git reset 트러블슈팅 문서 작성](https://github.com/codyssey-git/B2-2/issues/26) | [#11 docs: 충돌 대응 흐름 작성](https://github.com/codyssey-git/B2-2/pull/11)<br>[#23 feat: 빈 값 검증 함수 추가](https://github.com/codyssey-git/B2-2/pull/23)<br>[#36 docs: reset soft 트러블슈팅 추가](https://github.com/codyssey-git/B2-2/pull/36) | [#11 리뷰 포함 PR](https://github.com/codyssey-git/B2-2/pull/11)<br>[#23 리뷰 포함 PR](https://github.com/codyssey-git/B2-2/pull/23)<br>[#36 리뷰 포함 PR](https://github.com/codyssey-git/B2-2/pull/36) | `CONTRIBUTING.md`에 충돌 대응 흐름 작성<br>빈 값 검증 함수 `is_blank` 작성<br>트러블슈팅 문서에 `git reset` 트러블 슈팅 작성 |

## 문서 링크

- 협업 가이드: https://github.com/codyssey-git/B2-2/blob/main/docs/CONTRIBUTING.md
- 충돌 해결 기록: https://github.com/codyssey-git/B2-2/blob/main/docs/conflict-resolution.md
- 트러블슈팅 기록: https://github.com/codyssey-git/B2-2/blob/main/docs/troubleshooting-log.md
- Git 히스토리 증빙: https://github.com/codyssey-git/B2-2/commits/main/

## 보너스: CODEOWNERS / 리뷰어 자동화

### 수행 목적

`.github/CODEOWNERS` 파일을 추가하여 파일 또는 폴더별 책임 리뷰어를 지정하고, PR 생성 시 GitHub에서 자동으로 리뷰어가 지정되는 흐름을 확인했다.

### 수행 내용

- CODEOWNERS 추가용 Issue 생성
- 팀원 GitHub 사용자명 확인
- 파일/폴더별 책임 리뷰어 지정
- `.github/CODEOWNERS` 파일 추가
- CODEOWNERS 추가 PR 생성 및 병합
- `/docs/` 경로 변경 테스트 PR을 통해 자동 리뷰어 지정 여부 확인

### 증빙 링크

- CODEOWNERS 추가 Issue: #33
- CODEOWNERS 추가 PR: #34
- CODEOWNERS 파일: `.github/CODEOWNERS`
- 자동 리뷰어 지정 확인 PR & 스크린샷: #40

### 확인 결과

- `.github/CODEOWNERS` 파일이 `main` 브랜치에 추가되었다.
- CODEOWNERS 추가 PR에서 `.github/CODEOWNERS` 파일 변경 사항을 확인했다.
- CODEOWNERS 병합 후 `/docs/` 경로를 수정하는 테스트 PR에서 자동 리뷰어 지정 여부를 확인했다.
