from sys import argv

def main():

    # checks version
    # aks for permission
    # deletes main file
    # downloads update
    # saves update

    script_name = argv[0]
    len_arguments = len(argv)
    argument_list = [argv[argument] for argument in range(1, len_arguments)]

    app_version = 1.0

    if('v' in argument_list):
        print(f'Currently using version {app_version}')
        return app_version


if(__name__ == '__main__'):
    main()