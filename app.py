import streamlit as st
import pandas as pd
from supabase import create_client
url="https://wlgqfclaytwuwqbxtcgt.supabase.co"
key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndsZ3FmY2xheXR3dXdxYnh0Y2d0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODA1NDY1MTgsImV4cCI6MjA5NjEyMjUxOH0.Mpx7Hu9WmcU5dhi5tW8zX4aS8byZy0vOBK6ZFgzJNPk"
supabase=create_client(url,key)
page=st.sidebar.radio("Select Page",["Student","Admin"])
if page=="Student":
    st.title("Exam Room Finder")
    rollno=st.text_input("Enter Roll Number")
    if st.button("Search"):
        try:
            result=(
                supabase.table("find_exam_rooms").select("*").eq("rollno",rollno).execute()
            )
            if result.data:
                data=result.data[0]
                st.success("Exam Details Found")
                st.write(f"Room Number:{data['roomno']}")
                st.write(f"Building Name:{data['buildingno']}")
            else:
                st.error("Roll no not found")
                
                
                
        except Exception as e:
            st.error(f"error:{e}")  
            
            
            
            
