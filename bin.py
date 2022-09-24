# import argparse
#
# # Initializing Parser
# parser = argparse.ArgumentParser(description='sort some integers.')
#
# # Adding Argument
# parser.add_argument('integers',
#                     metavar='N',
#                     type=int,
#                     nargs='+',
#                     help='an integer for the accumulator')
#
# parser.add_argument(dest='accumulate',
#                     action='store_const',
#                     const=sorted,
#                     help='arranges the integers in ascending order')
#
# args = parser.parse_args()
# print(args.accumulate(args.integers))

import os

cmd = "py buge/manage.py runserver 127.0.0.1:8060"

returned_value = os.system(cmd)  # returns the exit code in unix
print('returned value:', returned_value)