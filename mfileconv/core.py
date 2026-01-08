import json
import sys

from mfileconv.utils.log import get_logger

log = get_logger()


def csv_to_dict(csv_file: str) -> list:
    registers = []
    try:
        with open(csv_file) as _file:
            headers = _file.readline().strip().split(",")
            for line in _file:
                line = line.strip()
                if not line:
                    continue

                values = line.split(",")
                register = {}

                for i in range(len(headers)):
                    key = headers[i].strip()
                    value = values[i].strip() if i < len(values) else ""

                    key_levels = key.split(".")
                    current_level = register

                    for level in key_levels[:-1]:
                        if level not in current_level:
                            current_level[level] = {}
                        current_level = current_level[level]

                    current_level[key_levels[-1]] = value

                registers.append(register)
    except FileNotFoundError as e:
        log.error(e)
        log.info("System closed with error.")
        sys.exit(1)
    except PermissionError as e:
        log.error(e)
        log.info("System closed with error.")
        sys.exit(2)
    return registers


def dict_to_json(dict_file: dict) -> str:
    json_str = json.dumps(dict_file, ensure_ascii=False, indent=4)
    return json_str
