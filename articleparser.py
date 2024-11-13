import openai

# Wprowadź swój klucz API OpenAI
openai.api_key = 'YOUR_API_KEY'

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

# Funkcja do zapisu odpowiedzi w pliku HTML
def save_to_html(content, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Główna funkcja programu
def main():
    # Ścieżka do pliku artykułu
    article_path = 'C:/Users/karolkens/zadanieopenai/plikartykulu.txt'  # Podaj rzeczywistą ścieżkę do pliku z artykułem
    article_text = read_article(article_path)
    
    # Przetwarzanie artykułu przez OpenAI
    html_content = process_article(article_text)
    
    # Zapis do pliku HTML
    output_path = 'artykul.html'
    save_to_html(html_content, output_path)
    print(f"Artykuł został zapisany do pliku {output_path}")

if __name__ == "__main__":
    main()
