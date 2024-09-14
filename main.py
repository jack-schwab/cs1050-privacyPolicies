import requests
from bs4 import BeautifulSoup
import textstat

# URLs of the privacy policies
urls = {
    "Google": "https://policies.google.com/privacy",
    "Facebook": "https://www.facebook.com/privacy/policy",
    "Amazon": "https://www.amazon.com/privacy",
    "Twitter": "https://twitter.com/en/privacy",
    "Microsoft": "https://privacy.microsoft.com/en-us/privacystatement"
}

# Function to extract text from the privacy policy webpage
def get_privacy_policy_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract all paragraph text
    paragraphs = soup.find_all('p')
    policy_text = " ".join([para.get_text() for para in paragraphs])
    
    return policy_text

# Analyze the length and readability of the privacy policy
def analyze_policy(policy_text):
    word_count = len(policy_text.split())
    flesch_reading_ease = textstat.flesch_reading_ease(policy_text)
    fk_grade_level = textstat.flesch_kincaid_grade(policy_text)
    avg_sentence_length = textstat.avg_sentence_length(policy_text)
    
    return {
        "Word Count": word_count,
        "Flesch Reading Ease": flesch_reading_ease,
        "FK Grade Level": fk_grade_level,
        "Avg Sentence Length": avg_sentence_length
    }

# Dictionary to hold the results
results = {}

# Loop through each URL, get the privacy policy text, and analyze it
for site, url in urls.items():
    policy_text = get_privacy_policy_text(url)
    analysis = analyze_policy(policy_text)
    results[site] = analysis

# Display the results in a readable format
for site, analysis in results.items():
    print(f"{site} Privacy Policy:")
    print(f"  Word Count: {analysis['Word Count']}")
    print(f"  Flesch Reading Ease: {analysis['Flesch Reading Ease']}")
    print(f"  FK Grade Level: {analysis['FK Grade Level']}")
    print(f"  Avg Sentence Length: {analysis['Avg Sentence Length']}")
    print()
