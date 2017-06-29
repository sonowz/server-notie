from configparser import ConfigParser

config = ConfigParser()
config.read('../config.ini')
blacklist_loc = config['core']['DataLocation'] + config['email']['BlacklistFile']


def add_blacklist(word):
    with open(blacklist_loc, 'a', encoding='utf8') as f:
        f.write(word)


def remove_blacklist(word):
    with open(blacklist_loc, 'w', encoding='utf8') as f:
        blacklist = f.readlines()
        blacklist = [x for x in blacklist if x != word]
        f.seek(0, 0)
        f.write(u'\n'.join(blacklist))