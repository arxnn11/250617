import streamlit as st

# 페이지 선택
st.sidebar.title("🩺 간호 웹 도구")
page = st.sidebar.radio("기능 선택", ["🧾 환자 상태 평가", "💊 약물 계산기"])

# ===== PAGE 1: 환자 상태 평가 도구 =====
if page == "🧾 환자 상태 평가":
    st.title("🧾 환자 상태 평가 도구 (MEWS 기반)")

    st.subheader("🧍 환자 Vital Sign 입력")
    temp = st.number_input("체온 (℃)", min_value=30.0, max_value=43.0, step=0.1)
    rr = st.number_input("호흡수 (회/분)", min_value=0, max_value=60, step=1)
    hr = st.number_input("심박수 (회/분)", min_value=0, max_value=200, step=1)
    sbp = st.number_input("수축기 혈압 (mmHg)", min_value=50, max_value=250, step=1)
    avpu = st.selectbox("의식 수준 (AVPU)", ["Alert", "Voice", "Pain", "Unresponsive"])

    # MEWS 점수 계산 함수
    def calc_mews(temp, rr, hr, sbp, avpu):
        score = 0
        # 호흡수
        if rr <= 8 or rr >= 30: score += 3
        elif rr >= 21: score += 2
        elif rr <= 14: score += 0
        else: score += 1
        # 심박수
        if hr <= 40 or hr >= 130: score += 3
        elif 111 <= hr <= 129: score += 2
        elif 101 <= hr <= 110: score += 1
        elif 51 <= hr <= 100: score += 0
        else: score += 1
        # 혈압
        if sbp <= 70: score += 3
        elif sbp <= 80: score += 2
        elif sbp <= 100: score += 1
        elif sbp <= 199: score += 0
        else: score += 2
        # 체온
        if temp < 35 or temp > 38.5: score += 2
        else: score += 0
        # AVPU
        if avpu != "Alert": score += 3
        return score

    if st.button("📊 MEWS 점수 계산"):
        score = calc_mews(temp, rr, hr, sbp, avpu)
        st.success(f"✅ 총 MEWS 점수: **{score}점**")
        if score >= 5:
            st.error("🚨 중증 위험! 즉시 의사에게 보고 필요.")
        elif score >= 3:
            st.warning("⚠️ 주의 요망. 모니터링 강화 필요.")
        else:
            st.info("🟢 안정 상태")

# ===== PAGE 2: 약물 계산기 =====
elif page == "💊 약물 계산기":
    st.title("💊 약물 용량 및 주입 속도 계산기")

    st.subheader("1️⃣ 체중 기반 용량 계산")
    dose_mg_per_kg = st.number_input("용량 (mg/kg)", min_value=0.0)
    weight = st.number_input("환자 체중 (kg)", min_value=0.0)
    if st.button("💉 용량 계산"):
        total_dose = dose_mg_per_kg * weight
        st.success(f"총 투여 용량: **{total_dose:.2f} mg**")

    st.subheader("2️⃣ 점적수 계산기")
    volume = st.number_input("총 수액량 (ml)", min_value=0.0)
    time_hr = st.number_input("투여 시간 (시간)", min_value=0.1)
    drop_factor = st.selectbox("점적 수 (gtt/ml)", [10, 15, 20, 60])

    if st.button("⏱️ 점적수 계산"):
        flow_rate = volume / time_hr
        drops_per_min = (volume * drop_factor) / (time_hr * 60)
        st.info(f"💧 주입 속도: **{flow_rate:.1f} ml/hr**")
        st.success(f"🔢 점적수: **{drops_per_min:.1f} gtt/min**")

