import streamlit as st
import datetime
import pandas as pd
import matplotlib.pyplot as plt

STUDY_LOG_FILE = "data/study_log.txt"


def load_study_log():
    """Loads the study log."""
    try:
        # Read the file, assuming two columns: date and hours
        study_log = pd.read_csv("data/study_log.txt", names=["date", "hours"])
        if study_log.empty:
            print("Debug: Study log is empty.")
            return pd.DataFrame(columns=["date", "hours"])  # Return an empty DataFrame
        return study_log
    except FileNotFoundError:
        print("Debug: Study log file not found.")
        return pd.DataFrame(columns=["date", "hours"])  # Return an empty DataFrame if the file is missing


def save_study_log(date, hours):
    """Saves study hours to the log file."""
    with open(STUDY_LOG_FILE, "a") as log_file:
        log_file.write(f"{date},{hours}\n")


def study_hours_log():
    """Logs and visualizes study hours."""
    st.subheader("Study Hours Log")
    date = st.date_input("Date", value=datetime.date.today())
    hours = st.number_input("Hours Studied", min_value=0.0, max_value=24.0, step=0.5)

    if st.button("Log Hours"):
        save_study_log(date, hours)
        st.success("Study hours logged!")

    # Load and display study log
    study_log = load_study_log()
    if not study_log.empty:
        st.write("Study Log:")
        st.write(study_log)

def study_hours_log():
    """Logs and visualizes study hours."""
    st.subheader("Study Hours Log")

    # Load the study log
    study_log = load_study_log()

    # Debugging: Display the loaded DataFrame
    st.write("Debug: Loaded study log")
    st.write(study_log)

    if study_log.empty:
        st.warning("No study log data available.")
        return

    # Ensure data validation
    study_log["hours"] = pd.to_numeric(study_log["hours"], errors="coerce")  # Convert hours to numeric
    study_log.dropna(subset=["hours"], inplace=True)  # Remove rows with invalid hours
    study_log["date"] = pd.to_datetime(study_log["date"], errors="coerce")  # Convert date to datetime
    study_log.dropna(subset=["date"], inplace=True)  # Remove rows with invalid dates

    # Debugging: Display the cleaned DataFrame
    st.write("Debug: Cleaned study log")
    st.write(study_log)

    if not study_log.empty:
        # Visualize study hours
        st.write("Study Hours Over Time:")
        fig, ax = plt.subplots()
        study_log.groupby("date")["hours"].sum().plot(kind="bar", ax=ax)
        st.pyplot(fig)
    else:
        st.warning("No valid data available to plot.")
