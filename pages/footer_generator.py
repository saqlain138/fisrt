# footer_generator.py

def generate_footer_html():
    return """
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
