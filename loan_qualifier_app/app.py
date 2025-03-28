import streamlit as st

st.title("Loan Qualifier App")

income = st.number_input("Monthly Income ($):", min_value=0)
debt = st.number_input("Monthly Debt Payments ($):", min_value=0)
credit_score = st.slider("Credit Score:", 300, 850, 650)

if st.button("Check Eligibility"):
    dti = debt / income if income > 0 else 1  # debt-to-income ratio
    if credit_score >= 650 and dti < 0.4:
        st.success("✅ You qualify for the loan!")
    else:
        st.error("❌ You do NOT qualify for the loan.")