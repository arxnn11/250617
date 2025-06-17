import streamlit as st
import random

st.set_page_config(page_title="간호 퀴즈 앱", layout="centered")
st.title("🩺 간호 실습생 퀴즈 앱")
st.markdown("실습 전 지식을 점검해보세요!")

# ==== 퀴즈 데이터 (간단한 예시) ====
QUIZ_DATA = {
    "기본간호학": [
        {
            "question": "체온 측정 부위 중 가장 정확한 부위는?",
            "options": ["액와", "입", "직장", "이마"],
            "answer": "직장",
            "explanation": "직장 체온은 중심체온과 가장 근접하여 정확도가 높습니다."
        },
        {
            "question": "체위 중 호흡곤란 환자에게 가장 적합한 것은?",
            "options": ["앙와위", "측위", "좌위", "반좌위"],
            "answer": "반좌위",
            "explanation": "반좌위는 횡격막을 내려 호흡을 용이하게 합니다."
        }
    ],
    "내과간호학": [
        {
            "question": "당뇨병 환자의 식전 정상 혈당 수치는?",
            "options": ["60-90 mg/dL", "70-100 mg/dL", "90-140 mg/dL", "100-160 mg/dL"],
            "answer": "70-100 mg/dL",
            "explanation": "공복 시 혈당 정상 범위는 70-100 mg/dL입니다."
        },
        {
            "question": "심부전 환자 간호 중 우선순위는?",
            "options": ["수분 섭취 증가", "운동 제한", "이뇨제 투여", "염분 섭취 증가"],
            "answer": "이뇨제 투여",
            "explanation": "체액 과다를 줄이기 위한 이뇨제 투여가 우선입니다."
        }
    ]
}

# ==== 사용자 선택 ====
category = st.selectbox("🧪 퀴즈 카테고리 선택", list(QUIZ_DATA.keys()))
quiz_list = QUIZ_DATA[category]
random.shuffle(quiz_list)

st.markdown("---")

# ==== 퀴즈 진행 ====
score = 0
user_answers = []

for idx, item in enumerate(quiz_list):
    st.subheader(f"❓ 문제 {idx + 1}: {item['question']}")
    user_choice = st.radio(
        label="정답을 선택하세요:",
        options=item["options"],
        key=f"q{idx}"
    )
    user_answers.append((item, user_choice))
    st.markdown("--
