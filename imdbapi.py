import requests
import json
import streamlit as st
from deep_translator import GoogleTranslator 



def getMovieID(movieName):
    url = "https://imdb8.p.rapidapi.com/title/find"

    querystring1 = {"q":movieName}

    headers = {
        "X-RapidAPI-Key": "8a67def28cmsh0bf8c467709ccdfp1df2ddjsncc7b6e252b1d",
        "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring1)
    data = json.loads(response.text)
    # a = (data["results"])
    # a = json.dumps(data["results"])
    a = data["results"][0]["id"]
    return(a.replace("/","").replace("title",""))



def getData(id):
    url = "https://imdb8.p.rapidapi.com/title/get-overview-details"

    querystring = {"tconst":id}

    headers = {
        "X-RapidAPI-Key": "8a67def28cmsh0bf8c467709ccdfp1df2ddjsncc7b6e252b1d",
        "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    return data

def getDuration(data):
    return (data["title"])["runningTimeInMinutes"]

def getRelease(data):
    return (data["releaseDate"])

def getRating(data):
    return data["ratings"]

def getGenres(data):
    return data["genres"]
   


with st.container():
    st.title("IMDb API movie details")
    name = st.text_input("Please enter the movie name!")
    
    submit = st.button("Grab the details")
    if submit and name:
        try:
         id = str(getMovieID(name))
         st.text("Movie Rating: "+ str(getRating(id)))
         st.text("Movie duration: " + str(getDuration(id)) + " minutes")
        except:
            st.error("Your input isn't a valid movie name, please fix your input.")
    if submit and not(name):
        st.error("Please fill out the name field!")




    
    



# data = getData(getMovieID("Hobbit"))
# print("Rating: " + str(getRating(data)["rating"]))
# print("Duration: " + str(getDuration(data)))
# print("Release date: " + str(getRelease(data))[:4])
# print("Genres: " + GoogleTranslator(source='auto', target='de').translate(",".join(getGenres(data))))
        # return(a.replace("/","").replace("title",""))
