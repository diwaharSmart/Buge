import argparse
import os
import json

def start_buge_server():

    # Initializing Parser
    all_args = argparse.ArgumentParser()

    # Add arguments to the parser
    all_args.add_argument("-c", "--conf", required=True,
                          help="PATH OF THE CONFIGURATION FILE")

    all_args.add_argument("-dj_cmd", "--django_command", required=False,
                          help="DJANGO COMMANDS")

    args = vars(all_args.parse_args())

    with open(args["conf"], "r") as file:
        config = json.load(file)

    for key, value in config.items():
        os.putenv(key, value)


    if args["django_command"] is None:
        makemigrations = "py buge/manage.py makemigrations"
        migrate        = "py buge/manage.py migrate"
        cmd            = "py buge/manage.py runserver "+str(config["ip_address"])+":"+str(config["port"])
        os.system(makemigrations)
        os.system(migrate)
        os.system(cmd)

    else:
        cmd = "py buge/manage.py "+args["django_command"]
        os.system(cmd)




if __name__ == "__main__":
    start_buge_server()

