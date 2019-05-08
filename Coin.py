import random

class Coin(object):

  def __init__(self):
    self.face = random.choice(["head", "tails"])

  def get_face(self):
    return self.face

  def flip(self):

    self.face = random.choice(["heads", "tails"])

if __name__ == '__main__':

  heads = 0
  tails = 0

  for i in range(1000):
    myCoin = Coin()
    myCoin.flip()

    if myCoin.get_face() == "heads":
      heads += 1
    else:
      tails += 1

  print("total heads: " + str(heads) + "\nTotal tails: " + str(tails))
