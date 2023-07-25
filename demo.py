import streamlit as st

from streamlit.components.v1 import html
def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)


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
    
    if st.button('Register'):

        registration_link = f"https://form.gov.sg/64bfbe8bf8b1ef0011d9a0df?64bfbebb7b53ad0011459dde={st.session_state.queue_counter}"
        on_click=open_page(registration_link)        

        # Increment the queue counter for the next person
        st.session_state.queue_counter += 1

        if st.session_state.queue_counter <= 10:
            st.write(f"Queue Number: {st.session_state.queue_counter}")
        else:
            st.write("""
            Due to overwhelming response, the event has been fully registered.
            You may email to [abc@gov.sg](mailto:abc@gov.sg) to check if there are any more vacancies for the event.
            """)

else:
    st.write("""
    Due to overwhelming response, the event has been fully registered.
    You may email to [abc@gov.sg](mailto:abc@gov.sg) to check if there are any more vacancies for the event.
    """)