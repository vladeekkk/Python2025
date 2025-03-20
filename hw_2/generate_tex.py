def convert_to_tex(table):
    def create_tex_row(row):
        return "  " + " & ".join(row)

    def add_header_footer(content, columns):
        header = "\\begin{tabular}{ " + "c " * columns + "}\n"
        footer = "\\end{tabular}\n"
        return header + content + '\n' + footer

    return add_header_footer(" \\\\\n".join(map(create_tex_row, table)), len(table[0]))
