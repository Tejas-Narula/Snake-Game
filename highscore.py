import shelve

score = 6

class Highscore:
  def __init__(self, score):
    self.score = score
    self.scoreFile = shelve.open('score.txt')
    try:
      self.current_HighScore = self.scoreFile['score']
    except KeyError:
      self.current_HighScore = 0
  
  def save_highscore(self):
    self.scoreFile['score'] = self.score
    self.current_HighScore += 1
    self.scoreFile.close()
  
  def checkAndUpdateScore(self):
    if self.score > self.current_HighScore:
      self.save_highscore()
      #print("New high score updated! to " + str(self.current_HighScore))
      
    elif self.score < self.current_HighScore:
      pass
      #print("You didnt get a highscore! Try again!")
    else:
      print("ooooo! You are very close to a highscore! " + str(self.current_HighScore))
    
    return self.current_HighScore





#Running Highscore(score).checkAndUpdateScore() will check if score is high enogh and update it if it is and store it in disk

# if you want to reset the highscore manually run
#Highscore(score).scoreFile['score'] = 57
# and chenge  = score to what value you want it to be for example:- Highscore(score).scoreFile['score'] = 0