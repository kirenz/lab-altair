import streamlit as st
import pandas as pd
import altair as alt

st.markdown("## Exercise 6.2 - Dashboard")
st.markdown("### Task 4")

# Data Preperation
# --------------------------------------- 

df = pd.read_excel("/Users/lukas/Downloads/6.2 EXERCISE.xlsx")
df["Month"] = df[2019]
df["Penetration_Rate"] = df["Penetration Rate"]
df = df.drop(columns=2019, axis=1)

df["Penetration_Rate"] = df["Penetration_Rate"].apply(lambda x : round(x*100))

# Chart
# --------------------------------------- 

line_chart = alt.Chart(df).mark_line(point=True).encode(
    x=alt.X("Month", sort=["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"],
    axis=alt.Axis(title="2019", titleAnchor="start", labelAngle=0,grid=False, labelPadding=10, tickSize=0)),
    y=alt.Y("Penetration_Rate", axis=alt.Axis(title="Penetration Rate", titleAnchor="end", grid=False, values=[0,10,20,30,40,50,60,70,80,90,100]),scale=alt.Scale(domain=[0, 60])),
    strokeWidth=alt.value(4),
    color=alt.value("black"),
    tooltip=["Penetration_Rate","Month"]
).properties(
    title="Penetration rate over time in 2019",
    width=550,
    height=400
)

chart = alt.layer(line_chart).configure_title( 
    fontSize=22,
    font='Arial',
    color='black',
    anchor='start',
    fontWeight="normal"
).configure_point(
    size=60,
).configure_axis(
    labelFont='Arial',
    titleFont='Arial',
    labelFontSize=11,
    titleFontSize=14,
    titleFontWeight="normal",
    titleColor="grey",
    labelColor="grey",
    titlePadding=8
).configure_view(
    strokeWidth=0
).interactive()



st.altair_chart(chart)
