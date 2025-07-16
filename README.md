1. Template Repository를 템플릿으로 하여, 새 레포지토리 생성
2. 로컬에서 해당 레포지토리를 clone 하여 작업
3. Push 하기전, GHCR_PAT(개인Classic Token), GHCR_USERNAME 을 레포지토리 환경변수로 설정
4. Repository > Settings > Secrets > Actions > Repository Secret
5. 로컬 작업 내용 Push후 Github Action 상태 확인
6. 서버에서 clone(Pull) 하시고, docker-compose up -d(백그라운드)
7. 이후 작업에는 push 만 하고 GitHub Action만 확인해주면, 자동 반영
8. 웹에서 확인은 /api/모델명/home 으로 접근가능
