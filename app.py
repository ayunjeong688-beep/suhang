import streamlit as st

st.set_page_config(
    page_title="진로 나침반",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# 기본 설정 및 화면 스타일
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Pretendard', sans-serif; }
.block-container { max-width: 1180px; padding-top: 1.2rem; padding-bottom: 1rem; }
header, footer, #MainMenu {visibility: hidden;}
.stApp { background: #F5F7FB; }
.hero {
    background: linear-gradient(120deg, #173B5E 0%, #286B83 100%);
    padding: 25px 28px; border-radius: 20px; color: white; margin-bottom: 16px;
}
.hero h1 { color: white; font-size: 2rem; margin: 0 0 5px 0; }
.hero p { color: #DCEAF2; margin: 0; }
.step {
    display: inline-block; padding: 5px 11px; border-radius: 30px;
    background: #E5F0F4; color: #1D566D; font-size: 0.82rem; font-weight: 700;
    margin-bottom: 10px;
}
.info-card {
    background: white; border: 1px solid #E6EAF0; border-radius: 15px;
    padding: 16px 18px; min-height: 112px;
}
.small-muted { color: #697586; font-size: 0.88rem; }
div.stButton > button {
    border-radius: 12px; min-height: 46px; font-weight: 650;
    border: 1px solid #DCE3EA;
}
div.stButton > button[kind="primary"] {
    background: #1F5875; border-color: #1F5875;
}
[data-testid="stMetric"] {
    background: white; border: 1px solid #E6EAF0; padding: 12px;
    border-radius: 12px;
}
a { color: #1F5875 !important; font-weight: 600; }
div[data-testid="stMarkdownContainer"] p { line-height: 1.48; }
</style>
""", unsafe_allow_html=True)

# 데이터는 커리어넷 직업백과·학과정보, Q-Net 자격정보 등의 분류와 공개 설명을 참고해
# 탐색용으로 직접 정리한 예시입니다. 실시간 API 연동 데이터가 아닙니다.
CAREERS = {
    "의료·보건": {
        "🏥 환자 치료·간호": [
            {"name":"간호사","work":"환자의 건강 상태를 관찰하고 간호, 치료 보조, 건강 교육을 수행합니다.","skills":"의사소통, 관찰력, 책임감, 기초 생명과학","majors":"간호학과","path":"간호학과 등 관련 교육과정을 이수하고 간호사 국가시험에 합격해야 합니다.","tags":"환자와 직접 소통하며 건강 회복을 돕는 일에 관심 있는 사람"},
            {"name":"응급구조사","work":"응급 상황에서 환자 평가와 응급처치를 하고 의료기관 이송을 돕습니다.","skills":"침착함, 빠른 판단, 협업, 응급처치 지식","majors":"응급구조학과","path":"관련 교육과정 이수 후 응급구조사 국가시험 등 자격 요건을 확인합니다.","tags":"긴급한 상황에서 신속하게 사람을 돕는 일에 관심 있는 사람"},
            {"name":"물리치료사","work":"운동 및 물리적 방법을 활용해 신체 기능 회복과 움직임 개선을 돕습니다.","skills":"인체 구조 이해, 관찰력, 소통, 꾸준함","majors":"물리치료학과","path":"관련 학과 교육과정을 이수하고 물리치료사 국가시험에 합격해야 합니다.","tags":"재활과 신체 움직임에 관심 있는 사람"},
        ],
        "🧪 검사·진단": [
            {"name":"임상병리사","work":"혈액, 체액, 조직 등의 검체를 검사해 질병의 진단과 치료에 필요한 정보를 제공합니다.","skills":"정확성, 분석력, 생명과학 기초, 꼼꼼함","majors":"임상병리학과","path":"관련 교육과정 이수 후 임상병리사 국가시험에 합격해야 합니다.","tags":"실험과 검사 결과 분석에 흥미가 있는 사람"},
            {"name":"방사선사","work":"의료영상 장비를 이용해 진단과 치료에 필요한 영상 정보를 얻는 업무를 합니다.","skills":"기기 활용, 안전 의식, 정확성, 해부학 기초","majors":"방사선학과","path":"관련 교육과정 이수 후 방사선사 국가시험에 합격해야 합니다.","tags":"의료와 영상·기술을 함께 탐구하고 싶은 사람"},
            {"name":"치과위생사","work":"구강질환 예방 교육, 구강 관리 및 치과 진료 협조 업무를 수행합니다.","skills":"손재능, 세심함, 의사소통, 구강보건 지식","majors":"치위생학과","path":"관련 교육과정 이수 후 치과위생사 국가시험에 합격해야 합니다.","tags":"구강 건강과 예방 교육에 관심 있는 사람"},
        ],
        "💊 의약·건강관리": [
            {"name":"약사","work":"의약품을 조제·관리하고 올바른 복용 방법과 약물 정보를 안내합니다.","skills":"화학·생명과학 기초, 꼼꼼함, 윤리의식","majors":"약학과","path":"약학 교육과정과 약사 국가시험 등 관련 요건을 확인합니다.","tags":"약물과 건강의 관계를 깊이 공부하고 싶은 사람"},
            {"name":"영양사","work":"개인과 집단의 건강 상태에 맞춰 식단을 계획하고 영양 관리를 수행합니다.","skills":"영양 지식, 계획력, 소통, 위생 관리","majors":"식품영양학과","path":"관련 교과목·실습 등 자격 요건을 갖추고 영양사 국가시험에 합격해야 합니다.","tags":"식생활과 건강 증진에 관심 있는 사람"},
            {"name":"보건교육사","work":"개인과 지역사회가 건강한 생활 습관을 실천하도록 교육 프로그램을 기획합니다.","skills":"교육 기획, 의사소통, 자료 분석, 건강 지식","majors":"보건학과, 보건행정학과 등","path":"등급별 관련 교과목과 자격 요건을 확인해야 합니다.","tags":"사람들에게 건강 정보를 알기 쉽게 전달하고 싶은 사람"},
        ],
    },
    "과학·기술": {
        "🔬 생명·연구": [
            {"name":"생명과학 연구원","work":"생물의 구조와 기능, 생명 현상을 연구하고 실험 자료를 분석합니다.","skills":"탐구력, 실험 설계, 데이터 분석, 끈기","majors":"생명과학과, 생명공학과","path":"관련 전공과 연구 경험을 쌓고 대학원 진학 등을 고려할 수 있습니다.","tags":"생명 현상의 원리를 발견하고 싶은 사람"},
            {"name":"식품 연구원","work":"식품의 성분, 품질, 안전성 및 새로운 식품 개발을 연구합니다.","skills":"화학·생명과학, 분석력, 실험 능력","majors":"식품공학과, 식품영양학과","path":"관련 전공과 연구·품질관리 경험을 쌓을 수 있습니다.","tags":"먹거리의 안전과 과학적 원리에 관심 있는 사람"},
        ],
        "💻 컴퓨터·AI": [
            {"name":"소프트웨어 개발자","work":"사용자의 문제를 해결하는 프로그램과 서비스를 설계하고 개발합니다.","skills":"논리적 사고, 문제 해결, 협업, 코딩","majors":"컴퓨터공학과, 소프트웨어학과","path":"전공 학습과 프로젝트·포트폴리오를 통해 역량을 쌓을 수 있습니다.","tags":"디지털 도구를 만들어 문제를 해결하고 싶은 사람"},
            {"name":"데이터 분석가","work":"데이터를 수집·정리·분석해 의미 있는 패턴과 의사결정 근거를 찾습니다.","skills":"통계, 논리력, 시각화, 질문하는 태도","majors":"통계학과, 데이터사이언스학과, 컴퓨터공학과","path":"통계·프로그래밍·분야별 지식을 함께 학습할 수 있습니다.","tags":"숫자와 자료에서 숨은 의미를 찾는 사람"},
        ],
    },
    "사회·행정": {
        "⚖️ 법·공공": [
            {"name":"법률 전문가","work":"법과 제도를 해석하고 분쟁 해결과 권리 보호를 지원합니다.","skills":"논리력, 글쓰기, 자료 해석, 윤리의식","majors":"법학과, 행정학과 등","path":"희망 직무에 따라 법학전문대학원 등 별도 진로 요건을 확인합니다.","tags":"사회 문제와 규칙, 정의에 관심 있는 사람"},
            {"name":"공무원","work":"행정기관에서 정책 집행, 민원, 행정 지원 등 공공 업무를 수행합니다.","skills":"책임감, 문서 작성, 소통, 공공성","majors":"행정학과, 사회학과 등","path":"직렬별 공개경쟁채용 등 채용 공고와 시험 과목을 확인합니다.","tags":"지역사회와 공공서비스에 기여하고 싶은 사람"},
        ],
        "🤝 복지·상담": [
            {"name":"사회복지사","work":"도움이 필요한 사람과 가족을 지원하고 복지 서비스와 자원을 연결합니다.","skills":"공감적 소통, 문제 해결, 상담, 윤리의식","majors":"사회복지학과","path":"사회복지사 자격 기준에 따른 교과목과 실습을 이수합니다.","tags":"사람들의 생활 문제를 함께 해결하고 싶은 사람"},
            {"name":"상담 전문가","work":"상담을 통해 개인이 자신의 어려움을 이해하고 해결 방향을 찾도록 돕습니다.","skills":"경청, 공감, 의사소통, 전문 지식","majors":"심리학과, 상담심리학과","path":"활동 분야에 따라 대학원·수련·자격 요건이 다릅니다.","tags":"사람의 마음과 행동을 이해하고 싶은 사람"},
        ],
    },
    "교육": {
        "📚 학교·교육": [
            {"name":"교사","work":"학생의 발달과 학습 수준에 맞춰 수업과 생활 지도를 합니다.","skills":"설명력, 소통, 인내심, 교과 전문성","majors":"교육학과, 사범대학 각 교과교육과","path":"교원자격 취득 및 임용 등 진출 경로를 확인합니다.","tags":"배우고 가르치는 과정에 보람을 느끼는 사람"},
            {"name":"특수교사","work":"장애 학생의 특성과 교육적 요구에 맞는 개별화 교육을 지원합니다.","skills":"관찰력, 소통, 교육 설계, 협력","majors":"특수교육과","path":"특수교사 교원자격과 임용 관련 요건을 확인합니다.","tags":"다양한 학습 방식을 존중하고 지원하고 싶은 사람"},
        ],
    },
    "예술·디자인": {
        "🎨 시각·콘텐츠": [
            {"name":"시각디자이너","work":"정보와 메시지를 이미지·글자·색상으로 구성해 시각적으로 전달합니다.","skills":"창의력, 시각화, 소통, 디자인 도구 활용","majors":"시각디자인학과, 디자인학과","path":"작업물과 포트폴리오를 준비하고 분야별 실무 역량을 쌓습니다.","tags":"아이디어를 이미지로 표현하는 것을 좋아하는 사람"},
            {"name":"영상 콘텐츠 제작자","work":"영상 기획부터 촬영, 편집, 배포까지 콘텐츠 제작 과정을 담당합니다.","skills":"기획력, 스토리텔링, 편집, 협업","majors":"영상학과, 미디어학과, 방송영상학과","path":"개인·팀 프로젝트와 포트폴리오를 통해 경험을 쌓을 수 있습니다.","tags":"이야기를 영상으로 전달하고 싶은 사람"},
        ],
    },
    "경영·경제": {
        "📈 경영·기획": [
            {"name":"마케팅 전문가","work":"시장과 소비자를 분석하고 제품·서비스의 홍보 전략을 기획합니다.","skills":"분석력, 창의력, 소통, 데이터 활용","majors":"경영학과, 광고홍보학과","path":"시장 조사와 기획 프로젝트 경험을 쌓을 수 있습니다.","tags":"사람들의 선택과 시장 변화에 관심 있는 사람"},
            {"name":"회계 전문가","work":"조직의 재무 정보를 기록·분석하고 회계 기준에 맞게 보고합니다.","skills":"수리력, 정확성, 윤리의식, 분석력","majors":"회계학과, 경영학과","path":"업무 분야에 따라 회계·세무 관련 자격과 실무 경험을 준비합니다.","tags":"숫자를 정확하게 다루고 체계적으로 정리하는 사람"},
        ],
    },
}

AREAS = list(CAREERS.keys())
ALL_JOBS = [job for groups in CAREERS.values() for jobs in groups.values() for job in jobs]

if "page" not in st.session_state:
    st.session_state.page = "home"
if "area" not in st.session_state:
    st.session_state.area = None
if "field" not in st.session_state:
    st.session_state.field = None
if "job" not in st.session_state:
    st.session_state.job = None
if "saved" not in st.session_state:
    st.session_state.saved = []

def go(page):
    st.session_state.page = page

def reset():
    st.session_state.area = None
    st.session_state.field = None
    st.session_state.job = None
    go("home")

def header():
    c1, c2 = st.columns([5, 1])
    with c1:
        st.markdown("### 🧭 진로 나침반")
        st.caption("관심사에서 시작해 나에게 맞는 진로를 단계별로 탐색해요.")
    with c2:
        if st.button("⌂ 처음으로", use_container_width=True):
            reset()
    st.divider()

def job_card(job, key):
    with st.container(border=True):
        st.markdown(f"#### {job['name']}")
        st.write(job["work"])
        st.caption(f"관련 학과: {job['majors']}")
        if st.button("자세히 보기", key=key, use_container_width=True):
            st.session_state.job = job
            go("detail")
            st.rerun()

# -----------------------------
# 화면 1: 시작
# -----------------------------
header()
if st.session_state.page == "home":
    st.markdown("""
    <div class="hero">
      <h1>나의 관심사에서 미래 직업까지</h1>
      <p>정답을 정해두지 말고, 궁금한 분야부터 하나씩 선택해 보세요.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<span class="step">STEP 1 · 관심 영역</span>', unsafe_allow_html=True)
    st.subheader("가장 관심 있는 분야를 선택해 주세요.")
    st.caption("선택한 분야에 따라 다음 화면의 세부 분야가 달라집니다.")
    cols = st.columns(3)
    icons = {"의료·보건":"🏥","과학·기술":"🧬","사회·행정":"🌏","교육":"📚","예술·디자인":"🎨","경영·경제":"📊"}
    for i, area in enumerate(AREAS):
        with cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"## {icons[area]}")
                st.markdown(f"### {area}")
                st.caption(f"{len(CAREERS[area])}개 세부 분야")
                if st.button("이 분야 탐색하기", key=f"area_{i}", type="primary", use_container_width=True):
                    st.session_state.area = area
                    go("fields")
                    st.rerun()
    st.divider()
    a, b, c = st.columns(3)
    a.metric("탐색 분야", f"{len(AREAS)}개")
    b.metric("세부 분야", f"{sum(len(x) for x in CAREERS.values())}개")
    c.metric("직업 예시", f"{len(ALL_JOBS)}개")
    x, y = st.columns(2)
    with x:
        if st.button("🔎 직업 전체 검색", use_container_width=True):
            go("search"); st.rerun()
    with y:
        if st.button(f"⭐ 관심 직업 모아보기 ({len(st.session_state.saved)})", use_container_width=True):
            go("saved"); st.rerun()

# -----------------------------
# 화면 2: 세부 분야
# -----------------------------
elif st.session_state.page == "fields":
    area = st.session_state.area
    st.markdown('<span class="step">STEP 2 · 세부 분야</span>', unsafe_allow_html=True)
    st.subheader(f"{area}에서 어떤 분야가 궁금한가요?")
    st.caption("관심 있는 세부 분야를 선택하면 관련 직업을 확인할 수 있어요.")
    cols = st.columns(2)
    for i, (field, jobs) in enumerate(CAREERS[area].items()):
        with cols[i % 2]:
            with st.container(border=True):
                st.markdown(f"### {field}")
                st.caption(" · ".join(j["name"] for j in jobs))
                if st.button("이 분야 선택", key=f"field_{i}", type="primary", use_container_width=True):
                    st.session_state.field = field
                    go("jobs"); st.rerun()
    st.write("")
    if st.button("← 관심 영역 다시 선택"):
        reset(); st.rerun()

# -----------------------------
# 화면 3: 직업 목록
# -----------------------------
elif st.session_state.page == "jobs":
    area, field = st.session_state.area, st.session_state.field
    st.markdown('<span class="step">STEP 3 · 직업 탐색</span>', unsafe_allow_html=True)
    st.subheader(f"{area}  /  {field}")
    jobs = CAREERS[area][field]
    cols = st.columns(2)
    for i, job in enumerate(jobs):
        with cols[i % 2]:
            job_card(job, f"job_{area}_{i}")
    st.write("")
    if st.button("← 세부 분야 다시 선택"):
        go("fields"); st.rerun()

# -----------------------------
# 화면 4: 직업 상세
# -----------------------------
elif st.session_state.page == "detail":
    job = st.session_state.job
    st.markdown('<span class="step">STEP 4 · 직업 상세 정보</span>', unsafe_allow_html=True)
    st.title(job["name"])
    st.caption("아래 내용은 진로 탐색을 위한 요약이며, 실제 업무와 자격 요건은 기관·분야별로 달라질 수 있습니다.")
    left, right = st.columns([1.35, 1])
    with left:
        with st.container(border=True):
            st.markdown("#### 💼 주요 업무")
            st.write(job["work"])
            st.markdown("#### 🧠 필요한 역량")
            st.write(job["skills"])
            st.markdown("#### 🎓 관련 학과")
            st.write(job["majors"])
            st.markdown("#### 🛤️ 준비 경로")
            st.write(job["path"])
        with st.container(border=True):
            st.markdown("#### 🙋 이런 관심이 있다면 살펴보세요")
            st.write(job["tags"])
    with right:
        with st.container(border=True):
            st.markdown("#### 🔗 공식 진로 정보")
            st.markdown("[커리어넷 직업백과](https://www.career.go.kr/cloud/w/job/list)")
            st.markdown("[커리어넷 학과정보](https://www.career.go.kr/cloud/w/main/home)")
            st.markdown("[고용24](https://www.work24.go.kr/)")
            st.markdown("[Q-Net 자격정보](https://www.q-net.or.kr/)")
            st.caption("자격이 필요한 직업은 공식 사이트에서 최신 응시·자격 요건을 확인하세요.")
        is_saved = job["name"] in [x["name"] for x in st.session_state.saved]
        if st.button("⭐ 관심 직업에서 제거" if is_saved else "☆ 관심 직업으로 저장", type="primary", use_container_width=True):
            if is_saved:
                st.session_state.saved = [x for x in st.session_state.saved if x["name"] != job["name"]]
            else:
                st.session_state.saved.append(job)
            st.rerun()
        if st.button("다른 직업 탐색하기", use_container_width=True):
            go("home"); st.rerun()
    st.info("진로 선택은 한 번에 확정할 필요가 없어요. 여러 직업의 업무와 필요한 역량을 비교해 보세요.")

# -----------------------------
# 화면 5: 전체 직업 검색
# -----------------------------
elif st.session_state.page == "search":
    st.markdown('<span class="step">직업 검색</span>', unsafe_allow_html=True)
    st.subheader("궁금한 직업을 직접 찾아보세요.")
    query = st.text_input("직업명 또는 관련 학과 검색", placeholder="예: 간호사, 심리학과, 데이터")
    filtered = [j for j in ALL_JOBS if query.lower() in (j["name"] + j["majors"] + j["work"]).lower()] if query else ALL_JOBS
    st.caption(f"검색 결과 {len(filtered)}개")
    if filtered:
        cols = st.columns(2)
        for i, job in enumerate(filtered):
            with cols[i % 2]:
                job_card(job, f"search_{i}_{job['name']}")
    else:
        st.warning("검색 결과가 없어요. 다른 단어로 검색해 보세요.")
    if st.button("← 처음 화면"):
        reset(); st.rerun()

# -----------------------------
# 화면 6: 저장한 직업
# -----------------------------
elif st.session_state.page == "saved":
    st.markdown('<span class="step">나의 관심 직업</span>', unsafe_allow_html=True)
    st.subheader("저장한 직업을 비교해 보세요.")
    if not st.session_state.saved:
        st.info("아직 저장한 직업이 없어요. 직업 상세 화면에서 별표 버튼을 눌러 저장할 수 있어요.")
    else:
        cols = st.columns(2)
        for i, job in enumerate(st.session_state.saved):
            with cols[i % 2]:
                job_card(job, f"saved_{i}_{job['name']}")
    if st.button("← 처음 화면"):
        reset(); st.rerun()

# -----------------------------
# 공통 출처 및 안내
# -----------------------------
st.divider()
with st.expander("📌 정보 출처와 이용 안내"):
    st.markdown("""
    - [커리어넷](https://www.career.go.kr/): 직업백과, 직업정보, 학과정보, 진로심리검사 등을 제공하는 진로정보망입니다.
    - [커리어넷 Open API 센터](https://www.career.go.kr/cnet/front/openapi/openApiMainCenter.do): 직업정보·학과정보 등 공개 API 안내를 확인할 수 있습니다. API를 실제 연결하려면 인증키가 필요합니다.
    - [고용24](https://www.work24.go.kr/): 고용·직업능력개발 등 통합 고용서비스를 제공합니다.
    - [Q-Net](https://www.q-net.or.kr/): 국가자격 종목과 시험 관련 정보를 확인할 수 있습니다.

    **데이터 안내:** 현재 앱의 직업 목록과 설명은 위 공식 사이트의 정보 항목 및 직업 분류를 참고해 탐색용으로 직접 구성한 예시 데이터입니다. 실시간 API 호출이나 개인 맞춤형 적성검사는 포함하지 않습니다. 직업별 최신 자격·전망·학과 정보는 반드시 공식 사이트에서 재확인하세요.
    """)
st.caption("진로 나침반 · 탐색은 넓게, 선택은 천천히.")
