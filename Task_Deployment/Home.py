import streamlit as st
import os
# This is the main streamlit app file
print(os.system('pwd'))

st.set_page_config(page_title='Discovering the Relationship Between Crime Statistics and Weather in the Houston Area', layout = 'wide')


st.title('Discovering the Relationship Between Crime Statistics and Weather in the Houston Area')

st.title("Mission and Vision Statements")
mission_statement = """
Mission:
- Promote real-world AI through running open-source projects
- Provide case study-based education
- Provide AI services to local AI enthusiasts and businesses around the world
- Host offline events
"""

vision_statement = """
Vision:
- Collaborate
- Network
- Deliver
"""
st.markdown(mission_statement, unsafe_allow_html=True)
st.markdown(vision_statement, unsafe_allow_html=True)
st.markdown(
'''
## [Omdena  Houston, USA Chapter](https://omdena.com/chapter-challenges/discover-the-relationship-between-crime-statistics-and-weather-in-the-houston-area/)
'''
)




