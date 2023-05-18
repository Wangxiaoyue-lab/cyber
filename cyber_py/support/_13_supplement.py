
def filter_supplement(data):
    result = [item for item in data if any(value is not None for value in item.values())]
    if not result:
        result = "Unknown"
    return result

def generate_supplement_div(data):
    if data == "Unknown":
        return "<div class='supplement'><p>Unknown</p ></div>"

    result = "<div class='supplement'><ul>"
    for item in data:
        result += "<li>"
        result += "<ul>"
        for key, value in item.items():
            if value is not None:
                result += f"<li>{key}: {value}</li>"
        result += "</ul>"
        result += "</li>"
    result += "</ul></div>"

    return result  

#    filtered_data = filter_supplement(raw_data)
#    html = generate_supplement_div(filtered_data)    