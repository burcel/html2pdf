import os
import pdfkit


class PdfCreator:

    def __init__(self):
        self._working_directory = os.path.abspath(os.path.dirname(__file__))
        self._html_path = os.path.join(self._working_directory, "html")
        self._template_path = os.path.join(self._html_path, "template.html")
        self._header_template_path = os.path.join(self._html_path, "header_template.html")
        self._header_path = os.path.join(self._html_path, "header.html")
        self._footer_template_path = os.path.join(self._html_path, "footer_template.html")
        self._footer_path = os.path.join(self._html_path, "footer.html")
        self._index_path = os.path.join(self._html_path, "index.html")
        self._pdf_path = os.path.join(self._working_directory, "out.pdf")
        self._default_dict = {
            "title": "A whole new world!",
            "header_str": "Example Header String",
            "footer_str": "Example Footer String",
            "section_title": "Table name #1",
            "table_list": [
                {
                    "td_0": "885",
                    "td_1": 482,
                    "td_2": "127.0.0.1",
                    "td_3": "01.01.2020 01:00:00",
                    "td_4": "example"
                },
                {
                    "td_0": "105",
                    "td_1": 11,
                    "td_2": "localhost",
                    "td_3": "01.01.2021 01:00:00",
                    "td_4": "link"
                }
            ]
        }
        self._tr_template = """
          <tr>
            <td>{td_0}</td>
            <td>{td_1}</td>
            <td>{td_2}</td>
            <td>{td_3}</td>
            <td><a href="https://www.google.com/search?q={td_4}">{td_4}</a></td>
          </tr>
        """

    def start(self, input_dict):
        """
        Start pdf creator
        :param input_dict:
        :return:
        """
        if input_dict is None:
            input_dict = self._default_dict
        # Populate HTML file from given parameters
        self._populate(input_dict)
        # Create PDF
        options = {
            "page-size": "A4",
            "enable-local-file-access": "",
            "print-media-type": "",
            "viewport-size": "1920x1080",
            "footer-html": self._footer_path,
            "header-html": self._header_path,
            "image-quality": 100,
            "header-spacing": 10,
            "footer-spacing": 5
        }
        pdfkit.from_file(self._index_path, self._pdf_path, options=options)

    def _populate(self, input_dict):
        """
        Populate HTML file
        :param input_dict:
        :return:
        """
        self._populate_table(input_dict)
        self._populate_template_file(input_dict, self._header_template_path, self._header_path)
        self._populate_template_file(input_dict, self._footer_template_path, self._footer_path)
        self._populate_template_file(input_dict, self._template_path, self._index_path)

    def _populate_template_file(self, input_dict, template_path, file_path):
        """
        Read file content from template_path, populate constants and write resulting string to file_path
        :param input_dict:
        :param template_path:
        :param file_path:
        :return:
        """
        with open(template_path, 'r') as f_read:
            html_str = f_read.read()
            html_str = html_str.format(**input_dict)
            with open(file_path, 'w') as f_write:
                f_write.write(html_str)

    def _populate_table(self, input_dict):
        """
        Populate table from given dict
        :param input_dict:
        :return:
        """
        input_dict["table_body"] = ""
        for item_dict in input_dict["table_list"]:
            input_dict["table_body"] += self._tr_template.format(**item_dict)


def main():
    pdf_creator = PdfCreator()
    pdf_creator.start(None)


if __name__ == "__main__":
    main()
