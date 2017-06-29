# DBus WebAPI
## Projekt z programowania systemowego

Aplikacja webowa składająca się z 2 głównych modułów:
* Strona wyświetlająca nazwy eksportowane na szynie sesji DBus
* JSON-RPC API dostępne pod adresem `/api` pozwalające wywoływanie metod exportowanych na DBus
oraz wyświetlanie

Ponadto test_api.py zawiera funkcję przedstawiającą korzystanie z API

# Zależności
* `flask`
* `pydbus` - uwaga: brak w PyPI, należy zainstalować globalnie (wymaga bibliotek systemowych)
* `json-rpc`

# Uruchomienie
1. Sklonuj repozytorium
2. `cd dbus-webapi`
3. `export FLASK_APP="website/website.py"`
4. `flask run`
5. Otwórz `http://localhost:5000` w przeglądarce

