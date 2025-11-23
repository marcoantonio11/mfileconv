import os


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
        return current_user

    def available_conversions():
        """Shows available conversions"""
        print("Conversion currently available:")
        print("-> CSV to JSON")
        print()

    welcome_screen()

    available_conversions()
