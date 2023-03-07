

with open("colors.txt", "r", encoding="UTF-8") as file_handle:

  for data in file_handle:
      print(data.strip())
