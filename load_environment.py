import os
import configparser
#
# class ConfigLoader:
#     def __init__(self, environment):
#         self.environment = environment
#         self.config = configparser.ConfigParser()
#         self.load_config()
#
#     def load_config(self):
#         config_file = f"config_{self.environment}.ini"
#         if not os.path.exists(config_file):
#             raise FileNotFoundError(f"Arquivo de configuração '{config_file}' não encontrado.")
#         self.config.read(config_file)
#
#     def get_database_config(self):
#         db_config = self.config['database']
#         return {
#             'server': db_config.get('server'),
#             'database': db_config.get('database'),
#             'schema_main': db_config.get('schema_main'),
#             'schema_udc': db_config.get('schema_udc')
#         }


class ConfigLoader:
    def __init__(self, environment):
        self.environment = environment
        self.config = self.load_config()

    def load_config(self):
        if self.environment == 'dev':
            db_config = {
                'server': 'DBDEV',
                'database': 'JDE_CRP',
                'schema_main': 'CRPDTA',
                'schema_udc': 'CRPCTL'
            }
        elif self.environment == 'prod':
            db_config = {
                'server': 'ENTERPRISE',
                'database': 'JDE_PRODUCTION',
                'schema_main': 'PRODDTA',
                'schema_udc': 'PRODCTL'
            }
        else:
            raise ValueError(f"Ambiente desconhecido '{self.environment}'")
        return db_config

    def get_database_config(self):
        return self.config
