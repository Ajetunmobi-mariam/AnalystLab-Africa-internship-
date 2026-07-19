# Weather Data ETL Pipeline Project

## Project Overview

This project demonstrates the implementation of a simple ETL (Extract, Transform, Load) pipeline using real-time weather data from the OpenWeather API. The pipeline extracts weather information for selected Nigerian cities, transforms the data into a structured format, and stores it for future analysis.

## Objective

The objective of this project is to build a basic ETL(Extract, Transform,Load) pipeline that automates process of collecting, cleaning, transforming and storing weather data in a structured format for future analysis

## Data Source

OpenWeather API

Weather data was collected for:
- Lagos
- Abuja
- Port Harcourt

## Tools Used

- Python
- Pandas
- Requests
- VS Code
- OpenWeather API

## ETL Process

### Extract

Weather data was extracted from the OpenWeather API using an API key. The following fields were collected:

- City Name
- Temperature
- Humidity
- Weather Condition
- Wind Speed
- Date and Time

### Transform

The extracted data was converted into a Pandas DataFrame and organized into a structured format. The timestamp was converted into a readable date and time format.

### Load

The transformed dataset was saved as a CSV file for future analysis.

## Basic Analysis

The weather data collected from Lagos, Abuja, and Port Harcourt was analyzed to compare temperature, humidity, and weather conditions across the cities.


## Key Findings

- Port Harcourt recorded the highest temperature at 27.16°C.
- Abuja recorded a temperature of 25.52°C.
- Lagos recorded the lowest temperature at 24.56°C.
- Lagos had the highest humidity level at 89%.
- All three cities experienced Clouds as their weather condition at the time the data was collected.

## Conclusion 
The analysis showed variations in temperature and humidity across the selected cities. As at the time the data was collected, Port Harcourt was the warmest city, while Lagos had the highest humidity level. Despite these differences, all three cities shared the same weather condition (Clouds) when the data was retrieved from the OpenWeather API.


