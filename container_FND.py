import streamlit as st

# Render a sticky box in the sidebar
with st.sidebar:
    st.markdown("## Sticky Box")
    st.markdown("This box remains sticky even when the page is scrolled.")

# Add some content to make the page scrollable
for i in range(50):
    st.write(f"Scrollable content {i}")
