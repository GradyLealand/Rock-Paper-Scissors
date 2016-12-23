import sys, random

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import RPS_Lib


#CHANGE THE SECOND PARAMETER HERE TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, RPS_Lib.Ui_MainWindow):
    # initialise gobal variables (i know i shouldn't have any)
    rounds = 0
    wins = 0

        # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        # END DO NOT MODIFY

        # ADD SLOTS HERE
        self.pushButtonRock.clicked.connect(self.Rock_Clicked)
        self.pushButtonPapper.clicked.connect(self.Papper_Clicked)
        self.pushButtonScissors.clicked.connect(self.Scissors_Clicked)
        self.actionNew_Game.triggered.connect(self.Clear_Window)
        self.actionExit.triggered.connect(self.Exit_Game)

    # ADD SLOT FUNCTIONS HERE
    def Rock_Clicked(self):
        playType = "Rock"
        self.Play(playType)

    def Papper_Clicked(self):
        playType = "Papper"
        self.Play(playType)

    def Scissors_Clicked(self):
        playType = "Scissors"
        self.Play(playType)

    def Play(self, throw):
        # add the file path to the throw and set it in the player frame
        filePlayer = "Images\\" + throw
        self.labelDisPlayerHand.setPixmap(QPixmap(filePlayer))
        # get the opponents throw, add the file path and set it to opponents frame
        opponent = self.Opponent_Play()
        fileOpponent = "Images\\" + opponent
        self.labelDisOpponentsHand.setPixmap(QPixmap(fileOpponent))
        self.CheckOutcome(throw, opponent)
        # add one to the total rounds then display how many rounds have been played
        self.rounds += 1
        self.textBrowserDisGamesPlayed.setText(str(self.rounds))
        # display how many times the player has won
        self.textBrowserDisGamesWon.setText(str(self.wins))
        # get the percent of games won then display it
        winPercent = self.WinPercent(self.rounds, self.wins)
        self.textBrowserDisPercentWon.setText(winPercent)

    def Clear_Window(self):
        # reset global variables
        self.wins = 0
        self.rounds = 0
        # Clear all display fields
        self.textBrowserDisGamesPlayed.clear()
        self.textBrowserDisGamesWon.clear()
        self.textBrowserDisPercentWon.clear()
        self.labelDisPlayerHand.clear()
        self.labelDisOpponentsHand.clear()

    def Exit_Game(self):
        reply = QMessageBox.question(self, "EXIT?",
                                     "Would you like to exit the game?",
                                     QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            sys.exit(app.exec_())

    #ADD HELPER FUNCTIONS HERE
    def Opponent_Play(self):
        # roll between 1 and 3 then match each number to an outcome
        roll = random.randint(1,3)
        if roll == 1:
            throw = "Rock"
        elif roll == 2:
            throw = "Papper"
        else:
            throw = "Scissors"
        # return file name
        return throw

    def CheckOutcome(self, player, comp):
        # check first to see what the player has thrown
        if player == "Rock":
            # check to see if the comp has throw a loss and add to wins if it has
            if comp == "Scissors":
                self.wins += 1
        elif player == "Papper":
            if comp == "Rock":
                self.wins += 1
        else:
            if comp == "Papper":
                self.wins += 1

    def WinPercent(self, game, win):
        percent = (win/game) * 100
        percentFormat = str(round(percent, 2)) + "%"
        return percentFormat




# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
# END DO NOT MODIFY
