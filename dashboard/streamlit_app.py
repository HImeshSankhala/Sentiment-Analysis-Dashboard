import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from sentiment_analysis.sentiment import analyze_text

# Streamlit Page Configuration
st.set_page_config(page_title="Sentiment, Emotion & Toxicity Analysis Dashboard", layout="wide")

# Title
st.title("📊 Sentiment, Emotion & Toxicity Analysis Dashboard")

# Sidebar input
st.sidebar.header("User Input")
user_input = st.sidebar.text_area("Enter text for analysis:")

# Sentiment, Emotion & Toxicity Analysis Output
if user_input:
    sentiment_score, sentiment_label, emotions, toxicity_score, toxicity_category = analyze_text(user_input)
    st.subheader("Analysis Result:")
    st.write(f"**Sentiment Score:** {sentiment_score}")
    st.write(f"**Sentiment Label:** {sentiment_label}")
    st.write(f"**Toxicity Score:** {toxicity_score}")
    st.write(f"**Toxicity Category:** {toxicity_category}")

    # Sentiment Score Chart
    fig = px.bar(x=[sentiment_label], y=[sentiment_score], title="Sentiment Score", labels={'x': "Sentiment", 'y': "Score"})
    fig.update_traces(marker_color="red")
    st.plotly_chart(fig, use_container_width=True)

    # Emotion Breakdown Chart
    if emotions:
        st.subheader("Emotion Breakdown")
        fig_emotion = px.bar(x=list(emotions.keys()), y=list(emotions.values()), title="Emotion Analysis")
        fig_emotion.update_traces(marker_color="blue")
        st.plotly_chart(fig_emotion, use_container_width=True)

    # Toxicity Score Chart
    st.subheader("Toxicity Analysis")
    fig_toxicity = px.bar(x=[toxicity_category], y=[toxicity_score], title="Toxicity Score", labels={'x': "Toxicity Category", 'y': "Score"})
    fig_toxicity.update_traces(marker_color="green" if toxicity_category == "Safe" else "red")
    st.plotly_chart(fig_toxicity, use_container_width=True)

# File Upload for Batch Processing
st.sidebar.subheader("Upload a CSV File")
uploaded_file = st.sidebar.file_uploader("Upload any CSV file (Choose a text column for analysis)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    selected_column = st.sidebar.selectbox("Select the text column for analysis:", df.columns)

    if selected_column:
        df[["sentiment_score", "sentiment_label", "emotion_analysis", "toxicity_score", "toxicity_category"]] = df[selected_column].apply(analyze_text).apply(pd.Series)

        # Convert emotions dictionary to separate columns
        emotions_df = df["emotion_analysis"].apply(pd.Series).fillna(0)
        df = pd.concat([df, emotions_df], axis=1).drop(columns=["emotion_analysis"], errors='ignore')

        # Display results
        st.subheader("Batch Sentiment, Emotion & Toxicity Analysis Results")
        st.dataframe(df[[selected_column, "sentiment_score", "sentiment_label", "toxicity_score", "toxicity_category"] + list(emotions_df.columns)])

        # Sentiment Distribution Pie Chart
        fig_pie = px.pie(df, names="sentiment_label", title="Sentiment Distribution")
        st.plotly_chart(fig_pie, use_container_width=True)

        # Toxicity Distribution Pie Chart
        fig_toxicity_pie = px.pie(df, names="toxicity_category", title="Toxicity Distribution")
        st.plotly_chart(fig_toxicity_pie, use_container_width=True)

        # Emotion Distribution for Batch Analysis
        if not emotions_df.empty:
            st.subheader("Overall Emotion Distribution")
            emotions_sum = emotions_df.mean()
            fig_emotion_batch = px.bar(x=emotions_sum.index, y=emotions_sum.values, title="Overall Emotion Analysis")
            fig_emotion_batch.update_traces(marker_color="blue")
            st.plotly_chart(fig_emotion_batch, use_container_width=True)

# Footer
st.markdown("---")