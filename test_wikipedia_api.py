import wikipediaapi

UA = "ChapmanBiasProj/0.1 (mtamura@chapman.edu)"
wiki = wikipediaapi.Wikipedia(language="en", user_agent=UA)

page = wiki.page("Lebron James")
print("Page - Exists:", page.exists())
print("Page - Title:", page.title)
print("Page - Summary:", page.summary[:500])

# Add a word count for a specific word
word_to_count = "basketball"
text = page.text.lower()  
count = text.count(word_to_count.lower())

print(f"The word '{word_to_count}' appears {count} times in the article.")