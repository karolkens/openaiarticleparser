
# Article to HTML Converter

## Opis

Ten projekt jest aplikacją w Pythonie, która konwertuje treść artykułu z pliku tekstowego do strukturalnego kodu HTML. Aplikacja korzysta z OpenAI API, aby wygenerować HTML, który spełnia konkretne wymagania dotyczące struktury artykułu oraz miejsc na grafiki. Jest to rozwiązanie zaprojektowane jako część zadania rekrutacyjnego dla Junior AI Developera w firmie Oxido.

## Wymagania

- Python 3.6 lub nowszy
- Biblioteka `openai`

## Instalacja

1. **Klonowanie repozytorium**:
   ```bash
   git clone https://github.com/TwojUzytkownik/article-to-html.git
   cd article-to-html
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

1. **Przygotowanie pliku artykułu**:
   Umieść plik tekstowy z artykułem w folderze głównym projektu lub podaj do niego pełną ścieżkę. Domyślna ścieżka pliku jest ustawiona w zmiennej `article_path` w funkcji `main`.

2. **Uruchomienie aplikacji**:
   Aby uruchomić aplikację, w terminalu wykonaj:
   ```bash
   python articleparser.py
   ```

3. **Wynik**:
   Po uruchomieniu aplikacja wygeneruje plik `artykul.html`, który zawiera kod HTML artykułu. HTML jest przygotowany zgodnie z wymogami:
   - Tekst jest strukturalnie podzielony na odpowiednie sekcje HTML.
   - W miejscach na grafiki wstawiono tagi `<img src="image_placeholder.jpg" alt="prompt do grafiki">` wraz z podpisami.

## Pliki

- `articleparser.py` – główny skrypt programu, który konwertuje artykuł do HTML.
- `artykul.html` – wynikowy plik HTML generowany przez aplikację.

## Wymagania dotyczące HTML

- Struktura HTML ogranicza się do sekcji `<body>`.
- Nie dodawano stylów CSS ani JavaScript, zgodnie z wymaganiami.

## Autor

Aplikacja została stworzona na potrzeby rekrutacji do firmy Oxido.

## Informacje dodatkowe

Jeśli masz pytania lub napotkasz problemy, skontaktuj się ze mną poprzez sekcję Issues w tym repozytorium.
