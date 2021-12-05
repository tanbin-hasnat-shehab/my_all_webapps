import streamlit as st
import plotly.express as px


import plotly.graph_objects as go
xx=[1,2,3,4]
yy=[7,4,5,8]
x1=[2,7,5,4,3,6,5,3]
y1=[3,4,5,6,7,8,9,6]
x2=[5,4,3,6,7,8,9,7,6,5,2,4,4,3,2]
y2=[4,3,5,6,2,9,7,0,3,6,4,3,2,1,8]

#fr=[go.Frame(data=[go.Scatter(x=xx, y=yy)]),go.Frame(data=[go.Scatter(x=[1, 4], y=[1, 4])]),go.Frame(data=[go.Scatter(x=xx, y=yy)])]
fr=[go.Frame(data=[go.Scatter(x=xx, y=yy)]),go.Frame(data=[go.Scatter(x=x1,y=y1)]),go.Frame(data=[go.Scatter(x=x2,y=y2)])]
#layout=go.Layout(title_text="End Title"))
fig1= go.Figure(
    data=[go.Scatter(x=[0, 1], y=[0, 1])],
    layout=go.Layout(
        xaxis=dict(range=[-10, 10], autorange=False),
        yaxis=dict(range=[-10, 10], autorange=False),
        title="Start Title",
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None])])]
    ),
    
	    frames=fr
)

#fig.show()
st.write(fig1)