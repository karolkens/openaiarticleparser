import os
import openai

# Wprowadź swój klucz API OpenAI
openai.api_key = 'YOUR_API_KEY'

# Ustalanie bieżącej ścieżki pliku skryptu
current_file_path = os.path.dirname(os.path.abspath(__file__))

# Ścieżki do plików
article_path = os.path.join(current_file_path, 'plikartykulu.txt')
template_path = os.path.join(current_file_path, 'szablon.html')
output_article_path = os.path.join(current_file_path, 'artykul.html')
output_preview_path = os.path.join(current_file_path, 'podglad.html')

# Funkcja do odczytu treści artykułu
def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Prompt do przetworzenia artykułu
def generate_prompt(article_text):
    prompt = (
        "Przetwórz poniższy artykuł w kod HTML, strukturyzując tekst odpowiednimi tagami HTML "
        "i dodając miejsca na grafiki oznaczone tagiem <img src='image_placeholder.jpg' alt='prompt do grafiki'>."
        f"\n\nArtykuł:\n{article_text}\n\n"
    )
    return prompt

# Funkcja do przetworzenia tekstu przez OpenAI z użyciem endpointu Chat
def process_article(article_text):
    prompt = generate_prompt(article_text)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that formats articles in HTML."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2048,
        temperature=0.5
    )
    return response.choices[0].message['content'].strip()

# Funkcja do zapisu zawartości do pliku HTML
def save_to_html(content, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Funkcja do generowania podglądu w oparciu o szablon
def create_preview(html_content, template_path, output_path):
    # Odczytaj zawartość szablonu
    with open(template_path, 'r', encoding='utf-8') as template_file:
        template_content = template_file.read()
    
    # Wstaw kod artykułu do sekcji <body> szablonu
    preview_content = template_content.replace(
        "<body>\n    <!-- Miejsce na artykuł - wklej tutaj kod HTML artykułu -->\n</body>",
        f"<body>\n{html_content}\n</body>"
    )
    
    # Zapisz podgląd do pliku
    save_to_html(preview_content, output_path)

# Główna funkcja programu
def main():
    article_text = read_article(article_path)
    
    # Przetwarzanie artykułu przez OpenAI
    html_content = process_article(article_text)
    
    # Zapisanie wygenerowanego artykułu do pliku artykul.html
    save_to_html(html_content, output_article_path)
    print(f"Artykuł został zapisany do pliku {output_article_path}")
    
    # Generowanie podglądu artykułu w oparciu o szablon
    create_preview(html_content, template_path, output_preview_path)
    print(f"Podgląd artykułu został zapisany do pliku {output_preview_path}")

if __name__ == "__main__":
    main()
