import streamlit as st
import random

# 앱 설정
st.set_page_config(page_title="간호 퀴즈 앱", layout="centered")
st.title("🩺 간호 실습 퀴즈 앱")
st.caption("기초 지식 점검을 위한 간단한 퀴즈 앱입니다.")

# 퀴즈 데이터 정의
quiz_data = {
    "기본간호학": [
        {
            "question": "체온 측정 부위 중 가장 정확한 부위는?",
            "options": ["입", "액와", "직장", "이마"],
            "answer": "직장",
            "explanation": "직장은 중심체온과 가장 가까워 정확도가 높습니다."
        },
        {
            "question": "호흡곤란 환자에게 가장 적절한 체위는?",
            "options": ["앙와위", "측위", "반좌위", "복위"],
            "answer": "반좌위",
            "explanation": "반좌위는 횡격막을 내려 호흡을 도와줍니다."
        }
    ],
    "내과간호학": [
        {
            "question": "공복 시 정상 혈당 수치는?",
            "options": ["60-90 mg/dL", "70-100 mg/dL", "90-140 mg/dL", "100-160 mg/dL"],
            "answer": "70-100 mg/dL",
            "explanation": "공복 시 정상 혈당은 70-100 mg/dL입니다."
        },
        {
            "question": "심부전 간호에서 우선 간호는?",
            "options": ["수분 섭취 증가", "염분 섭취 증가", "운동 권장", "이뇨제 투여"],
            "answer": "이뇨제 투여",
            "explanation": "심부전은 체액 과다를 유발하므로 이뇨제가 필요합니다."
        }
    ]
}

# 카테고리 선택
category = st.selectbox("🧪 퀴즈 카테고리를 선택하세요:", list(quiz_data.keys()))
questions = quiz_data[category]
random.shuffle(questions)

# 정답 기록
user_answers = []
score = 0

st.markdown("---")

# 퀴즈 문제 출력
for idx, q in enumerate(questions):
    st.subheader(f"❓ 문제 {idx+1}: {q['question']}")
    choice = st.radio("선택하세요:", q["options"], key=f"q{idx}")
    user_answers.append((q, choice))
    st.markdown("---")

# 결과 확인
if st.button("📊 결과 확인"):
    st.subheader("📋 퀴즈 결과")
    for idx, (q, user_choice) in enumerate(user_answers):
        is_correct = user_choice == q["answer"]
        st.write(f"**문제 {idx+1}: {q['question']}**")
        st.write(f"👉 당신의 답: `{user_choice}`")
        if is_correct:
            st.success("✅ 정답입니다!")
            score += 1
        else:
            st.error(f"❌ 오답입니다. 정답: `{q['answer']}`")
        st.info(f"💡 해설: {q['explanation']}")
        st.markdown("---")

    st.subheader("🏁 총 점수")
    percent = score / len(questions) * 100
    st.write(f"{len(questions)}문제 중 {score}문제 정답 (정답률 {percent:.0f}%)")
    st.progress(percent / 100)
    if percent == 100:
        st.balloons()
        st.success("🎉 완벽해요! 실습 준비 완료!")
    elif percent >= 70:
        st
