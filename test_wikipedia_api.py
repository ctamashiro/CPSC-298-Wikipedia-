import wikipediaapi

UA = "ChapmanBiasProj/0.1 (mtamura@chapman.edu)"
wiki = wikipediaapi.Wikipedia(language="en", user_agent=UA)

page = wiki.page("Lebron James")
print("Page - Exists:", page.exists())
print("Page - Title:", page.title)
print("Page - Summary:", page.summary[:500])
