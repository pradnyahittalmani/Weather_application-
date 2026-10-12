# Weather Application

## Features
- Search weather by city
- Display temperature
- Display humidity
- Display wind speed
- Display current weather condition
- Display weather alerts, if available
- Responsive web interface
- Error handling for invalid cities and connection problems

## Technology Used
- Python
- Flask
- HTML
- CSS
- WeatherAPI.com

## How to Run

### 1. Install Python
Install Python 3.9 or later.

### 2. Open the project folder
Open Command Prompt/Terminal inside this project folder.

### 3. Install required packages
```bash
pip install -r requirements.txt
```

### 4. Get a WeatherAPI.com API key
Create an account at WeatherAPI.com and obtain an API key.

### 5. Add the API key
Open `app.py` and replace:

```python
API_KEY = os.getenv("WEATHER_API_KEY", "YOUR_API_KEY_HERE")
```

with:

```python
API_KEY = "YOUR_ACTUAL_API_KEY"
```

You can also set the `WEATHER_API_KEY` environment variable instead.

### 6. Run the application
```bash
python app.py
```

### 7. Open in browser
Go to:

http://127.0.0.1:5000

Enter a city such as Bengaluru, Mumbai, Delhi, or London and click **Search Weather**.

## Project Structure

weather_application/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css

## Note
The application needs an internet connection and a valid WeatherAPI.com API key to retrieve live weather information.
