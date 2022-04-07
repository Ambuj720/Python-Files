###To run oprn cmd streamlit run {Filenamne}###

from turtle import title
import streamlit as st
from db import Moviees, Product, engine
from sqlalchemy.orm import sessionmaker
st.title("DB demo")

oplist=['Add Movie','View Movie']
choice=st.selectbox('Select an Option',oplist)

def opendb():
    Session = sessionmaker(bind=engine)
    return Session()

def save_movee(title,year,director,genre,rating,summary):
    db = opendb()
    movie = Moviees(title=title,year=year,director=director,genre=genre,rating=rating,summary=summary)
    db.add(movie)
    db.commit()
    db.close()

st.sidebar.title("Movies List")

oplist = ['Add Movie','View Movie']
choice = st.sidebar.selectbox('Select an Option',oplist)
if choice == oplist[0]:
    st.header("Add a new Movie detail")
    f = st.form('Add Movie Details here:')
    title = f.text_input('Movie Name')
    year = f.('student class',[1,2,3,4,5,6,7,8,9,10,11,12])
    btn = f.form_submit_button("Save movie Details")
    if btn and name and klass:
        save_student(name,klass)
        st.success("form data saved")

elif choice == oplist[1]:
    st.header("view student details")
    db = opendb()
    students = db.query(Student).all()
    for std in students:
        st.markdown(f'''
        {std.name}
        {std.klas