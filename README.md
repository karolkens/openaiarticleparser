
# Article Parser

## Opis

Ten projekt zawiera skrypt `articleparser.py`, który jest aplikacją napisaną w Pythonie. Aplikacja odczytuje treść artykułu z pliku tekstowego, przesyła ją do API OpenAI w celu przetworzenia, a następnie generuje strukturalny kod HTML, który można wyświetlić w przeglądarce.

## Funkcjonalności

- Łączenie się z API OpenAI i przetwarzanie treści artykułu na kod HTML.
- Generowanie pliku `artykul.html` z przetworzonym artykułem.
- Generowanie `podglad.html` opartego na szablonie HTML (`szablon.html`), który umożliwia pełny podgląd artykułu.

## Wymagania

- Python 3.6 lub nowszy
- Biblioteka `openai`
- Biblioteka `os` (standardowa biblioteka Pythona)

## Instalacja

1. **Klonowanie repozytorium**:
   ```bash
   git clone https://github.com/TwojUzytkownik/article-parser.git
   cd article-parser
   ```

2. **Instalacja zależności**:
   Zainstaluj bibliotekę OpenAI:
   ```bash
   pip install openai
   ```

3. **Konfiguracja API Key**:
   Aby uruchomić aplikację, potrzebujesz klucza API OpenAI. Klucz można uzyskać, rejestrując się na platformie [OpenAI](https://platform.openai.com/).

   Wprowadź swój klucz API w pliku `articleparser.py` w linii:
   ```python
   openai.api_key = 'YOUR_API_KEY'
   ```

## Użycie

1. **Przygotowanie pliku artykułu (`plikartykulu.txt`)**:
   Umieść plik tekstowy `plikartykulu.txt` zawierający treść artykułu w tym samym katalogu, co `articleparser.py`. Skrypt automatycznie wczyta ten plik.

2. **Uruchomienie aplikacji**:
   Aby uruchomić aplikację, użyj komendy:
   ```bash
   python articleparser.py
   ```

3. **Wyniki**:
   - **artykul.html**: Plik z przetworzonym artykułem w formacie HTML.
   - **podglad.html**: Podgląd artykułu w przeglądarce, oparty na szablonie HTML (`szablon.html`).

## Pliki

- `articleparser.py` – główny skrypt programu.
- `plikartykulu.txt` – plik tekstowy z treścią artykułu (wymagany).
- `szablon.html` – pusty szablon HTML używany do generacji podglądu (wymagany).
- `artykul.html` – wynikowy plik HTML generowany przez aplikację.
- `podglad.html` – pełny podgląd artykułu generowany w oparciu o szablon.

## Wymagania dotyczące HTML

- Struktura HTML ogranicza się do sekcji `<body>`.


## Informacje dodatkowe

Jeśli masz pytania lub napotkasz problemy, otwórz nowy issue w repozytorium.
