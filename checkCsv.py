import csv
with open(r'savedrecs.csv', 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    headers = next(csv_reader)  # 获取第一行，可能是头
    for i in headers:
        print(i)
    print(headers)



    # 每一行索引用
    # for row in csv_reader:
    #     print(row[0])


    # 返回所有的列的信息
    # for row in csv_reader:
    #     print(row)