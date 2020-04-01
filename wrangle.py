import os
import tabula
import pandas as pd
 

def get_ny_employment():
	employment = pd.read_excel(os.path.join(os.getcwd(), "data/ny_employment.xlsx"))
	employment = employment.dropna(axis=1,how='all')
	employment = employment.dropna(axis=0, how="any").reset_index(drop = True)
	employment.columns = ["naics_code","industry","2019","2021","net_change","pct_change"]
	employment.naics_code = employment.naics_code.astype(int)
	employment['2019'] = employment['2019'].astype(int)
	employment['2021'] = employment['2021'].astype(int)
	industry_codes = [601,11,21,22,23,31,42,44,48,51,1023,1024,61,62,71,72,81,9,]

	employment_inds = employment[employment.naics_code.isin(industry_codes)]

	return employment_inds


def get_nj_employment():
    nj_dir = os.path.join(os.getcwd(),"data/nj_employment.xlsx")
    employment = pd.read_excel(nj_dir,sheet_name=0).dropna(axis=0, how="all").dropna(axis=0,how="all").loc[4:22]
    employment.columns = ["industry","2016","2026","net_change","pct_change"]
    employment = employment.reset_index(drop = True)
    return employment


def get_ca_employment():
    ca_dir = os.path.join(os.getcwd(),"data/ca_employment.xlsx")
    employment = pd.read_excel(ca_dir,sheet_name=0).dropna(axis=0, how="all").dropna(axis=0,how="all").loc[4:273]
    employment.columns = ['naics_1',"naics_code_2","industry","2019","2021","net_change","pct_change"]
    employment = employment.reset_index(drop = True)
    return employment


def get_pa_employment():
    pa_dir = os.path.join(os.getcwd(),"data/pa_employment.xlsx")
    employment = pd.read_excel(pa_dir,sheet_name=0).dropna(axis=0, how="all").dropna(axis=0,how="all")
    employment = employment.loc[5:120].drop(columns = "Unnamed: 6")
    employment.columns = ["naics_code","industry","2019","2021","net_change","pct_change"]
    return employment


def get_az_employment():
    az_dir = os.path.join(os.getcwd(),"data/az_employment.xlsx")
    employment = pd.read_excel(az_dir,sheet_name=0).dropna(axis=0, how="all").dropna(axis=0,how="all")
    employment = employment.iloc[2:110,[0,1,2,3]]
    employment.columns = ["naics_code","industry","2019","2021",]
    employment = employment.reset_index()
    return employment


def get_wa_employment():
    wa_dir = os.path.join(os.getcwd(),"data/wa_employment.xlsx")
    employment = pd.read_excel(wa_dir,sheet_name="Washington State").dropna(axis=0, how="all").dropna(axis=0,how="all")
    employment = employment.loc[4:]
    employment.columns = ["industry","2019","2021","pct_change"]
    employment = employment.reset_index(drop = True)
    return employment


def get_nc_employment():
    nc_dir = os.path.join(os.getcwd(),"data/nc_employment.xlsx")
    employment = pd.read_excel(nc_dir,sheet_name="Public 2019-2021, ALL").dropna(axis=0, how="all").dropna(axis=0,how="all")
    employment = employment.iloc[2:133,[0,1,2,3,4,5]]
    employment.columns = ["naics_code","industry","industry_lvl","2019","2021","net_change"]
    employment = employment.reset_index(drop = True)
    return employment


def get_ut_employment():
    dir_ = os.path.join(os.getcwd(),"data/ut_employment.csv")
    employment = pd.read_csv(dir_,sep='\t',encoding='utf-16')
    employment.columns = ["industry", "2019","2021","net_change","pct_change"]
    return employment


def get_ak_employment():
    dir_ = os.path.join(os.getcwd(),"data/ak_employment.xlsx")
    employment = pd.read_excel(dir_,sheet_name=0).dropna(axis=0, how="all").dropna(axis=0,how="all")
    employment = employment.iloc[2:55,]
    employment.columns = ["industry_lvl0","industry_lvl1","industry_lvl2","industry_lvl3",
                          "industry_lvl4","2016","2026","net_change","pct_change"]
    employment = employment.reset_index(drop = True)
    return employment


def get_ar_employment():
    dir_ = os.path.join(os.getcwd(),"data/ar_employment.xlsx")
    employment = pd.read_excel(dir_,sheet_name=0).dropna(axis=0, how="all").dropna(axis=0,how="all")
    employment.columns = ["naics_code","industry","2018","2020","net_change","pct_change"]
    employment = employment.loc[1:]
    employment = employment.reset_index(drop = True)
    return employment


def get_de_employment():
    dir_ = os.path.join(os.getcwd(),"data/de_employment.csv")
    employment = pd.read_csv(dir_).dropna(axis=0, how="all").dropna(axis=0,how="all")
    employment = employment.iloc[:,[0,1,3]]
    employment.columns = ["industry","2019","2021"]
    return employment


def get_fl_employment():
    dir_ = os.path.join(os.getcwd(),"data/fl_employment.xlsx")
    employment = pd.read_excel(dir_,sheet_name=0).dropna(axis=0, how="all").dropna(axis=0,how="all")
    employment = employment.loc[6:]
    employment.columns = ["naics_code","industry","2019","2021","net_change","pct_change"]
    employment = employment.reset_index(drop = True)
    return employment


def get_hi_employment():
    dir_ = os.path.join(os.getcwd(),"data/hi_employment.xlsx")
    employment = pd.read_excel(dir_,sheet_name=0).dropna(axis=0, how="all").dropna(axis=0,how="all")
    employment = employment.iloc[2:115,[0,1,2,3,4,5]]
    employment.columns = ["naics_code","industry","2019","2021","net_change","pct_change"]
    employment = employment.reset_index(drop = True)
    return employment


def get_id_employment():
    dir_ = os.path.join(os.getcwd(),"data/id_employment.xlsx")
    employment = pd.read_excel(dir_,sheet_name=0).dropna(axis=0, how="all").dropna(axis=0,how="all")
    employment = employment.iloc[:,[0,1,2,3,4,5]]
    employment.columns = ["naics_code","industry","2016","2026","net_change","pct_change"]
    
    return employment


def get_il_employment():
    dir_ = os.path.join(os.getcwd(),"data/il_employment.xlsx")
    employment = pd.read_excel(dir_,sheet_name=0).dropna(axis=0, how="all").dropna(axis=0,how="all")
    employment = employment.iloc[1:,[0,1,2,3,4,5]]
    employment.columns = ["naics_code","industry","2019","2021","net_change","pct_change"]
    employment = employment.reset_index(drop = True)
    
    return employment


def get_ia_employment():
    dir_ = os.path.join(os.getcwd(),"data/ia_employment.xlsx")
    employment = pd.read_excel(dir_).dropna(axis=0, how="all").dropna(axis=1,how="all")
    employment = employment.iloc[3:96,[0,1,2,3,4,5]]
    employment = employment.reset_index(drop=True)
    employment.columns = ["industry","naics_code","2019","2021","net_change","pct_change"]
    return employment


def get_ks_employment():
    dir_ = os.path.join(os.getcwd(),"data/ks_employment.xlsx")
    employment = pd.read_excel(dir_).dropna(axis=0, how="all").dropna(axis=1,how="all")
    employment = employment.iloc[4:133,[0,1,2,3,4,5]]
    employment = employment.reset_index(drop=True)
    employment.columns = ["naics_code","industry","2018","2020","net_change","pct_change"]
    return employment


def get_la_employment():
    dir_ = os.path.join(os.getcwd(),"data/la_employment.xlsx")
    employment = pd.read_excel(dir_).dropna(axis=0, how="all").dropna(axis=1,how="all")
    employment = employment.loc[6:141]
    employment = employment.reset_index(drop=True)
    employment.columns = ["industry","naics_code","2016","2026","net_change","pct_change"]
    return employment





def get_covid_data(date):
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{}.csv".format(date)
    covid19_df = pd.read_csv(url, index_col=0)
    covid19_df = covid19_df.reset_index()
    covid19_df = covid19_df[covid19_df["Country_Region"] == "US"]
    return covid19_df


def get_ok_employment():
    dir_ = os.path.join(os.getcwd(),"data/ok_employment.xlsx")
    employment = pd.read_excel(dir_,sheet_name="Industry").dropna(axis=0, how="all").dropna(axis=0,how="all")
    employment = employment.loc[3:146]
    employment.columns = ["industry","2019","2021","net_change","pct_change"]
    employment = employment.reset_index(drop = True)
    return employment


def get_nv_employment():
    dir_ = os.path.join(os.getcwd(),"data/nv_employment.xlsx")
    employment = pd.read_excel(dir_,sheet_name=0).dropna(axis=0, how="all").dropna(axis=0,how="all")
    employment = employment.iloc[3:,[0,1,2,3,4]]
    employment.columns = ["industry_type","naics_code","industry","2018","2020"]
    employment = employment.reset_index(drop = True)
    return employment


def get_ga_employment():
    dir_ = os.path.join(os.getcwd(),"data/ga_employment.xlsx")
    employment = pd.read_excel(dir_,sheet_name=0).dropna(axis=0, how="all").dropna(axis=0,how="all")
    employment = employment.iloc[8:123,[0,1,2,3]]
    employment.columns = ["naics_code","industry","2019","2021"]
    employment = employment.reset_index(drop = True)
    return employment


def get_population_data():
    url = "https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/state/detail/SCPRC-EST2019-18+POP-RES.csv"
    df = pd.read_csv(url)
    return df


def get_gdp_by_states(data_dir):
    gdp_df = tabula.read_pdf(data_dir, pages = 7)
    gdp_df = gdp_df[0].iloc[3:,[0,1,2,3,4]]
    gdp_df = pd.concat([gdp_df,gdp_df["Millions of dollars"].str.split(" ",expand = True)],axis=1)
    gdp_df = gdp_df.drop(columns=["Millions of dollars","Unnamed: 3",5,6,7,8])
    gdp_df.columns = ["areas","2018-1","2018-2","2018-3","2018-4","2019-1","2019-2","2019-3"]
    gdp_df = gdp_df.reset_index(drop=True)
    
    return gdp_df


def get_gdp_pct_by_states_by_inds(data_dir):
    
    # part 1
    gdp_by_state_by_inds_p1 = tabula.read_pdf(data_dir,pages = 5)
    gdp_by_state_by_inds_p1 = gdp_by_state_by_inds_p1[0]
    gdp_by_state_by_inds_p1 = gdp_by_state_by_inds_p1.dropna(axis=0, how='all').dropna(axis=1, how='all')
    gdp_by_state_by_inds_p1 = gdp_by_state_by_inds_p1.loc[5:]
    gdp_by_state_by_inds_p1 = pd.concat([gdp_by_state_by_inds_p1,gdp_by_state_by_inds_p1[
                                            'Seasonally adjusted at annual rates'].str.split(" ", expand=True)], axis=1)
    gdp_by_state_by_inds_p1 = gdp_by_state_by_inds_p1.drop(columns=['Seasonally adjusted at annual rates'])
    gdp_by_state_by_inds_p1 = pd.concat([gdp_by_state_by_inds_p1,gdp_by_state_by_inds_p1[
                                            'Unnamed: 8'].str.split(" ", expand=True)], axis=1)
    gdp_by_state_by_inds_p1 = gdp_by_state_by_inds_p1.drop(columns=['Unnamed: 8'])
    cols = ["areas", "states_overall","Agriculture,forestry, fishing insuranceand hunting", 
            "Mining,quarrying, and oil and gas extraction","Utilities","Construction", 
            "Retail trade","Transportation and warehousing","Durable goods manufacturing",
            "Nondurable goods manufacturing", "Wholesale trade", "Information", 
            "Finance and insurance"]
    gdp_by_state_by_inds_p1.columns = cols
    gdp_by_state_by_inds_p1 = gdp_by_state_by_inds_p1.reset_index(drop=True)

    #part 2
    gdp_by_state_by_inds_p2 = tabula.read_pdf(data_dir, pages = 6)

    gdp_by_state_by_inds_p2 = gdp_by_state_by_inds_p2[0]
    gdp_by_state_by_inds_p2 = gdp_by_state_by_inds_p2[2:]

    gdp_by_state_by_inds_p2[["Real estate and rental and leasing",
                      "Professional, scientific, and technical services"]] = gdp_by_state_by_inds_p2["Unnamed: 1"].str.split(" ",expand = True)

    gdp_by_state_by_inds_p2[["Educational services",
                      "Health care and social assistance"]] = gdp_by_state_by_inds_p2[
                                                            "Seasonally adjusted at annual rates"
                                                                                  ].str.split(" ", expand = True)
    gdp_by_state_by_inds_p2[["Other services (except government and government enterprises)",
                      "Government and government enterprises"]] = gdp_by_state_by_inds_p2["Unnamed: 14"].str.split(" ", expand = True)
    gdp_by_state_by_inds_p2 = gdp_by_state_by_inds_p2.drop(
                        columns= ["Unnamed: 1","Unnamed: 14","Seasonally adjusted at annual rates"])
    gdp_by_state_by_inds_p2 = gdp_by_state_by_inds_p2.dropna(axis=1)
    name_dic = {"Unnamed: 0":"areas",
                "Unnamed: 2":"Management of companies and enterprises",
                "Unnamed: 5":"Administrative and support and waste management and remediation services",
                "Unnamed: 9":"Arts, entertainment, and recreation", 
                "Unnamed: 11":"Accomodation and food services"}
    gdp_by_state_by_inds_p2 = gdp_by_state_by_inds_p2.rename(columns=name_dic)
    gdp_by_state_by_inds_p2 = gdp_by_state_by_inds_p2.reset_index(drop=True)
    # JOIN
    gdp_by_state_by_inds = pd.concat([gdp_by_state_by_inds_p1,gdp_by_state_by_inds_p2], axis = 1,)
    gdp_by_state_by_inds.columns = gdp_by_state_by_inds.columns.str.replace(
                                                "\)|\(|,| ","_").str.replace("__","_").str.lower()
    gdp_by_state_by_inds = gdp_by_state_by_inds.iloc[:,~gdp_by_state_by_inds.columns.duplicated()]
    return gdp_by_state_by_inds