import jsonpickle

colors = ['yellow','orange','purple']

class Color:

  def __init__(self, name, hexcode):
    self.name = name
    self.hexcode = hexcode

  def __repr__(self):
    return f"name: {self.name}, hexcode: {self.hexcode}"

colors = [
  Color("red", "ff0000"),
  Color("green", "00ff00"),
  Color("blue", "0000ff")
]

# json_text = jsonpickle.encode(color, unpicklable=True)
# print(json_text)
# color2 = jsonpickle.decode(json_text)
# print(type(color2))

with open("colors2.json", "w", encoding="UTF-8") as file_handle:
    file_handle.write(jsonpickle.encode(colors, unpicklable=True))