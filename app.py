import streamlit as st
from openpyxl import load_workbook
import pandas as pd
from earthquak import EQ
from sfd import sfd
from loc_fishing import loc_ph

from steel_db import stdb
from circle_detection import cir
from cpm_python import cp3
from moving_load import go
from sfd import sfd


choices=st.sidebar.selectbox('list of apps',['Earthquak load calculation',
											'wind load calculation',
											'structural analysis of beam,frame,truss',
											'aisc steel section database',
											'circle detection',
											'critical path method-cpm',
											'location phising',
											'moving load analysis'
											])


if choices=='Earthquak load calculation':
	EQ.Earthquak_load_cal()
if choices=='structural analysis of beam,frame,truss':
	sfd.sfd_bmd()



if choices=='aisc steel section database':
	stdb.st_database()

if choices=='circle detection':
	cir.main_detection()
if choices=='critical path method-cpm':
	cp3.cpm_main()
if choices=='location phising':
	loc_ph.loc_main()
if choices=='moving load analysis':
	go.moving_main()


	
