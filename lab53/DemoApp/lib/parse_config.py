from configparser import ConfigParser


def read_db_config(filename='../config.ini', section='mysql'):
  """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
  """
  # create parser and read the configuration file
  parser = ConfigParser()
  parser.read(filename)


  db_config = {}
  if parser.has_section(section):
    items = parser.items(section)
    for item in items:
      db_config[item[0]] = item[1]
  else:
    raise Exception(f'{section} not found in the {filename} file')

  return db_config

if __name__ == '__main__':
	db_config = read_db_config()
	print(db_config)