import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

url = "https://kinogo.biz/istoricheskie/"

# The path to the ChromeDriver is specified
chrome_driver_path = "D:\chromedriver_win32\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)

options = webdriver.ChromeOptions()

# Create a browser instance with the given options
browser = webdriver.Chrome(service=service, options=options)

browser.get(url)

# Set an explicit wait condition
wait = WebDriverWait(browser, 10)

# Wait until elements with class "shortstory" become visible
movie_elements = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".shortstory")))

movies = []

for movie_element in movie_elements:
    title_element = movie_element.find_elements(By.CSS_SELECTOR, ".shortstory__title")
    if title_element:
        title = title_element[0].text
        link = title_element[0].find_element(By.TAG_NAME, "a").get_attribute("href")

        # Get the year of release, country and description of the movie
        movie_info_element = movie_element.find_element(By.CSS_SELECTOR, ".shortstory__info")
        movie_info = movie_info_element.text
        year = None
        country = None
        description = None
        # Split the string into parts
        movie_info_parts = movie_info.split("\n")
        if len(movie_info_parts) > 0:
            year = movie_info_parts[0].split(":")[1].strip()
        if len(movie_info_parts) > 1:
            country = movie_info_parts[1].split(":")[1].strip()
        if len(movie_info_parts) > 2:
            description = movie_info_parts[2]
        # Add movie data to dictionary
        movies.append({"title": title, "link": link, "year": year, "country": country, "description": description})

# Create a DataFrame from a dictionary
df = pd.DataFrame(movies, columns=["title", "year", "country", "description", "link"])
print(df)

# Save DataFrame to file
df.to_excel("historical_movies.xlsx", index=False)

# Close browser after use
browser.quit()
