import configparser


class Conf:
    STANDARD_PATH = "./config.ini"

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.STANDARD_PATH)

    def ConfigSectionMap(self, section):
        dict = {}
        options = self.config.options(section)
        for option in options:
            try:
                dict[option] = self.config.get(section, option)
                if dict[option] == -1:
                    print("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict[option] = None
        return dict
