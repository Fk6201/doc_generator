from api_clients import APIClient
from report_generator import ReportGenerator
from utils import transform_api_json_to_items

def main():
    print("Program started")

    city = input("Enter city name: ").strip().title()
    print("City entered:", city)

    BASE_URL = "https://wttr.in"
    PATH = city
    PARAMS = {"format": "j1"}

    OUTPUT_FILENAME = "weather_report.docx"
    REPORT_TITLE = f"Live Weather Report - {city}"

    client = APIClient(BASE_URL)

    try:
        print("Fetching weather data...")
        raw = client.get(PATH, params=PARAMS)
        print("API data received")
    except Exception as e:
        print("❌ API ERROR:", e)
        return

    try:
        items = transform_api_json_to_items(raw, city)
        print("Data transformed")
    except Exception as e:
        print("❌ DATA ERROR:", e)
        return

    try:
        generator = ReportGenerator()
        out_path = generator.generate(
            filename=OUTPUT_FILENAME,
            title=REPORT_TITLE,
            items=items
        )
        print("✅ Weather report created successfully!")
        print("📄 File location:", out_path)
    except Exception as e:
        print("❌ FILE ERROR:", e)

if __name__ == "__main__":
    main()
