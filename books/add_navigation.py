#!/usr/bin/env python3
"""
Add improved navigation to World English Bible HTML files.
- Sidebar with all books
- Breadcrumb navigation
- Chapter dropdown
- Prev/Next buttons
"""

import os
import re
import glob

# Book data: (filename_prefix, display_name, chapter_count, testament)
BOOKS = [
    # Old Testament
    ('Genesis', 'Genesis', 50, 'ot'),
    ('Exodus', 'Exodus', 40, 'ot'),
    ('Leviticus', 'Leviticus', 27, 'ot'),
    ('Numbers', 'Numbers', 36, 'ot'),
    ('Deuteronomy', 'Deuteronomy', 34, 'ot'),
    ('Joshua', 'Joshua', 24, 'ot'),
    ('Judges', 'Judges', 21, 'ot'),
    ('Ruth', 'Ruth', 4, 'ot'),
    ('1_Samuel', '1 Samuel', 31, 'ot'),
    ('2_Samuel', '2 Samuel', 24, 'ot'),
    ('1_Kings', '1 Kings', 22, 'ot'),
    ('2_Kings', '2 Kings', 25, 'ot'),
    ('1_Chronicles', '1 Chronicles', 29, 'ot'),
    ('2_Chronicles', '2 Chronicles', 36, 'ot'),
    ('Ezra', 'Ezra', 10, 'ot'),
    ('Nehemiah', 'Nehemiah', 13, 'ot'),
    ('Esther', 'Esther', 10, 'ot'),
    ('Job', 'Job', 42, 'ot'),
    ('Psalms', 'Psalms', 150, 'ot'),
    ('Proverbs', 'Proverbs', 31, 'ot'),
    ('Ecclesiastes', 'Ecclesiastes', 12, 'ot'),
    ('Song_of_Solomon', 'Song of Solomon', 8, 'ot'),
    ('Isaiah', 'Isaiah', 66, 'ot'),
    ('Jeremiah', 'Jeremiah', 52, 'ot'),
    ('Lamentations', 'Lamentations', 5, 'ot'),
    ('Ezekiel', 'Ezekiel', 48, 'ot'),
    ('Daniel', 'Daniel', 12, 'ot'),
    ('Hosea', 'Hosea', 14, 'ot'),
    ('Joel', 'Joel', 3, 'ot'),
    ('Amos', 'Amos', 9, 'ot'),
    ('Obadiah', 'Obadiah', 1, 'ot'),
    ('Jonah', 'Jonah', 4, 'ot'),
    ('Micah', 'Micah', 7, 'ot'),
    ('Nahum', 'Nahum', 3, 'ot'),
    ('Habakkuk', 'Habakkuk', 3, 'ot'),
    ('Zephaniah', 'Zephaniah', 3, 'ot'),
    ('Haggai', 'Haggai', 2, 'ot'),
    ('Zechariah', 'Zechariah', 14, 'ot'),
    ('Malachi', 'Malachi', 4, 'ot'),
    # Deuterocanon
    ('Tobit', 'Tobit', 14, 'dc'),
    ('Judith', 'Judith', 16, 'dc'),
    ('Esther_Greek', 'Esther (Greek)', 10, 'dc'),
    ('Wisdom_of_Solomon', 'Wisdom of Solomon', 19, 'dc'),
    ('Sirach', 'Sirach', 51, 'dc'),
    ('Baruch', 'Baruch', 6, 'dc'),
    ('Daniel_Greek', 'Daniel (Greek)', 14, 'dc'),
    ('1_Maccabees', '1 Maccabees', 16, 'dc'),
    ('2_Maccabees', '2 Maccabees', 15, 'dc'),
    ('1_Esdras', '1 Esdras', 9, 'dc'),
    ('Prayer_of_Manasseh', 'Prayer of Manasseh', 1, 'dc'),
    ('Psalm_151', 'Psalm 151', 1, 'dc'),
    ('3_Maccabees', '3 Maccabees', 7, 'dc'),
    ('2_Esdras', '2 Esdras', 16, 'dc'),
    ('4_Maccabees', '4 Maccabees', 18, 'dc'),
    # New Testament
    ('Matthew', 'Matthew', 28, 'nt'),
    ('Mark', 'Mark', 16, 'nt'),
    ('Luke', 'Luke', 24, 'nt'),
    ('John', 'John', 21, 'nt'),
    ('Acts', 'Acts', 28, 'nt'),
    ('Romans', 'Romans', 16, 'nt'),
    ('1_Corinthians', '1 Corinthians', 16, 'nt'),
    ('2_Corinthians', '2 Corinthians', 13, 'nt'),
    ('Galatians', 'Galatians', 6, 'nt'),
    ('Ephesians', 'Ephesians', 6, 'nt'),
    ('Philippians', 'Philippians', 4, 'nt'),
    ('Colossians', 'Colossians', 4, 'nt'),
    ('1_Thessalonians', '1 Thessalonians', 5, 'nt'),
    ('2_Thessalonians', '2 Thessalonians', 3, 'nt'),
    ('1_Timothy', '1 Timothy', 6, 'nt'),
    ('2_Timothy', '2 Timothy', 4, 'nt'),
    ('Titus', 'Titus', 3, 'nt'),
    ('Philemon', 'Philemon', 1, 'nt'),
    ('Hebrews', 'Hebrews', 13, 'nt'),
    ('James', 'James', 5, 'nt'),
    ('1_Peter', '1 Peter', 5, 'nt'),
    ('2_Peter', '2 Peter', 3, 'nt'),
    ('1_John', '1 John', 5, 'nt'),
    ('2_John', '2 John', 1, 'nt'),
    ('3_John', '3 John', 1, 'nt'),
    ('Jude', 'Jude', 1, 'nt'),
    ('Revelation', 'Revelation', 22, 'nt'),
]

def get_book_info(filename_prefix):
    """Get book info from filename prefix."""
    for book in BOOKS:
        if book[0] == filename_prefix:
            return book
    return None

def generate_sidebar_html(current_book=None):
    """Generate the sidebar HTML."""
    html = '''  <aside class="sidebar" id="sidebar">
    <div class="sidebar-header">
      <h2>Books</h2>
      <button class="sidebar-close" aria-label="Close menu">&times;</button>
    </div>

    <details class="sidebar-section" open>
      <summary>Old Testament</summary>
      <ul>
'''
    for book in BOOKS:
        if book[3] == 'ot':
            active = ' class="active"' if book[0] == current_book else ''
            html += f'        <li><a href="{book[0]}01.htm"{active}>{book[1]}</a></li>\n'

    html += '''      </ul>
    </details>

    <details class="sidebar-section">
      <summary>Deuterocanon</summary>
      <ul>
'''
    for book in BOOKS:
        if book[3] == 'dc':
            active = ' class="active"' if book[0] == current_book else ''
            html += f'        <li><a href="{book[0]}01.htm"{active}>{book[1]}</a></li>\n'

    html += '''      </ul>
    </details>

    <details class="sidebar-section">
      <summary>New Testament</summary>
      <ul>
'''
    for book in BOOKS:
        if book[3] == 'nt':
            active = ' class="active"' if book[0] == current_book else ''
            html += f'        <li><a href="{book[0]}01.htm"{active}>{book[1]}</a></li>\n'

    html += '''      </ul>
    </details>
  </aside>
  <div class="sidebar-overlay" id="sidebar-overlay"></div>
'''
    return html


def generate_chapter_options(book_prefix, chapter_count, current_chapter):
    """Generate chapter dropdown options."""
    options = []
    for i in range(1, chapter_count + 1):
        ch_str = f'{i:02d}' if book_prefix == 'Psalms' and i < 100 else f'{i:02d}'
        if book_prefix == 'Psalms':
            ch_str = f'{i:03d}'
        selected = ' selected' if str(i) == str(current_chapter) else ''
        options.append(f'        <option value="{book_prefix}{ch_str}.htm"{selected}>Chapter {i}</option>')
    return '\n'.join(options)


def generate_nav_html(book_prefix, book_name, chapter_num, chapter_count, prev_href, next_href):
    """Generate the navigation HTML."""
    # Chapter dropdown
    chapter_options = generate_chapter_options(book_prefix, chapter_count, chapter_num)

    # Prev/Next classes
    prev_class = '' if prev_href else ' class="disabled"'
    next_class = '' if next_href else ' class="disabled"'
    prev_href = prev_href or '#'
    next_href = next_href or '#'

    html = f'''  <div class="top-nav">
    <button class="menu-toggle" aria-label="Open book menu">&#9776; Books</button>

    <nav class="breadcrumb">
      <a href="../index.htm">Home</a>
      <span class="separator">&rsaquo;</span>
      <a href="{book_prefix}.htm">{book_name}</a>
      <span class="separator">&rsaquo;</span>
      <span class="current">Chapter {chapter_num}</span>
    </nav>

    <div class="chapter-nav">
      <select aria-label="Select chapter">
{chapter_options}
      </select>
    </div>

    <div class="prev-next">
      <a href="{prev_href}"{prev_class} title="Previous">&larr;</a>
      <a href="{next_href}"{next_class} title="Next">&rarr;</a>
    </div>
  </div>
'''
    return html


def process_chapter_file(filepath):
    """Process a chapter file and add navigation."""
    basename = os.path.basename(filepath)

    # Parse filename to get book and chapter
    if basename == 'Psalms.htm':
        return None  # Skip chapter list pages

    match = re.match(r'^(.+?)(\d+)\.htm$', basename)
    if not match:
        return None

    book_prefix = match.group(1)
    chapter_str = match.group(2)
    chapter_num = int(chapter_str)

    book_info = get_book_info(book_prefix)
    if not book_info:
        return None

    book_name = book_info[1]
    chapter_count = book_info[2]

    # Determine prev/next links
    prev_href = None
    next_href = None

    if chapter_num > 1:
        prev_ch = chapter_num - 1
        if book_prefix == 'Psalms':
            prev_href = f'{book_prefix}{prev_ch:03d}.htm'
        else:
            prev_href = f'{book_prefix}{prev_ch:02d}.htm'

    if chapter_num < chapter_count:
        next_ch = chapter_num + 1
        if book_prefix == 'Psalms':
            next_href = f'{book_prefix}{next_ch:03d}.htm'
        else:
            next_href = f'{book_prefix}{next_ch:02d}.htm'

    # Read existing file
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already processed
    if 'class="sidebar"' in content:
        return None

    # Extract the main content
    main_match = re.search(r'<main class="main">(.*?)</main>', content, re.DOTALL)
    if not main_match:
        return None

    main_content = main_match.group(1)

    # Extract footnotes
    footnote_match = re.search(r'<footer class="footnote">(.*?)</footer>', content, re.DOTALL)
    footnote_content = footnote_match.group(0) if footnote_match else ''

    # Generate new HTML
    sidebar_html = generate_sidebar_html(book_prefix)
    nav_html = generate_nav_html(book_prefix, book_name, chapter_num, chapter_count, prev_href, next_href)

    new_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{book_name} Chapter {chapter_num} - World English Bible">
  <title>World English Bible - {book_name} {chapter_num}</title>
  <link rel="stylesheet" href="../styles/styles.css">
</head>
<body>
  <div class="page-wrapper">
{sidebar_html}
    <div class="content-wrapper">
{nav_html}
      <main class="main">
{main_content}
      </main>

{footnote_content}

      <footer class="copyright">
        <p><a href="https://eBible.org/">eBible.org</a> | <a href="webfaq.htm">FAQ</a> | Public Domain</p>
      </footer>
    </div>
  </div>
  <script src="../scripts/navigation.js"></script>
</body>
</html>
'''
    return new_html


def main():
    books_dir = os.path.dirname(os.path.abspath(__file__))
    htm_files = glob.glob(os.path.join(books_dir, '*.htm'))

    # Skip certain files
    skip_files = {'links.htm', 'webfaq.htm', 'copyright.htm', 'index.htm'}

    # Only process chapter files (with numbers)
    chapter_files = [f for f in htm_files
                     if re.search(r'\d+\.htm$', os.path.basename(f))
                     and os.path.basename(f) not in skip_files]

    print(f"Found {len(chapter_files)} chapter files")

    updated = 0
    for filepath in sorted(chapter_files):
        basename = os.path.basename(filepath)
        try:
            new_content = process_chapter_file(filepath)
            if new_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                updated += 1
                if updated % 100 == 0:
                    print(f"  Processed {updated} files...")
        except Exception as e:
            print(f"  Error processing {basename}: {e}")

    print(f"\nUpdated {updated} files with new navigation")


if __name__ == '__main__':
    main()
