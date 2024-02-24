# Airbnb_Data_Analysis
In this Airbnb project airbnb data from Mongodb sample cluster  has been analysed. Interactive hotel explorer app in streamlit along with Data Visualization in powerbi has been carried out

**Problem Statement:**
1. Retrieve Airbnb dataset from mongodb Atlas sample cluster
2. Perform Exploratory Data Analysis(EDA)
3. Develop Streamlit web application with interactive maps,allowing users to explore prices,ratings and other relevant factors
4. Build a comprehensive dashboard using Tableau or PowerBi

**Tools and Technologies Used:**
Mongodb Atlas,Mongodb Compass,Python,PowerBi,Visual Studio,Jupyter,Streamlit

**Approach:**
Airbnb Sample cluster data from Mongodb Atlas has been downloaded into local system and explored using Mongodb Compass.Connection was made to Mongodb database using python Mongoclient module and json data type converted into dataframe for easy analysis.After data retrieval and conversion, Exploratory Data Analysis has been performed, which can be accessed here - [EDA](https://github.com/KiruthikaParanthaman/Airbnb_Data_Analysis/blob/main/Airbnb%20Exploratory%20Data%20Analysis%20markdown.md)

After the EDA process, interactive streamlit app with airbnb hotel selection option with geo-visualization has been developed

**End Product :**

![airbnb streamlit](https://github.com/KiruthikaParanthaman/Airbnb_Data_Analysis/assets/141828622/e5c52333-049f-41a0-8905-056b1febdef5)

**Overview of Options:**

**Select country/Region :** Lets user to select Country
**Select Area           :** Lets user to select Area/city like Porto,Newyork etc
**Select Hotel          :** This option displays hotel name along with rating, price and street name
**Map                   :** Map displays list of hotels nearby in the seected city
**Details tab           :** Details tab displays hotel name,price,rating,location,amenities and other features of selected hotel
**Price Chart           :** Price Chart displays average price of that area with similar accomodates on comparison with selected hotel's price, which enables user to calculated decision
**Rating chart          :** Rating chart displays average Rating of that area with similar accomodates on comparison with selected hotel's rating
