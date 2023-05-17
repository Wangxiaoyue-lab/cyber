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
    """

style_script = """
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
    """

style_packages = """
    .packages {
        border: 1px solid black;
        padding: 10px;
    }

    .packages p {
        margin: 0;
    }
    """

style_tree = """
    .tree {
        width: 80%;
        border: 1px solid #ccc;
        padding: 10px;
    }

    .tree img {
        width: 80%;
    }
    """

style_pictures = """
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
        .tables .label { 
            font-weight: bold; 
            color: green; 
            }

        .tables .value { 
            display: block; 
            margin-left: 2em; 
            max-width: 30ch; 
            word-wrap: break-word; 
            }
    """

style_store = """
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

style_Pre_report = """
    .Pre_report {
        border: 1px solid black;
        padding: 10px;
        margin: 10px;
    }
    """

style_Post_report = """
    .Post_report {
        background-color: lightyellow;
        border: 1px solid black;
        padding: 10px;
        margin: 10px;
    }
"""

style_head = """
    .report_head_container { 
        background-color: white; 
        width: 960px; 
        height: 110px;
        margin: 0 auto; 
        border-left: 1px solid #ccc; 
        border-right: 1px solid #ccc; 
    }
    
    .report_head_title {
        background-color: green;
        text-align: center;
        margin: 10px;
    }
    
    .report_head_title h1 {
        font-family: 'Brush Script MT', cursive;
        color: white;
        font-size: 78px;
    }
    """

style_body = """
    body { 
        max-width: 1200px;
        margin: 0; 
        padding: 20px; 
        background-color: white;
            }
    .container_whole {
        position: relative;
        width: 100%;
        margin: 0 auto;
        padding: 20px;
        background-color: #D1EED1;
        border: 1px solid black;
        }
"""
style_logo ="""
    .existing-div {
    display: flex;
    justify-content: center;
    }

.logo {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background-color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

.logo:before {
    content: "";
    width: 100px;
    height: 100px;
    border-radius: 50%;
    border: 10px solid green;
    position: absolute;
    top: -15px;
    left: -15px;
    transform: rotate(45deg);
    z-index: -1;
}

.top-left,
.top-right,
.bottom-left,
.bottom-right {
    content: "";
    width: 10px;
    height: 10px;
    border-radius: 50%;
    position: absolute;
}

.top-left {
    top: -5px;
    left: -5px;
    border: 2px solid green;
    background-color: white;
}

.top-right {
    top: -5px;
    right: -5px;
    background-color: green;
}

.bottom-left {
    bottom: -5px;
    left: -5px;
    background-color: green;
}

.bottom-right {
    bottom: -5px;
    right: -5px;
    border: 2px solid green;
    background-color: white;
}
.logo-text {
  color: green;
  font-family: "Lucida Handwriting", cursive;
  font-size: 25px;
}
"""

style_content ="""
.content ul {
  position: sticky;
  top: 0;
  left: 0;
}
"""

style_bottom = """
.back-to-top {
  position: fixed;
  bottom: 50px;
  right: 50px;
  width: 50px;
  height: 50px;
  border-radius: 25px;
  background-color: #333;
  color: white;
  text-align: center;
  line-height: 50px;
  font-size: 30px;
  font-weight: bold;
}
"""

style_clearfix ="""
    .clearfix::after {
      content: "";
      display: table;
      clear: both;
    }
    """

style_dir = {
    'style_date': style_date,
    'style_input': style_input,
    'style_script': style_script,
    'style_packages': style_packages,
    'style_tree': style_tree,
    'style_pictures': style_pictures,
    'style_tables': style_tables,
    'style_store': style_store,
    'style_supplement': style_supplement,
    'style_Pre_report': style_Pre_report,
    'style_Post_report': style_Post_report,
    'style_head': style_head,
    'style_body':style_body,
    'style_logo':style_logo,
    'style_content':style_content,
    'style_bottom':style_bottom,
    'style_clearfix':style_clearfix
}
