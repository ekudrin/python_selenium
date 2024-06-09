from dataclasses import dataclass


class Data:
    dropdown_menu = {
        "Autocomplete": "autocomplete",
        "Buttons": "buttons",
        "Checkbox": "checkbox",
        "Datepicker": "datepicker",
        "Drag and Drop": "dragdrop",
        "Dropdown": "dropdown",
        "Enabled and disbled elements": "enabled",
        "File Upload": "fileupload",
        "Key and Mouse Press": "keypress",
        "Modal": "modal",
        "Page Scroll": "scroll",
        "Radio Button": "radiobutton",
        "Switch Window": "switch-window",
        "Complete Web Form": "form"
    }

    month_dict = {
        '01': "Jan",
        '02': "Feb",
        '03': "Mar",
        '04': "Apr",
        '05': "May",
        '06': "Jun",
        '07': "Jul",
        '08': "Aug",
        '09': "Sep",
        '10': "Oct",
        '11': "Nov",
        '12': "Dec"
    }


@dataclass
class Person:
    first_name: str = None
    last_name: str = None
    job_title: str = None
