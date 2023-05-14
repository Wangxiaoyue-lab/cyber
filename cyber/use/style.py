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


style_dir={'style_date':style_date, 'style_input':style_input, 'style_script':style_script}
