import streamlit as st
import matplotlib.pyplot as plt
from datetime import date
from assistant.thread_manager import get_or_create_thread
from assistant.functions import add_expense_fn, get_summary_fn, get_weekly_stats_fn
from utils.config import ASSISTANT_ID

st.title("AI Personal Finance Tracker")

# --- User identification ---
user_email = st.text_input("Enter your email:")

if user_email:
    thread_id = get_or_create_thread(user_email)
    st.write(f"Your session thread: {thread_id}")

    # --- Expense form ---
    with st.form("add_expense_form"):
        category = st.text_input("Category (groceries, transport, etc.)")
        amount = st.number_input("Amount", min_value=0.0)
        expense_date = st.date_input("Date", value=date.today())
        submitted = st.form_submit_button("Add Expense")
        if submitted:
            result = add_expense_fn({
            "email": user_email,
            "category": category,
            "amount": amount,
            "date": expense_date,
            "thread_id" : thread_id
            })
            st.success(result["message"])


    # --- Chat with assistant (placeholder for function calling integration) ---
    user_message = st.text_input("Ask your finance assistant anything:")
    if user_message:
        assistant_response = get_summary_fn({"email": user_email,"thread_id":thread_id,"user_message":user_message,"ASSISTANT_ID":ASSISTANT_ID})
        # TODO: Call OpenAI assistant with thread_id and function calling
        st.write(f"Assistant response for: {assistant_response}")

    # --- Weekly stats visualization ---
    weekly_data = get_weekly_stats_fn({"email": user_email})
    if weekly_data:
        weeks = list(weekly_data.keys())
        totals = list(weekly_data.values())

        fig, ax = plt.subplots()
        plt.style.use('seaborn-v0_8')
        ax.scatter(weeks, totals,s=100,c='red',edgecolors='none')
        ax.set_xlabel("Week Number",fontsize=14)
        ax.set_ylabel("Total Spent (₹)",fontsize=14)
        ax.set_title("Weekly Expense Summary",fontsize=24)
        st.pyplot(fig)
    else:
        st.write("No expenses found to plot.")
