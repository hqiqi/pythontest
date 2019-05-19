class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score


    def best_score(players):
        """From the given list of players, return the
        player with the best highscore.
        """

        if len(players) == 0:
            return None

        # Assume for now that the best player is the first one
        best_player = players[0]
        best_score = players[0].score

        i = 1
        while i < len(players):
            player = players[i]
            score = players[i].score

            if score > best_score:
                best_player = player
                best_score = score

            i += 1

        # `best_player` now refers to the Player object with
        # the best highscore.
        return best_player


# Some sample code that uses the Player class.
p1 = Player('Homer', 50)
p2 = Player('Bart', 250)
p3 = Player('Lisa', 150)

ls = [p1, p2, p3]
best = Player.best_score(ls)

msg = '{} has the best score, with {} points!'.format(best.name, best.score)
print(msg)  # Bart has the best score, with 250 points!
