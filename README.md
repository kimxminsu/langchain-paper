![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=300&section=header&text=Team13)

## 👥 Members
| <img src="https://avatars.githubusercontent.com/jenner9212" width=150px><br />[박재윤](https://github.com/jenner9212) | <img src="https://avatars.githubusercontent.com/kimxminsu" width=150px><br />[김민수](https://github.com/kimxminsu) | <img src="https://avatars.githubusercontent.com/a-day-and-the-day" width=150px><br />[박나현](https://github.com/a-day-and-the-day) | <img src="https://avatars.githubusercontent.com/zuzizzuziz1" width=150px><br />[최승아](https://github.com/zuzizzuziz1]) | <img src="https://avatars.githubusercontent.com/00nam11" width=150px><br />[전영남](https://github.com/00nam11) |
|:--:|:--:|:--:|:--:|:--:|
|main, crawl, gemini|vector_store, retreiver|chat, gemini|logger|sql


## 👀 How to run

1. git clone `https://github.com/jenner9212/langchain.git`
2. cd `langchain`
3. python `main.py`
4. `Enter search term for arXiv papers: ` 가 나오면 `검색할 논문 주제` 를 입력하세요.
5. 해당 주제와 관련된 논문 내용을 수집중입니다.

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Orbit&pause=1000&color=000000&center=true&vCenter=true&random=false&width=435&lines=Please+wait+...)](https://git.io/typing-svg)

6. `User question: `가 나오면 `질문 내용`을 입력하세요....반복 ( ! 토큰 제한으로 인해 토큰 초과시 에러가 발생할 수 있습니다)
7. `exit`를 입력하시면 실행이 종료됩니다.

## :computer: Result
![439CCC4A-2068-41A3-A167-B0C7274034BE](https://github.com/jenner9212/langchain/assets/35947676/332f57e6-fca4-4a25-b7d3-88afb175459a)

## 작동 순서
1. 검색할 논문 주제를 입력받습니다.
2. 해당 주제와 관련된 논문의 내용을 Crawler.crawl에서 수집합니다.
3. 수집된 내용을 VectorStore.store에서 청크 사이즈 500으로 자르고 임베딩(벡터화)하여 vector_db에 저장합니다.
4. 찾고 싶은 내용을 입력받습니다.
5. Chat.generate_response에서 Retriever.retrieve를 호출합니다.
6. Retriever.retrieve에서 vector_db를 읽어와 찾는 내용과 가장 가까운 결과를 반환합니다.
7. 반환된 결과와 찾고 싶은 내용을 GeminiAPI.generate_response로 전달합니다.
8. ConversationChain을 이용해 prompt, 사용할 model(gemini), 기억시킬 memory(반환된 결과)를 묶어서 conversation에 저장합니다.
9. conversation에 찾고 싶은 내용을 넣어서 gemini의 결과값을 반환합니다.

## Module
`main`: 애플리케이션의 메인 실행 흐름을 제어합니다.   
`gemini` : gemini API를 호출하고, response를 받는 역할을 합니다.   
`vector-store` : RAG를 구축하기 위해서, 텍스트 데이터를 Split하고 Vector DB에 store하는 역할을 합니다.   
`retriever`: Vector DB에서 사용자 입력과 연관된 Knowledge를 찾는 검색하는 역할을 합니다.   
`crawler` : KB를 구축하는데 필요한 문서 데이터를 수집하는 역할을 합니다.   
`chat` : user input과 LLM answer를 기반으로 답변을 어떻게 생성할지 정하는 역할을 합니다.   
`sql` : sqlite나 MySQL을 사용하기 위해서 RDBMS를 연동하고, SQL을 처리하는 역할을 합니다. -> 사용X   
`logger` : chat이 실행될 때마다 User question 입력값, gemini response값, 시간을 저장합니다.   

## Project explain
![image](https://github.com/jenner9212/langchain/assets/35947676/75a24a25-ab1f-4375-a67a-59b82ec9a2d0)

[Source](https://www.youtube.com/watch?v=tIU2tw3PMUE&t=13s)

  이번 프로젝트는 LangChain을 이용해서 Knowledge Base를 구축하고, 이를 응용한 `QA Engine을 개발`하는 것을 목표로 합니다.

  프로젝트의 목표는 Google Gemini API를 사용하여 수집한 문서 데이터를 기준으로 답변을 만드는 QA Bot을 만드는 것입니다. 이번 프로젝트에서는 QA Bot 자체의 답변 퀄리티를 높이는 것에 집중하는 것이 아니라, 이러한 **기능을 할 수 있는 구조**를 만드는 것에 집중합니다.

  **수집하는 문서는 자유롭게 정하시면 됩니다(기획 단계에 포함)**. 꼭 크롤링 코드를 작성하여 수집할 필요는 없으며, 예를 들어 AI논문이라고 한다면 arXiv에서 직접 PDF를 다운로드 받아서 사용해도 무방합니다. 또는 네이버 뉴스기사를 크롤링하거나, 특정 분야의 tech report, Harvard Business Review, Numpy documentation 등등 자유롭게 정하세요.

## Requirements
1. **개발 언어**: 전체 프로젝트는 Python으로 개발됩니다.
2. **API 사용**: Gemini API를 통해 LLM의 답변을 받습니다. 모델은 `gemini-pro` 또는 `gemini-1.5-pro-latest`를 사용합니다.
3. **모듈 구조**: 프로젝트는 최소 다섯개 이상의 모듈로 구성됩니다. 예를 들면 다음과 같습니다.
(다음은 예시이며, 기획 단계에서 어떻게 구현할지 팀 단위로 고민해보세요. **기획 단계도 평가 요소**에 들어갑니다.)
    - `main`: 애플리케이션의 메인 실행 흐름을 제어합니다. **(main은 필수로 포함합니다)**
    - `gemini` : gemini API를 호출하고, response를 받는 역할을 합니다.
    - `vector-store` : RAG를 구축하기 위해서, 텍스트 데이터를 Split하고 Vector DB에 store하는 역할을 합니다.
    - `retriever`: Vector DB에서 사용자 입력과 연관된 Knowledge를 찾는 검색하는 역할을 합니다.
    - `crawler` : KB를 구축하는데 필요한 문서 데이터를 수집하는 역할을 합니다.
    - `chat` : user input과 LLM answer를 기반으로 답변을 어떻게 생성할지 정하는 역할을 합니다.
    - `sql` : sqlite나 MySQL을 사용하기 위해서 RDBMS를 연동하고, SQL을 처리하는 역할을 합니다.
    - `logger` : 실행되면서 기록되는 내용들을 저장합니다.
4. **오픈소스 라이브러리 사용 :** 사용할 수 있는 오픈소스에 제한은 없습니다.
5. **LLM 사용 제한**: openai GPT-4나, Claude3 Opus 같은 다른 라이브러리를 사용하는 경우 평가에서 제외됩니다. 개인적으로 테스트하는 것은 상관없으나 이번 프로젝트에서는 Gemini만 사용해주세요.
6. **코드 협업**: GitHub를 사용하여 소스 코드 관리 및 협업을 진행합니다. 각 모듈별로 브랜치를 나누어 개발하고, Pull Request를 통해 코드 리뷰를 수행합니다. 모든 팀원이 최소한 1번 이상 PR을 수행하여 프로젝트의 Contributor로 참여해야 합니다.
7. **클래스 사용**: 각 모듈은 클래스 기반으로 설계합니다. **[main.py](http://main.py/)**에선 모든 모듈을 불러와서 전체적인 기능을 한번에 수행합니다.

## 필수 기능

1. Gemini API를 통해 답변이 제대로 생성되었는지 확인하는 기능
2. LLM의 답변을 의도대로 생성하기 위해 System Prompt를 세팅하는 기능
3. RAG를 하기 위해 데이터를 VectorDB에 저장하는 기능 (최소 문서의 개수는 **30**개)
(++ 여기서 30개의 문서는 뉴스 기사 30개 정도의 텍스트 길이라는 의미이며, 글자 수로는 **대략 20000자** 정도 됩니다.)
4. Retrieve를 통해 사용자 입력과 적절한 Knowledge를 추출하는 기능
5. main.py를 통해서 나머지 모듈들을 불러와서 한번에 실행하는 기능
6. Chat History를 기억하여 지정한 페르소나, 주어진 역할, 답변의 출력 양식등을 유지하는 기능
→ 평가시 사용자 입력은 5번 수행이 될것이므로, 5번 이상 기억할 수 있으면 됩니다.



## 🧱 Tech Stack

### Language
  <!--Python-->
  <img alt="Python" src ="https://img.shields.io/badge/Python-3776AB.svg?&style=for-the-badge&logo=Python&logoColor=white"/>

### Framework
  <!--Pandas-->
  <img alt="langchain" src ="https://img.shields.io/badge/langchain-83B81A?&style=for-the-badge&logo=langchain&logoColor=white"/>
  <!--Matplotlib-->
  <img alt="gemini" src ="https://img.shields.io/badge/googlegemini-8E75B2.svg?&style=for-the-badge&logo=googlegemini&logoColor=white"/>
