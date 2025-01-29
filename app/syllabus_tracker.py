import sqlite3
import streamlit as st
import os
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
syllabus_path = os.path.join(current_dir, "..", "data", "syllabus.csv")

def load_syllabus():
    """Load the syllabus from the CSV file."""
    try:
        syllabus = pd.read_csv(syllabus_path)
        # Normalize column names
        syllabus.columns = syllabus.columns.str.strip().str.lower()
        syllabus.rename(columns={"topic id": "topic_id", "topic": "topic_name"}, inplace=True)
        syllabus['completed'] = syllabus['completed'].map({'yes': True, 'no': False})
        return syllabus
    except FileNotFoundError:
        st.error(f"File not found: {syllabus_path}")
        return pd.DataFrame(columns=["topic_id", "subject", "topic_name", "completed"])

def save_syllabus(syllabus):
    """Save the updated syllabus back to the CSV file."""
    syllabus['completed'] = syllabus['completed'].map({True: 'yes', False: 'no'})  # Convert boolean to yes/no
    syllabus.to_csv(syllabus_path, index=False)

def syllabus_tracker():
    """Display and manage the syllabus."""
    st.subheader("Syllabus Tracker")

    # Load the syllabus
    syllabus = load_syllabus()

    # Check if syllabus is empty
    if syllabus.empty:
        st.warning("No syllabus data available. Please check the syllabus file.")
        return

    # Display the syllabus and allow marking topics as completed
    for index, row in syllabus.iterrows():
        is_completed = st.checkbox(f"{row['topic_name']} ({row['subject']})", value=row['completed'])
        syllabus.at[index, 'completed'] = is_completed

    # Save progress
    if st.button("Save Progress"):
        save_syllabus(syllabus)
        st.success("Progress saved!")