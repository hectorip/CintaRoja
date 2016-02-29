import sys
# exercises form codeeval.com
file = open(sys.argv[1], 'r')
for t in file:
    # 2, 5
    if t.strip() != '':
        vals = t.split(",")  # ["2", " 5"]
        number_list = [int(x.strip()) for x in vals if (x != '' or x != ' ')]

    print(number_list)
