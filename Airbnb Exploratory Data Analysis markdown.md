### Loading Airbnb dataset


```python
# Importing Necessary packages
from pprint import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pymongo import MongoClient 
import certifi
import re
from cprint import *
import ast
```


```python
#Connecting to Mongodb database
client = MongoClient("mongodb://localhost:27017/") 
mydb = client['airbnb']
mycol = mydb['airbnb_project']
```


```python
#Extracting Data from Mongodb
x=mycol.find()
```


```python
# Convert json data to dataframe
df = pd.json_normalize(x)
```


```python
#Finding the number of Rows and Columns
print("Number of Rows :",df.shape[0])
print("Number of Columns :",df.shape[1])
```

    Number of Rows : 5555
    Number of Columns : 77
    

### Exploring data


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 5555 entries, 0 to 5554
    Data columns (total 77 columns):
     #   Column                                     Non-Null Count  Dtype         
    ---  ------                                     --------------  -----         
     0   _id                                        5555 non-null   object        
     1   listing_url                                5555 non-null   object        
     2   name                                       5555 non-null   object        
     3   summary                                    5555 non-null   object        
     4   space                                      5555 non-null   object        
     5   description                                5555 non-null   object        
     6   neighborhood_overview                      5555 non-null   object        
     7   notes                                      5555 non-null   object        
     8   transit                                    5555 non-null   object        
     9   access                                     5555 non-null   object        
     10  interaction                                5555 non-null   object        
     11  house_rules                                5555 non-null   object        
     12  property_type                              5555 non-null   object        
     13  room_type                                  5555 non-null   object        
     14  bed_type                                   5555 non-null   object        
     15  minimum_nights                             5555 non-null   object        
     16  maximum_nights                             5555 non-null   object        
     17  cancellation_policy                        5555 non-null   object        
     18  last_scraped                               5555 non-null   datetime64[ns]
     19  calendar_last_scraped                      5555 non-null   datetime64[ns]
     20  first_review                               4167 non-null   datetime64[ns]
     21  last_review                                4167 non-null   datetime64[ns]
     22  accommodates                               5555 non-null   int64         
     23  bedrooms                                   5550 non-null   float64       
     24  beds                                       5542 non-null   float64       
     25  number_of_reviews                          5555 non-null   int64         
     26  bathrooms                                  5545 non-null   object        
     27  amenities                                  5555 non-null   object        
     28  price                                      5555 non-null   object        
     29  extra_people                               5555 non-null   object        
     30  guests_included                            5555 non-null   object        
     31  reviews                                    5555 non-null   object        
     32  images.thumbnail_url                       5555 non-null   object        
     33  images.medium_url                          5555 non-null   object        
     34  images.picture_url                         5555 non-null   object        
     35  images.xl_picture_url                      5555 non-null   object        
     36  host.host_id                               5555 non-null   object        
     37  host.host_url                              5555 non-null   object        
     38  host.host_name                             5555 non-null   object        
     39  host.host_location                         5555 non-null   object        
     40  host.host_about                            5555 non-null   object        
     41  host.host_thumbnail_url                    5555 non-null   object        
     42  host.host_picture_url                      5555 non-null   object        
     43  host.host_neighbourhood                    5555 non-null   object        
     44  host.host_is_superhost                     5555 non-null   bool          
     45  host.host_has_profile_pic                  5555 non-null   bool          
     46  host.host_identity_verified                5555 non-null   bool          
     47  host.host_listings_count                   5555 non-null   int64         
     48  host.host_total_listings_count             5555 non-null   int64         
     49  host.host_verifications                    5555 non-null   object        
     50  address.street                             5555 non-null   object        
     51  address.suburb                             5555 non-null   object        
     52  address.government_area                    5555 non-null   object        
     53  address.market                             5555 non-null   object        
     54  address.country                            5555 non-null   object        
     55  address.country_code                       5555 non-null   object        
     56  address.location.type                      5555 non-null   object        
     57  address.location.coordinates               5555 non-null   object        
     58  address.location.is_location_exact         5555 non-null   bool          
     59  availability.availability_30               5555 non-null   int64         
     60  availability.availability_60               5555 non-null   int64         
     61  availability.availability_90               5555 non-null   int64         
     62  availability.availability_365              5555 non-null   int64         
     63  review_scores.review_scores_accuracy       4079 non-null   float64       
     64  review_scores.review_scores_cleanliness    4082 non-null   float64       
     65  review_scores.review_scores_checkin        4080 non-null   float64       
     66  review_scores.review_scores_communication  4081 non-null   float64       
     67  review_scores.review_scores_location       4081 non-null   float64       
     68  review_scores.review_scores_value          4080 non-null   float64       
     69  review_scores.review_scores_rating         4081 non-null   float64       
     70  security_deposit                           3471 non-null   object        
     71  cleaning_fee                               4024 non-null   object        
     72  host.host_response_time                    4167 non-null   object        
     73  host.host_response_rate                    4167 non-null   float64       
     74  weekly_price                               714 non-null    object        
     75  monthly_price                              656 non-null    object        
     76  reviews_per_month                          94 non-null     float64       
    dtypes: bool(4), datetime64[ns](4), float64(11), int64(8), object(50)
    memory usage: 3.1+ MB
    


```python
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>accommodates</th>
      <th>bedrooms</th>
      <th>beds</th>
      <th>number_of_reviews</th>
      <th>host.host_listings_count</th>
      <th>host.host_total_listings_count</th>
      <th>availability.availability_30</th>
      <th>availability.availability_60</th>
      <th>availability.availability_90</th>
      <th>availability.availability_365</th>
      <th>review_scores.review_scores_accuracy</th>
      <th>review_scores.review_scores_cleanliness</th>
      <th>review_scores.review_scores_checkin</th>
      <th>review_scores.review_scores_communication</th>
      <th>review_scores.review_scores_location</th>
      <th>review_scores.review_scores_value</th>
      <th>review_scores.review_scores_rating</th>
      <th>host.host_response_rate</th>
      <th>reviews_per_month</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>5555.000000</td>
      <td>5550.000000</td>
      <td>5542.000000</td>
      <td>5555.000000</td>
      <td>5555.000000</td>
      <td>5555.000000</td>
      <td>5555.000000</td>
      <td>5555.000000</td>
      <td>5555.000000</td>
      <td>5555.000000</td>
      <td>4079.000000</td>
      <td>4082.000000</td>
      <td>4080.000000</td>
      <td>4081.000000</td>
      <td>4081.000000</td>
      <td>4080.000000</td>
      <td>4081.000000</td>
      <td>4167.000000</td>
      <td>94.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>3.505851</td>
      <td>1.411712</td>
      <td>2.071454</td>
      <td>27.606481</td>
      <td>14.405761</td>
      <td>14.405761</td>
      <td>11.816202</td>
      <td>26.451305</td>
      <td>42.758056</td>
      <td>173.105671</td>
      <td>9.557490</td>
      <td>9.315287</td>
      <td>9.699265</td>
      <td>9.688312</td>
      <td>9.601078</td>
      <td>9.305147</td>
      <td>93.099240</td>
      <td>93.118311</td>
      <td>1.712766</td>
    </tr>
    <tr>
      <th>std</th>
      <td>2.297019</td>
      <td>1.041942</td>
      <td>1.619660</td>
      <td>49.798376</td>
      <td>65.848868</td>
      <td>65.848868</td>
      <td>11.686113</td>
      <td>23.476011</td>
      <td>35.226897</td>
      <td>139.841893</td>
      <td>0.899603</td>
      <td>1.088492</td>
      <td>0.784753</td>
      <td>0.806155</td>
      <td>0.759023</td>
      <td>0.939855</td>
      <td>9.023483</td>
      <td>18.541507</td>
      <td>1.492795</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>20.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>17.000000</td>
      <td>9.000000</td>
      <td>9.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>9.000000</td>
      <td>9.000000</td>
      <td>90.000000</td>
      <td>98.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>3.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>5.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>8.000000</td>
      <td>23.000000</td>
      <td>43.000000</td>
      <td>171.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>9.000000</td>
      <td>95.000000</td>
      <td>100.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>4.000000</td>
      <td>2.000000</td>
      <td>3.000000</td>
      <td>32.000000</td>
      <td>6.000000</td>
      <td>6.000000</td>
      <td>24.000000</td>
      <td>52.000000</td>
      <td>80.000000</td>
      <td>317.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>99.000000</td>
      <td>100.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>16.000000</td>
      <td>20.000000</td>
      <td>25.000000</td>
      <td>533.000000</td>
      <td>1198.000000</td>
      <td>1198.000000</td>
      <td>30.000000</td>
      <td>60.000000</td>
      <td>90.000000</td>
      <td>365.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>10.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.head(5).T
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>_id</th>
      <td>10021707</td>
      <td>10030955</td>
      <td>10047964</td>
      <td>10059244</td>
      <td>10112159</td>
    </tr>
    <tr>
      <th>listing_url</th>
      <td>https://www.airbnb.com/rooms/10021707</td>
      <td>https://www.airbnb.com/rooms/10030955</td>
      <td>https://www.airbnb.com/rooms/10047964</td>
      <td>https://www.airbnb.com/rooms/10059244</td>
      <td>https://www.airbnb.com/rooms/10112159</td>
    </tr>
    <tr>
      <th>name</th>
      <td>Private Room in Bushwick</td>
      <td>Apt Linda Vista Lagoa - Rio</td>
      <td>Charming Flat in Downtown Moda</td>
      <td>Ligne verte - à 15 min de métro du centre ville.</td>
      <td>Downtown Oporto Inn (room cleaning)</td>
    </tr>
    <tr>
      <th>summary</th>
      <td>Here exists a very cozy room for rent in a sha...</td>
      <td>Quarto com vista para a Lagoa Rodrigo de Freit...</td>
      <td>Fully furnished 3+1 flat decorated with vintag...</td>
      <td>À 30 secondes du métro Joliette. Belle grande ...</td>
      <td>Tradicional building, with high ceilings next ...</td>
    </tr>
    <tr>
      <th>space</th>
      <td></td>
      <td></td>
      <td>The apartment is composed of 1 big bedroom wit...</td>
      <td></td>
      <td>Cozy, located near the most interesting points...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>host.host_response_time</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>within an hour</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>host.host_response_rate</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>100.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>weekly_price</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>230.00</td>
    </tr>
    <tr>
      <th>monthly_price</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>600.00</td>
    </tr>
    <tr>
      <th>reviews_per_month</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>77 rows × 5 columns</p>
</div>



### Cleaning Data


```python
#Renaming columns
df=df.rename(columns = {'address.street':'street','address.suburb':'suburb','address.government_area':'government_area',
   'address.market':'market','address.country':'country','address.country_code' :'country_code',
'address.location.coordinates':'location_coordinates','availability.availability_30':'avail_30','availability.availability_60':'avail_60','availability.availability_90':'avail_90',
'availability.availability_365':'avail_365','review_scores.review_scores_accuracy':'accuracy_score',
'review_scores.review_scores_cleanliness':'cleanliness_score','review_scores.review_scores_checkin':'checkin_score',
 'review_scores.review_scores_communication':'communication_score','review_scores.review_scores_location':'location_score',
'review_scores.review_scores_value':'value_score','review_scores.review_scores_rating':'rating_score',
'host.host_response_time':'host_response_time','host.host_response_rate':'host_response_rate',
'host.host_is_superhost':'host_is_superhost','host.host_listings_count':'host_listings_count'})
```


```python
#Dropping columns
df_new = df.drop(columns = ['listing_url','summary','description','neighborhood_overview','notes','transit','last_scraped','calendar_last_scraped',
                  'first_review','last_review','reviews','images.thumbnail_url','images.medium_url','images.picture_url','images.xl_picture_url',
                  'host.host_url','host.host_thumbnail_url','host.host_about','host.host_picture_url','host.host_neighbourhood','host.host_has_profile_pic',
                  'location_coordinates','address.location.is_location_exact','space','access','interaction','house_rules',
                            'host.host_verifications','reviews_per_month','weekly_price','monthly_price'])
```


```python
#check columns with null values before conversion
pd.isnull(df_new).sum()[pd.isnull(df_new).sum()>0]
```




    bedrooms                  5
    beds                     13
    bathrooms                10
    accuracy_score         1476
    cleanliness_score      1473
    checkin_score          1475
    communication_score    1474
    location_score         1474
    value_score            1475
    rating_score           1474
    security_deposit       2084
    cleaning_fee           1531
    host_response_time     1388
    host_response_rate     1388
    dtype: int64



### Handling NaN, empty string Values


```python
#Handling Nan values
#Replacing Nan security depsoit with values zero,cleaning_fee nan values with zero.bedrooms,beds,bathrooms with 1
#and other values with average

df_new['security_deposit']= df_new['security_deposit'].fillna(0)
df_new['cleaning_fee']= df_new['cleaning_fee'].fillna(0)
df_new['bedrooms'] = df_new['bedrooms'].fillna(1)
df_new['beds'] = df_new['beds'].fillna(1)
df_new['bathrooms'] = df_new['bathrooms'].fillna(1)
df_new['accuracy_score'] = df_new['accuracy_score'].fillna(df_new['accuracy_score'].mean())
df_new['cleanliness_score'] = df_new['cleanliness_score'].fillna(df_new['cleanliness_score'].mean())
df_new['checkin_score'] = df_new['checkin_score'].fillna(df_new['checkin_score'].mean())
df_new['communication_score'] = df_new['communication_score'].fillna(df['communication_score'].mean())
df_new['location_score'] = df_new['location_score'].fillna(df_new['location_score'].mean())
df_new['value_score'] = df_new['value_score'].fillna(df_new['value_score'].mean())
df_new['rating_score'] = df_new['rating_score'].fillna(df_new['rating_score'].mean())
df_new['host_response_time'] = df_new['host_response_time'].fillna('within an hour')
df_new['host_response_rate'] = df_new['host_response_rate'].fillna(df_new['host_response_rate'].mean())

#Removing spaces and camelcasing street name to avoid duplicates
df_new['street'] = df_new['street'].apply(lambda x: re.sub(r'\s', '', x))
df_new['street'] = df_new["street"].str.title()

#Handling missing values in market
df_new.loc[(df_new['country']=="Brazil") & (df_new['market']== ""),['market']]="Rio De Janeiro"
df_new.loc[(df_new['_id'] == "13528649" ),['market']] = "New York"
df_new.loc[(df_new['_id'] == "14234514" ),['market']] = "Kapaa"
df_new.loc[(df_new['_id'] == "13702505" ),['market']] = "Montreal"
df_new.loc[(df_new['_id'] == "14161732" ),['market']] = "Barcelona"
df_new.loc[(df_new['_id'] == "13363311") ,['market']] = "Waverley"
```


```python
#check columns with null values after conversion
pd.isnull(df_new).sum()[pd.isnull(df_new).sum()>0]
```




    Series([], dtype: int64)



### Data type Conversion


```python
#Data type Conversion
col1 =['price','cleaning_fee','security_deposit']
col2 = ['extra_people','minimum_nights','maximum_nights','accommodates','guests_included']
col3 = ['beds','bedrooms']
for i in col1:
    df_new[i] = df_new[i].astype(str).astype(float)
for i in col2:
    df_new[i] = df_new[i].astype(str).astype(float).round().astype(int)

for i in col3:
     df_new[i] = df_new[i].round().astype('Int64')    
df_new['bathrooms']=df_new['bathrooms'].astype('str').astype('float').round().astype('Int64')   

```


```python
#Finding the number of Rows and Columns
print("Number of Rows :",df_new.shape[0])
print("Number of Columns :",df_new.shape[1])
```

    Number of Rows : 5555
    Number of Columns : 46
    


```python
df_new.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 5555 entries, 0 to 5554
    Data columns (total 46 columns):
     #   Column                          Non-Null Count  Dtype  
    ---  ------                          --------------  -----  
     0   _id                             5555 non-null   object 
     1   name                            5555 non-null   object 
     2   property_type                   5555 non-null   object 
     3   room_type                       5555 non-null   object 
     4   bed_type                        5555 non-null   object 
     5   minimum_nights                  5555 non-null   int32  
     6   maximum_nights                  5555 non-null   int32  
     7   cancellation_policy             5555 non-null   object 
     8   accommodates                    5555 non-null   int32  
     9   bedrooms                        5555 non-null   Int64  
     10  beds                            5555 non-null   Int64  
     11  number_of_reviews               5555 non-null   int64  
     12  bathrooms                       5555 non-null   Int64  
     13  amenities                       5555 non-null   object 
     14  price                           5555 non-null   float64
     15  extra_people                    5555 non-null   int32  
     16  guests_included                 5555 non-null   int32  
     17  host.host_id                    5555 non-null   object 
     18  host.host_name                  5555 non-null   object 
     19  host.host_location              5555 non-null   object 
     20  host_is_superhost               5555 non-null   bool   
     21  host.host_identity_verified     5555 non-null   bool   
     22  host_listings_count             5555 non-null   int64  
     23  host.host_total_listings_count  5555 non-null   int64  
     24  street                          5555 non-null   object 
     25  suburb                          5555 non-null   object 
     26  government_area                 5555 non-null   object 
     27  market                          5555 non-null   object 
     28  country                         5555 non-null   object 
     29  country_code                    5555 non-null   object 
     30  address.location.type           5555 non-null   object 
     31  avail_30                        5555 non-null   int64  
     32  avail_60                        5555 non-null   int64  
     33  avail_90                        5555 non-null   int64  
     34  avail_365                       5555 non-null   int64  
     35  accuracy_score                  5555 non-null   float64
     36  cleanliness_score               5555 non-null   float64
     37  checkin_score                   5555 non-null   float64
     38  communication_score             5555 non-null   float64
     39  location_score                  5555 non-null   float64
     40  value_score                     5555 non-null   float64
     41  rating_score                    5555 non-null   float64
     42  security_deposit                5555 non-null   float64
     43  cleaning_fee                    5555 non-null   float64
     44  host_response_time              5555 non-null   object 
     45  host_response_rate              5555 non-null   float64
    dtypes: Int64(3), bool(2), float64(11), int32(5), int64(7), object(18)
    memory usage: 1.8+ MB
    


```python

```
