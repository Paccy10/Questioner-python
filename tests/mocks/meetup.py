VALID_MEETUP = {
    'topic': 'Python Meetup',
    'location': 'Kigali Convention Center',
    'happening_on': '2050-08-06',
    'images': ['http://www.kigalicc.com/uploads/9/8/2/4/98249186/radisson-kigali-24_orig.jpg',
               'http://www.kigalicc.com/uploads/9/8/2/4/98249186/radisson-kigali-47_orig.jpg'],
    'tags': ['Andela', 'Python', 'Programming']
}

INVALID_MEETUP_WITHOUT_TOPIC = {
    'topic': '',
    'location': 'Kigali Convention Center',
    'happening_on': '2050-08-06'
}

INVALID_MEETUP_WITHOUT_LOCATION = {
    'topic': 'Python Meetup',
    'location': '',
    'happening_on': '2050-08-06'
}

INVALID_MEETUP_WITHOUT_DATE = {
    'topic': 'Python Meetup',
    'location': 'Kigali Convention Center',
    'happening_on': ''
}

INVALID_MEETUP_WITH_INVALID_DATE_FORMAT = {
    'topic': 'Python Meetup',
    'location': 'Kigali Convention Center',
    'happening_on': '05-08-2050'
}

INVALID_MEETUP_WITH_INVALID_DATE = {
    'topic': 'Python Meetup',
    'location': 'Kigali Convention Center',
    'happening_on': '2000-08-01'
}

VALID_IMAGES = {
    'images': ['Image1', 'Image2']
}

INVALID_IMAGES = {
    'images': ''
}

INVALID_STRING_IMAGES = {
    'images': 'Image1'
}

VALID_TAGS = {
    'tags': ['Tag1', 'Tag2']
}

INVALID_TAGS = {
    'tags': ''
}

INVALID_STRING_TAGS = {
    'tags': 'Tag1'
}
