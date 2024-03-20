import streamlit as st
from streamlit_option_menu import option_menu

# Sidebar with option menu
with st.sidebar:
    selected = option_menu(
        menu_title="Data Planet",
        options=["📊 Projects", "📁 Folders", "📝 Template", "🔍 Data", "📱 Apps"],
        default_index=0,
    )

# Main content based on selected option
if selected == "📊 Projects":
    st.title("")
elif selected == "📁 Folders":
    st.title("")
elif selected == "📝 Template":
    st.title("")
elif selected == "🔍 Data":
    st.title("")
elif selected == "📱 Apps":
    st.title("")



# Navbar
nav_items = {
    "Partners": "/Partners",
    "shared": "/shared",
    "operations": "/operations",
    "Account": "/Account",
    "Message": "/Message",
    "profile": "/profile",
}

# Define the URL for the new file or section for Partners
partners_url = "pathner.py"  # Replace with the actual URL of the new file

# Generate HTML links for navbar items
nav_links = ''.join(f'<a href="{url}">{label}</a>' for label, url in nav_items.items())

navbar_template = f"""
    <style>
        .navbar {{
          
            display: flex;
            justify-content: center;
            align-items: center;
            width: 50%; 
            padding: 10px 0px; 
            margin: 0;
            position: fixed; 
            top: 39px; 
            z-index: 999;
        }}

        .navbar a {{
            color: #0000FF;
            
            text-align: center;
            text-decoration: none;
            font-size: 17px;
            padding: 14px 20px;
            margin-right: 50px; /* Add margin to the right side of each link */
        }}

        .navbar a:hover {{
            background-color: #ddd;
            color: black;
        }}
    </style>
    <div class="navbar">
        {nav_links}
    </div>
"""

st.markdown(navbar_template, unsafe_allow_html=True)

# Footer
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

