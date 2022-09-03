from prettytable import PrettyTable

table = PrettyTable()
table.add_column("니트", [4000, 3200, 1600])
table.add_column("셔터", [1.231, 0.9976, 0.2134])
table.align = "r"
print(table)