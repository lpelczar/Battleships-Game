import collections

from texttable import Texttable


class HighScoreManager():
    highscore_dict = collections.OrderedDict() #where the key is score int and value is player name

    @staticmethod
    def _load_highscore(filename:str = 'highscore.txt'):
        """
        Method loads scores from given file name and add to dictionary
        :param filename: str -> name of file to load from
        :return: None
        """
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                splitted_line = line.split(';')
                player_name = splitted_line[0]
                score = int(splitted_line[1])
                HighScoreManager.highscore_dict.__setitem__(score, player_name)

    @staticmethod
    def _save_highscore(filename:str = 'highscore.txt'):
        """
        Method saves all highscores from dictionary to given file name.
        :param filename: str -> name of file to save
        :return: None
        """
        dict = HighScoreManager.highscore_dict
        with open(filename, 'w') as file:
            for key, value in dict.items():
                file.write(str(value) + ';' + str(key) + '\n')

    @staticmethod
    def print_highscore():
        """
        Method print in the terminal all scores sorted descending
        :return: None
        """
        dict = HighScoreManager.highscore_dict
        if not dict:
            HighScoreManager._load_highscore()
        t = Texttable()
        t.header(['ID', 'Name', 'Score'])
        id = 1
        for key, value in sorted(dict.items(), reverse=True):
            t.add_row([str(id),value, str(key)])
            id += 1
        print(t.draw())

    @staticmethod
    def add_to_highscore(player_name:str, total_hits:int, misses:int, time_in_seconds:int):
        """
        Method add score to highscore dictionary. If such entry exists and score is lower it overits it
        with higher value.
        :param player_name: str - > name of player
        :param total_hits: int -> component need to calculate score
        :param misses: int -> component need to calculate score
        :param time_in_seconds: int -> component need to calculate score
        :return: None
        """
        dict = HighScoreManager.highscore_dict
        if not dict:
            HighScoreManager._load_highscore()
        score = ((total_hits + 10) - misses) * 100 - time_in_seconds
        key_by_value = [k for k, v in dict.items() if v == player_name]
        if key_by_value and key_by_value[0] < score:
            dict.__setitem__(score, player_name)
        elif not key_by_value:
            dict.__setitem__(score, player_name)
        HighScoreManager._save_highscore()

