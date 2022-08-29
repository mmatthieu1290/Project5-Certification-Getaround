current_datetime = datetime.datetime(lt.tm_year, lt.tm_mon, lt.tm_mday, lt.tm_hour, lt.tm_min)

lt = time.localtime()

st.sidebar.header("Book your rent")
start_datetime = datetime.datetime(lt.tm_year, lt.tm_mon, lt.tm_mday, lt.tm_hour, lt.tm_min)
try:
 end_datetime = datetime.datetime(lt.tm_year, lt.tm_mon, lt.tm_mday+1, lt.tm_hour, lt.tm_min)
except ValueError: 
 try:
  end_datetime = datetime.datetime(lt.tm_year, lt.tm_mon+1,1, lt.tm_hour, lt.tm_min)  
 except ValueError: 
  end_datetime = datetime.datetime(lt.tm_year+1, 1,1, lt.tm_hour, lt.tm_min) 


start_date = st.sidebar.date_input('start rent', start_datetime)
start_time = st.sidebar.time_input('',datetime.time(0,0),key = "1")
end_date = st.sidebar.date_input("end rent", end_datetime)
end_time = st.sidebar.time_input('',datetime.time(0,0), key = "2")