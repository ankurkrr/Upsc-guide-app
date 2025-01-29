import sys
import os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

print("Current Python Path:")
for path in sys.path:
    print(path)

import streamlit as st
from app.syllabus_tracker import syllabus_tracker
from app.timetable_tracker import timetable_tracker
from app.youtube_tracker import youtube_tracker
from app.study_tracker import study_hours_log
import datetime

# Add parent directory to sys.path

# App title
st.title("UPSC Preparation Tracker")
st.sidebar.header("Navigation")

# Sidebar navigation
option = st.sidebar.selectbox("Choose an option", ["Syllabus Tracker", "Timetable Tracker", "Study Hours Log", "YouTube Study Tracker"])
import streamlit as st
from app.syllabus_tracker import syllabus_tracker


# Option logic
if option == "Syllabus Tracker":
    syllabus_tracker()

elif option == "Timetable Tracker":
    timetable_tracker()

elif option == "YouTube Study Tracker":
    youtube_tracker()s


elif option == "Study Hours Log":
    study_hours_log()