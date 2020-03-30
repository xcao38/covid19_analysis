import os
import pandas as pd
 

def get_ny_employment():
	employment_ny = pd.read_excel(os.path.join(os.getcwd(), "data/2019-2021-Statewide-Short-Term-Industry-Projections.xlsx"))
	employment_ny = employment_ny.dropna(axis=1,how='all')
	employment_ny = employment_ny.dropna(axis=0, how="any").reset_index(drop = True)
	employment_ny.columns = ["naics_code","industry","2019","2021","net_change","pct_change"]
	employment_ny.naics_code = employment_ny.naics_code.astype(int)
	employment_ny['2019'] = employment_ny['2019'].astype(int)
	employment_ny['2021'] = employment_ny['2021'].astype(int)
	industry_codes = [601,11,21,22,23,31,42,44,48,51,1023,1024,61,62,71,72,81,9,]

	employment_ny_inds = employment_ny[employment_ny.naics_code.isin(industry_codes)]

	return employment_ny_inds


def get_covid_data(date):
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{}.csv".format(date)
    covid19_df = pd.read_csv(url, index_col=0)
    covid19_df = covid19_df.reset_index()
    covid19_df = covid19_df[covid19_df["Country_Region"] == "US"]
    return covid19_df


def get_population_data():
    url = "https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/state/detail/SCPRC-EST2019-18+POP-RES.csv"
    df = pd.read_csv(url)
    return df