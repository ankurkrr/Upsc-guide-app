import streamlit as st
from utils.nlp_utils import extract_upsc_keywords
from utils.stopwatch import Stopwatch  # Absolute import for Stopwatch

def youtube_tracker():
    """Tracks YouTube videos and extracts UPSC-related keywords."""
    st.subheader("YouTube Study Tracker")

    video_url = st.text_input("Enter YouTube Video URL:")
    if st.button("Start Tracking"):
        st.write("Tracking video play/pause events...")
        stopwatch = Stopwatch()

        # Simulate tracking for demonstration
        st.write("Simulating video play...")
        stopwatch.start()
        st.write("Simulating video pause...")
        stopwatch.stop()

        # Mock caption processing
        captions = "This is a mock caption containing keywords like governance, polity, and biodiversity."
        keywords = extract_upsc_keywords(captions)

        st.write("Keywords extracted from video:")
        st.write(keywords)

        st.success(f"Time spent: {stopwatch.get_time()} seconds")
