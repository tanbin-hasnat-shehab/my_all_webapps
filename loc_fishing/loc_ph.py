import streamlit as st
import codecs
import streamlit.components.v1 as stc
def loc_main():
	def my_html(html_file,width=700,height=500):
		html_file=codecs.open(html_file,'r')
		page=html_file.read()
		stc.html(page,width=width,height=height,scrolling=False)


	my_html('loc_fishing/map.html')
