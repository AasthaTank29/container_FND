import streamlit as st

# Define the CSS style for the horizontal sticky box
css = """
<style>
.horizontal-sticky {
    position: -webkit-sticky; /* Safari */
    position: sticky;
    top: 0; /* Stick to the top of the viewport */
    z-index: 1000; /* Ensure the box is above other content */
    width: 100%;
    background-color: #f9f9f9;
    overflow-x: auto; /* Allow horizontal scrolling */
    white-space: nowrap; /* Prevent text wrapping */
}
.horizontal-sticky div {
    display: inline-block; /* Display elements in a row */
    padding: 10px; /* Add padding to the elements */
    border: 1px solid #ccc; /* Add a border to the elements */
}
</style>
"""

# Render the CSS style
st.markdown(css, unsafe_allow_html=True)

# Render the horizontal sticky box
st.markdown("""
<div class="horizontal-sticky">
    <div>Item 1</div>
    <div>Item 2</div>
    <div>Item 3</div>
    <div>Item 4</div>
    <div>Item 5</div>
    <div>Item 6</div>
</div>
""", unsafe_allow_html=True)

# Add some content to make the page scrollable
for i in range(50):
    st.write(f"Scrollable content {i}")
