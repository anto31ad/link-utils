import os
import sys

INDENT_STR = '    '

def parse_csv_line(line: str):
    fields = []
    current_field = ''
    inside_quotes = False

    for char in line:
        if char == '"':
            inside_quotes = not inside_quotes
        elif char == ',' and not inside_quotes:
            fields.append(current_field.strip())
            current_field = ''
        else:
            current_field += char

    fields.append(current_field.strip())

    return fields

def write_links(outfile, inpath, nest_lvl):
    with open(inpath, 'r') as infile:
            count = 1

            outfile.write(f"{INDENT_STR * nest_lvl}<DL>\n")
            for line in infile:
                fields = parse_csv_line(line)
                print(f"{count} : {fields}")
                # if len(fields) == 0:
                #     print(f"failed to parse line {count}")
                #     continue
                outfile.write(f"{INDENT_STR * (nest_lvl + 1)}<DT><a href=\"{fields[0]}\">{fields[1]}</a></DT>\n")
                count += 1
            
            outfile.write(f"{INDENT_STR * nest_lvl}</DL>\n")


def get_filename_no_ext(path: str):
    path_tokens = path.split('/')
    return path_tokens[-1]

def run(args):

    if len(args) != 2:
        print ("Args: <input file path> <output file path>")
        return

    inpath = os.path.join(args[0])
    outpath = os.path.join(args[1])
    # infile_format = args[3]

    if not os.path.exists(inpath):
        print("input file does not exist")
        return

    # if infile_format != 'csv-comma' :
    #     print("file format not supported")
    #     return

    with open(outpath, 'w') as outfile:

        outfile.write(
"""<head>
    <meta charset="UTF-8">
    <title>Exported Bookmarks</title>
</head>

<body>""")

        outfile.write(
f"""
<DL>
    <DT><H3>{get_filename_no_ext(inpath)}</H3></DT>\n""")

        write_links(outfile, inpath, 1)
        outfile.write(
"""</DL>
</body>
</html>""")

        

if __name__ == "__main__":
    
    args = sys.argv[1:]
    run(args)
