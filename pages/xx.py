import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import mpld3
import streamlit as st
import matplotlib.pylab as pylab

#create your figure and get the figure object returned

def st_pyplot(fig):
size = fig.get_size_inches()
width = int(size[0]) * 100+50
height = int(size[1]) * 100+50
params = {‘legend.fontsize’: 30,
‘figure.figsize’: (10, 10),
‘axes.labelsize’: 30,
‘axes.titlesize’: 30,
‘xtick.labelsize’: 30,
‘ytick.labelsize’: 30}
pylab.rcParams.update(params)
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, width=width, height=height)

if name == “main”:
fig = plt.figure()
# fig = plt.figure(figsize=(15,10))
plt.plot([1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
plt.xlabel(“Length (nm)”)
plt.ylabel(“Force (pN)”)
st_pyplot(fig)
