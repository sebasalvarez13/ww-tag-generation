#!/usr/bin/env python3

import pandas as pd
from IPython.display import HTML
from combine_csv import MergedDataFrame

def tagdisplay():
    df = MergedDataFrame.merge()
    html = df.to_html()

    # write html to file
    output_file = "../templates/tagstable.html"
    try:
        with open(output_file, 'w') as outputfile:
            outputfile.write(
        """
        <!DOCTYPE html>
        <html>
        <head>
        <style>


        .container{
        display: inline-block;
        width: 1000px;
        height: 700px;
        border: 1px solid black;
        overflow: auto;
        }
        table {
        border-collapse: collapse;
        width: 100%;
        }

        td {
        text-align: left;
        padding: 8px;
        }
        th {
        text-align: left;
        padding: 8px;
        height: 10px;
        }

        tr:nth-child(even) {background-color: #f2f2f2;}
        </style>
        </head>
        <body>

        <h2>Responsive Table</h2>
        <p>A responsive table will display a horizontal scroll bar if the screen is too 
        small to display the full content. Resize the browser window to see the effect:</p>
        <p>To create a responsive table, add a container element (like div) with <strong>overflow-x:auto</strong> around the table element:</p>

        <div class = container>

        """
            )
            outputfile.write(html)
            outputfile.write(
        """
        </div>
        </body>
        </html>
        """
            )
    except IOError:
        print("I/O error")
    return()

if __name__ == "__main__":
    tagdisplay()
    
