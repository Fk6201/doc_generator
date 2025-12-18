from models import ReportItem

def transform_api_json_to_items(data, city):
    current = data["current_condition"][0]

    temp = current["temp_C"]
    desc = current["weatherDesc"][0]["value"]

    return [
        ReportItem(
            title=f"Weather Report - {city}",
            summary=f"Current condition: {desc}",
            value=float(temp)
        )
    ]
