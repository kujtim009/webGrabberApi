"""Example to scrape a list of Companies, and put overviews in csv form"""

from scrape_linkedin import CompanyScraper
import pandas as pd

# LIST YOUR COMPANIES HERE
my_company_list = []

with open("comp.txt", "r") as f:
    for line in f.readlines():
        my_company_list.append(line.lower())


company_data = []

with CompanyScraper(cookie='AQEDAS6InWoCpYoDAAABbtrZyx8AAAFu_uZPH00Aq-Oq6Jl03e0UOg0qtlrADIM9OoDsKDBN_-4bHeRmqC4-0fJ-GSv9F66-O8SZY2GpuaojYtoKPvpU32fmdVXwxr-IzYl_otB8ADTv5BuayrVdQ5d_') as scraper:
    # Get each company's overview, add to company_data list
    counter = 0
    for name in my_company_list:
        try:

            overview = scraper.scrape(company=name).overview
            overview['company_name'] = name
            company_data.append(overview)

        except:
            pass
        

# Turn into dataframe for easy csv output
df = pd.DataFrame(company_data)
df.to_csv('out.csv', index=False)


