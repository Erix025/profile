#!/usr/bin/env python3
"""
BibTeX to Hugo Markdown converter for publications
Usage: python scripts/bib2md.py <input.bib> [output_dir]
"""

import sys
import os
import re
from pathlib import Path


def parse_bibtex(bib_content):
    """Simple BibTeX parser that extracts entries"""
    entries = []

    # Match BibTeX entries
    pattern = r'@(\w+)\{([^,]+),\s*\n((?:[^}]|\n)*)\}'
    matches = re.finditer(pattern, bib_content, re.MULTILINE)

    for match in matches:
        entry_type = match.group(1)
        cite_key = match.group(2)
        fields_str = match.group(3)

        # Parse fields
        fields = {'type': entry_type, 'citekey': cite_key}
        field_pattern = r'(\w+)\s*=\s*\{([^}]*)\}|(\w+)\s*=\s*"([^"]*)"'

        for field_match in re.finditer(field_pattern, fields_str):
            if field_match.group(1):
                key = field_match.group(1).lower()
                value = field_match.group(2)
            else:
                key = field_match.group(3).lower()
                value = field_match.group(4)

            fields[key] = value.strip()

        entries.append(fields)

    return entries


def parse_authors(author_string):
    """Parse author string and return list of authors"""
    if not author_string:
        return []

    # Split by 'and'
    authors = re.split(r'\s+and\s+', author_string)

    # Clean up author names
    cleaned_authors = []
    for author in authors:
        # Handle "Last, First" format
        if ',' in author:
            parts = author.split(',')
            author = f"{parts[1].strip()} {parts[0].strip()}"
        cleaned_authors.append(author.strip())

    return cleaned_authors


def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text


def create_markdown(entry, output_dir):
    """Create Hugo markdown file from BibTeX entry"""

    # Extract fields
    title = entry.get('title', 'Untitled')
    authors = parse_authors(entry.get('author', ''))
    year = entry.get('year', '2024')
    month = entry.get('month', '01')

    # Try to get publication venue
    venue = entry.get('booktitle') or entry.get('journal') or entry.get('venue', '')

    # Get DOI or URL
    doi = entry.get('doi', '')
    url = entry.get('url', '')
    if doi and not url:
        url = f"https://doi.org/{doi}"

    # Create description from abstract or title
    description = entry.get('abstract', f"Publication: {venue}")
    if len(description) > 200:
        description = description[:197] + "..."

    # Determine pubtype
    entry_type = entry.get('type', 'article').lower()
    pubtype_map = {
        'article': 'Paper',
        'inproceedings': 'Conference Paper',
        'incollection': 'Conference Paper',
        'techreport': 'Technical Report',
        'phdthesis': 'PhD Thesis',
        'mastersthesis': 'Master Thesis',
        'book': 'Book',
    }
    pubtype = pubtype_map.get(entry_type, 'Paper')

    # Create filename
    slug = slugify(title[:50])
    filename = f"{slug}.md"
    filepath = Path(output_dir) / filename

    # Format month
    month_num = month.strip().zfill(2) if month.isdigit() else "01"
    date = f"{year}-{month_num}-01"

    # Create markdown content
    md_content = f"""---
title: "{title}"
date: {date}
pubtype: "{pubtype}"
featured: true
description: "{description}"
authors: [{', '.join([f'"{a}"' for a in authors])}]
tags: []
image: "/img/publications/{slug}.png"
link: "{url}"
venue: "{venue}"
weight: 500
sitemap:
  priority: 0.8
---

{entry.get('abstract', '')}

"""

    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md_content)

    print(f"Created: {filename}")
    print(f"  Title: {title}")
    print(f"  Authors: {', '.join(authors)}")
    print(f"  Image needed: /img/publications/{slug}.png")
    print()

    return filename


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/bib2md.py <input.bib> [output_dir]")
        sys.exit(1)

    bib_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "content/publications"

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Read BibTeX file
    try:
        with open(bib_file, 'r', encoding='utf-8') as f:
            bib_content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{bib_file}' not found")
        sys.exit(1)

    # Parse BibTeX
    entries = parse_bibtex(bib_content)

    if not entries:
        print("No BibTeX entries found in the file")
        sys.exit(1)

    print(f"Found {len(entries)} publication(s)\n")
    print("=" * 60)
    print()

    # Create markdown files
    for entry in entries:
        create_markdown(entry, output_dir)

    print("=" * 60)
    print(f"\nDone! Created {len(entries)} markdown file(s) in {output_dir}")
    print("\nNext steps:")
    print("1. Add images for each publication to static/img/publications/")
    print("2. Review and edit the generated markdown files")
    print("3. Run 'hugo server' to preview your site")


if __name__ == '__main__':
    main()
