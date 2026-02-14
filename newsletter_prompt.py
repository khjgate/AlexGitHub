
"""
뉴스레터 프롬프트/조회조건 설정 파일


이 파일에서 아래 항목을 자유롭게 수정하면 뉴스레터의 수집/출력 조건이 바로 반영됩니다.

- trusted_sources: 신뢰할 수 있는 주요 언론사 목록 (이 언론사에 해당하는 뉴스만 우선 노출)
- trusted_academic_sources: 신뢰할 수 있는 주요 학술기관/연구소/저널/기업 목록 (학술기관 AX Trend 카테고리로 출력)
- categories: 카테고리별 뉴스 검색 키워드 (카테고리명: [키워드 리스트])

※ 카테고리명, 키워드, 언론사, 학술기관 모두 자유롭게 추가/삭제/수정 가능
※ 이 파일만 수정하면 코드 변경 없이 뉴스레터 조건이 바뀜

# 참고: 더 많은 뉴스 확보를 원할 경우
# - Google News RSS 외에 Bing News, Yahoo News, Naver 뉴스 등 다양한 뉴스 API/검색 엔진을 활용하는 코드로 확장할 수 있습니다.
# - 예시: requests로 Bing News API, Yahoo News API 등에서 기사 수집 후 기존 로직에 통합
# - 필요시 개발 요청 시 코드 예시 제공 가능
"""

# 신뢰할 수 있는 주요 언론사
trusted_sources = [
    # 국내 주요 언론사
    '연합뉴스', '한국경제', '매일경제', '조선일보', '중앙일보', '동아일보',
    'KBS', 'MBC', 'SBS', 'YTN', 'JTBC', 'TV조선', '채널A',
    '한겨레', '경향신문', '서울경제', '아시아경제', '뉴시스', '뉴스1',
    '이데일리', '머니투데이', '파이낸셜뉴스', '헤럴드경제', '전자신문',
    'ZDNet', '지디넷', 'IT조선', 'ITWorld', '디지털타임스', '디지털데일리',
    'AI타임즈', '인공지능신문', '로봇신문', '테크M', 'Bloter', '블로터',
    'The Guru', '글로벌이코노믹', '비즈한국', '더팩트', '데일리안',
    '데이터넷', '보안뉴스', 'IT동아', 'ITBizNews', 'CIO Korea', 'ITWorld Korea',
    '전자신문인터넷', '디지털투데이', '플래텀', '벤처스퀘어', '바이라인네트워크',
    # 해외 주요 언론사 (영문 기사 검색 시)
    'BBC', 'CNN', 'The New York Times', 'The Guardian', 'Reuters', 
    'Bloomberg', 'TechCrunch', 'Wired', 'The Verge', 'Ars Technica', 
    'VentureBeat', 'Engadget', 'ZDNet', 'CNET', 'Gizmodo', 'Mashable', 
    'The Next Web', 'Forbes', 'Fortune', 'Financial Times', 'MIT Technology Review',
    'Nature', 'Science', 'Scientific American', 'New Scientist', 'PCMag', 'InfoWorld',
    'Fast Company', 'Quartz', 'Business Insider', 'The Information', 'Axios', 'Protocol',
]

# 신뢰할 수 있는 주요 학술기관
trusted_academic_sources = [
    # 국내 대학/연구기관
    '서울대', 'KAIST', '포항공대', '성균관대', '연세대', '고려대', '한양대', 
    '중앙대', '경희대', '부산대', '충남대', '전남대', '국민대', '세종대', 
    '한국과학기술원', '한국전자통신연구원', '한국과학기술정보연구원', '한국산업기술진흥원',
    '한국전자기술연구원', '한국생산기술연구원', '한국기계연구원', '한국항공우주연구원',
    '한국원자력연구원', '한국화학연구원', '한국생명공학연구원', '한국뇌연구원',
    # 해외 대학/연구기관/기업
    'MIT', 'Stanford', 'Berkeley', 'Carnegie Mellon', 'Oxford', 'Cambridge',
    'Harvard', 'Caltech', 'ETH Zurich', 'Tsinghua', 'Peking University',
    'Google Research', 'Microsoft Research', 'OpenAI', 'DeepMind', 'NVIDIA Research',
    'Facebook AI Research', 'Amazon AI', 'IBM Research', 'Apple AI Research',
    '삼성전자', '네이버', 'LG전자', 'SK텔레콤', '카카오',
    # 저널/학회
    '네이처 (Nature)', '사이언스 (Science)', '셀 (Cell)', 'PNAS', 'IEEE', 'ACM', 'AAAI', 'IJCAI', 'CVPR', 'NeurIPS', 'ICLR', 'ICML', 'ECCV', 'AI 전문 저널 등'
]

# 카테고리별 검색 키워드
categories = {
    'AX 활용 사례': [
        'AX 트랜드', 'AI 트랜드', 'AX 성공 사례', 'AX 실패사례', 'AX 진행', 'AX 도입', 'AX 혁신', 'AX 기업 사례', 'AX 산업 동향', 'AX 기술 동향',     
        'AX 자동화 혁신', 'AI 업무 자동화 사례', 'RPA AI 도입', '기업 AI 전환', 'AI 디지털 전환',
        'AI 기반 업무 혁신', 'DX 성공 사례', 'AI 도입 효과', 'AI 생산성 향상', 'AI 업무 효율화',
        'AI+RPA 융합', 'AI 챗봇 도입', 'AI 문서 자동화', 'AI 기반 프로세스 혁신', 'AI 기반 고객 서비스', 
        'AI 기반 데이터 분석', 'AI 기반 의사결정 지원', 'AI 기반 예측 분석', 'AI 기반 업무 최적화', 'AI 기반 혁신 사례', 
    ],
    '국내 AI 소식': [
        'AI 인공지능', 'AI 기술', 'AI 산업', 'AI 정책', 'AI 연구', 'AI 스타트업', 'AI 투자', 'AI 윤리', 'AI 규제', 
        'AI 인공지능 기술', '딥러닝 머신러닝', 'GPU AI 인프라', 'AI 연구 대학', '삼성 AI', '네이버 AI', 'LG AI', 'SK AI', '카카오 AI',
        '국내 AI 정책', 'AI 스타트업', 'AI 정부 지원', 'AI 인재 양성', 'AI 윤리', 'AI 규제', 'AI 산업 동향', 'AI 투자', 'AI 생태계',
        'AI 의료', 'AI 교육', 'AI 로봇', 'AI 반도체', 'AI 보안', 'AI 빅데이터', 'AI 클라우드', 'AI IoT', 'AI 스마트팩토리',
        'AI 금융', 'AI 투자', 'AI 윤리', 'AI 정책', 'AI 글로벌', 'AI 혁신', 'AI 미래',
        'AI 실전', 'AI 실습', 'AI 실전 활용', 'AI 실전 사례', 'AI 실전 강의', 'AI 실전 프로젝트', 'AI 실전 연구', 'AI 실전 개발',
        'AI 실전 클라우드', 'AI 실전 빅데이터', 'AI 실전 IoT', 'AI 실전 스마트팩토리', 'AI 실전 금융', 'AI 실전 투자'
    ],
    '해외 AI 신규뉴스': [
        'OpenAI GPT', '구글 AI Gemini', '마이크로소프트 Copilot', '애플 AI', '메타 AI 라마', '엔비디아 AI',
        '해외 AI 정책', 'AI 글로벌 트렌드', 'AI 국제 협력', 'AI 스타트업 해외', 'AI 투자 해외', 'AI 윤리 해외',
        'AI 의료 해외', 'AI 교육 해외', 'AI 로봇 해외', 'AI 반도체 해외', 'AI 보안 해외', 'AI 빅데이터 해외', 'AI 클라우드 해외', 'AI IoT 해외', 'AI 스마트팩토리 해외',
        'AI 금융 해외', 'AI 투자 해외', 'AI 윤리 해외', 'AI 정책 해외', 'AI 글로벌 해외', 'AI 혁신 해외', 'AI 미래 해외',
        'AI 실전 해외', 'AI 실습 해외', 'AI 실전 활용 해외', 'AI 실전 사례 해외', 'AI 실전 강의 해외', 'AI 실전 프로젝트 해외', 'AI 실전 연구 해외', 'AI 실전 개발 해외',
        'AI 실전 클라우드 해외', 'AI 실전 빅데이터 해외', 'AI 실전 IoT 해외', 'AI 실전 스마트팩토리 해외', 'AI 실전 금융 해외', 'AI 실전 투자 해외',
        'AI 실전 윤리 해외', 'AI 실전 정책 해외', 'AI 실전 글로벌 해외', 'AI 실전 혁신 해외', 'AI 실전 미래 해외'
        
    ],
    '학술기관 AX Trend': [
        '서울대 AI 연구', 'KAIST AI 논문', 'MIT AI 연구', 'Stanford AI 프로젝트', 'Google Research AI', 'Microsoft Research AI', 'OpenAI 연구', 'DeepMind 연구',
        'AI 학회 논문', 'AI 국제학회', 'AI 연구성과', 'AI 논문 발표', 'AI 연구실', 'AI 대학원', 'AI 교수 연구', 'AI 산학협력', 'AI 융합 연구', 'AI 특허',
        'AI 학술지', 'AI 연구자', 'AI 연구 동향', 'AI 연구 프로젝트', 'AI 연구 논문', 'AI 연구 발표', 'AI 연구 성과', 'AI 연구 실적'
    ],
    '피지컬 AI': [
        '테슬라 옵티머스 로봇', 'Figure AI 휴머노이드', '엔비디아 로봇 AI', '보스턴다이나믹스 아틀라스', '중국 휴머노이드 로봇',
        '로봇 자동화', 'AI 로봇 개발', 'AI 로봇 혁신', 'AI 로봇 산업', 'AI 로봇 기술', 'AI 로봇 서비스', 'AI 로봇 시장', 'AI 로봇 트렌드', 'AI 로봇 연구', 'AI 로봇 응용'
    ],
    '금융사 AI 적용 사례 및 규제 완화 소식': [
        '금융 AI 도입', '은행 AI 서비스', '핀테크 AI', '보험 AI', '금융 규제 완화',
        'AI 금융 혁신', 'AI 금융 자동화', 'AI 금융 서비스', 'AI 금융 보안', 'AI 금융 데이터', 'AI 금융 트렌드', 'AI 금융 사례', 'AI 금융 연구', 'AI 금융 정책', 'AI 금융 투자'
    ],
    '🔥 한화그룹 Hot News': [
        '한화 그룹', '한화에어로스페이스', '한화오션', '한화솔루션', '한화생명', '한화 방산',
        '한화 AI', '한화 디지털 전환', '한화 혁신 사례', '한화 기업 뉴스',
        '한화 신사업', '한화 투자', '한화 글로벌', '한화 ESG', '한화 R&D', '한화 스타트업', '한화 미래전략'
    ],
}


# 유튜브 추천 영상 검색 키워드
youtube_search_keywords = [
    'AI 인공지능 강의',
    'AI Tool 활용법',
    'AI 업무 자동화',
    '디지털전환 DX 사례',
    '데이터 분석 실무',
    'AX 기업 혁신',
    '인공지능 비즈니스',
    'AI 트렌드',
    'AI 최신 기술',
    'AI 실무 활용',
    'AI 스타트업',
    'AI 연구 동향',
    'AI 논문 해설',
    'AI 개발자 인터뷰',
    'AI 컨퍼런스',
    'AI 산업 전망',
    'AI 자동화 사례',
    'AI RPA',
    'AI 챗봇',
    'AI 로봇',
    'AI 의료',
    'AI 교육',
    'AI 반도체',
    'AI 클라우드',
    'AI 빅데이터',
    'AI IoT',
    'AI 스마트팩토리',
    'AI 금융',
    'AI 투자',
    'AI 윤리',
    'AI 정책',
    'AI 글로벌',
    'AI 혁신',
    'AI 미래',
    'AI 실전',
    'AI 실습',
    'AI 실전 활용',
    'AI 실전 사례',
    'AI 실전 강의',
    'AI 실전 프로젝트',
    'AI 실전 연구',
    'AI 실전 개발',
    'AI 실전 인터뷰',
    'AI 실전 컨퍼런스',
    'AI 실전 산업',
    'AI 실전 전망',
    'AI 실전 자동화',
    'AI 실전 RPA',
    'AI 실전 챗봇',
    'AI 실전 로봇',
    'AI 실전 의료',
    'AI 실전 교육',
    'AI 실전 반도체',
    'AI 실전 클라우드',
    'AI 실전 빅데이터',
    'AI 실전 IoT',
    'AI 실전 스마트팩토리',
    'AI 실전 금융',
    'AI 실전 투자',
    'AI 실전 윤리',
    'AI 실전 정책',
    'AI 실전 글로벌',
    'AI 실전 혁신',
    'AI 실전 미래'
]