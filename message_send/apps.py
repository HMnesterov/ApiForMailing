from django.apps import AppConfig


class MessageSendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'message_send'
nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', "I","J","K", "L")
distances = {
    'B': {'A':None, 'C':None, "H":None, "I":None, "G":None, },
    "C":{'B':None, "D":None, "H":None, "I":None, "J":None},
    "D":{"C":None, "E":None, "J":None, "I":None, "K":None},

    "E":{"D":None, "F":None, "K":None, "J":None, "L":None, },
    "F":{"E":None,  "K":None, "G":None, 'A':None,  "L":None,},
    "A":{'B':None, "F":None, "G":None, "L":None, "H":None,},
    "G":{"L":None, "H":None,  "F":None, "A":None, "B":None, "K":None, "J":None, "I":None,},
    "L":{"K":None, "J":None, "I":None, "G":None, "H":None, "F":None, "A":None, "E":None},
    "K":{"G":None, "H":None, "J":None, "I":None, "L":None, "E":None, 'C':None, "D":None,},
    "J":{"E":None, 'C':None, "D":None,  "I":None, "K":None, "G":None, "H":None,"L":None, },
    "I":{"D":None,'C':None,"B":None, "J":None, "H":None,"L":None, "K":None, "G":None,},
    "H":{'A':None, 'C':None, 'B':None, "K":None, "J":None, "I":None, "G":None, "L":None,}
}