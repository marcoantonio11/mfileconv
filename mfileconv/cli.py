import os
import sys

from mfileconv.core import csv_to_dict, dict_to_json
from mfileconv.utils.log import get_logger

log = get_logger()


def main():
    def welcome_screen() -> str:
        """Set welcome screen"""
        current_user = os.getenv("USER", "anonymous")
        print("")
        print("#" * 80)
        print(
            f"{' Hello ' + current_user.capitalize() +', welcome to mfileconv! ':#^80}"
        )
        print("#" * 80)
        print("")
        log.info(f"'{current_user}' started the system.")
        return current_user

    def available_conversions() -> None:
        """Shows available conversions"""
        print("Conversion currently available:")
        print("-> CSV to JSON")
        print()

    def check_if_cvs_has_a_header() -> str | None:
        print("WARNING: Make sure to use a dot to separate subkeys.")
        print("Example: name,email,address.street,address.neighborhood")
        print()
        while True:
            has_a_header = input(
                "Does your CSV file has a header and is formatted correctly (y/n)? "
            ).lower()
            if has_a_header == "y":
                log.debug(
                    "Does your CSV file has a header and is formatted correctly (y/n)?"
                )
                log.debug(f"Option chosen '{has_a_header}'.")
                return get_csv_file()
            elif has_a_header == "n":
                print("Ok, fix the file and run the program again.")
                log.debug(
                    "Does your CSV file has a header and is formatted correctly (y/n)?"
                )
                log.debug(f"Option chosen '{has_a_header}'.")
                log.info("System closed.")
                print()
                sys.exit(0)
            else:
                print(f"You typed '{has_a_header}'!")
                print("Invalid option. Please enter 'y' or 'n'.")
                print()
                log.debug(
                    "Does your CSV file has a header and is formatted correctly (y/n)?"
                )
                log.debug(
                    f"Invalid option '{has_a_header}'. Waiting for '{user}' to type again..."
                )

    def get_csv_file() -> str:
        filepath = input("Enter the absolute path of the file: ")
        return filepath

    user = welcome_screen()
    available_conversions()
    csv_filepath = check_if_cvs_has_a_header()
    new_dict_file = csv_to_dict(csv_filepath)
    log.info("dict created successfully.")
    json_str = dict_to_json(new_dict_file)
    print(json_str)
    log.info("JSON string created successfully.")
    log.info("System closed.")
