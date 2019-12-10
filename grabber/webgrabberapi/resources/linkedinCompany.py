from scrape_linkedin import CompanyScraper
import pandas as pd


class companyLinkedin(object):
    def __init__(self, cpNames):
        self.cpNames = cpNames
        self.companyData = []

    def getCompanyData(self):
        with CompanyScraper(cookie='AQEDAS6InWoCpYoDAAABbtrZyx8AAAFu_uZPH00Aq-Oq6Jl03e0UOg0qtlrADIM9OoDsKDBN_-4bHeRmqC4-0fJ-GSv9F66-O8SZY2GpuaojYtoKPvpU32fmdVXwxr-IzYl_otB8ADTv5BuayrVdQ5d_') as scraper:
            for name in self.cpNames:
                try:
                    overview = scraper.scrape(company=name).overview
                    overview['company_name'] = name
                    self.company_data.append(overview)
                except:
                    pass

    def getJson(self):
        df = pd.DataFrame(self.companyData)
        df.to_csv('out.csv', index=False)
        return df.to_json()