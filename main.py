import csv
import re
import pandas as pd
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By


runtime_list = []
genres = []
certifications = []
descriptions = []
ratings = []
votes = []
titles = []
metastores = []
grosses = []

try:
    #first of all you need to identify from where it starts the only repetitif bloc
    #to use it later when elements becomes more and more nested
    url = "https://www.imdb.com/search/title/?release_date=2019&sort=num_votes,desc&page=1"
    driver = webdriver.Firefox(executable_path=r'/home/hosni/Downloads/geckodriver/geckodriver')
    driver.get(url)
    runtime = driver.find_elements(By.XPATH, "//span[@class='runtime']")
    genre = driver.find_elements(By.XPATH, "//span[@class='genre']")
    certification = driver.find_elements(By.XPATH, "//span[@class='certificate']")
    desc = driver.find_elements(By.XPATH, "//div/div/p[@class='text-muted']")
    rating = driver.find_elements(By.NAME, "ir")
    vote = driver.find_elements(By.XPATH, "//div/div/p/span[@name='nv'][1]")
    gross = driver.find_elements(By.XPATH, "//div/div/p/span[@name='nv'][2]")
    title = driver.find_elements(By.XPATH, "//div/div/h3/a[1]")
    metastore = driver.find_elements(By.XPATH, "//div/div/div/div/span[@class='metascore  mixed']")
    for i in metastore:
        metastores.append(i.text)
    for i in title:
        titles.append(i.text)
    for i in vote:
        votes.append(i.text)
    for i in gross:
        grosses.append(i.text)
    for i in rating:
        ratings.append(i.text)
    for i in desc:
        descriptions.append(i.text)
    for i in certification:
        certifications.append(i.text)
    for i in genre:
        genres.append(i.text)
    for i in runtime:
        runtime_list.append(i.text)
except Exception as e:
    pass

print("Runtime", len(runtime_list))
print("Genres", len(genres))
print("Certifications", len(certifications))
print("Description", len(descriptions))
print("Ratings", len(ratings))
print("Votes", len(votes))
print("title", len(titles))
print("metastore", len(metastores))
print("Gross", len(grosses))

s0 = pd.Series(titles, name='Movie_Title')
s1 = pd.Series(runtime_list, name='Duration')
s3 = pd.Series(certifications, name='Certification_Of_Film')
s4 = pd.Series(descriptions, name="Description_Of_Film")
s5 = pd.Series(ratings, name='Rating_Of_Film')
s6 = pd.Series(votes, name='Votes_Of_Film')
s7 = pd.Series(metastores, name='Metastores')
s8 = pd.Series(grosses, name="Gross")
df = pd.concat([s0, s1, s3, s4, s5, s6, s7, s8], axis=1)
df.to_csv("IMDB_Smatphone.csv")