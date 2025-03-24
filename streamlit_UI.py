import streamlit as st
import requests
import base64


def main():
    """
    Streamlit UI for company sentiment analysis and Hindi TTS summary.
    Accepts user input, sends request to FastAPI backend, and displays the result.
    """
    st.title("Company Sentiment Analyzer with Hindi TTS")
    company = st.text_input("Enter Company Name", "Tesla")

    if st.button("Analyze News"):
        with st.spinner("Collecting news and analyzing..."):
            response = requests.post(
                "http://localhost:8000/analyze/", json={"company": company}
            )
            result = response.json()

            st.subheader("Sentiment Report")
            for article in result["Articles"]:
                st.markdown(f"**Title:** {article['Title']}")
                st.markdown(f"**Summary:** {article['Summary']}")
                st.markdown(f"**Sentiment:** {article['Sentiment']}")
                st.markdown(f"**Topics:** {', '.join(article['Topics'])}")
                st.markdown("---")

            st.subheader("Comparative Analysis")
            st.json(result["Comparative Sentiment Score"])

            st.subheader("Final Sentiment Summary")
            st.write("English Summary:", result["Final Sentiment Analysis (English)"])
            st.write("Hindi Summary:", result["Final Sentiment Analysis (Hindi)"])

            st.subheader("Hindi Speech Output")
            audio_bytes = base64.b64decode(result["Audio"])
            st.audio(audio_bytes, format="audio/wav")


if __name__ == "__main__":
    main()
