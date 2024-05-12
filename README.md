# link-utils

## Conversions

This tool only supports *CSV (comma separated)* to *Firefox's HTML Bookmark format* conversion.

Maybe more will be supported in the future.

### CSV (comma separated) to Firefox HTML Bookmarks

For now, bookmarks need to be formatted in the following way

```
<link>, <title>
```

#### Example

```
https://somelink.com, Some Page
https://anotherlink.com, Another Page
```

#### Usage

- Clone the repo
- install python on your system, if it's not already installed
- run `python3 <path/to>/src/firefox_bookmarks.py <input file path> <output file path>` (or `python`, `python.exe`, `python3.exe` or others depending on your system configuration)


#### Importing into Firefox

1. Open the bookmark library panel (from the menu or by pressing `CTRL+SHIFT+O`)
2. click on *Import and Backup*, then *import bookmarks from HTML* and select your file.

