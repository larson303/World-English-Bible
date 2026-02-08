/**
 * World English Bible - Sidebar Navigation
 * Generates the sidebar HTML and injects it into the page.
 */
(function() {
  'use strict';

  var sidebar = document.getElementById('sidebar');
  if (!sidebar) return;

  // Determine link prefix based on page location
  var inBooks = window.location.pathname.indexOf('/books/') !== -1;
  var prefix = inBooks ? '' : 'books/';

  function link(href, text) {
    return '<li><a href="' + prefix + href + '">' + text + '</a></li>';
  }

  sidebar.className = 'sidebar';
  sidebar.innerHTML =
    '<div class="sidebar-header">' +
      '<h2>Books</h2>' +
      '<button class="sidebar-close" aria-label="Close menu">&times;</button>' +
    '</div>' +

    '<details class="sidebar-section">' +
      '<summary>Old Testament</summary>' +
      '<ul>' +
        link('Genesis01.html', 'Genesis') +
        link('Exodus01.html', 'Exodus') +
        link('Leviticus01.html', 'Leviticus') +
        link('Numbers01.html', 'Numbers') +
        link('Deuteronomy01.html', 'Deuteronomy') +
        link('Joshua01.html', 'Joshua') +
        link('Judges01.html', 'Judges') +
        link('Ruth01.html', 'Ruth') +
        link('1_Samuel01.html', '1 Samuel') +
        link('2_Samuel01.html', '2 Samuel') +
        link('1_Kings01.html', '1 Kings') +
        link('2_Kings01.html', '2 Kings') +
        link('1_Chronicles01.html', '1 Chronicles') +
        link('2_Chronicles01.html', '2 Chronicles') +
        link('Ezra01.html', 'Ezra') +
        link('Nehemiah01.html', 'Nehemiah') +
        link('Esther01.html', 'Esther') +
        link('Job01.html', 'Job') +
        link('Psalms001.html', 'Psalms') +
        link('Proverbs01.html', 'Proverbs') +
        link('Ecclesiastes01.html', 'Ecclesiastes') +
        link('Song_of_Solomon01.html', 'Song of Solomon') +
        link('Isaiah01.html', 'Isaiah') +
        link('Jeremiah01.html', 'Jeremiah') +
        link('Lamentations01.html', 'Lamentations') +
        link('Ezekiel01.html', 'Ezekiel') +
        link('Daniel01.html', 'Daniel') +
        link('Hosea01.html', 'Hosea') +
        link('Joel01.html', 'Joel') +
        link('Amos01.html', 'Amos') +
        link('Obadiah01.html', 'Obadiah') +
        link('Jonah01.html', 'Jonah') +
        link('Micah01.html', 'Micah') +
        link('Nahum01.html', 'Nahum') +
        link('Habakkuk01.html', 'Habakkuk') +
        link('Zephaniah01.html', 'Zephaniah') +
        link('Haggai01.html', 'Haggai') +
        link('Zechariah01.html', 'Zechariah') +
        link('Malachi01.html', 'Malachi') +
      '</ul>' +
    '</details>' +

    '<details class="sidebar-section">' +
      '<summary>Deuterocanon</summary>' +
      '<ul>' +
        link('Tobit01.html', 'Tobit') +
        link('Judith01.html', 'Judith') +
        link('Esther_Greek01.html', 'Esther (Greek)') +
        link('Wisdom_of_Solomon01.html', 'Wisdom of Solomon') +
        link('Sirach01.html', 'Sirach') +
        link('Baruch01.html', 'Baruch') +
        link('Daniel_Greek01.html', 'Daniel (Greek)') +
        link('1_Maccabees01.html', '1 Maccabees') +
        link('2_Maccabees01.html', '2 Maccabees') +
        link('1_Esdras01.html', '1 Esdras') +
        link('Prayer_of_Manasseh01.html', 'Prayer of Manasseh') +
        link('Psalm_15101.html', 'Psalm 151') +
        link('3_Maccabees01.html', '3 Maccabees') +
        link('2_Esdras01.html', '2 Esdras') +
        link('4_Maccabees01.html', '4 Maccabees') +
      '</ul>' +
    '</details>' +

    '<details class="sidebar-section">' +
      '<summary>New Testament</summary>' +
      '<ul>' +
        link('Matthew01.html', 'Matthew') +
        link('Mark01.html', 'Mark') +
        link('Luke01.html', 'Luke') +
        link('John01.html', 'John') +
        link('Acts01.html', 'Acts') +
        link('Romans01.html', 'Romans') +
        link('1_Corinthians01.html', '1 Corinthians') +
        link('2_Corinthians01.html', '2 Corinthians') +
        link('Galatians01.html', 'Galatians') +
        link('Ephesians01.html', 'Ephesians') +
        link('Philippians01.html', 'Philippians') +
        link('Colossians01.html', 'Colossians') +
        link('1_Thessalonians01.html', '1 Thessalonians') +
        link('2_Thessalonians01.html', '2 Thessalonians') +
        link('1_Timothy01.html', '1 Timothy') +
        link('2_Timothy01.html', '2 Timothy') +
        link('Titus01.html', 'Titus') +
        link('Philemon01.html', 'Philemon') +
        link('Hebrews01.html', 'Hebrews') +
        link('James01.html', 'James') +
        link('1_Peter01.html', '1 Peter') +
        link('2_Peter01.html', '2 Peter') +
        link('1_John01.html', '1 John') +
        link('2_John01.html', '2 John') +
        link('3_John01.html', '3 John') +
        link('Jude01.html', 'Jude') +
        link('Revelation01.html', 'Revelation') +
      '</ul>' +
    '</details>';
})();
