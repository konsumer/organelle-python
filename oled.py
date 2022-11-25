from fonts import characters

class Oled:
  def calcxpos(self, line):
    return ((line - 1) * 11) + ((line > 0) * 9 )

  def setLine(self, lineNum, line):
    self.clearLine(lineNum)
    tlen = len(line)
    if (tlen > 21):
      tlen = 21
    self.println_8(line, tlen, 2, self.calcxpos(lineNum) + 1)

  def println_8(self, line, tlen, x, y):
    deltax = x
    for i in range(0, tlen):
      deltax += self.put_char_small(line[i], deltax, y, 1)
      deltax += 1

  def put_char_small(self, char, y, x, color):
    c = ord(char)
    if (c < 32):
      c = 32
    if (c > 127):
      c = 127
    c = c - 32
    for i in range(0, 5):
      for j in range(0, 8):
        if (characters[(c * 5) + i] >> j) & 0x01:
          self.put_pixel(color, y + i, x + j)
    return 5

  def clearLine(self, lineNum):
    # if the first line, also clear the row of pixels right above...
    # fixes a problem if an old 'set line' style patch is loaded after a newer graphics patch
    # otherwise this row of pixels might not be cleared 
    if lineNum == 1:
      for i in range(0, 128):
        self.put_pixel(0, i, 8)

    for i in range(0, 128):
      for j in range(0, 11):
        self.put_pixel(0, i, j + self.calcxpos(lineNum))

  def invertLine(self, lineNum):
    l1 = self.calcxpos(lineNum)
    l2 = self.calcxpos(lineNum + 1)
    self.invert_area(0, l1, 128, l2 - l1)

  def invert_area(self, x, y, sizex, sizey):
    if sizex > 0x80:
      sizex = 0x80
    if sizey > 0x40:
      sizex = 0x40
    for i in range(x, x + sizex):
      for j in range(y, y + sizey):
        self.put_pixel(not self.get_pixel(i, j) , i, j)



