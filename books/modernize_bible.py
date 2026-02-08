#!/usr/bin/env python3
"""
Modernize World English Bible HTML files:
1. Rename files to full book names
2. Update internal links
3. Clean up HTML structure
"""

import os
import re
import glob
import shutil

# Mapping of old abbreviations to new full names
BOOK_MAPPING = {
    'GEN': 'Genesis',
    'EXO': 'Exodus',
    'LEV': 'Leviticus',
    'NUM': 'Numbers',
    'DEU': 'Deuteronomy',
    'JOS': 'Joshua',
    'JDG': 'Judges',
    'RUT': 'Ruth',
    '1SA': '1_Samuel',
    '2SA': '2_Samuel',
    '1KI': '1_Kings',
    '2KI': '2_Kings',
    '1CH': '1_Chronicles',
    '2CH': '2_Chronicles',
    'EZR': 'Ezra',
    'NEH': 'Nehemiah',
    'EST': 'Esther',
    'JOB': 'Job',
    'PSA': 'Psalms',
    'PRO': 'Proverbs',
    'ECC': 'Ecclesiastes',
    'SNG': 'Song_of_Solomon',
    'ISA': 'Isaiah',
    'JER': 'Jeremiah',
    'LAM': 'Lamentations',
    'EZK': 'Ezekiel',
    'DAN': 'Daniel',
    'HOS': 'Hosea',
    'JOL': 'Joel',
    'AMO': 'Amos',
    'OBA': 'Obadiah',
    'JON': 'Jonah',
    'MIC': 'Micah',
    'NAM': 'Nahum',
    'HAB': 'Habakkuk',
    'ZEP': 'Zephaniah',
    'HAG': 'Haggai',
    'ZEC': 'Zechariah',
    'MAL': 'Malachi',
    'MAT': 'Matthew',
    'MRK': 'Mark',
    'LUK': 'Luke',
    'JHN': 'John',
    'ACT': 'Acts',
    'ROM': 'Romans',
    '1CO': '1_Corinthians',
    '2CO': '2_Corinthians',
    'GAL': 'Galatians',
    'EPH': 'Ephesians',
    'PHP': 'Philippians',
    'COL': 'Colossians',
    '1TH': '1_Thessalonians',
    '2TH': '2_Thessalonians',
    '1TI': '1_Timothy',
    '2TI': '2_Timothy',
    'TIT': 'Titus',
    'PHM': 'Philemon',
    'HEB': 'Hebrews',
    'JAS': 'James',
    '1PE': '1_Peter',
    '2PE': '2_Peter',
    '1JN': '1_John',
    '2JN': '2_John',
    '3JN': '3_John',
    'JUD': 'Jude',
    'REV': 'Revelation',
    # Deuterocanonical
    'TOB': 'Tobit',
    'JDT': 'Judith',
    'ESG': 'Esther_Greek',
    'WIS': 'Wisdom_of_Solomon',
    'SIR': 'Sirach',
    'BAR': 'Baruch',
    'DAG': 'Daniel_Greek',
    'MAN': 'Prayer_of_Manasseh',
    '1MA': '1_Maccabees',
    '2MA': '2_Maccabees',
    '3MA': '3_Maccabees',
    '4MA': '4_Maccabees',
    '1ES': '1_Esdras',
    '2ES': '2_Esdras',
    'PS': 'Psalm_151',
    # Supplementary
    'FRT': 'Front_Matter',
    'GLO': 'Glossary',
}

def update_links_in_content(content):
    """Update all internal links in HTML content."""
    for old_abbrev, new_name in BOOK_MAPPING.items():
        # Match href='ABB.htm' or href='ABB01.htm' patterns
        pattern = rf"(href=['\"]){old_abbrev}(\d*\.htm['\"])"
        replacement = rf"\g<1>{new_name}\2"
        content = re.sub(pattern, replacement, content)
    return content


def clean_html_content(content, book_name, chapter_num, is_chapter_list):
    """Clean and modernize HTML content."""

    if is_chapter_list:
        return clean_chapter_list(content, book_name)
    else:
        return clean_chapter_content(content, book_name, chapter_num)


def clean_chapter_list(content, book_name):
    """Clean a chapter list page."""
    # Extract chapter links
    chapter_links = re.findall(r"<li><a href=['\"]([^'\"]+)['\"]>(\d+)</a></li>", content)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>World English Bible - {book_name}</title>
  <link rel="stylesheet" href="../styles/styles.css">
</head>
<body class="chlist">
  <header>
    <h1><a href="https://eBible.org/">World English Bible</a></h1>
    <h2><a href="../index.htm">{book_name}</a></h2>
  </header>

  <nav class="tnav">
'''
    # Add chapter links in rows of 5
    for i, (href, num) in enumerate(chapter_links):
        if i % 5 == 0 and i > 0:
            html += '  </nav>\n\n  <nav class="tnav">\n'
        html += f'    <a href="{href}">{num}</a>\n'

    html += '''  </nav>
</body>
</html>
'''
    return html


def clean_chapter_content(content, book_name, chapter_num):
    """Clean a chapter content page."""

    # Extract navigation links
    nav_match = re.search(r"<ul class=['\"]tnav['\"]>(.*?)</ul>", content, re.DOTALL)
    nav_links = []
    if nav_match:
        nav_links = re.findall(r"<li><a href=['\"]([^'\"]+)['\"]>([^<]+)</a></li>", nav_match.group(1))

    # Build navigation HTML
    nav_html = '  <nav class="tnav">\n'
    for href, text in nav_links:
        text = text.replace('&lt;', '\u2190').replace('&gt;', '\u2192')
        nav_html += f'    <a href="{href}">{text}</a>\n'
    nav_html += '  </nav>\n'

    # Extract and clean main content
    main_match = re.search(r"<div class=['\"]main['\"]>(.*?)(?:<ul class=['\"]tnav|<div class=['\"]footnote)",
                          content, re.DOTALL)
    main_content = main_match.group(1) if main_match else ''

    # Process title elements
    titles = []
    for match in re.finditer(r"<div class=['\"]mt(\d?)['\"]>([^<]*)</div>", main_content):
        cls = 'mt' + match.group(1) if match.group(1) else 'mt'
        text = match.group(2).strip()
        if text:
            titles.append(f'    <div class="{cls}">{text}</div>')

    # Process chapter label
    chapter_label = ''
    ch_match = re.search(r"<div class=['\"]chapterlabel['\"][^>]*>([^<]*)</div>", main_content)
    if ch_match:
        chapter_label = f'    <h2 class="chapterlabel">{ch_match.group(1).strip()}</h2>'

    # Process section markers (ms)
    sections = []
    for match in re.finditer(r"<div class=['\"]ms['\"]>([^<]*)</div>", main_content):
        text = match.group(1).strip()
        if text:
            sections.append(f'    <div class="ms">{text}</div>')

    # Process paragraphs and poetry
    paragraphs = []
    for match in re.finditer(r"<div class=['\"]([pqbm][\d]?)['\"]>(.*?)</div>", main_content, re.DOTALL):
        cls = match.group(1)
        para_content = clean_paragraph(match.group(2))
        if para_content.strip():
            paragraphs.append(f'    <p class="{cls}">{para_content}</p>')

    # Build main content
    main_parts = titles + ([chapter_label] if chapter_label else []) + sections + paragraphs
    main_html = '\n'.join(main_parts)

    # Extract and clean footnotes
    footnotes_html = ''
    fn_match = re.search(r"<div class=['\"]footnote['\"]>(.*?)</div>", content, re.DOTALL)
    if fn_match:
        footnotes_html = clean_footnotes(fn_match.group(1))

    # Build final HTML
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{book_name} Chapter {chapter_num} - World English Bible">
  <title>World English Bible - {book_name} {chapter_num}</title>
  <link rel="stylesheet" href="../styles/styles.css">
</head>
<body>
{nav_html}
  <main class="main">
{main_html}
  </main>

{nav_html}
{footnotes_html}
  <footer class="copyright">
    <p><a href="https://eBible.org/">eBible.org</a> | <a href="webfaq.htm">FAQ</a> | Public Domain</p>
  </footer>
</body>
</html>
'''
    return html


def clean_paragraph(content):
    """Clean paragraph content."""
    # Standardize quotes
    content = re.sub(r"(\w+)='([^']*)'", r'\1="\2"', content)

    # Clean verse spans
    content = re.sub(
        r'<span class="verse" id="V(\d+)">(\d+)&#160;</span>',
        r'<span class="verse" id="v\1">\2</span> ',
        content
    )

    # Move popup content to title attribute for cleaner HTML
    content = re.sub(
        r'<a href="#(FN\d+)" class="notemark">([^<]*)<span class="popup">([^<]*)</span></a>',
        r'<a href="#\1" class="notemark" title="\3">\2</a>',
        content
    )

    # Clean whitespace
    content = re.sub(r'\s+', ' ', content).strip()

    return content


def clean_footnotes(content):
    """Clean footnotes section."""
    content = re.sub(r'<hr\s*/?>', '', content)

    footnotes = []
    for match in re.finditer(
        r'<p class="f" id="(FN\d+)">\s*<span class="notemark">([^<]*)</span>\s*<a class="notebackref" href="#V(\d+)">([^<]*)</a>\s*<span class="ft">([^<]*)</span>\s*</p>',
        content, re.DOTALL
    ):
        fn_id, marker, verse_id, ref, text = match.groups()
        footnotes.append(f'    <p class="f" id="{fn_id}"><span class="notemark">{marker}</span> <a class="notebackref" href="#v{verse_id}">{ref}</a> {text.strip()}</p>')

    if not footnotes:
        return ''

    return '  <footer class="footnote">\n' + '\n'.join(footnotes) + '\n  </footer>\n'


def get_book_abbrev(filename):
    """Extract book abbreviation from filename."""
    match = re.match(r'^([A-Z0-9]+?)(\d*)\.htm$', filename, re.IGNORECASE)
    if match:
        return match.group(1).upper(), match.group(2)
    return None, None


def process_file(filepath):
    """Process a single file: update links and clean HTML."""
    basename = os.path.basename(filepath)
    abbrev, chapter = get_book_abbrev(basename)

    if not abbrev or abbrev not in BOOK_MAPPING:
        return None, None

    new_name = BOOK_MAPPING[abbrev]
    is_chapter_list = not chapter

    # Read content
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        content = f.read()

    # Update links first
    content = update_links_in_content(content)

    # Clean HTML
    book_display = new_name.replace('_', ' ')
    content = clean_html_content(content, book_display, chapter, is_chapter_list)

    # Determine new filename
    new_filename = f"{new_name}{chapter}.htm" if chapter else f"{new_name}.htm"

    return new_filename, content


def main():
    books_dir = os.path.dirname(os.path.abspath(__file__))

    # Get all HTML files
    htm_files = glob.glob(os.path.join(books_dir, '*.htm'))

    # Skip utility files
    skip_files = {'links.htm', 'webfaq.htm', 'copyright.htm', 'index.htm',
                  'modernize_bible.py', 'cleanup_html.py', 'convert_to_json.py', 'update_links.py'}

    print(f"Found {len(htm_files)} HTML files")

    # Process files - collect results first
    results = []
    for filepath in sorted(htm_files):
        basename = os.path.basename(filepath)
        if basename in skip_files:
            continue

        try:
            new_filename, content = process_file(filepath)
            if new_filename and content:
                results.append((filepath, new_filename, content))
        except Exception as e:
            print(f"  Error processing {basename}: {e}")

    print(f"Processing {len(results)} Bible files...")

    # Delete old files and write new ones
    for old_path, new_filename, content in results:
        old_basename = os.path.basename(old_path)
        new_path = os.path.join(books_dir, new_filename)

        # Remove old file
        if os.path.exists(old_path):
            os.remove(old_path)

        # Write new file
        with open(new_path, 'w', encoding='utf-8') as f:
            f.write(content)

        if old_basename != new_filename:
            print(f"  {old_basename} -> {new_filename}")
        else:
            print(f"  Updated: {new_filename}")

    print(f"\nDone! Processed {len(results)} files")


if __name__ == '__main__':
    main()
