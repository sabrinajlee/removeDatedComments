import sys

def remove_dated_comments(input_file, output_file):    
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:  
        inside_dated_multiline = False      
        inside_nondated_multiline = False
        for line in infile:

            # skip the line if its a dated multiline comment
            if not inside_dated_multiline and not inside_nondated_multiline:
                # check if the first line of a multiline comment contains a date
                multi_line_start = line.find('/*')
                if multi_line_start != -1:
                    inside_nondated_multiline = True
                    inside_dated_multiline = check_for_date(line[multi_line_start:])
                    if inside_dated_multiline:
                        continue
            elif inside_dated_multiline:
                # check if its the end of the multiline comment
                multi_line_end = line.find('*/')
                # update the flag if its the end of the comment before skipping the line
                if multi_line_end != -1:
                    inside_dated_multiline = False
                continue
            else:
                nondated_multi_end = line.find('*/')
                if nondated_multi_end != -1:
                    inside_nondated_multiline = False

             # skip the line if its a dated single line comment
            if is_dated_singleline_comment(line) and not inside_nondated_multiline:
                continue
            outfile.write(line)

def is_dated_singleline_comment(line):
    single_line_comment = line.find('//')
    if single_line_comment != -1:
        # check the string after the characters the begin the comment
        return check_for_date(line[single_line_comment+2:])

def check_for_date(comment):
    # Checks if the comment contains a date in the format "dd/dd/dddd"
    if len(comment) < 10:
        return False
    for i in range(len(comment) - 9):
        if (comment[i].isdigit() and comment[i + 1].isdigit() and comment[i + 2] == '/' and
            comment[i + 3].isdigit() and comment[i + 4].isdigit() and comment[i + 5] == '/' and
            comment[i + 6].isdigit() and comment[i + 7].isdigit() and comment[i + 8].isdigit() and
            comment[i + 9].isdigit()):
            return True
    return False

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    remove_dated_comments(input_file, output_file)
