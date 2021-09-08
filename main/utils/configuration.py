import configparser


class Configuration(object):
    def __init__(self, env):
        config = configparser.ConfigParser(allow_no_value=True)
        if env == 'qa':
            config.read('resources/project-qa.cfg')
        elif env == 'staging':
            config.read('resources/project-lt.cfg')
        elif env == 'pr0d':
            config.read('resources/project-prd.cfg')
        else:
            config.read('project-qa.cfg')

        self.base_uri = config.get('ConfigurationSection', 'base_uri')
        self.auth_uri = config.get('ConfigurationSection', 'auth_uri')
        self.db_host = config.get('ConfigurationSection', 'audience_uri')
