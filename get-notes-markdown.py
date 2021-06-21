#!/usr/bin/env python3
import json

HEADER = "<h1>All 🌲🌴 **TREES** 🎄🌳 in this deck</h1>"
NOTE_SEPARATOR = "\n<hr>\n"
HTML_REPLACEMENTS = [
    ['<img src="', '<img height="300" src="media/']
]
JSON_FILE = "deck.json"

def generate_html_for_note(note, field_names):
    string = "<h2>"
    string += note['fields'][0]
    string += "</h2>"
    string += "<table>"
    for i, field in enumerate(note['fields']):
        string += "\n"
        string += generate_html_for_field(field_names[i], field)
    string += "</table>"
    return string

def generate_html_for_field(field_name, field_value):
    for replacement in HTML_REPLACEMENTS:
        field_value = field_value.replace(replacement[0], replacement[1])

    string = "<tr>"
    string += "<td>"
    string += "<code>"
    string += field_name
    string += "</code>"
    string += "</td>"
    string += "<td>"
    string += field_value
    string += "</td>"
    string += "</tr>"
    return string

if __name__ == "__main__":
    data = json.load(open(JSON_FILE, "r"))
    fields = data['note_models'][0]['flds']
    field_names = [f["name"] for f in fields]

    notes = data['notes']
    print(HEADER)
    print("<em>("+str(len(notes))+" notes)</em>")
    for note in notes:
        print(generate_html_for_note(note, field_names))
        print(NOTE_SEPARATOR)