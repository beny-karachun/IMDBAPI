from multiprocessing.connection import wait
import requests
import json
import streamlit as st
def getRating(id):
 url = "https://imdb8.p.rapidapi.com/title/get-ratings"

 querystring = {"tconst":id}

 headers = {
		"X-RapidAPI-Key": "8a67def28cmsh0bf8c467709ccdfp1df2ddjsncc7b6e252b1d",
		"X-RapidAPI-Host": "imdb8.p.rapidapi.com"
	}

 response = requests.request("GET", url, headers=headers, params=querystring)
 data = json.loads(response.text)

 return (data["rating"])


def getMovieID(movieName):


 url = "https://imdb8.p.rapidapi.com/title/find"

 querystring1 = {"q":movieName}

 headers = {
		"X-RapidAPI-Key": "8a67def28cmsh0bf8c467709ccdfp1df2ddjsncc7b6e252b1d",
		"X-RapidAPI-Host": "imdb8.p.rapidapi.com"
	}

 response = requests.request("GET", url, headers=headers, params=querystring1)
 data = json.loads(response.text)
 a = json.dumps(data["results"])
 a = a[9:26]
 
 return(a.replace("/","").replace("title",""))
 


def getDuration(ID):
 url = "https://imdb8.p.rapidapi.com/title/get-details"

 querystring = {"tconst":ID}

 headers = {
	"X-RapidAPI-Key": "8a67def28cmsh0bf8c467709ccdfp1df2ddjsncc7b6e252b1d",
	"X-RapidAPI-Host": "imdb8.p.rapidapi.com"
 }

 response = requests.request("GET", url, headers=headers, params=querystring)
 data = json.loads(response.text)
 return(data["runningTimeInMinutes"])



with st.container():
    st.title("IMDb API movie details")
    name = st.text_input("Please enter the movie name!")
    
    submit = st.button("Grab the details")
    if submit and name:
        id = str(getMovieID(name))
        st.text("Movie Rating: "+ str(getRating(id)))
        st.text("Movie duration: " + str(getDuration(id)) + " minutes")
    
    
    
# def getReleaseDate(ID):
#  url = "https://imdb8.p.rapidapi.com/title/get-top-crew"


#  querystring = {"tconst":ID}

#  headers = {
# 	"X-RapidAPI-Key": "8a67def28cmsh0bf8c467709ccdfp1df2ddjsncc7b6e252b1d",
# 	"X-RapidAPI-Host": "imdb8.p.rapidapi.com"
#  }

#  response = requests.request("GET", url, headers=headers, params=querystring)
#  data = json.loads(response.text)
#  print(data)

# getReleaseDate("tt4565380")