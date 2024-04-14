import streamlit as st
from backend.jobSearcher import JobSearcher

class JobPortal:

    @staticmethod
    def Job_Suggestion():
        try:
            JOB_HTML_TEMPLATE = """
            <div style="width:100%;height:100%;margin:1px;padding:5px;position:relative;border-radius:5px;border-bottom-right-radius: 10px;
            box-shadow:0 0 1px 1px #eee; background-color: #31333F;
            border-left: 5px solid #6c6c6c;color:white;">
            <h4>Title: {}</h4>
            <h4>Company: {}</h4>
            <h5>Location: {}</h5>
            <h6>Plateform: {}</h6>
            </div>
            """

            st.title("CareerCraft Jobs Suggestions")
            # Nav Search Form
            with st.form(key='searchform'):
                nav1, nav2, nav3 = st.columns([3, 2, 1])

                with nav1:
                    query = st.text_input("Enter your job search query:", "data analyst Pakistan")
                with nav2:
                    total_jobs = st.slider("Select total number of jobs to display:", 1, 50, 10)

                with nav3:
                    st.text("Search ")
                    submit_search = st.form_submit_button(label='Search')

            

            # Results
            col1, col2 = st.columns([2, 1])

            with col1:
                if submit_search:
                    # Create Search Query
                    st.success("You searched for {}".format(query, total_jobs))
                    with st.spinner('Loading...'):
                        data = JobSearcher.scrape_jobs(query, total_jobs)
                    
                    for i, row in data.iterrows():
                        st.markdown(JOB_HTML_TEMPLATE.format(row['Title'], row['Company'], row['Location'], row['Source']),
                                    unsafe_allow_html=True)

                        # Description
                        with st.expander("Description"):
                            description_content = row['Description']
                            st.write(description_content)

                        # How to Apply
                        with st.expander("How To Apply"):
                            st.write("Job Link:", row['Link'])
                    if data.empty:
                        st.error(f"{query} is not available")

            with col2:
                with st.form(key='email_form'):
                    st.write("Be the first to get new jobs info")
                    email = st.text_input("Email")

                    submit_email = st.form_submit_button(label='Subscribe')

                    if submit_email:
                        st.success("A message was sent to {}".format(email))
        except Exception as e:
            st.error("An error occurred. Please try again later.")
