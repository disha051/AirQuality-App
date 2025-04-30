import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



# Load the dataset
data = pd.read_csv('Data/city_day.csv')

# Set page title
st.set_page_config(page_title='Air Quality Dashboard')

# Introduction
st.title('🏭 Air Quality Dashboard')
st.write(""" Visualizing Air Pollution Levels in Indian Cities. """)

# Data cleaning and preprocessing
data['Date'] = pd.to_datetime(data['Date'])
data.dropna(subset=['AQI'], inplace=True)


# Sidebar options
st.sidebar.title('Study the AQI Patterns')
display_aqi_by_city = st.sidebar.checkbox('📶 AQI by City ')
display_aqi_by_year = st.sidebar.checkbox(' 📉 AQI by Year')
display_aqi_by_bucket = st.sidebar.checkbox('💹 AQI by AQI_Bucket')
display_pollutants_over_time = st.sidebar.checkbox('📜 Pollutants Over Time',value = True)


# AQI by City
if display_aqi_by_city:
    st.subheader('AQI by City')
    cities = data['City'].unique()
    selected_city = st.selectbox('Select a city', cities)
    city_data = data[data['City'] == selected_city]

    fig_aqi_city, ax_aqi_city = plt.subplots()
    sns.barplot(x=city_data['Date'].dt.year, y=city_data['AQI'], ax=ax_aqi_city)
    ax_aqi_city.set_xlabel('Year')
    ax_aqi_city.set_ylabel('Average AQI')
    ax_aqi_city.set_title(f'AQI Trend for {selected_city}')
    sns.despine(fig=fig_aqi_city)
    st.pyplot(fig_aqi_city)

    st.write('Observations:')
    st.write('- The graph shows the average AQI trend for the selected city over the years.')
    st.write('- Higher AQI values indicate worse air quality.')
    st.write('- The trend can help identify if air quality has improved or deteriorated over time in the selected city.')

# AQI by Year
if display_aqi_by_year:
    st.subheader('AQI by Year')
    years = data['Date'].dt.year.unique()
    selected_year = st.selectbox('Select a year', years)
    year_data = data[data['Date'].dt.year == selected_year]

    fig_aqi_year, ax_aqi_year = plt.subplots()
    sns.barplot(x=year_data['City'], y=year_data['AQI'], ax=ax_aqi_year)
    ax_aqi_year.set_xlabel('City')
    ax_aqi_year.set_ylabel('Average AQI')
    ax_aqi_year.set_title(f'AQI by City for {selected_year}')
    plt.xticks(rotation=45)
    sns.despine(fig=fig_aqi_year)
    st.pyplot(fig_aqi_year)

    st.write('Observations:')
    st.write('- The graph shows the average AQI for different cities in the selected year.')
    st.write('- It allows comparing air quality across cities for a specific year.')
    st.write('- Cities with higher bars have worse air quality compared to those with lower bars.')

# AQI by AQI_Bucket
if display_aqi_by_bucket:
    st.subheader('AQI by AQI_Bucket')
    aqi_buckets = data['AQI_Bucket'].unique()

    fig_aqi_bucket, ax_aqi_bucket = plt.subplots()
    sns.countplot(x=data['AQI_Bucket'], ax=ax_aqi_bucket)
    ax_aqi_bucket.set_xlabel('AQI_Bucket')
    ax_aqi_bucket.set_ylabel('Count')
    plt.xticks(rotation=45)
    sns.despine(fig=fig_aqi_bucket)
    st.pyplot(fig_aqi_bucket)

    st.write('Observations:')
    st.write('- The graph shows the count of AQI values falling into each AQI_Bucket.')
    st.write('- It provides an overview of the distribution of AQI values across different buckets.')
    st.write('- Higher counts in the "Poor" or "Very Poor" buckets indicate a higher frequency of poor air quality.')

# Pollutants Over Time
if display_pollutants_over_time:
    st.subheader('Pollutants Over Time')
    pollutants = ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene']
    selected_pollutants = st.multiselect('Select pollutants', pollutants, default=['PM2.5', 'PM10'])

    cities = data['City'].unique()
    selected_city = st.selectbox('Select a city', cities, key='pollutant_city')
    city_data = data[data['City'] == selected_city]

    fig_pollutants, ax_pollutants = plt.subplots(figsize=(10, 6))
    for pollutant in selected_pollutants:
        sns.lineplot(x=city_data['Date'], y=city_data[pollutant], label=pollutant, ax=ax_pollutants)
    ax_pollutants.set_xlabel('Date')
    ax_pollutants.set_ylabel('Pollutant Level')
    ax_pollutants.set_title(f'Pollutants Over Time for {selected_city}')
    ax_pollutants.legend()
    sns.despine(fig=fig_pollutants)
    st.pyplot(fig_pollutants)

    st.write('Observations:')
    st.write('- The graph shows the levels of selected pollutants over time for the selected city.')
    st.write('- It allows monitoring the trends and patterns of pollutant levels.')
    st.write('- Higher pollutant levels indicate worse air quality.')
    st.write('- The graph can help identify any seasonal or long-term variations in pollutant levels.')
