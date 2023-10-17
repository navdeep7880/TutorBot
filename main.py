# Importing dependencies

import streamlit as st
from streamlit_chat import message
from bardapi import Bard
import json

# Reading the JSON file to fetch credentials
token = '******' #you can use your own code



# Funtion that generates and returns the response
def generate_response(prompt):
    bard = Bard(token=token)
    response = bard.get_answer(prompt)
    return response['content']


#function to recieve queries

def get_text():
    input_text = st.text_input("You: ", "Hey bot!", key="input")
    return input_text
# Main function

st.title("🤖Personal Tutoring! By Lakhan Gupta")

changes = '''
<style>
[data-testid="stAppViewContainer"]
{
background-image:url('https://images.unsplash.com/photo-1501389683017-9f916b4671b0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80');
background-size:cover;
}

</style>
'''

    # Pushing changes to the UI
st.markdown(changes, unsafe_allow_html=True)
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# Get text from the input field


user_input = get_text()

if user_input:
    print(user_input)
    output = generate_response(user_input)
    print(output)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)


if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        print(st.session_state["generated"], i)
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')


