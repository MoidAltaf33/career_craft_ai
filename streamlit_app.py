# Frontend Framework
import streamlit as st
from streamlit_option_menu import option_menu

# From files
from Frontend.home_page import home as HP 
from Frontend.instruction_page import Instruction as Ins
from Frontend.ats_page import Ats_page as ats
from Frontend.job_portal import JobPortal as JP
from Frontend.about import About_section as Ab_sec

# File Path
image_path = r"assets/logo/Colorlogo.png"




def main():
    """    Main function to control the application flow.

    This function sets the page configuration to a wide layout and hides the menu and footer. It then checks the session state for a switch button and updates the menu option accordingly. It then displays an option menu in the sidebar and based on the selected option, it calls different functions to display the corresponding content. It also includes a button to navigate to the next page and a footer note.
    """

    st.set_page_config(layout="wide")
    hide_menu = """
        <style>
        #MainMenu {visibility:hidden;}
        footer {visibility:hidden;}
        </style>
        """
    st.markdown(hide_menu, unsafe_allow_html=True)
    
    if st.session_state.get('switch_button', False):
        st.session_state['menu_option'] = (st.session_state.get('menu_option', 0) + 1) % 5
        manual_select = st.session_state['menu_option']
    else:
        manual_select = None
    
    selected_main = option_menu( None , ["Home","Instruction","ATS Analyzer","Job Portal","About"],
        icons=[ 'house','folder','cloud', 'person','gear'], 
        orientation="horizontal", manual_select=manual_select, key='menu_4')

    with st.sidebar:
        st.image(image_path) 

    if selected_main == "Home":
        HP.home_page()
    if selected_main == "Instruction":
        Ins.instruction()
    elif selected_main == "ATS Analyzer":
        ats.resume_parser()
    elif selected_main == "Job Portal":
        JP.Job_Suggestion()
    elif selected_main == "About":
        Ab_sec.About_Section()

    # Create an empty space to center the button horizontally
    col1, col2, col3 = st.columns([7, 5, 5])

    # Place the button inside the middle column
    with col2:
        st.button(f"Next Page", key='switch_button')
    # Footer note
    footer_html = """
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: -9px;
            width: 100%;
            background-color: #262730;
            display:flex;
            flex-direction: column;
            align-items:center;
        }
        .footer b{
            color: #FF4B4B;
            font-size: 20px;
        }
    </style>
    <div class="footer">
        <b>CareerCraft AI</b>
        <p>Copyright © 2024 DataDrive Innovator, Inc.</p>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
