import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(page_title="Physical Therapy Student Daily Routine", layout="wide")

# Title of the app
st.title("Day in the Life of a Physical Therapy Student")

# Sidebar for User Input
st.sidebar.header("Student's Daily Schedule")

# Time Input: Start time of the day
start_time = st.sidebar.time_input("Start Time", value=pd.to_datetime("08:00:00").time())
session_duration = st.sidebar.slider("Session Duration (minutes)", min_value=10, max_value=180, value=60)

# Number of clinical hours today
num_clinical_sessions = st.sidebar.number_input("Number of Clinical Sessions Today", min_value=1, max_value=5, value=2)

# Example data for clinical sessions
clinical_sessions = [
    {
        "Patient Name": "Zehra",
        "Condition": "Chronic lower back pain",
        "Treatment Type": "Massage and Stretching"
    },
    {
        "Patient Name": "Huda",
        "Condition": "Post-spinalcord surgery rehabilitation",
        "Treatment Type": "Strengthening and Manual Therapy"
    }
]

# Daily Study Tasks Section
st.sidebar.header("Study Tasks")
study_tasks = [
    {
        "Task Name": "Review Anatomy",
        "Duration (minutes)": 60
    },
    {
        "Task Name": "Study Physical Therapy Techniques",
        "Duration (minutes)": 90
    },
    {
        "Task Name": "Prepare for Case Study Presentation",
        "Duration (minutes)": 60
    }
]

# Main content
st.header("Today's Schedule")

# Create a DataFrame to show the student's schedule (clinical and study sessions)
clinical_data = pd.DataFrame(clinical_sessions)
study_data = pd.DataFrame(study_tasks)

# Create a simple timeline of the day
timeline = []

# Add clinical sessions to the timeline
current_time = pd.to_datetime(f"2023-03-08 {start_time}")
for i, session in enumerate(clinical_sessions):
    timeline.append({
        "Time": current_time.strftime("%H:%M"),
        "Activity": f"Clinical Session with {session['Patient Name']} ({session['Treatment Type']})"
    })
    current_time += pd.Timedelta(minutes=session_duration)

# Add study tasks to the timeline
for task in study_tasks:
    timeline.append({
        "Time": current_time.strftime("%H:%M"),
        "Activity": f"Study: {task['Task Name']} ({task['Duration (minutes)']} min)"
    })
    current_time += pd.Timedelta(minutes=task["Duration (minutes)"])

# Display the timeline of the day
timeline_df = pd.DataFrame(timeline)
st.subheader("Today's Timeline")
st.dataframe(timeline_df)

# Additional Insights
st.subheader("Student Reflection & Goals")
st.write("At the end of the day, reflect on your progress, challenges, and any learning moments.")
reflection = st.text_area("Reflection What did you learn today? What challenges did you face?")

# Set a goal for tomorrow
goal_for_tomorrow = st.text_input("Goal for Tomorrow", "Improve manual therapy techniques or complete a review of anatomy.")
st.write(f"Your goal for tomorrow is: {goal_for_tomorrow}")

# Footer
st.markdown("\n*Powered by Streamlit* 🚀")
