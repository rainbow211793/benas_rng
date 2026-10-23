# This file contains variables that are used in the main program. It is imported into the main program to access the variables.

from pathlib import Path

# Resetting variables
rng = 0
loop = 0
rolls = 1
badges = 1
plays = 0

# Badges
b2 = False
b3 = False
b4 = False
b5 = False

save_file = Path(__file__).with_name("benas_save.txt")
extra_save_values = {}


def load_save():
    global rng, rolls, badges, plays, b2, b3, b4, b5

    if not save_file.exists():
        return

    known_values = {"rng", "rolls", "badges", "plays", "b2", "b3", "b4", "b5"}
    with save_file.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            key, separator, value = line.partition("=")
            key = key.strip()
            value = value.strip()
            if not separator or not key:
                raise ValueError(f"Invalid save data on line {line_number} of {save_file}")

            if key == "rng":
                rng = int(value)
            elif key == "rolls":
                rolls = int(value)
            elif key == "badges":
                badges = int(value)
            elif key == "plays":
                plays = int(value)
            elif key == "b2":
                if value.lower() not in ("true", "false"):
                    raise ValueError(f"Invalid boolean for {key} on line {line_number} of {save_file}")
                b2 = value.lower() == "true"
            elif key == "b3":
                if value.lower() not in ("true", "false"):
                    raise ValueError(f"Invalid boolean for {key} on line {line_number} of {save_file}")
                b3 = value.lower() == "true"
            elif key == "b4":
                if value.lower() not in ("true", "false"):
                    raise ValueError(f"Invalid boolean for {key} on line {line_number} of {save_file}")
                b4 = value.lower() == "true"
            elif key == "b5":
                if value.lower() not in ("true", "false"):
                    raise ValueError(f"Invalid boolean for {key} on line {line_number} of {save_file}")
                b5 = value.lower() == "true"
            elif key not in known_values:
                extra_save_values[key] = value


def save():
    with save_file.open("w", encoding="utf-8") as file:
        file.write("# Benas RNG save file\n")
        file.write(f"plays = {plays}\n")
        file.write(f"rng = {rng}\n")
        file.write(f"rolls = {rolls}\n")
        file.write(f"badges = {badges}\n")
        file.write(f"b2 = {str(b2).lower()}\n")
        file.write(f"b3 = {str(b3).lower()}\n")
        file.write(f"b4 = {str(b4).lower()}\n")
        file.write(f"b5 = {str(b5).lower()}\n")
        for key, value in extra_save_values.items():
            file.write(f"{key} = {value}\n")


load_save()
plays += 1
save()
