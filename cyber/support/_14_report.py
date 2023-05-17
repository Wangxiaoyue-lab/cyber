def report_head(title):
    html_string = f"""
        <div class="report_head_container">
            <div class="report_head_title">
                <h1>{title}</h1>
            </div>
        </div>
        """
    return html_string

def Pre_report_to_div(data):
    div = '<div class="Pre-report">'
    for key, value in data.items():
        div += f'<p>{key}: {value}</p >'
    div += '</div>'
    return div

def Post_report_to_div(data):
    div = '<div class="Post_report">'
    for key, value in data.items():
        if isinstance(value, list):
            div += f'<p>{key}:<ul>'
            for item in value:
                div += f'<li>{item}</li>'
            div += '</ul></p >'
        else:
            div += f'<p>{key}: {value}</p >'
    div += '</div>'
    return div    

