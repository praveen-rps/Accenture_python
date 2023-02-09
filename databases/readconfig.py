import configparser

def read_db_params():
		#reading the configuration parameters
		config = configparser.ConfigParser();
		config.read('config/local.env')
		return config;

	