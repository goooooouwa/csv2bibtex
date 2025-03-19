import json
from datetime import datetime

def csl_json_to_bibtex(csl_json):
    bibtex_entries = []
    for index, entry in enumerate(csl_json):
        accessed_date = datetime.fromtimestamp(entry["issued"]["date-parts"][0][0]).strftime("%Y-%m-%d")
        keywords = entry["categories"][0].replace("|", ", ") if entry.get("categories") else ""

        bibtex_entry = f"""@online{{entry{index},
  title = "{entry["title"]}",
  url = "{entry["URL"]}",
  accessed = "{accessed_date}",
  keywords = "{keywords}",
  note = "{entry["status"]}"
}}"""

        bibtex_entries.append(bibtex_entry)

    return "\n\n".join(bibtex_entries)

# Example usage
csl_json = [
        {
            "type": "webpage",
            "title": "Example Title",
            "URL": "http://example.com",
            "issued": {"date-parts": [[1637050429]]},  # Unix timestamp
            "categories": ["example|test"],
            "status": "unread",
            }
        ]

bibtex_output = csl_json_to_bibtex(csl_json)
print(bibtex_output)

