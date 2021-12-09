import data.commands as cmd

keywords_en = {
    ("hello", "hi"): cmd.greetings,
    ("bye", "goodbye"): cmd.farewell,
    ("create", "new"): cmd.create_new_event,
    ("password", ""): cmd.change_password,
    ("main", ""): cmd.go_main,
    ("delete", "remove"): cmd.delete_event,
    ("yes", "accept"): cmd.yes,
    ("no", "decline"): cmd.no,
    ("back", "previous"): cmd.go_back,
    ("next", ""): cmd.go_next,
    ("writting", ""): cmd.writting
}