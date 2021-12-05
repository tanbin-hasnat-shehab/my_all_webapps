import streamlit as st
import codecs
import streamlit.components.v1 as stc
from anastruct import SystemElements
import math
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import json
def moving_main():

    def my_html(html_file,width=2000,height=200):
        html_file=codecs.open(html_file,'r')
        page=html_file.read()
        stc.html(page,width=width,height=height,scrolling=False)


    my_html('moving_load/a.html')


    #st.set_page_config(layout="wide")
    n=st.slider("Number of wheels", 0, 30, value=5)
    myverbs = st.radio('show values on graph:', ['yes','no'])
    myfig=st.radio('select what to analys', ['REACTIONS','DISPLACEMENTS','SHEAR FORCE','BENDING MOMENT'])

    if myverbs=='yes':
        myverb=0
    else:
        myverb=1
    js_str=st.text_input('paste here')
    c1, c2 = st.beta_columns((1,1))
    if True:
        value=json.loads(js_str)
        ss = SystemElements()
        new_data=[]
        for i in range(len(value)):
            if value[i] not  in new_data:
                new_data.append(value[i])
        number_of_beams=0
        for data in new_data:
            if data['type']=='line':
                number_of_beams+=1
        all_x=[]
        for data in new_data:
            if data['type']=='line':
                all_x.append(data['x1'])
                all_x.append(data['x2'])

        min_x=min(all_x)
        for data in new_data:
            if data['type']=='line':
                data['x1']=data['x1']-min_x
                data['x2']=data['x2']-min_x
            if data['type']=='fixed_support':
                data['x']=data['x']-min_x
            if data['type']=='hinged_support':
                data['x']=data['x']-min_x
            if data['type']=='roller_support':
                data['x']=data['x']-min_x
                
               
        


        with c1:
            st.subheader('Wheel loads')
            wheel_loads={}
            wheel_loads_one_d=[]
            for i in range(n):
                wheel_loads[f'wheel_no_{i}']=''
            for k, v in wheel_loads.items():
                wheel_loads[k] = st.text_input(k, v)
                #st.write(task_names[k])
            for i in range(n):
                wheel_loads_one_d.append((wheel_loads[f'wheel_no_{i}']))
            #print(wheel_loads_one_d)
            load=wheel_loads_one_d
        with c2:
            st.subheader('Inter distances')
            inter_distances={}
            inter_distances_one_d=[]
            for i in range(n):
                inter_distances[f'inter_distances_no_{i}']=''
            for k, v in inter_distances.items():
                inter_distances[k] = st.text_input(k, v)
                #st.write(durations[k])
            for i in range(n):
                inter_distances_one_d.append(float(inter_distances[f'inter_distances_no_{i}']))
            #print(inter_distances_one_d)
            trial_distances=inter_distances_one_d





    if st.button("Run"):
        dist=[]
        m_a=0
        for i in range(len(trial_distances)):
            
            if i ==0:
                dist.append(trial_distances[i])
            else:
                m_a=m_a+trial_distances[i-1]
                dist.append(-1*(m_a+trial_distances[i]))

        #print(f'absolute dist array is {dist}')


        my_d=[]
        for i in range(-10*int(dist[-1])+400):
            
            dx=[]
            for j in range(len(dist)):
                dx.append(dist[j]+0.5*i)
            my_d.append(dx)

        #print(my_d)




        class mBeams():
            def __init__(self,length,x1,x2,load_list,dist_list):
                self.length=length
                self.x1=x1
                self.x2=x2
                self.load_list=load_list
                self.dist_list=dist_list

        beams=[]
       
        for data in new_data:
            if data['type']=='grid_spacing':
                grid=data['value']
        for data in new_data:
            if data['type']=='line':
                data['x1']=data['x1']/grid
                data['x2']=data['x2']/grid
                line_tr=mBeams((data['x2']-data['x1']), data['x1'], data['x2'], [], [])
                beams.append(line_tr)
            if data['type']=='internal_hinge':
                data['x']=data['x']/grid
                data['y']=data['y']/grid
            if data['type']=='fixed_support':
                data['x']=data['x']/grid
                data['y']=data['y']/grid
            if data['type']=='hinged_support':
                data['x']=data['x']/grid
                data['y']=data['y']/grid



        start=beams[0].x1
        arr=[]

        for i in range(len(beams)):
            lower=beams[i].x1
            higher=beams[i].x2
            for j in range(len(my_d)):
                tr_val=[]
                tr_val2=[]
                for k in range(len(dist)):
                    if my_d[j][k]>=lower and my_d[j][k]<higher:
                        tr_val.append(load[my_d[j].index(my_d[j][k])])
                        tr_val2.append(my_d[j][k])
                
                beams[i].load_list.append(tr_val)
                beams[i].dist_list.append(tr_val2)
        ############################################################################
        for i in range(len(beams)):
            if len(beams[i].load_list)!=0:
                for j in range(len(beams[i].dist_list)):
                    for k in range(len(beams[i].dist_list[j])):
                        beams[i].dist_list[j][k]=-start+beams[i].dist_list[j][k]
            #print(f'beam no {i} and dist lis is {beams[i].dist_list}')
        #print('\n\n\nstarting\n\n\n')
        #print(f'load list of distances is {beams[i].load_list[j]}')
        def looping_structure(j):
            ss=SystemElements()
            #print(f'this is trial {j}')


            for i in range(number_of_beams):

                ss.add_element( location=[[(beams[i].x1),5] , [(beams[i].x2),5] ])
                #print('adddddddddddddddddddddddddddddddddddddddddddddddded')
                
                #print(f'this is beam no {i} and trial no {j}  and dist list is {beams[i].dist_list[j]} \n\t and load list is {beams[i].load_list[j]}\n\n\n\n\n')
                

                if len(beams[i].load_list[j])==0:
                    pass
                else:
                    for k in range(len(beams[i].load_list[j])):
                        #print(f'this is j={j} and BEAM NO {i} and distances are {beams[i].dist_list[j][k]}')
                        if beams[i].dist_list[j][k]!=beams[i].x1:
                            ss.insert_node(element_id=ss.id_last_element,location=[((beams[i].dist_list[j][k])),5])
                            
          
                
            for i in range(number_of_beams):
                for l in range(len(beams[i].load_list[j])):
                    if len(beams[i].load_list[j])!=0:
                        ss.point_load(Fx=float(beams[i].load_list[j][l]),rotation=90,node_id=ss.find_node_id([beams[i].dist_list[j][l],5]))
            for i in range(len(new_data)):
                if new_data[i]['type']=='fixed_support':
                    ss.add_support_fixed(node_id=ss.find_node_id([new_data[i]['x'],5]))
                if new_data[i]['type']=='hinged_support':
                    ss.add_support_hinged(node_id=ss.find_node_id([new_data[i]['x'],5]))
                if new_data[i]['type']=='roller_support':
                    ss.add_support_hinged(node_id=ss.find_node_id([new_data[i]['x'],5]))





            try:
                ss.show_structure()
                plt.savefig(f'moving_load/st_{j}.png')
                imageLocationstr.image(f'moving_load/st_{j}.png')


                ss.solve()
                if myfig=='REACTIONS':
                    ss.show_reaction_force(verbosity=myverb)
                    plt.savefig(f'moving_load/{j}.png')
                    imageLocation.image(f'moving_load/{j}.png')
                if myfig=='DISPLACEMENTS':
                    ss.show_displacement(verbosity=myverb)
                    plt.savefig(f'moving_load/{j}.png')
                    imageLocation.image(f'moving_load/{j}.png')
                if myfig=='SHEAR FORCE':
                    ss.show_shear_force(verbosity=myverb)
                    plt.savefig(f'moving_load/{j}.png')
                    imageLocation.image(f'moving_load/{j}.png')
                if myfig=='BENDING MOMENT':
                    ss.show_bending_moment(verbosity=myverb)
                    plt.savefig(f'moving_load/{j}.png')
                    imageLocation.image(f'moving_load/{j}.png')
                
            except:
                pass
        
        imageLocationstr = st.empty()
        imageLocation = st.empty()
        for i in range(number_of_beams):
            for j in range(len(beams[0].load_list)):
                beams[i].dist_list[j].reverse()
                beams[i].load_list[j].reverse()    
        for j in range(len(beams[0].load_list)):
            looping_structure(j)
                

      

        
        
