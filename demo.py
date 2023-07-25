import streamlit as st

# Check if 'queue_counter' is already in the session state
if 'queue_counter' not in st.session_state:
    st.session_state.queue_counter = 1  # Initialize queue_counter to 1 if not present

# Title of the event
st.title('Registration for Event ABC')

# Description
st.write("""
Kindly click the button below to register for the event.
The event is limited to 10 pax.
""")

# Check if the queue counter exceeds the limit
if st.session_state.queue_counter <= 10:

    if st.button('Generate Latest Queue Number'):
        registration_link = f"https://form.gov.sg/64bfbe8bf8b1ef0011d9a0df?64bfbebb7b53ad0011459dde={st.session_state.queue_counter}"
        
        # Using markdown to style the link as a button and display the queue counter without target="_blank"
        button_code = f'<a href="{registration_link}" target="_blank" style="padding: 10px 20px; background-color: #FF2E63; color: white; border-radius: 4px; text-decoration: none;">Register</a>'
        st.markdown(button_code, unsafe_allow_html=True)
        
        st.write(f"Queue Number: {st.session_state.queue_counter}")

        # Increment the queue counter for the next person
        st.session_state.queue_counter += 1

else:
    st.write("""
    Due to overwhelming response, the event has been fully registered.
    You may email to [abc@gov.sg](mailto:abc@gov.sg) to check if there are any more vacancies for the event.
    """)