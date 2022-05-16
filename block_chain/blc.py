import hashlib
from block_chain.pyrebase_module import*
import streamlit as st
#database link 
#https://console.firebase.google.com/u/0/project/my-project-5277687837074/database/my-project-5277687837074-default-rtdb/data/~2F
def blc_fn():
	st.title('hashlib sha256 block-chain')
	c1,c2=st.beta_columns((1,1))
	with c1:
		ID=st.text_input('enter id')
	with c2:
		vote=st.radio('select vote',['A','B'])
		terminate=st.text_input('delete database enter admin key')
		terminate=int(terminate)

	db=object_database(database_name='mydb')
	all_data=db.show_data()

	#data_list=list(all_data.items())
	if all_data==None:
		db.input_data(path='user-1/ID',value='xxxxx')
		db.input_data(path='user-1/VOTE',value='X')
	if terminate==441:
		db.delete_data(path='mydb')
	#db=object_database(database_name='mydb')
	#db.input_data(path='initiate',value=True)

	def create_has(data,vote):
		db=object_database(database_name='mydb')
		all_data=db.show_data()
		mega_str=''
		data_list=list(all_data.items())
		#st.write(data_list)
		#st.write(data_list)
		serial=len(data_list)

		#for i in range(len(data_list)):
			#mega_str=mega_str+str(data_list[i][0])+str(data_list[i][1])

		#st.write(mega_str)
		#st.write(data_list)
		already_cast=False
		for i in range(len(data_list)):
			if data_list[i][1]['ID']==data:
				already_cast=True
		if already_cast==False and data!='':
			db.input_data(path=f'user-{serial+1}/ID',value=data)
			db.input_data(path=f'user-{serial+1}/VOTE',value=vote)
		all_data=db.show_data()
		mega_str=''
		data_list=list(all_data.items())
		#st.write(data_list)
		#st.write(data_list)
		serial=len(data_list)

		for i in range(len(data_list)):
			mega_str=mega_str+str(data_list[i][0])+str(data_list[i][1])
		
		

		x='-'+str(data)+'-'+str(vote)+mega_str
		#st.write(x)
		hashcode=hashlib.sha256(x.encode()).hexdigest()
		st.success(f'your serial is {len(data_list)} & hashcode is {hashcode}')


	def check_vote(ser,ID_NO):
		ser=int(ser)
		db=object_database(database_name='mydb')
		all_data=db.show_data()
		mega_str=''
		data_list=list(all_data.items())
		#st.write(data_list)
		vote=data_list[ser-1][1]['VOTE']
		#st.write(vote)
		for i in range(ser):
			mega_str=mega_str+str(data_list[i][0])+str(data_list[i][1])

		x='-'+str(ID_NO)+'-'+str(vote)+mega_str
		#st.write(x)
		hashcode=hashlib.sha256(x.encode()).hexdigest()
		st.success(f'your serial is {ser} & hashcode is {hashcode}')
		
	if st.button('add'):
		create_has(ID,vote)


	check=st.checkbox('check')
	if check:
		ser=st.text_input('serial')
		ID_NO=st.text_input('ID_NO')
		if ser!='' and ID_NO!='':
			check_vote(ser,ID_NO)
	see_d=st.checkbox('see database')
	if see_d:
		my_data=db.show_data()
		st.write(my_data)
		st.write(f'Link is \n https://console.firebase.google.com/u/0/project/my-project-5277687837074/database/my-project-5277687837074-default-rtdb/data/~2F')
