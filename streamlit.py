import streamlit as st

# Title of the application
st.title("My Streamlit App")

# Header
st.header("Welcome to my app!")

# Subheader
st.subheader("Here's a sample code snippet:")

# Code block
code = """
def greet(name):
    print(f"Hello, {name}!")

greet("Streamlit")
"""
st.code(code, language="python")


st.code(code, language="python")


# Display an image
image_url = "https://via.placeholder.com/400"
st.image(image_url, caption="Sample Image", use_column_width=True)

# Markdown text
st.markdown("You can use **Markdown** syntax to format your text.")

# Sidebar
st.sidebar.header("Sidebar")
selected_option = st.sidebar.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])
st.sidebar.write("You selected:", selected_option)

# Data
data = [1, 2, 3, 4, 5]
st.line_chart(data)

# Interactive widgets
number = st.number_input("Enter a number", min_value=0, max_value=100, value=50)
st.write("The number you entered is:", number)

# Button
if st.button("Click me"):
    st.write("Button clicked!")
st.table(data)
