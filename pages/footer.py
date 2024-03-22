import streamlit as st

footer_html = """
<style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #09ab3b ;
        text-align: center;
        padding: 10px;
    }
</style>
<div class="footer">
    <p>This is a Streamlit footer</p>
</div>
"""

st.markdown(footer_html, unsafe_allow_html=True)
