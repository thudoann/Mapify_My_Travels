import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Visited Countries Map", layout="wide")

# Load country list from Plotly dataset
df = px.data.gapminder().query("year == 2007")
all_countries = df['country'].unique().tolist()

# Custom styling
st.markdown("""
<style>
body {
    background-color: #f6f9fc;
}
h1, h2, h3 {
    color: #2c3e50;
    font-family: 'Poppins', sans-serif;
    text-align: center;
}
.stMultiSelect, .stButton, .stPlotlyChart {
    border-radius: 12px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.stPlotlyChart {
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

st.title("🌎✨ Countries I've Visited")


st.markdown("""
<p style='font-size:18px;'>Select the countries you’ve visited and see them highlighted beautifully on the world map! 🌍✨</p>
""", unsafe_allow_html=True)

visited_countries = st.multiselect(
    "✨ Start typing and select the countries you've visited:",
    options=sorted(all_countries),
    help="Choose from the list and your map will update instantly."
)

# Add a dataframe column indicating visited or not
df['visited'] = df['country'].apply(lambda x: 1 if x in visited_countries else 0)

# Create a more elegant map
fig = px.choropleth(
    df,
    locations="iso_alpha",
    color="visited",
    hover_name="country",
    color_continuous_scale=[[0, '#f0f0f0'], [1, '#ffff77']], 
    range_color=(0, 1),
    projection="natural earth",
    title="🌍 Your Travel Footprint",
    template="plotly_white"
)

fig.update_layout(
    coloraxis_showscale=False,
    geo=dict(
        showframe=False,
        showcoastlines=True,
        landcolor='#f0f2f6',
        projection_scale=0.95
    ),
    margin=dict(l=0, r=0, t=50, b=0),
    font=dict(family="Poppins, sans-serif", size=14),
    title_x=0.5
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("""<p style='text-align: center; color: #95a5a6;'>Made with ❤️ by Thudoann</p>""", unsafe_allow_html=True)
