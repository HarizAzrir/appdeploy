import streamlit as st

import folium

import pandas as pd
import numpy as np



def popup_html(row,df):
    col_list = list(df.columns)
    col_dict = {}

    for i in range(len(col_list)):
        col_dict.update({col_list[i]:df[col_list[i]][row]})

    keys = list(col_dict.keys())
    values = list(col_dict.values())


    left_col_color = "#ADD8E6"
    right_col_color = "#f2f0d3"
    
    html = """<!DOCTYPE html>
<html>
<head>
<h4 style="margin-bottom:10"; width="200px">{}</h4>""".format(values[0]) + """
</head>
    <table style="height: 126px; width: 350px;">
<tbody>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[1]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[1]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[2]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[2]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[3]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[3]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[4]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[4]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[5]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[5]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[6]) +""" </span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[6]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[7]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[7]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[8]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[8]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[9]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[9]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[10]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[10]) + """
</tr><tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[11]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[11]) + """
</tr><tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[12]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[12]) + """
</tr><tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[13]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[13]) + """
</tr><tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[14]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[14]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[15]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[15]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[16]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[16]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[17]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[17]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[18]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[18]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[19]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[19]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[20]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[20]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[21]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[21]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[22]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[22]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[23]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[23]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[24]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[24]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[25]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[25]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[26]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[26]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[27]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[27]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[28]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[28]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[29]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[29]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[30]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[30]) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";">{}</td>""".format(keys[31]) +"""</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(values[31]) + """
</tr>
</tbody>
</table>
</html>
"""
    return html

st.set_page_config(layout='wide')

st.title('Laundromat analytics')

df = pd.read_csv('data_weather.csv')

pos = df[['latitude','longitude']]

df['Date_Time'] = pd.to_datetime(df['Date_Time'])

time_option = st.selectbox('Select time:',
                          ('Early Morning','Morning','Night','Everning','None'))

month_option = st.selectbox('select month:',
                           (1,2,3,4,5,6,7,8,9,10,11,12,'None')
                           )


year_option = st.selectbox ('Select Year',
                            (2015,2016)
                            )

st.write('You Selected:',time_option,month_option,year_option)


map = folium.Map(location=[df.latitude.mean(),df.longitude.mean()], tiles="OpenStreetMap", zoom_start=11, control_scale=True)
folium.vector_layers.Marker(location=[df.latitude.mean(),df.longitude.mean()], tooltip='Dobi',icon=folium.Icon(color="green")).add_to(map)


df['year'] = pd.DatetimeIndex(df['Date_Time']).year
df['month'] = pd.DatetimeIndex(df['Date_Time']).month

df_year = df.loc[df['year'] == year_option]
df_year.reset_index(drop = True,inplace = True)

if (month_option == 'None'):
    df_month = df_year
else :
    df_month = df_year.loc[df_year['month'] == month_option]
    df_month.reset_index(drop = True,inplace = True)

if(time_option == "None"):
    df_time = df_month
else:
    df_time = df_month.loc[df_month['Time_Bin'] == time_option]
    df_time.reset_index(inplace =True)
print(df_time)



data = st.dataframe(data = df_time)

if st.button('save dataframe'):
    open('data.csv', 'w').write(df.to_csv())


for i in range (df_time.shape[0]) :
    html = popup_html(i,df)
    popup  = folium.Popup(folium.Html(html,script = True), max_width=600, max_height=600)
    folium.vector_layers.Marker(location=[df_time.latitude[i],df_time.longitude[i]], tooltip=i,popup = popup).add_to(map)
    print('yum',i)

map
print(map)
print('done')
