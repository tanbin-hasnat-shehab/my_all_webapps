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
from block_chain import blc


choices=st.sidebar.selectbox('list of apps',['structural analysis of beam,frame,truss','Earthquak load calculation',
											
											'aisc steel section database',
											'circle detection',
											'critical path method-cpm',
											'location phising',
											'moving load analysis',
											'wind load calculation',
					     						'block chain hashlib sha256',
											'Contact dev'
											])


if choices=='Earthquak load calculation':
	EQ.Earthquak_load_cal()
if choices=='block chain hashlib sha256':
	blc.blc_fn()
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

if choices=='wind load calculation':
	st.title('coming soon..')



if choices=='Contact dev':
	st.title('About me')
	messege=f'<p style="font-family:Courier; color:Red; font-size: 20px;">mail - tanbinhasnat04@gmail.com  git - https://github.com/tanbin-hasnat-shehab</p>'
	st.markdown(messege, unsafe_allow_html=True)



	
