import streamlit as st

class AddForm:
    def __init__(self): 
        with st.form("add_form"):
            st.write("Inside the form")
            slider_val = st.slider("Form slider")
            checkbox_val = st.checkbox("Form checkbox")

            # Every form must have a submit button.
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.write("slider", slider_val, "checkbox", checkbox_val)


######
class CustomerForm:
    def __init__(self):
        self.first_name = request.form.get('first_name')
        self.last_name = request.form.get('last_name')
        self.city = request.form.get('city')
        self.country = request.form.get('country')
        self.phone = request.form.get('phone')
