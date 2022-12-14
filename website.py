import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pendulum

title_Font = {'fontname': 'Comic Sans MS'}
header_Font = {'fontname': 'Helvetica'}

df = pd.read_csv("Skyscrapers_2021.csv",
                 header=0)

st.title("Viewing Skyscrapers around the World") #using a python package we did not use in class
date = pendulum.now()
st.write(date)

# TextBox
txt = st.text_input('What is your name?')
st.write(txt + ' welcome to my Website!')

#Button
if st.button('Look at the Map of Skyscrapers below'):
    st.write('It shows the 99 tallest skyscrapers in the world')
    #Map
    df2 = pd.DataFrame({'City': df['CITY'], 'lat': df['Latitude'], 'lon': df['Longitude']})
    st.map(df2)

# Sidebar
langs = st.sidebar.multiselect("Which do you want to see?",
                               ["Ranking the Tallest Buildings", "The Tallest Building in the World",
                                "Cities with Skyscrapers"])

if "Ranking the Tallest Buildings" in langs:
    df_to_display = pd.DataFrame({'Name of Building': df['NAME'], 'City': df['CITY'],
                                  'Height': [int(df['Meters'][i][:3]) for i in
                                             range(len(df['Meters']))]})  # loops thru a list, list comprehension
    buildings = st.slider("How many buildings would you like to see?", 2, 99, 10)
    df_to_display = df_to_display[:buildings].sort_values(by=['City', 'Height'])  # sorted by city ,then height
    st.write(df_to_display)
    plt.scatter(df_to_display['Name of Building'], df_to_display['Height'], color='red')
    plt.title("Tallest Buildings", **title_Font, fontsize=35, color='red')
    plt.ylabel("Height in Meters", **header_Font, fontsize=20, color='grey')
    plt.xlabel("Skyscraper Name", **header_Font, fontsize=20, color='grey')
    plt.xticks(rotation=90, color='grey')
    plt.yticks(color='grey')
    st.pyplot(plt)
def Merge(dict1, dict2):  # merges the two dicts together from cities to create an empty city
    res = {**dict1, **dict2}
    return res

if "The Tallest Building in the World" in langs:
    st.image("Inspiration Project_Burj Khalifa_Main Pic_2880 x 1620px.jpg")
    tallest = max(df['Height'])
    total_floors = max(df['FLOORS'])#filtering by one condition
    st.write(tallest)
    st.write(total_floors)

if "Cities with Skyscrapers" in langs:
    cities = {}
    for city in df['CITY']:
        if city not in cities:
            cities = Merge(cities, {city: 1})
        else:
            cities[city] += 1
    plt.scatter(cities.keys(), cities.values(), color='red')
    plt.title("Cities with Skyscrapers", **title_Font, fontsize=35)
    plt.ylabel("Count in City", **header_Font, fontsize=20, color='grey')
    plt.xlabel("City", **header_Font, fontsize=20, color='grey')
    plt.xticks(rotation=90, color='grey')
    plt.yticks(color='grey')
    st.pyplot(plt)
