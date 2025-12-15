from typing import List, Any
from models import ReportItem

def transform_api_json_to_items(data: Any, limit: int = 10) -> List[ReportItem]:
    items: List[ReportItem] = []
    seq = data if not isinstance(data, dict) else (data.get("results") or data.get("items") or [])
    try:
        iterator = iter(seq)
    except TypeError:
        return items

    for obj in list(iterator)[:limit]:
        title = obj.get("title") if isinstance(obj, dict) else str(obj)
        summary = obj.get("body") or obj.get("summary") or obj.get("desc") or ""
        value = None
        for key in ("value", "score", "rating"):
            if isinstance(obj.get(key), (int, float)):
                value = obj.get(key)
                break
        items.append(ReportItem(title=title, summary=summary, value=value))
    return items
