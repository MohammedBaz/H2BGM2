from dataclasses import dataclass
from typing import Dict, List, Optional

import folium
import requests
import streamlit as st
from streamlit_folium import st_folium

st.set_page_config(layout="wide")

@st.experimental_singleton
def get_data() -> List[Dict]:
    api_key = st.secrets["api_key"]
    url = f"https://developer.nps.gov/api/v1/parks?api_key={api_key}&limit=500"
    resp = requests.get(url)
    data = resp.json()["data"]
    parks = [park for park in data if park["designation"] == "National Park"]

    for park in parks:
        park["_point"] = Point.from_dict(park)
        
