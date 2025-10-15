# week7.py
import wikipediaapi
from googletrans import Translator

def get_summary(topic, target_lang, translator):
    """
    Try to retrieve a Wikipedia summary for a topic in a given language.
    1. Try the English page's language link (if exists)
    2. If not found, translate the topic title and search that in target language
    """
    user_agent = "ChapmanBiasProj/0.1 (mtamura@chapman.edu)"

    # English Wikipedia reference page
    wiki_en = wikipediaapi.Wikipedia(user_agent=user_agent, language='en')
    page_en = wiki_en.page(topic)

    # Fallback variable
    summary = None

    # --- STEP 1: Try English language links ---
    if page_en.exists() and target_lang in page_en.langlinks:
        linked_page = page_en.langlinks[target_lang]
        wiki_target = wikipediaapi.Wikipedia(user_agent=user_agent, language=target_lang)
        target_page = wiki_target.page(linked_page.title)
        if target_page.exists():
            summary = target_page.summary[:800]

    # --- STEP 2: If not found, translate title & retry ---
    if not summary:
        translated_title = translator.translate(topic, src='en', dest=target_lang).text
        wiki_target = wikipediaapi.Wikipedia(user_agent=user_agent, language=target_lang)
        target_page = wiki_target.page(translated_title)
        if target_page.exists():
            summary = target_page.summary[:800]
        else:
            return f"No page found for '{topic}' (or '{translated_title}') in {target_lang} Wikipedia."

    return summary


def main():
    translator = Translator()
    topic = input("Enter a topic (e.g., 'Climate change' or 'LeBron James'): ")

    languages = {
        "English": "en",
        "Japanese": "ja",
        "Spanish": "es"
    }

    print(f"\n🌐 Summaries for '{topic}' across different Wikipedia languages:\n")

    for lang_name, lang_code in languages.items():
        print(f"--- {lang_name} Wikipedia ---")
        summary = get_summary(topic, lang_code, translator)
        print(summary)
        print()

        # Translate non-English summaries into English
        if lang_code != "en" and "No page found" not in summary:
            translation = translator.translate(summary, src=lang_code, dest='en')
            print(f"--- English Translation of {lang_name} Summary ---")
            print(translation.text)
            print()

if __name__ == "__main__":
    main()
