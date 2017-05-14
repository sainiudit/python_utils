from pandas.io.json import json_normalize
All_data=pd.read_csv('all_indian_school_new_url.csv')
All_data['json_school_details']=All_data.json_school_details.apply(lambda x:json.loads(x))
dict_col = All_data.pop('json_school_details')
All_data=pd.concat([All_data, dict_col.apply(pd.Series)], axis=1)