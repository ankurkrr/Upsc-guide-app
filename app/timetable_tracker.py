import pandas as pd
import streamlit as st

TIMETABLE_FILE = "data/timetable.csv"

def load_timetable():
    try:
        timetable = pd.read_csv(TIMETABLE_FILE)
        return timetable
    except FileNotFoundError:
        st.error(f"File not found: {TIMETABLE_FILE}")
        return pd.DataFrame(columns=["day", "subject", "time", "topic"])

def timetable_tracker():
    st.subheader("Timetable Tracker")

    # Load timetable
    timetable = load_timetable()

    # Display timetable
    if not timetable.empty:
        st.table(timetable)
    else:
        st.warning("No timetable data available.")

