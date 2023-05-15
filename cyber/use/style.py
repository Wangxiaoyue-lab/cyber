style_date = """
    .date {
        position: absolute;
        top: 0;
        left: 0;
        padding: 10px;
        font-size: 0.8em;
        color: gray;
    }
    """

style_input = """
        <style>
            .input-table table, .input-table th, .input-table td {
                border: 1px solid black;
                border-collapse: collapse;
            }
            .input-table th {
                text-align: center;
                background-color: green;
                color:white;
            }
            .input-table td {
                padding: 5px;
                text-align: left;
                max-width: 180px;
                word-wrap: break-word;
                background-color: lightyellow;
            }
        </style>
    """

style_script = """
        <style>
            .script-table table, .script-table th, .script-table td {
                border: 1px solid black;
                border-collapse: collapse;
            }
            .script-table th {
                text-align: center;
                background-color: green;
                color:white;
            }
            .script-table td {
                padding: 5px;
                text-align: left;
                max-width: 240px;
                word-wrap: break-word;
                background-color: lightyellow;
            }
        </style>
    """

style_packages = """
    .my-class {
        border: 1px solid black;
        padding: 10px;
    }

    .my-class p {
        margin: 0;
    }
    """

style_tree = """
    .tree {
        width: 100%;
        border: 1px solid #ccc;
        padding: 10px;
    }

    .tree img {
        width: 100%;
    }
    """

style_pictures =  """
    .pictures .left {
        float: left;
        width: 45%;
        padding: 5px;
    }

    .pictures .right {
        float: right;
        width: 45%;
        padding: 5px;
    }

    .pictures p {
        word-wrap: break-word;
    }
    """

style_tables = """
    <style>
        .tables .label { font-weight: bold; color: green; }
        .tables .value { display: block; margin-left: 2em; max-width: 30ch; word-wrap: break-word; }
    </style>
    """

style_store = """
        <style>
            .store-table table, .store-table th, .store-table td {
                border: 1px solid black;
                border-collapse: collapse;
            }
            .store-table th {
                text-align: center;
                background-color: green;
                color:white;
            }
            .store-table td {
                padding: 5px;
                text-align: left;
                max-width: 180px;
                word-wrap: break-word;
                background-color: lightyellow;
            }
        </style>
    """

style_supplement = """
    .supplement {
        font-family: Arial, sans-serif;
        font-size: 14px;
        color: #333;
    }

    .supplement ul {
        list-style: none;
        margin: 0;
        padding: 0;
    }

    .supplement li {
        margin-bottom: 10px;
    }

    .supplement li ul li {
        margin-left: 20px;
    }
    """

style_Pre_report="""
    .Pre_report {
        border: 1px solid black;
        padding: 10px;
        margin: 10px;
    }
    """

style_Post_report="""
    .Post_report {
        border: 1px solid black;
        padding: 10px;
        margin: 10px;
    }
"""

style_head = """
    .report_head_container { 
        background-color: white; 
        width: 800px; 
        margin: 2 auto; 
        border-left: 1px solid #ccc; 
        border-right: 1px solid #ccc; 
        padding: 16px; 
    }
    
    .report_head_title {
        background-color: green;
        text-align: center;
        height: 103px;
    }
    
    .report_head_title h1 {
        font-family: 'Brush Script MT', cursive;
        color: white;
        font-size: 78px;
    }
    """

style_dir={
    'style_date':style_date, 
    'style_input':style_input, 
    'style_script':style_script,
    'style_packages':style_packages,
    'style_tree':style_tree,
    'style_pictures':style_pictures,
    'style_tables':style_tables,
    'style_store':style_store,
    'style_supplement':style_supplement,
    'style_Pre_report':style_Pre_report,
    'style_Post_report':style_Post_report,
    'style_head':style_head
}

