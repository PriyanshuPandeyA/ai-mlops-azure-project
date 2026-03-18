import streamlit as st
import requests

# 🔹 Backend URL (UPDATED)
BACKEND_URL = "https://feedback-app.purplesky-636b69a6.westus2.azurecontainerapps.io/predict"

# 🔹 Page Config
st.set_page_config(
    page_title="AI Feedback Analyzer",
    page_icon="📊",
    layout="centered"
)

# 🔹 Title Section
st.markdown("""
# 📊 AI Customer Feedback Analyzer
### Understand your users instantly 🚀
""")

st.divider()

# 🔹 Input Box
text = st.text_area("✍️ Enter customer feedback", height=150)

# 🔹 Button
if st.button("🔍 Analyze Feedback"):

    if text.strip() == "":
        st.warning("⚠️ Please enter some feedback")
    else:
        try:
            with st.spinner("Analyzing... ⏳"):
                res = requests.post(
                    BACKEND_URL,
                    json={"text": text}
                )

                data = res.json()

            st.divider()

            # 🔹 Result Display
            if data["output"] == "positive":
                st.success("😊 Positive Feedback")
            else:
                st.error("😠 Negative Feedback")

            # 🔹 Metrics
            col1, col2 = st.columns(2)

            col1.metric("Model Version", data["model_version"])
            col2.metric("Response Time (sec)", f"{data['response_time']:.4f}")

        except Exception as e:
            st.error("❌ Error connecting to backend")
            st.write(e)

# 🔹 Footer
st.divider()
st.caption("Built with ❤️ using FastAPI + Streamlit + Azure Container Apps")