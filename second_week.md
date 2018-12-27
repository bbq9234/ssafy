# SSAFY Start Camp 챗봇 퀘스트



서울 8반  김대훈



##  I. 스펙

(1) Bugs 실시간 TOP10

- 사용자가 `music` 이라는 텍스트를 입력하면 벅스에서 실시간 랭킹을 크롤링해 보여준다.
- `music 주간` 이라고 입력할 경우엔 주간 랭킹을 보여준다.

(2) Youtube 링크 보여주기

- 크롤링해 온 실시간 랭킹에 따라 각 곡과 아티스트 명으로 Youtube에서 검색을 해, 
결과 리스트의 첫 번째 항목을 보여준다.


## II. 회고

(1)  Youtube 링크 보여주기

- Selenium으로 Youtube 화면에 요청을 보내고 로딩을 기다리는 작업을 했는데, 랭킹에 올라가있는 
매 곡에 대해 요청을 보내다 보니 Too many connections 문제가 발생했다.


## III. 보완 계획 

(1) Youtube 링크 펼쳐서 보여주기

- Selenium을 통해 얻어온 링크를 Slack에서 펼쳐서 영상 썸네일과 함께 보여준다.