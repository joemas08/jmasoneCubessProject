def send_form_data_to_file(form_passed: list[dict], file_passed: str):
    _clear_file(file_passed)
    for lists, entries in form_passed.items():
        for entry in entries:
            for field, data in entry.items():
                if data == "":
                    data = "No entry"
                with open(file_passed, "a") as file:
                    file.write(f"{field}\t{data}\n")
            with open("entries.txt", "a") as file:
                file.write("-" * 50 + "\n")


def _clear_file(file_passed):
    with open(file_passed, "a", encoding="UTF-8") as file:
        file.truncate(0)
