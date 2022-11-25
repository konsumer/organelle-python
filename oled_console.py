from drawille import Canvas
from oled import Oled

class OledConsole(Oled):
  def __init__(self):
    self.canvas = Canvas()
    self.draw_border()

  def draw(self):
    """
    Draw current OLED
    """
    print('\033[A\033[K' * 64)
    print('\033[H\033[2J' + self.canvas.frame())

  def draw_border(self):
    """
    Draws border around OLED. Should only need to be called, initially
    """
    for x in range(0, 132):
      self.canvas.set(x, 0)
      self.canvas.set(x, 67)
    for y in range(0, 68):
      self.canvas.set(0, y)
      self.canvas.set(131, y)

  def invert_area(self, x, y, sizex, sizey):
    """
    Invert an area of the OLED. Overriding so I can use toggle
    """
    if sizex > 0x80:
      sizex = 0x80
    if sizey > 0x40:
      sizex = 0x40
    for i in range(x, x + sizex):
      for j in range(y, y + sizey):
        self.canvas.toggle(i+2, j+2)

  def put_pixel(self, color, x, y):
    """
    Place or clear a single pixel
    """
    if (color):
      self.canvas.set(x+2, y+2)
    else:
      self.canvas.unset(x+2, y+2)

  def get_pixel(self, x, y):
    return this.canvas.get(x, y)

  def clear(self):
    """
    Clear the OLED
    """
    self.canvas.clear()
    self.draw_border()




