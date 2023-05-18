#wkhtmltopdf或WeasyPrint
import argparse
import pdfkit


#'/public/home/caojun/software/wkhtmltopdf/wkhtmltopdf/local/bin/wkhtmltopdf'
def html_to_pdf(html, to_file, path_wkthmltopdf):
    wkhtmltopdf_options = {
        'enable-local-file-access': None
    }
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdfkit.from_file(html, to_file, configuration=config,options=wkhtmltopdf_options)

def main():
    parser = argparse.ArgumentParser(description='Get script info')
    parser.add_argument('input_html', type=str, help='Path to the input HTML file')
    parser.add_argument('output_pdf', type=str, help='Path to the output PDF file')
    parser.add_argument('path_wkthmltopdf', type=str, help='Path to wkthmltopdf')
    args = parser.parse_args()
    html_to_pdf(args.input_html, args.output_pdf, args.path_wkthmltopdf)

if(__name__=="__main__"):
    main()