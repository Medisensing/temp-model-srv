1. Template Repository로, 레포지토리 새로 생성
2. 로컬에서 clone 하여 작업
3. Push 하기전에, GHCR_PAT(개인Classic Token), GHCR_USERNAME 을 레포지토리 Secrets -> Actions -> 환경변수 설정
4. Push
5. 서버에서 clone(Pull) 하시고, docker-compose up -d(백그라운드)
6. 이후 작업에는 push 만 하고 GitHub Action 체크하면 자동 반영
7. 웹에서 확인은 /api/모델명/hoke
