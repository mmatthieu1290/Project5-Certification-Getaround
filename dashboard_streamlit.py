import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import numpy as np
#import SessionState

with open('time_losse.pkl','rb') as tl:
    time_losse = pickle.load(tl)

with open('estimator_problems_inverse.pkl','rb') as est_problem:
    estimator_problems = pickle.load(est_problem)      

### Config
st.set_page_config(
    page_title="App-car-rental",
    layout="wide"
)

### HEADER
st.title('')

connexion = sqlite3.connect('db_deployment.db')

connexion.commit()

df_at_time_late_vs_checkin_type = pd.read_sql_query('select * from at_time_late_vs_checkin_type' \
    , con = connexion,index_col = 'index')

at_time = df_at_time_late_vs_checkin_type.loc['at_time'].tolist()

late = df_at_time_late_vs_checkin_type.loc['late'].tolist()    

#delay = pd.read_excel('get_around_delay_analysis.xlsx')

choice = st.sidebar.selectbox("What do you want to see?",\
    ["First look at the dataset","Mean delay in minutes"\
        ,"Rents with delay","Delay versus Check-in type",\
    "Influence of threhold"])

if choice == "First look at the dataset": 

 st.header("First look at the dataset.")    

 st.write(pd.read_sql_query('select * from lines_of_dataset'\
, con = connexion).sample(10))

 st.write("The dataset has 21310 data.")

 st.header("Missing values.")

 st.write(pd.read_sql_query('select * from missing_values'\
, con = connexion).rename(columns = {'index':'column'}))  

if choice == "Mean delay in minutes":

 st.header("Mean delay in minutes")   

 st.write(pd.read_sql_query('select * from mean_late_vs_checkin_type' \
    , con = connexion,index_col = 'checkin_type'))         

if choice =="Rents with delay":

 st.header("Rents with delay")

 st.sidebar.header("")

 labels = ['At time', 'Late']
 sizes = [np.sum(at_time),np.sum(late)]
 colors = ['blue', 'red']

 fig,ax = plt.subplots()

 ax.pie(sizes, labels=labels, colors=colors, 
        autopct='%1.1f%%', shadow=False, startangle=90)

 ax.axis('equal')

 st.pyplot(fig)

if choice == "Delay versus Check-in type":

 st.header("Delay versus Check-in type")        

 st.sidebar.header("")



 



 barWidth = 0.05
 fig = plt.subplots(figsize =(12, 8))

 
# set height of bar


 
 # Set position of bar on X axis
 br1 = 0.3*np.arange(len(at_time))
 br2 = [x + barWidth for x in br1]
 
 percent_at_time_mobile = 100*at_time[0]/(at_time[0]+late[0])

 percent_late_mobile = 100 - percent_at_time_mobile

 mobile_percent = [f'{round(percent_at_time_mobile,2)}%',\
                  f'{round(percent_late_mobile,2)}%']

 percent_at_time_connect = 100*at_time[1]/(at_time[1]+late[1])

 percent_late_connect = 100 - percent_at_time_connect

 connect_percent = [f'{round(percent_at_time_connect,2)}%',\
                   f'{round(percent_late_connect,2)}%']

 connect_percent = [f'{round(percent_at_time_connect,2)}%',\
                   f'{round(percent_late_connect,2)}%']

 fig, ax = plt.subplots()                   

 # Make the plot
 ax.bar(br1, at_time, color ='b', width = barWidth,
        edgecolor ='grey', label ='At time')
 ax.bar(br2, late, color ='r', width = barWidth,
        edgecolor ='grey', label ='Late')
 
 # Adding Xticks
 ax.set_xlabel('Checkin_type', fontweight ='bold', fontsize = 15)
 #plt.ylabel('', fontweight ='bold', fontsize = 15)
 ax.set_xticks([0.3*(r + barWidth) for r in range(len(at_time))],
        ['Mobile','Connect'])

 ax.text(x = -barWidth/2.1 , y = at_time[0]/2,s = mobile_percent[0])
 ax.text(x = barWidth/1.8 , y = late[0]/2,s = mobile_percent[1])

 ax.text(x = 0.3-barWidth/2.1 , y = at_time[1]/2,s = connect_percent[0])
 ax.text(x = 0.3+barWidth/1.7 , y = late[1]/2,s = connect_percent[1])
 
 ax.legend()

 st.pyplot(fig)

if choice == "Influence of threhold":    

 st.header("Influence of threhold")

 threshold = st.sidebar.slider("Threshold between two rents in minutes",0,700) 

 time_of_rent = st.sidebar.number_input("Time of rent in days",1)

 mean_time_losse = round(max([0,float(time_losse.predict([[threshold,threshold**2]]))]),0)

 df_loss = pd.read_sql_query('select * from loss_time',con = connexion)

 df_problems = pd.read_sql_query('select * from check_out_problems',con = connexion)

 df_slope = pd.read_sql_query('select * from slope_check_out_problems',con = connexion)

 x = df_loss.iloc[:,0]

 y1 = df_loss.iloc[:,1]

 y2 = df_problems.iloc[:,1]

 if threshold < df_slope.iloc[0,0]:
    mean_problem = df_problems.iloc[0,1] + df_slope.iloc[0,1]*threshold
 else:
    mean_problem = 1/(float(estimator_problems.predict([[threshold]]))) 

 fig, ax1 = plt.subplots()

 ax2 = ax1.twinx()
 ax1.plot(x, np.max([np.array(y1).reshape((-1,1)),np.zeros((len(y1),1))],axis = 0), 'g-')
 ax1.plot(threshold*np.ones(400),np.linspace(-10,430,400),c = 'r')
 ax2.plot(x, 100*y2, 'b-')
 ax1.scatter(threshold,mean_time_losse,c='g')
 ax1.text(x=threshold-70,y=mean_time_losse+10,s=f'{mean_time_losse}',c='g')
 ax2.scatter(threshold,100*mean_problem,c = 'b')
 ax2.text(x=threshold+10,y=100*mean_problem+0.1,s=f'{round(100*mean_problem,2)}%',c='b')

 ax1.set_xlabel('Threshold')
 ax1.set_ylabel('Time loss in minute', color='g')
 ax2.set_ylabel('Percentage of check out with delay', color='b')

 st.pyplot(fig)


 mean_relative_time_losse = mean_time_losse/(24*60*time_of_rent)

 st.sidebar.write("On average",mean_time_losse," rental minutes will be lost per rental.\
     This represents",\
    round(100*mean_relative_time_losse,2),'% of the total rental time.')

   


 st.sidebar.write("We estimate that in ",round(100*mean_problem,2)," % of rentals, \
    the car will be returned after the scheduled time of the next rental.")



