# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Code starts here
df = pd.read_csv(path)
df['state'] = df['state'].apply(lambda x:x.lower())
df['total'] = df['Jan']+df['Feb']+df['Mar']
sum_row=df[["Jan","Feb","Mar","total"]].sum()
sum_df=pd.DataFrame(data=sum_row).T
df_final=df.append(sum_df,ignore_index=True)
# Code ends here


# --------------
import requests

# Code starts here
url = 'https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'
response = requests.get(url)
df1 = pd.read_html(response.content)[0]
headers = df1.iloc[11]
df1 = pd.DataFrame(df1.values[12:],columns=headers)
df1['United States of America'].apply(lambda x: x.strip())

# Code ends here


# --------------
df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)

# Code starts here
mapping=df1.set_index('United States of America')['US'].to_dict()
df_final['abbr']=df_final['state'].map(mapping)


# Code ends here


# --------------
# Code stars here




df_final ['abbr']=np.where(df_final['state']=='mississipi','MS',np.where(df_final['state']=='tenessee','TN','MS'))


# Code ends here


# --------------
# Code starts here

# Calculate the total amount
df_sub=df_final[["abbr", "Jan", "Feb", "Mar", "total"]].groupby("abbr").sum()
print(df_sub.shape)
# Add the $ symbol
formatted_df = df_sub.applymap(lambda x: "${:,.0f}".format(x))

# Code ends here


# --------------
# Code starts here
sum_row=df[["Jan","Feb","Mar","total"]].sum()
sum_df=pd.DataFrame(data=sum_row).T
df_sub_sum = sum_df.applymap(lambda x:"${:,.0f}".format(x))
final_table = formatted_df.append(df_sub_sum)
final_table = final_table.rename(index={0:'Total'})


# Code ends here


# --------------
# Code starts here
# Calculate the total
df_sub['total'] = df_sub['Jan'] + df_sub['Feb'] + df_sub['Mar']

# Plot the pie chart    
df_sub['total'].plot(kind='pie')


# Code ends here



