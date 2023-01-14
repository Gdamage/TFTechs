from sys import argv as sys_argv, exit
from importlib.metadata import version

# main app
def main(argv, *args, **kwargs):
    script_name = argv[0]
    len_arguments = len(argv)
    argument_list = [argv[argument] for argument in range(1, len_arguments)]

    #app_version = 1.0
    print(version("TFTechs"))

    if('v' in argument_list):
        print(f'Currently using version {app_version}')
        return app_version

    # calls updater
    # reports missing components
    # finishes if errors are found

if(__name__ == '__main__'):
    main(sys_argv)
    exit()