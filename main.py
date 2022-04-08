import streamlit as st
from topheadlines import topheadlines

top_head_lines_1 = topheadlines()

# bring the menu
st.title("This is our News App")


def initiate_sidebar_radio_button_options():
    with st.sidebar:
        add_radio = st.radio(
            "Filter News by: ",
            ("Top World Headlines", "Sources", "Any News")
        )
    return add_radio


option = initiate_sidebar_radio_button_options()
if option == "Top World Headlines":
    country_selected = st.selectbox("Select a country", options=top_head_lines_1.countries_of_the_world)
    top_head_lines_1.set_country(country_selected)
    top_head_lines_1.get_world_api_request()
    st.write(top_head_lines_1.get_articles_world())
    #if country_selected:
        #st.write("You have selected: " + country_selected)
        #articles = top_head_lines_1.show_article()
        #st.write(articles)

elif option == "Sources":
    st.write("This is sources still a work in progress")
elif option == "Any News":
    st.write("This is any news, but it is still a work in progress")
