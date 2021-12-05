import streamlit as st
from openpyxl import load_workbook
import pandas as pd
from earthquak import EQ
from sfd import sfd

choices=st.sidebar.selectbox('list of apps',['Earthquak load calculation','wind load calculation','structural analysis of beam,frame,truss'])


if choices=='Earthquak load calculation':
	EQ.Earthquak_load_cal()
if choices=='structural analysis of beam,frame,truss':
	sfd.sfd_bmd()

	
