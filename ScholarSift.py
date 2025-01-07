#Code by Shay, August 2024

from scholarly import scholarly
import time

def parse_year(year_str):
    try:
        # Attempt to convert the year to an integer
        return int(year_str)
    except ValueError:
        # If conversion fails, return None
        return None

def get_year_from_result(result):
    # Try to get the year from the 'pub_year' or other relevant fields
    year_str = result.get('bib', {}).get('pub_year', None)
    if year_str is None:
        # Try other fields if 'pub_year' is not available
        year_str = result.get('bib', {}).get('year', None)
        if year_str is None:
            year_str = result.get('bib', {}).get('date', None)

    return parse_year(year_str)

# Define the search query
query = '("*Coefficient of friction") AND ("*outsole" OR "grind diamond" OR "arctic grip" OR "shoe grip") AND ("footwear" OR "shoe" OR "*boot") AND ("mechanical test" OR "test" OR "Human test" OR "*models")'

# Perform the search
search_query = scholarly.search_pubs(query)

# Open a file to save the RIS references with UTF-8 encoding
with open('references.ris', 'w', encoding='utf-8') as ris_file:
    total_references = 0  # Counter for total references processed
    for i, result in enumerate(search_query):
        title = result.get('bib', {}).get('title', 'No title available')
        authors = result.get('bib', {}).get('author', [])
        year = get_year_from_result(result)
        # Set year to 1000 if it is None
        if year is None:
            year = 1000
        journal = result.get('bib', {}).get('journal', 'No journal available')
        abstract = result.get('bib', {}).get('abstract', 'No abstract available')

        # Skip papers published before 2014 (unless year is set to 1000)
        if year < 2014 and year != 1000:
            continue

        # Write RIS formatted reference to the file
        ris_file.write("TY  - JOUR\n")  # Type of reference (Journal article)
        ris_file.write(f"TI  - {title}\n")  # Title
        for author in authors:
            ris_file.write(f"AU  - {author}\n")  # Authors
        ris_file.write(f"PY  - {year}\n")  # Year
        ris_file.write(f"JO  - {journal}\n")  # Journal
        ris_file.write(f"AB  - {abstract}\n")  # Abstract
        ris_file.write("ER  - \n\n")  # End of reference

        # Increment the counter for total references
        total_references += 1

        # Add delay to avoid overwhelming the server
        time.sleep(5)  # Increase delay if necessary

        # Print progress every 100 references
        if total_references % 100 == 0:
            print(f"Processed {total_references} references so far...")

        # Save in batches
        ris_file.flush()

print(f"All references saved to references.ris, total references processed: {total_references}")
