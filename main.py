from api_clients import APIClient
from report_generator import ReportGenerator
from utils import transform_api_json_to_items

def main():
    BASE_URL = "https://jsonplaceholder.typicode.com"
    PATH = "posts"
    OUTPUT_FILENAME = "sample_report.docx"
    REPORT_TITLE = "Sample API Report"

    client = APIClient(BASE_URL)
    try:
        raw = client.get(PATH)
    except Exception as e:
        print("[ERROR] Failed to fetch API data:", e)
        return

    items = transform_api_json_to_items(raw, limit=10)
    if not items:
        print("No items found in API response.")
        return

    generator = ReportGenerator()
    out_path = generator.generate(filename=OUTPUT_FILENAME, title=REPORT_TITLE, items=items)
    print("Report saved to:", out_path)

if __name__ == "__main__":
    main()
