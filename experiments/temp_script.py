import inspect
import os

from csrank.util import configure_logging_numpy_keras
from experiments.dbconnection import DBConnector

if __name__ == '__main__':
    LOGS_FOLDER = 'logs'
    OPTIMIZER_FOLDER = 'optimizers'
    DIR_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    log_path = os.path.join(DIR_PATH, 'logs', 'temp.log')
    configure_logging_numpy_keras(log_path=log_path)
    config_file_path = os.path.join(DIR_PATH, 'config', 'clusterdb.json')
    self = DBConnector(config_file_path=config_file_path, is_gpu=True, schema='master')
    self.insert_new_jobs_with_different_fold()
