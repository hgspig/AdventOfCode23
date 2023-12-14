#my function starts by reading in the input from day2data.txt and splitting it by line
def day2part1():
    f = open("day2data.txt", "r")
    data = f.read().splitlines()
    f.close()
    impossible_games = []
    for i in range(0,len(data)):
        game = data[i]
        game = game.split(",")
        print(game)


day2part1()