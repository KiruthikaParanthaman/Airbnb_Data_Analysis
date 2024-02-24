# importing necessary packages
import streamlit as st
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import streamlit_option_menu
from pprint import pprint
import pandas as pd
from pymongo import MongoClient 
import certifi
import re
import ast
from PIL import Image

#importing data from mongodb cluster
# ca = certifi.where()
# client = MongoClient("mongodb+srv://username:pwd@mongodb.4r5lo5j.mongodb.net/",tlsCAFile=ca) 
# mydb = client['sample_airbnb']

#connecting to sample_airbnb from local system after downloading sample airbnb dataset
client = MongoClient("mongodb://localhost:27017/") 
mydb = client['airbnb']
mycol = mydb['airbnb_project']
x=mycol.find()

#Convert json data to dataframe
df = pd.json_normalize(x)

#Selecting necessary columns
df_new = df[['_id','name','address.street','address.suburb','address.government_area','address.market','address.country',
'address.country_code','address.location.coordinates','price',
'security_deposit','cleaning_fee','extra_people','minimum_nights','maximum_nights','cancellation_policy','accommodates','guests_included',
'property_type','room_type','bed_type','bedrooms','beds','bathrooms','amenities','summary','transit','interaction',
'availability.availability_30','availability.availability_60','availability.availability_90','availability.availability_365','number_of_reviews',
'review_scores.review_scores_accuracy','review_scores.review_scores_cleanliness','review_scores.review_scores_checkin',
'review_scores.review_scores_communication','review_scores.review_scores_location','review_scores.review_scores_value',  
'review_scores.review_scores_rating','host.host_response_time','host.host_response_rate','host.host_is_superhost','host.host_listings_count']]

#Renaming columns
df_renamed=df_new.rename(columns = {'address.street':'street','address.suburb':'suburb','address.government_area':'government_area',
   'address.market':'market','address.country':'country','address.country_code' :'country_code',
'address.location.coordinates':'location_coordinates','availability.availability_30':'avail_30','availability.availability_60':'avail_60','availability.availability_90':'avail_90',
'availability.availability_365':'avail_365','review_scores.review_scores_accuracy':'accuracy_score',
'review_scores.review_scores_cleanliness':'cleanliness_score','review_scores.review_scores_checkin':'checkin_score',
 'review_scores.review_scores_communication':'communication_score','review_scores.review_scores_location':'location_score',
'review_scores.review_scores_value':'value_score','review_scores.review_scores_rating':'rating_score',
'host.host_response_time':'host_response_time','host.host_response_rate':'host_response_rate',
'host.host_is_superhost':'host_is_superhost','host.host_listings_count':'host_listings_count'})

#Datatype conversion
col1 =['price','cleaning_fee','security_deposit']
col2 = ['extra_people','minimum_nights','maximum_nights','accommodates','guests_included']
col3 = ['beds','bedrooms']
for i in col1:
    df_renamed[i] = df_renamed[i].astype(str).astype(float)
for i in col2:
    df_renamed[i] = df_renamed[i].astype(str).astype(float).round().astype(int)

for i in col3:
     df_renamed[i] = df_renamed[i].round().astype('Int64')    
df_renamed['bathrooms']=df_renamed['bathrooms'].astype('str').astype('float').round().astype('Int64')


#Handling Nan values
#Replacing Nan security depsoit with values zero,cleaning_fee nan values with zero.bedrooms,beds,bathrooms with 1
#and other values with average
df_renamed['security_deposit'].describe()
df_renamed['security_deposit']= df_renamed['security_deposit'].fillna(0)
df_renamed['cleaning_fee']= df_renamed['cleaning_fee'].fillna(0)
df_renamed['bedrooms'] = df_renamed['bedrooms'].fillna(1)
df_renamed['beds'] = df_renamed['beds'].fillna(1)
df_renamed['bathrooms'] = df_renamed['bathrooms'].fillna(1)
df_renamed['accuracy_score'] = df_renamed['accuracy_score'].fillna(df_renamed['accuracy_score'].mean())
df_renamed['cleanliness_score'] = df_renamed['cleanliness_score'].fillna(df_renamed['cleanliness_score'].mean())
df_renamed['checkin_score'] = df_renamed['checkin_score'].fillna(df_renamed['checkin_score'].mean())
df_renamed['communication_score'] = df_renamed['communication_score'].fillna(df_renamed['communication_score'].mean())
df_renamed['location_score'] = df_renamed['location_score'].fillna(df_renamed['location_score'].mean())
df_renamed['value_score'] = df_renamed['value_score'].fillna(df_renamed['value_score'].mean())
df_renamed['rating_score'] = df_renamed['rating_score'].fillna(df_renamed['rating_score'].mean())
df_renamed['host_response_time'] = df_renamed['host_response_time'].fillna('within an hour')
df_renamed['host_response_rate'] = df_renamed['host_response_rate'].fillna(df_renamed['host_response_rate'].mean())

#Removing spaces and camelcasing street name to avoid duplicates
df_renamed['street'] = df_renamed['street'].apply(lambda x: re.sub(r'\s', '', x))
df_renamed['street'] = df_renamed["street"].str.title()

#Creating rating column with 10 score
df_renamed['rating'] = (df_renamed['rating_score']/10).round(2)

#column to display name,rating,price,street in dropdown 
df_renamed['display'] = df_renamed["name"] + " Rating : " + df_renamed['rating'].astype('str') + ' ⭐ '+ " price :" + (df_renamed["price"].astype('str')) + ' ' + df_renamed['street']

#Converting location co-ord string to list and splitting to lat and long column
df_renamed['location_coordinates']= df_renamed['location_coordinates'].apply(lambda x :ast.literal_eval(str(x)))
df_renamed['longitude'] = df_renamed['location_coordinates'].apply(lambda x : x[0])
df_renamed['latitude'] = df_renamed['location_coordinates'].apply(lambda x : x[1])


#Select country names
country_list = df_renamed['country'].unique().tolist()

#Handling missing values in market
df_renamed.loc[(df_renamed['country']=="Brazil") & (df_renamed['market']== ""),['market']]="Rio De Janeiro"
df_renamed.loc[(df_renamed['_id'] == "13528649" ),['market']] = "New York"
df_renamed.loc[(df_renamed['_id'] == "14234514" ),['market']] = "Kapaa"
df_renamed.loc[(df_renamed['_id'] == "13702505" ),['market']] = "Montreal"
df_renamed.loc[(df_renamed['_id'] == "14161732" ),['market']] = "Barcelona"
df_renamed.loc[(df_renamed['_id'] == "13363311" ),['market']] = "Waverley"

#getting market list countrywise

# portugal_market = ['Porto', 'Other (International)']
# brazil_market = ['Rio De Janeiro','Other (International)']
# us_market = ['Oahu','New York','The Big Island','Maui','Kauai','Kapaa','Other (Domestic)']
# turkey_market = ['Istanbul', 'Other (International)']
# canada_market = ['Montreal']
# hongkong_market = ['Hong Kong']
# spain_market = ['Barcelona']
# australia_market = ['Sydney', 'Waverley']
# china_market = ['Hong Kong']

portugal_market = df_renamed.loc[df_renamed['country']=="Portugal",['market']]['market'].unique().tolist()
brazil_market = df_renamed.loc[df_renamed['country']=="Brazil",['market']]['market'].unique().tolist()
us_market = df_renamed.loc[df_renamed['country']=="United States",['market']]['market'].unique().tolist()
turkey_market = df_renamed.loc[df_renamed['country']=="Turkey",['market']]['market'].unique().tolist()
canada_market = df_renamed.loc[df_renamed['country']=="Canada",['market']]['market'].unique().tolist()
hongkong_market = df_renamed.loc[df_renamed['country']=="Hong Kong",['market']]['market'].unique().tolist()
spain_market = df_renamed.loc[df_renamed['country']=="Spain",['market']]['market'].unique().tolist()
australia_market = df_renamed.loc[df_renamed['country']=="Australia",['market']]['market'].unique().tolist()
china_market = df_renamed.loc[df_renamed['country']=="China",['market']]['market'].unique().tolist()

def market_list(country_name):
    if country_name == "Portugal":
        return portugal_market
    elif country_name == "Brazil":
        return brazil_market
    elif country_name == "United States":
        return us_market
    elif country_name == "Turkey":
        return turkey_market
    elif country_name == "Canada":
        return canada_market
    elif country_name == "Hong Kong":
        return hongkong_market
    elif country_name == "Spain":
        return spain_market
    elif country_name == "Australia":
        return australia_market
    else:
        return china_market
    
# Function to return street list based on selection
def street_list(country,area):
    street = df_renamed.loc[(df_renamed['country']==country) & (df_renamed['market']==area),['street']].street.unique().tolist()
    street.sort()
    return street

# Function to return hotel list based on selection
def hotel_list(country_name,area_name):
    hotel_li = df_renamed.loc[(df_renamed['country']==country_name) & (df_renamed['market']==area_name),['display','latitude','longitude','property_type','accommodates','room_type']]
    return hotel_li

# Function to display hotel details
def hotel_details(hotel_name):
    df_hotel_details = df_renamed.loc[(df_renamed['display']==hotel_name),['name','street','market','property_type','room_type','bedrooms','beds','bathrooms','accommodates','rating','price','security_deposit','cleaning_fee','amenities',]]
    return df_hotel_details

st.set_page_config(page_title="Airbnb Analysis", layout="wide", initial_sidebar_state="collapsed", menu_items=None)
image = Image.open("E:\\Winnie Documents\\Guvi\project\\Airbnb Analysis\\ban1.jpg")
st.image(image)
# st.markdown("<h2 style='text-align: center; color: Red;'> Airbnb bookings</h2>", unsafe_allow_html=True)
st.divider()

col1,col2,col3 = st.columns([1,3,1])
with col2:
    c1,c2 = st.columns([1,1])
    with c1:
        country = st.selectbox("Select country/Region",options = ['Portugal','Brazil','United States','Turkey','Canada','Hong Kong','Spain','Australia','China'])
        
    with c2:
         market = st.selectbox("Select area",options = market_list(country))
    
col4,col5,col6 = st.columns([1,1,1])
    
with col4:
    hotel_li = hotel_list(country,market)
    hotels = st.selectbox("select hotel",hotel_li.display.tolist())
    st.map(hotel_li,latitude = hotel_li['latitude'],longitude = hotel_li['longitude'])
       

with col5:
    st.write("")
    st.write("")
    with st.container(border=True):
        df_hotel_details = hotel_details(hotels)
        r1,r2 = st.columns([1.25,2.75])
        with r1:
            st.write("**Name** ")
            st.write("**Rating**")
            st.write("**Price**")
            st.write("**Street** ")
            st.write("**Market**")
            st.write("**Property_type**")
            st.write("**room_type**")
            st.write("**Bedrooms**")
            st.write("**Beds**")
            st.write("**Accommodates**")
            st.write("**Bathrooms**")
            st.write("**security_deposit**")
            st.write("**Cleaning_fee** ")
            st.write("**Amenities**")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

        with r2:
            st.write(f"{(df_hotel_details['name'].to_string(index=False))}")
            st.write(f"{(df_hotel_details['rating'].to_string(index=False))} ⭐")
            st.write(f"{(df_hotel_details['price'].to_string(index=False))}")
            st.write(f"{(df_hotel_details['street'].to_string(index=False))}")
            st.write(f"{(df_hotel_details['market'].to_string(index=False))}")
            st.write(f"{(df_hotel_details['property_type'].to_string(index=False))}")
            st.write(f"{(df_hotel_details['room_type'].to_string(index=False))}")
            st.write(f"{(df_hotel_details['bedrooms'].to_string(index=False))}")
            st.write(f"{(df_hotel_details['beds'].to_string(index=False))}")
            st.write(f"{(df_hotel_details['accommodates'].to_string(index=False))}")
            st.write(f"{(df_hotel_details['bathrooms'].to_string(index=False))}")
            st.write(f"{(df_hotel_details['security_deposit'].to_string(index=False))}")
            st.write(f"{(df_hotel_details['cleaning_fee'].to_string(index=False))}")
            amen = df_hotel_details['amenities'].to_list()
            mystr = " ".join(map(str, amen))
            mystr = mystr.replace("[","")
            mystr = mystr.replace("]","")
            st.markdown(f"{mystr}")
with col6:
    
    #Price Bar chart histogrm display based on country market and accomodates.axvline to draw avg dash line
    acc_type = int(df_hotel_details['accommodates'].to_string(index=False))
    hotel_price = round(float(df_hotel_details['price'].to_string(index=False)))
    df_price = df_renamed.loc[(df_renamed['country']==country) & (df_renamed['market']==market)&(df_renamed['accommodates']==acc_type) ]
    plt.hist( df_price['price'], edgecolor='k' )
    plt.axvline(df_price['price'].mean(), color='k', linestyle='dashed', linewidth=1)
    plt.axvline(hotel_price, color='red', linestyle='dashed', linewidth=1)
    min_ylim, max_ylim = plt.ylim()
    plt.text(df_price['price'].mean()*1.1, max_ylim*0.9, 'Average Price: {:.2f}'.format(df_price['price'].mean()))
    plt.text(hotel_price*1.1, max_ylim*0.7, 'This hotel: {:.2f}'.format(hotel_price),color = "red")
    plt.title(f"Price chart for {market} city")
    plt.xlabel("price")
    st.pyplot(plt.gcf())

    # Rating Bar chart histogram display based on country market and accomodates
    acc_type = int(df_hotel_details['accommodates'].to_string(index=False))
    rating = float(df_hotel_details['rating'].to_string(index=False))
    df_rating = df_renamed.loc[(df_renamed['country']==country) & (df_renamed['market']==market)&(df_renamed['accommodates']==acc_type) ]
    fig, ax = plt.subplots()
    ax.hist( df_rating['rating'], edgecolor='k' )
    ax.axvline(df_rating['rating'].mean(), color='k', linestyle='dashed', linewidth=1)
    ax.axvline(rating, color='red', linestyle='dashed', linewidth=1)
    min_ylim, max_ylim = plt.ylim()
    ax.text(df_rating['rating'].mean()*0.85, max_ylim*0.9, 'Avg : {:.2f}'.format(df_rating['rating'].mean()))
    ax.text(float(rating)*0.80, max_ylim*0.7, f'This hotel : {rating}',color = "red")
    plt.title(f"Rating chart for {market} city")
    plt.xlabel("Rating")
    st.pyplot(fig)


#********************************************************************End********************************************************************************#



        
