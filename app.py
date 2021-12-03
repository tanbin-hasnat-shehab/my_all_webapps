import streamlit as st
from openpyxl import load_workbook
import pandas as pd
from earthquak import EQ

choices=st.sidebar.selectbox('list of apps',['Earthquak load calculation','wind load calculation'])


if choices=='Earthquak load calculation':
	EQ.Earthquak_load_cal()

	