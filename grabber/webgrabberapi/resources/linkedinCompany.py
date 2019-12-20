from scrape_linkedin import CompanyScraper, Scraper
import pandas as pd


class companyLinkedin(object):
    def __init__(self, cpNames):
        self.cpNames = cpNames
        self.companyData = []
        self.coockie = 'AQEDAS6InWoFvL_lAAABbvSnHPwAAAFvGLOg_E0AAfV7ciBpclPS8rTQsqWivxB0WMh_YqPM8UsjvlkCEC-NYRxFjjDOV6c65SgxklNeSRWNfeSeq4IVHYYQOaPOVwVZxil7XrhLV-wq5z4f2ZzpRdHF'

    def getCompanyData(self):
        with CompanyScraper(cookie=self.coockie) as scraper:
            for name in self.cpNames:
                try:
                    overview = scraper.scrape(company=name).overview
                    overview['company_name'] = name
                    self.companyData.append(overview)
                except:
                    pass

    def getJson(self):
        df = pd.DataFrame(self.companyData)
        return df.to_json(orient='records')
