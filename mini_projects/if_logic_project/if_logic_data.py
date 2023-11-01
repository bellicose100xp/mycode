characteristics: list[str] = [
    "Witty",
    "Eccentric",
    "Caring",
    "Competitive",
    "Laid-back",
    "Sarcastic",
    "Artistic",
    "Reserved",
    "Insecure",
    "Hardworking",
    "Organized",
    "Intelligent",
    "Enthusiastic",
    "Fashionista",
    "Opinionated",
    "Charming",
]

characters: list[str] = [
    "Michael Scott",
    "Dwight Schrute",
    "Jim Halpert",
    "Pam Beesly",
    "Andy Bernard",
    "Stanley Hudson",
    "Kevin Malone",
    "Angela Martin",
    "Oscar Martinez",
    "Kelly Kapoor",
]

characteristic_map: dict[str, dict[str, int]] = {
    "Michael Scott": {
        "Witty": 3,
        "Eccentric": 3,
        "Caring": 2,
        "Insecure": 3,
        "Hardworking": 1,
        "Enthusiastic": 3,
        "Opinionated": 2,
    },
    "Dwight Schrute": {
        "Eccentric": 3,
        "Competitive": 2,
        "Hardworking": 3,
        "Organized": 1,
        "Enthusiastic": 2,
        "Opinionated": 3,
    },
    "Jim Halpert": {
        "Witty": 3,
        "Laid-back": 2,
        "Sarcastic": 3,
        "Intelligent": 3,
        "Charming": 2,
    },
    "Pam Beesly": {
        "Caring": 3,
        "Artistic": 3,
        "Reserved": 2,
        "Intelligent": 1,
        "Charming": 3,
    },
    "Andy Bernard": {
        "Insecure": 3,
        "Hardworking": 1,
        "Enthusiastic": 1,
        "Fashionista": 2,
    },
    "Stanley Hudson": {
        "Laid-back": 3,
        "Reserved": 2,
        "Hardworking": 1,
        "Organized": 1,
    },
    "Kevin Malone": {
        "Laid-back": 3,
        "Reserved": 2,
        "Charming": 3,
    },
    "Angela Martin": {
        "Competitive": 1,
        "Insecure": 1,
        "Hardworking": 1,
        "Organized": 3,
        "Intelligent": 2,
        "Opinionated": 3,
    },
    "Oscar Martinez": {
        "Caring": 1,
        "Reserved": 2,
        "Organized": 1,
        "Intelligent": 3,
    },
    "Kelly Kapoor": {
        "Sarcastic": 1,
        "Insecure": 3,
        "Enthusiastic": 2,
        "Fashionista": 3,
    },
}
