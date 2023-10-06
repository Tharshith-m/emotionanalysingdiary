# -*- coding: utf-8 -*-  
"""
Created on Sun Jul  2 12:03:08 2023

@author: thars
"""                                   
import re 
import random
from collections import Counter
import numpy as np                                                
import pickle 
import streamlit as st
import datetime
import streamlit as st 
import sqlite3 
conn=sqlite3.connect('data.db') 
c=conn.cursor()  


favicon = "https://cdn-icons-png.flaticon.com/512/57/57364.png?w=740&t=st=1688968682~exp=1688969282~hmac=21ad59a12ff633786268321ba4ee456ac82c28a016b2ee8e03be845345aca71d"

# Set page configuration including the favicon
st.set_page_config(
    page_title="Diary",
    page_icon=favicon,
)









loginpage_bg_img = """
<style> 
[data-testid="stAppViewContainer"]{ 
    background-image:url("https://cdni.iconscout.com/illustration/premium/thumb/login-denied-4560629-3784195.png") ;
   background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
    } 

   

.element-container css-1hynsf2 esravye2{ 
    background-color:#104792;  
    }
    
[data-testid="stSidebar"] {
    background-image:url("https://img.freepik.com/free-vector/abstract-background_53876-90916.jpg?w=1060&t=st=1688967888~exp=1688968488~hmac=6a0a47218bd3065aac1a395c9f3a24d08914fd554de03f87d8e012ca56a4c9f3");
    background-size: cover;
    background-color: #f8f8f8;
    background-repeat: no-repeat;
    background-position: center;
    }
    
    
    
    
   


.stButton button {
    background-color: #104792; /* Set your desired background color */
    color: #ffffff; /* Set your desired text color */
    border-color: #ff0000; /* Set your desired border color */ 
}

.stAlert .stAlert-info {
    color: red; /* Set your desired color for st.info messages */
}

    
    
    

</style>
"""

home_page_pg_img="""
<style>
[data-testid="stAppViewContainer"]{ 
     background-image:url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPLi6woREzz6h-WOGDXaJMYsEPqqx8ccQM8g&usqp=CAU") ;
     #background-size: 60% auto;
     #background-color:#327EB7;
     background-size: cover;
    background-repeat: no-repeat;
    background-position: center; 
    
[data-testid="stVerticalBlock"] { 
   # background-image:url("https://img.freepik.com/premium-photo/beautiful-abstract-bluesky-water-color-background_364465-1332.jpg?w=2000") ;
    display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  
[data-baseweb="notification"]{ 
   # background-image:url("https://png.pngtree.com/background/20210712/original/pngtree-neon-double-color-futuristic-frame-colorful-background-picture-image_1178693.jpg") ;
    
    
    }
    }
     }

</style>
"""  

sign_page_bg_img="""
<style>
[data-testid="stAppViewContainer"]{ 
     
     background-image:url("https://st.depositphotos.com/18722762/51522/v/450/depositphotos_515228796-stock-illustration-online-registration-sign-login-account.jpg") ;
     background-size: contain;
     background-color:#C5E4F1;
    background-repeat: no-repeat;
    background-position: center;
     }
</style>
""" 

st.markdown(
    """
    <style>
    .css-1dj3z61.e1iq63gx0 {
        background-color: lightblue; 
        
    }
    </style>
    """,
    unsafe_allow_html=True
) 

st.markdown(
    """
    <style>
    .st-ae.st-af.st-ag.st-ah.st-ai.st-aj.st-ak.st-dt.st-am.st-ba.st-an.st-ao.st-ap.st-aq.st-ar.st-as.st-du.st-au.st-av.st-aw.st-ax.st-ay.st-bb.st-b0.st-b1.st-b2.st-b3.st-b4.st-b5.st-b6.st-b7 {
        background-color: lightblue;
    }
    </style>
    """,
    unsafe_allow_html=True
)   

recommendations = {
    'sadness': [
        "Listen to soothing music and let the melodies heal your heart.",
        "Write down your feelings in a journal to release the weight of sadness.",
        "Reach out to a close friend or family member for support and comfort.",
        "Engage in a creative outlet like painting, writing, or playing an instrument.",
        "Take a walk in nature and let the beauty around you bring solace.",
        "Watch a heartwarming movie or read a touching book to uplift your spirits.",
        "Practice self-care activities such as taking a bubble bath or getting a massage.",
        "Find a quiet space to meditate and allow yourself to process your emotions.",
        "Express your sadness through poetry or by writing a heartfelt letter.",
        "Seek professional help or therapy to navigate through your emotions.",
    ],
    'anger': [
        "Take deep breaths and practice mindfulness to calm your anger.",
        "Engage in physical exercise or activities to release pent-up frustration.",
        "Write a letter expressing your anger, then tear it up as a symbolic release.",
        "Practice active listening and open communication to resolve conflicts.",
        "Engage in a hobby or activity that helps you channel and release your anger.",
        "Take a break or step away from the situation to gain perspective.",
        "Talk to a trusted friend or therapist to help you process and manage your anger.",
        "Practice forgiveness and let go of grudges for your own peace of mind.",
        "Engage in relaxation techniques such as deep breathing or progressive muscle relaxation.",
        "Practice assertiveness skills to express your needs and boundaries effectively.",
    ],
    'fear': [
        "Challenge your fears by gradually exposing yourself to what scares you.",
        "Practice deep breathing exercises to calm your mind and body.",
        "Create a list of your fears and work on tackling them one by one.",
        "Seek support from loved ones or a professional to help you overcome your fears.",
        "Educate yourself about what you fear to gain a better understanding.",
        "Visualize yourself successfully facing and overcoming your fears.",
        "Practice positive affirmations to boost your confidence and courage.",
        "Engage in activities that make you feel empowered and strong.",
        "Set small, achievable goals to gradually confront and conquer your fears.",
        "Remember that fear is a normal emotion, and you have the strength to overcome it.",
    ],
    'surprise': [
        "Embrace the unexpected and enjoy the thrill of surprises in life.",
        "Try something new or participate in spontaneous activities for a sense of adventure.",
        "Keep an open mind and be flexible to embrace surprises as opportunities.",
        "Celebrate the joy of surprises by sharing them with loved ones.",
        "Appreciate the beauty of unexpected moments and let them inspire you.",
        "Stay curious and explore new experiences to invite more surprises into your life.",
        "Take a break from routine and allow yourself to be surprised by the world around you.",
        "Embrace uncertainty and see surprises as chances for personal growth.",
        "Share surprises with others through acts of kindness or unexpected gestures.",
        "Reflect on past surprises that brought you happiness and gratitude.",
    ],
    'love': [
        "Show appreciation and express love to the people who matter to you.",
        "Practice self-love and treat yourself with kindness and compassion.",
        "Engage in activities that bring you joy and make your heart soar.",
        "Reach out to loved ones and remind them how much they mean to you.",
        "Volunteer or contribute to causes that promote love and compassion.",
        "Write a heartfelt letter or poem to someone you love and cherish.",
        "Create special moments and memories with your loved ones.",
        "Practice active listening and empathy to deepen your connections.",
        "Celebrate love in all its forms and spread kindness wherever you go.",
        "Cherish the love you receive and let it inspire you to love others.",
    ]
}








 # Apply different background images based on the page selected
def apply_page_background(page):
    if page == "Login":
        st.markdown(loginpage_bg_img, unsafe_allow_html=True) 
    elif page == "Home":
        st.markdown(home_page_pg_img, unsafe_allow_html=True)
    elif page == "SignUp":
        st.markdown(sign_page_bg_img, unsafe_allow_html=True)














#creation of table named usertable
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS usertable(username TEXT,password TEXT)') 
    
#adding sign up info into the db
def add_userdata(username,password):
    c.execute('INSERT INTO usertable(username,password) VALUES(?,?)',(username,password))
    conn.commit() 
    
def create_Emotiontable(): 
    
    c.execute('CREATE TABLE IF NOT EXISTS emotionstable(username TEXT,emotion TEXT,date DATE)') 
    
    
#add into emotions table 
def add_userEdata(username,emotion,date):
    c.execute('INSERT INTO emotionstable(username,emotion,date) VALUES(?,?,?)',(username,emotion,date)) 
    conn.commit()  

def display_all_Edata():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM emotionstable')
    data = c.fetchall()
    for row in data:
        st.write("Username:", row[0])
        st.write("emotion:", row[1]) 
        st.write("date:",row[2])
        st.write("---")  
    
    
    

#login user 
def login_user(username,password):
    c.execute('SELECT * FROM usertable WHERE username =? AND password=?',(username,password))
    data=c.fetchall()
    return data 

#date
def get_current_date():
 now = datetime.datetime.now()
 return now.strftime("%Y-%m-%d") 

#retrieving all the users data
def display_all_data():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM usertable')
    data = c.fetchall()
    for row in data:
        st.write("Username:", row[0])
        st.write("Password:", row[1])
        st.write("---") 
#to get past 3 days data based on the date 
def get_past_three_days_data(username):
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=3)  
    c.execute("SELECT date, username, emotion FROM emotionstable WHERE username = ? AND date BETWEEN ? AND ?", (username, start_date, end_date))
    rows = c.fetchall() 
    return rows 

#counting the number of occurences of each word 
def get_max_occurrences(arr):
    counter = Counter(arr)
    max_occurrences = max(counter.values())
    max_strings = [string for string, count in counter.items() if count == max_occurrences]
    return max_strings




def main():
    #login page 
    #st.title("login page")
   # st.title("login")
    menu=["Login","Home","SignUp","Admin"] 
    choice=st.sidebar.selectbox("Menu",menu) 
    st.session_state.is_logged_in = False 
    apply_page_background(choice)

    
    #create_Etable() 
    
    #login code
    if choice == "Login": 
        st.title("Login page")
        st.subheader("Login Section") 
        username = st.text_input("Username")
        password = st.text_input("Password", type='password') 
        if st.button("Login"): 
            if len(username) >= 3 and len(password) >= 4: 
                create_table()
                result = login_user(username, password) 
                if result: 
                    st.session_state["username"] = username
                    st.session_state["is_logged_in"] = True 
                    st.success("Logged in as {}".format(username)) 
                else:
                  st.warning("Incorrect Username/Password")
            else:
              st.warning("Username must be at least 3 characters long and password must be at least 4 characters long")
     #home code
    
    elif choice=="Home":
       # if st.session_state.is_logged_in:
           create_Emotiontable() 
           st.title("Home page") 
           # date 
           st.title("Current Date")  
           st.write(get_current_date()) 
           todaydate=get_current_date() 
           count=0
           arr=[] 
           max_strings = [] 
           if st.session_state.get('username') is not None: 
               st.write("<p class='greeting'>Hi</p> <p class='username'>{}</p>".format(st.session_state["username"]), unsafe_allow_html=True) 
               k=st.session_state.get("username") 
               past_three_days_data = get_past_three_days_data(k) 
               for i in past_three_days_data:
                   arr.append(i[2]) 
               if arr: 
                   max_strings = get_max_occurrences(arr)
               if max_strings:  
                   if max_strings[0] in recommendations: 
                       emotion = max_strings[0] 
                       random_recommendations = random.sample(recommendations[emotion], k=1)  
                       for recommendation in random_recommendations: 
                            st.info(recommendation) 
                   else:  
                        st.info("Moving good, maintain a life with the same happiness streak. 😊😊😊")        
                   
                           
               else:
                   st.info("This diary analyses past 3 days and tracks your emotions trend ,so keep going ")
               # loading saved model  
               loaded_model = pickle.load(open("emotionsanalysing.sav", 'rb') )  # giving a title 
               def emotions_pred(input_data):
                 
                         y = loaded_model.predict(np.array(input_data))
                         if y == 0:
                             return "anger"
                         elif y == 1:
                             return 'fear'
                         elif y == 2:
                             return 'joy'
                         elif y == 3:
                             return 'love'
                         elif y == 4:
                             return 'sadness'
                         elif y == 5:
                             return 'surprise'  

               st.title("YOUR DIARY📖") 
                   #text = st.text_input('speak out:') 
               text = st.text_input('speak out:')

    # Regular expression pattern to match alphabets and numbers
               emotion = '' 
               pattern = r'^[A-Za-z0-9]+$'
               text_without_spaces = text.replace(" ", "") 
               if st.button('my feel'): 
                       if text.strip() == '' or (re.match(pattern, text) and not any(c.isalpha() for c in text)):
            # Invalid input: empty or only numbers without any alphabet characters
                          st.warning('Please enter a valid input with at least one alphabet character.')
                       elif sum(c.isalpha() for c in text_without_spaces) >= 3:
                          emotion = emotions_pred([text]) 
                          st.success(emotion) 
                          add_userEdata(st.session_state.get('username'),emotion,'2023-07-17')
                          
            # Process the emotion or perform other actions with the valid input
                       else:
                           st.warning('Please enter a valid input with at least three alphabet characters.')
                    
           else: 
               st.warning("please login") 
                 
                                
             
                
               
               
               
            
               
        
            
            
            
            
               
               
            
          
     #sign up code
    elif choice == "SignUp":
        st.title("Sign Up")
        st.subheader("Create new account") 
        new_user = st.text_input("Username") 
        new_password=st.text_input("Password",type='password')
        
        if st.button("Signup"):
            create_table()
            add_userdata(new_user, new_password) 
            st.success("You have succesfully created valid account")
            st.info("Go to Login Menu to login") 
    elif choice=="Admin":
        st.title("admin") 
       # st.write(get_current_date())
        #display_all_Edata() 
        #c.execute('DROP TABLE IF EXISTS emotionstable') 
        #c.execute('DROP TABLE IF EXISTS usertable') 
        display_all_Edata()
      
        
        
            
if __name__=='__main__':
    main() 
