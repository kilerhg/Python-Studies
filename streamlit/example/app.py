import streamlit as st
import pandas as pd
import numpy as np

apptitle = 'Postech Obesity Predictor'

st.set_page_config(page_title=apptitle, page_icon=":eyeglasses:")


st.title('Obesity Predictor')

st.sidebar.subheader('Input Values')

st.markdown("""
 * Use the menu at left to select data and set plot parameters
 * Your plots will appear below
""")

st.subheader('Results')

st.sidebar.selectbox(
        'Pick a Color',
        [None, 'red', 'orange', 'green', 'blue', 'violet'], args=[3]
    )

high_fs = st.sidebar.checkbox('Full sample rate data')

whiten = st.sidebar.checkbox('Whiten?', value=True)

dtboth = st.sidebar.slider('Time Range (seconds)', 0.1, 8.0, 1.0)  # min, max, default

with st.expander("See notes"):

    st.markdown("""
A Q-transform plot shows how a signal’s frequency changes with time.

 * The x-axis shows time
 * The y-axis shows frequency

The color scale shows the amount of “energy” or “signal power” in each time-frequency pixel.

A parameter called “Q” refers to the quality factor.  A higher quality factor corresponds to a larger number of cycles in each time-frequency pixel.  

For gravitational-wave signals, binary black holes are most clear with lower Q values (Q = 5-20), where binary neutron star mergers work better with higher Q values (Q = 80 - 120).

See also:

 * [GWpy q-transform](https://gwpy.github.io/docs/latest/examples/timeseries/qscan/)
 * [Reading Time-frequency plots](https://labcit.ligo.caltech.edu/~jkanner/aapt/web/math.html#tfplot)
 * [Shourov Chatterji PhD Thesis](https://dspace.mit.edu/handle/1721.1/34388)
""")
    
st.sidebar.button('Predict')