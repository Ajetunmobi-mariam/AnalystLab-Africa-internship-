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

- Port Harcourt recorded the highest temperature at 23.13°C.
- Abuja recorded the lowest  temperature of 21.03°C.
- Lagos recorded a temperature at 22.98°C.
- Abuja had the highest humidity level at 97%.
- All three cities experienced Clouds as their weather condition at the time the data was collected.

## Conclusion 
The weather data and analysis reflect conditions at the time the data was collected and may change as weather conditions update.


