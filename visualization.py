import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st

def create_bar_chart(df, x_col, y_col):
    fig = px.bar(df, x=x_col, y=y_col, title=f"Bar Chart: {x_col} vs {y_col}")
    return fig

def create_pie_chart(df, col):
    fig = px.pie(df, names=col, title=f"Pie Chart: {col}")
    return fig

def create_line_chart(df, x_col, y_col):
    fig = px.line(df, x=x_col, y=y_col, title=f"Line Chart: {x_col} vs {y_col}")
    return fig

def create_scatter_plot(df, x_col, y_col):
    fig = px.scatter(df, x=x_col, y=y_col, title=f"Scatter Plot: {x_col} vs {y_col}")
    return fig

def create_heatmap(correlations):
    if correlations is not None:
        fig, ax = plt.subplots()
        sns.heatmap(correlations, annot=True, ax=ax)
        return fig
    return None
