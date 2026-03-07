# World-English-Bible
- This is a project originally by Michael and Lori Johnson
- https://mljohnson.org/

## Original Project Links
-  https://ebible.org/
-  https://worldenglish.bible/

Please consider supporting them.

## So What is this project version about?
- The goal is to update the project
    - to a modern HTML/CSS/JavaScript format for better user experience.
    - Improved navigation.

## Theme Picker

The app includes a theme picker with four options: **Light** (default), **Night**, **Sepia**, and **Olive**. The user's selection is saved to `localStorage` so it persists across page loads and sessions.

In `scripts/navigation.js`, the saved theme is loaded at the top of the script (before DOM ready) to prevent a flash of the default theme:

```js
var savedTheme = localStorage.getItem('web-bible-theme') || 'default';
if (savedTheme !== 'default') {
  document.documentElement.setAttribute('data-theme', savedTheme);
}
```

### Setting a different default theme

To change which theme is used when no preference has been saved, replace `'default'` with the desired theme key (`dark`, `sepia`, or `olive`). For example, to default to the Sepia theme:

```js
var savedTheme = localStorage.getItem('web-bible-theme') || 'sepia';
if (savedTheme !== 'default') {
  document.documentElement.setAttribute('data-theme', savedTheme);
}
```

### Disabling the theme picker

If you want to lock the app to a single theme and remove the picker entirely:

1. In `scripts/navigation.js`, remove or comment out the `initThemeSwitcher()` call inside the `init()` function.
2. To lock to a non-default theme, set the `data-theme` attribute directly on the `<html>` element in each HTML file:
   ```html
   <html lang="en" data-theme="sepia">
   ```
3. Optionally remove the theme-related `localStorage` lines at the top of `navigation.js` since they are no longer needed.
