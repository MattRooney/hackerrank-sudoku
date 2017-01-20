import sys
def split_rows():
    rows = []
    for line in sys.stdin:
        clean_str = line.replace('\r\n', '')
        clean_ints = map(int, clean_str.split())
        rows.append(clean_ints)
    rows.remove(rows[0])
    return rows

def test_count():
    return sys.stdin.readline().replace('\r\n', '')

def collection_valid(num):
    return num == 45

def check_rows(collection):
    bool_list = []
    for row in collection:
        bool_list.append(collection_valid(sum(row)))
    if False in bool_list:
        return False
    else:
        return True

def build_columns(rows):
    return map(list, zip(*rows))

def main():
    t_count = test_count()
    rows = split_rows()
    columns = build_columns(rows)
    if check_rows(rows) and check_rows(columns):
        print 'Valid'
    else:
        print 'Invalid'


#   map(list, zip(*l))
#   transposerish--> [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
#   columns = build_columns
#   boxes = build_boxes
#   if check_rows(rows) and check_columns(columns) and check_boxes(boxes):

#    print("Rows: ", check_rows(columns), "T: ", t_count)

if __name__ == '__main__':
  main()
