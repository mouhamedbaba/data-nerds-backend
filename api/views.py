from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def api(request):
    data = [{
        "id": 1,
        "Code": "AAD003",
        "Numero": "2016023LD",
        "Nom": "NDIAYE",
        "Prenom": "mbaye",
        "Date_naissane": "12/09/00",
        "Classe": "5iemeA",
        "Notes": {
            "FRANCAIS": {
                "devoir": [
                    11.0,
                    17.0
                ],
                "exam": 15.0,
                "moyenne": 14.666666666666666
            },
            "ANGLAIS": {
                "devoir": [
                    19.0,
                    14.0
                ],
                "exam": 15.0,
                "moyenne": 15.5
            },
            "MATH": {
                "devoir": [
                    5.0,
                    13.0
                ],
                "exam": 5.0,
                "moyenne": 6.333333333333333
            },
            "SVT": {
                "devoir": [
                    12.0,
                    9.0
                ],
                "exam": 12.0,
                "moyenne": 11.5
            },
            "PC": {
                "devoir": [
                    13.0,
                    11.0
                ],
                "exam": 7.0,
                "moyenne": 8.666666666666666
            },
            "HG": {
                "devoir": [
                    16.0,
                    15.0
                ],
                "exam": 17.0,
                "moyenne": 16.5
            },
            "moyenne_general": 12.194444444444443
        },
        "Invalid_colums": [
            "Numero"
        ]
    }]
    return HttpResponse(data)