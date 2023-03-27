from bs4 import BeautifulSoup
import requests,openpyxl

excel=openpyxl.Workbook()
sheet=excel.active
sheet.title="movie list"
sheet.append(['Rank','Movie name',"Year of release",'IMDB Rating'])

try:
    response=requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
    soup=BeautifulSoup(response.text,"html.parser")
    #print(soup)
    movies=soup.find("tbody",class_="lister-list").find_all("tr")
    for movie in movies:
        #print(movie)
        rank=movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]
        movie_name=movie.find('td',class_="titleColumn").a.text
        rate=movie.find('td',class_="ratingColumn").strong.text
        year=movie.find('td',class_="titleColumn").span.text.replace(')',"")
        year=year.replace('(',"")
        print(rank,movie_name,year,rate)
        sheet.append([rank,movie_name,year,rate])

except Exception as e:
    print(e)

excel.save("Movie.xlsx")