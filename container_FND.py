import streamlit as st

# Add CSS for the sticky box
st.markdown(
    """
    <style>
    .sticky {
        position: -webkit-sticky; /* Safari */
        position: fixed;
        top: 20px;
        background-color: #f1f1f1;
        border: 1px solid #ddd;
        padding: 10px;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Render the sticky box
st.markdown(
    """
    <div class="sticky">
        This is a sticky box with a border.
    </div>
    """,
    unsafe_allow_html=True
)
