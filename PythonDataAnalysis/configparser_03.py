import configparser

config = configparser.ConfigParser()
config.read('example.cfg')

# Set the third, optional argument of get to 1 if you wish to use raw mode.
print(config.get('Section1', 'foo', raw=False))
print(config.get('Section1', 'foo', raw=True))

# The optional fourth argument is a dict with members that will take
# precedence in interpolation.
print(config.get('Section1', 'foo', raw=False, vars={'bar': 'Documentation', 'baz': 'evil'}))