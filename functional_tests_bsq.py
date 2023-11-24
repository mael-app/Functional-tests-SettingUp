import os

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'


def get_command_output(cmd):
    try:
        command = os.popen(cmd)
        command_output = command.read()
        command.close()
        return command_output
    except:
        exit(0)


def check_file(test_file_path, expected_output_file):
    c_program_path = 'setting_up'
    expected_output = ""
    with open(expected_output_file, 'r') as file:
        expected_output = file.read()
    program_output = get_command_output("./setting_up " + test_file_path)
    if program_output.strip() != expected_output.strip():
        print(f"{test_file_path} ->{RED} Test failed {RESET}")
        # print("GOT:")
        # print(program_output)
        # print("EXPECTED:")
        # print(expected_output)
    else:
        print(f"{test_file_path} ->{GREEN} Test passed {RESET}")


def run_tests():
    maps_directory = 'example_files/maps'

    map_files = [f for f in os.listdir(maps_directory) if
                 os.path.isfile(os.path.join(maps_directory, f))]

    for map_file in map_files:
        test_file_path = os.path.join(maps_directory, map_file)
        expected_output_file = os.path.join('example_files/solved', map_file)

        check_file(test_file_path, expected_output_file)


if __name__ == "__main__":
    run_tests()
