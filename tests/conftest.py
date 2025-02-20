import httpx
import pytest
from rich.console import Console
from typer.testing import CliRunner

from weather_command.models.location import Location
from weather_command.models.weather import CurrentWeather, OneCallWeather


@pytest.fixture(autouse=True)
def env_vars(monkeypatch):
    monkeypatch.setenv("OPEN_WEATHER_API_KEY", "test")
    yield
    monkeypatch.delenv("OPEN_WEATHER_API_KEY", raising=False)


@pytest.fixture
def test_console():
    return Console()


@pytest.fixture
def test_runner():
    return CliRunner()


@pytest.fixture
def mock_current_weather_dict():
    return {
        "coord": {"lon": -79.792, "lat": 36.0726},
        "weather": [
            {
                "id": 211,
                "main": "Thunderstorm",
                "description": "thunderstorm",
                "icon": "11d",
            },
            {"id": 701, "main": "Mist", "description": "mist", "icon": "50d"},
            {
                "id": 500,
                "main": "Rain",
                "description": "light rain",
                "icon": "10d",
            },
        ],
        "base": "stations",
        "main": {
            "temp": 296.92,
            "feels_like": 297.42,
            "temp_min": 295.27,
            "temp_max": 298.64,
            "pressure": 1009,
            "humidity": 79,
        },
        "visibility": 4828,
        "wind": {"speed": 0.45, "deg": 275, "gust": 3.58},
        "rain": {"1h": 0.55},
        "clouds": {"all": 90},
        "dt": 1632345032,
        "sys": {
            "type": 2,
            "id": 2003175,
            "country": "US",
            "sunrise": 1632308836,
            "sunset": 1632352582,
        },
        "timezone": -14400,
        "id": 4469146,
        "name": "Greensboro",
        "cod": 200,
    }


@pytest.fixture
def mock_current_weather(mock_current_weather_dict):
    return CurrentWeather(**mock_current_weather_dict)


@pytest.fixture
def mock_current_weather_response(mock_current_weather_dict):
    return httpx.Response(
        200,
        request=httpx.Request("GET", "https://localhost"),
        json=mock_current_weather_dict,
    )


@pytest.fixture
def mock_one_call_weather_dict():
    return {
        "lat": 36.1056,
        "lon": -79.7569,
        "timezone": "America/New_York",
        "timezone_offset": -14400,
        "current": {
            "dt": 1632878438,
            "sunrise": 1632827507,
            "sunset": 1632870436,
            "temp": 19.74,
            "feels_like": 19.75,
            "pressure": 1015,
            "humidity": 76,
            "dew_point": 15.39,
            "uvi": 0,
            "clouds": 6,
            "visibility": 10000,
            "wind_speed": 1.03,
            "wind_deg": 209,
            "wind_gust": 1.07,
            "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01n"}],
        },
        "minutely": [
            {"dt": 1632878460, "precipitation": 0},
            {"dt": 1632878520, "precipitation": 0},
        ],
        "hourly": [
            {
                "dt": 1632877200,
                "temp": 19.74,
                "feels_like": 19.75,
                "pressure": 1015,
                "humidity": 76,
                "dew_point": 15.39,
                "uvi": 0,
                "clouds": 6,
                "visibility": 10000,
                "wind_speed": 1.03,
                "wind_deg": 209,
                "wind_gust": 1.07,
                "weather": [
                    {"id": 800, "main": "Clear", "description": "clear sky", "icon": "01n"}
                ],
                "pop": 0,
            },
            {
                "dt": 1632880800,
                "temp": 19.76,
                "feels_like": 19.7,
                "pressure": 1015,
                "humidity": 73,
                "dew_point": 14.79,
                "uvi": 0,
                "clouds": 6,
                "visibility": 10000,
                "wind_speed": 1.04,
                "wind_deg": 233,
                "wind_gust": 1.08,
                "weather": [
                    {"id": 800, "main": "Clear", "description": "clear sky", "icon": "01n"}
                ],
                "pop": 0,
            },
            {
                "dt": 1632884400,
                "temp": 19.61,
                "feels_like": 19.45,
                "pressure": 1015,
                "humidity": 70,
                "dew_point": 13.99,
                "uvi": 0,
                "clouds": 5,
                "visibility": 10000,
                "wind_speed": 1.42,
                "wind_deg": 271,
                "wind_gust": 1.47,
                "weather": [
                    {"id": 800, "main": "Clear", "description": "clear sky", "icon": "01n"}
                ],
                "pop": 0,
            },
        ],
        "daily": [
            {
                "dt": 1632848400,
                "sunrise": 1632827507,
                "sunset": 1632870436,
                "moonrise": 1632887700,
                "moonset": 1632853200,
                "moon_phase": 0.75,
                "temp": {
                    "day": 29.18,
                    "min": 14.95,
                    "max": 29.7,
                    "night": 19.61,
                    "eve": 20.74,
                    "morn": 14.95,
                },
                "feels_like": {"day": 28.36, "night": 19.45, "eve": 20.65, "morn": 14.46},
                "pressure": 1014,
                "humidity": 35,
                "dew_point": 12.3,
                "wind_speed": 2.88,
                "wind_deg": 253,
                "wind_gust": 8.7,
                "weather": [
                    {"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}
                ],
                "clouds": 5,
                "pop": 0,
                "uvi": 5.67,
            },
            {
                "dt": 1632934800,
                "sunrise": 1632913955,
                "sunset": 1632956747,
                "moonrise": 0,
                "moonset": 1632942780,
                "moon_phase": 0.77,
                "temp": {
                    "day": 27.92,
                    "min": 17.69,
                    "max": 29.22,
                    "night": 18.78,
                    "eve": 24.18,
                    "morn": 17.69,
                },
                "feels_like": {"day": 27.88, "night": 18.62, "eve": 24.04, "morn": 17.5},
                "pressure": 1016,
                "humidity": 44,
                "dew_point": 14.51,
                "wind_speed": 3.17,
                "wind_deg": 8,
                "wind_gust": 7.44,
                "weather": [
                    {"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}
                ],
                "clouds": 0,
                "pop": 0,
                "uvi": 6.07,
            },
        ],
    }


@pytest.fixture
def mock_one_call_weather(mock_one_call_weather_dict):
    return OneCallWeather(**mock_one_call_weather_dict)


@pytest.fixture
def mock_one_call_weather_response(mock_one_call_weather_dict):
    return httpx.Response(
        200,
        request=httpx.Request("GET", "http://localhost"),
        json=mock_one_call_weather_dict,
    )


@pytest.fixture
def mock_location_dict(mock_one_call_weather_dict):
    return [
        {
            "display_name": "Greensboro, NC",
            "lat": mock_one_call_weather_dict["lat"],
            "lon": mock_one_call_weather_dict["lon"],
        }
    ]


@pytest.fixture
def mock_location(mock_location_dict):
    return Location(**mock_location_dict[0])


@pytest.fixture
def mock_location_response(mock_location_dict):
    return httpx.Response(
        200,
        request=httpx.Request("GET", "http://localhost"),
        json=mock_location_dict,
    )
