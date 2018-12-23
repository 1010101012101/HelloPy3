import configparser

config = configparser.RawConfigParser()

# When adding sections or items, add them in the reverse order of
# how you want them to be displayed in the actual file.
# In addition, please note that using RawConfigParser's and the raw
# mode of ConfigParser's respective set functions, you can assign
# non-string values to keys internally, but will receive an error
# when attempting to write to a file or when you get it in non-raw
# mode. SafeConfigParser does not allow such assignments to take place.
session = "Section1"
config.add_section(session)
config.set(session, 'an_int', '15')
config.set(session, 'a_bool', 'true')
config.set(session, 'a_float', '3.1415')
config.set(session, 'baz', 'fun')
config.set(session, 'bar', 'Python')
config.set(session, 'foo', '%(bar)s is %(baz)s!')

# Writing our configuration file to 'example.cfg'
with open('data/example.cfg', 'w') as configfile:
    config.write(configfile)