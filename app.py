import streamlit as st
from screenshot_analyzer import analyze_app_screenshots
import os

st.title('App Store Screenshot Analyzer')

st.write("""
Enter an App Store URL to analyze its screenshots and generate a report.
Example: https://apps.apple.com/us/app/instagram/id389801252
""")

url = st.text_input('App Store URL')

if st.button('Analyze Screenshots'):
    if url:
        try:
            st.info('Analyzing screenshots... Please wait.')
            output_file = analyze_app_screenshots(url)
            
            if os.path.exists(output_file):
                with open(output_file, 'rb') as f:
                    st.download_button(
                        'Download Analysis Report',
                        f,
                        file_name='screenshot_analysis.pdf',
                        mime='application/pdf'
                    )
            else:
                st.error('Failed to generate report.')
        except Exception as e:
            st.error(f'Error: {str(e)}')
    else:
        st.warning('Please enter an App Store URL')
