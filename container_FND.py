import streamlit as st

# Define the CSS style for the sticky box
css = """
<style>
.sticky {
    position: -webkit-sticky; /* Safari */
    position: sticky;
    top: 20px; /* Adjust this value to change the distance from the top */
    border: 1px solid #ccc;
    padding: 10px;
    background-color: #f9f9f9;
}
</style>
"""

# Render the CSS style
st.markdown(css, unsafe_allow_html=True)

# Render the sticky box
st.markdown('<div class="sticky">This is a sticky box with a border.</div>', unsafe_allow_html=True)

# Add some content to make the page scrollable
for i in range(50):
    st.write(f"Scrollable content {i}")
