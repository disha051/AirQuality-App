import streamlit as st

st.set_page_config(page_title=" Air Quality Index ✨ ")
st.header('🌪️ AirWatch India ')

st.image('India-2023.png', caption='India AQI', use_container_width=True)

st.markdown(
    """
    This app shows you the air pollution levels in Indian cities.
    It tracks NO2, CO, AOI, PM 2.5, PM 10, and more. You'll see pollution trends and get health recommendations.l.
    
    """
)


# Impact on Health and Well-being

st.header('🦠👩‍⚕🧬 Impact on Health and Well-being')

st.markdown("""
Poor air quality isn't just an inconvenience; it poses a serious threat to human health and well-being. 
Here's a breakdown of some key health concerns:

- **Respiratory diseases**: Exposure to air pollutants irritates the lungs, worsening asthma symptoms and triggering chronic obstructive pulmonary disease (COPD). 
    A 2023 study published in the European Respiratory Journal found a link between long-term exposure to air pollution (particularly PM2.5) and an increased risk of developing COPD, highlighting the long-term consequences of air quality.

- **Cardiovascular diseases**: Air pollution can damage blood vessels and increase the risk of heart attacks, strokes, and other cardiovascular problems. 
    A 2022 Harvard University study found that even short-term exposure to traffic-related air pollution can lead to an increased risk of heart attacks, emphasizing the need for immediate action in areas with high traffic volumes.
""")

# Impact on Life Expectancy
st.header('🧘‍♀️🥗🍎 Impact on Life Expectancy')

st.markdown("""
The impact of air pollution extends beyond immediate health problems. It can shorten lifespans:

- **Reduced Life Expectancy**: The World Health Organization (WHO) estimates that air pollution cuts global life expectancy by an average of 1.8 years. 
    This means millions of lives are lost prematurely due to poor air quality.

- **City-Specific Impact**: The impact varies by location. Highly polluted cities can see reductions in life expectancy as high as 4-5 years. 
    This highlights the need for stricter regulations and cleaner energy sources in urban areas.

- **Fine Particulate Matter (PM2.5)**: Long-term exposure to PM2.5, tiny particles that enter deep into the lungs, is particularly detrimental and significantly reduces life expectancy.
""")

# Conclusion
st.header('🕵 Conclusion')

st.markdown("""
The analysis of air quality data paints a grim picture of how poor air quality jeopardizes human health, well-being, and life expectancy. 
Implementing stricter regulations, promoting cleaner energy sources, and raising public awareness are crucial steps to combat air pollution and safeguard public health.
""")




