import streamlit as st
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
from dotenv import load_dotenv
import os
from openai import AsyncOpenAI
# from whatsapp_sender import send_whatsapp_message
import asyncio
# from get_data import get_all_complaints_data
from post_data import post_complete_data_to_sheet
from get_data import get_all_students_data_from_sheet
from instructions import registration_agent_instructions
# from whatsapp_sender import send_complaint_to_staff
load_dotenv()
set_tracing_disabled(True)

API_KEY = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

InnovistaCare = Agent(
    name="Registration Clerk Agent",
    instructions=registration_agent_instructions,
    model=model,
    tools=[post_complete_data_to_sheet,get_all_students_data_from_sheet],
)

# Streamlit App 
st.title("🎓 University Registration Agent")

st.markdown("""
###
Welcome to the official digital assistant for University registrations!

This smart assistant helps our registration clerk manage and record student data efficiently — from names, departments, fees, and more. Whether it's a new admission or an update, type the details and let the agent handle the rest.
###
""")

prompt = st.text_area("📝 Enter Student Registration Details:")

if "history" not in st.session_state:
    st.session_state.history = []

if st.button("📨 Submit Registration"):
    with st.spinner("Submitting student details, please wait..."):
        st.session_state.history.append({"role": "user", "content": prompt})

        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        result = loop.run_until_complete(
            Runner.run(
                starting_agent=InnovistaCare,
                input=st.session_state.history
            )
        )

        prompt = ""
        st.session_state.history.append({"role": "assistant", "content": result.final_output})

        st.success("Reply from Registration Assistant:")
        st.write(result.final_output)
