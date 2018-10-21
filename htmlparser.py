def htmlTable(table, row, column):
    tsplit = table.split('</tr><tr>')
    lastIndex = len(tsplit) - 1
    if row > lastIndex:
        return 'No such cell'
    tsplit[0] = tsplit[0][tsplit[0].index('<tr>') + 4:]
    tsplit[lastIndex] = tsplit[lastIndex][:tsplit[lastIndex].index('</tr>')]
    
    trow = tsplit[row]
    rsplit = trow.split('</td><td>')
    lastIndex = len(rsplit) - 1
    if column > lastIndex:
        return 'No such cell'
    rsplit[0] = rsplit[0][rsplit[0].index('<td>') + 4:]
    rsplit[lastIndex] = rsplit[lastIndex][:rsplit[lastIndex].index('</td>')]
    
    return rsplit[column]

"""
HTML tables allow web developers to arrange data into rows and columns of cells. They are created using the <table> tag. Its content consists of one or more rows denoted by the <tr> tag. Further, the content of each row comprises one or more cells denoted by the <td> tag, and content within the <td> tags is what site visitors see in the table. For this task assume that tags have no attributes in contrast to real world HTML.

Some tables contain the <th> tag. This tag defines header cells, which shouldn't be counted as regular cells.

You are given a rectangular HTML table. Extract the content of the cell with coordinates (row, column).

If you are not familiar with HTML, check out this note.

Example

For table = "<table><tr><td>1</td><td>TWO</td></tr><tr><td>three</td><td>FoUr4</td></tr></table>", row = 0, and column = 1, the output should be
htmlTable(table, row, column) = "TWO".

<table>
 <tr>
  <td>1</td>
  <td>TWO</td>
 </tr>
 <tr>
  <td>three</td>
  <td>FoUr4</td>
 </tr>
</table>
corresponds to:

1	TWO
three	FoUr4
For table = "<table><tr><td>1</td><td>TWO</td></tr></table>", row = 1, and column = 0, the output should be
htmlTable(table, row, column) = "No such cell".

<table>
 <tr>
  <td>1</td>
  <td>TWO</td>
 </tr>
</table>
corresponds to:

1	TWO
Input/Output

[execution time limit] 3 seconds (cs)

[input] string table

A syntactically correct representation of a rectangular HTML table with at least one cell. Each of its cells contains only letters and/or digits.

Guaranteed constraints:
35 ≤ table.length ≤ 1600.

[input] integer row

A non-negative integer representing 0-based index of the desired row (rows are numbered from top to bottom).

Guaranteed constraints:
0 ≤ row ≤ 10.

[input] integer column

A non-negative integer representing 0-based index of the desired column (columns are numbered from left to right).

Guaranteed constraints:
0 ≤ column ≤ 10.

[output] string

The content of the cell with coordinates (row, column) or the string "No such cell" if there is no cell with those coordinates in the table.
"""
