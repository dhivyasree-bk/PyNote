# Suggested Issues for PyNote

This document lists all suggested issues for contributors. Each issue includes difficulty level and acceptance criteria.

## Easy Issues

### 1. Add toolbar icons
**Labels**: `good first issue`, `easy`, `enhancement`
**Description**: Add small toolbar buttons for New/Open/Save above the text area.
**Acceptance Criteria**:
- Toolbar visible above text area
- Icons for New, Open, Save buttons
- Clicking each button triggers the expected action
- Icons are visually consistent

---

### 2. Add `Ctrl+N` shortcut for New
**Labels**: `good first issue`, `easy`, `enhancement`
**Description**: Bind `Ctrl+N` to create a new file.
**Acceptance Criteria**:
- Pressing Ctrl+N triggers new file creation
- Works consistently across platforms
- Shows unsaved changes dialog if needed

---

### 3. Create a dark theme
**Labels**: `good first issue`, `easy`, `enhancement`, `design`
**Description**: Add simple dark color values in `themes.py` and a toggle in the UI.
**Acceptance Criteria**:
- Dark theme defined in `themes.py`
- Toggle switches between light and dark
- All UI elements respect theme colors
- Theme persists across sessions

---

### 4. Add word/character count in status bar
**Labels**: `easy`, `enhancement`
**Description**: Show words and characters in real time in the status bar.
**Acceptance Criteria**:
- Status bar shows `Words: X | Chars: Y`
- Updates in real-time as user types
- Counts are accurate

---

### 5. Add line numbers gutter
**Labels**: `easy`, `enhancement`
**Description**: Show line numbers alongside the text widget.
**Acceptance Criteria**:
- Line numbers displayed in a gutter
- Lines correctly numbered starting from 1
- Updates as text changes (add/remove lines)
- Scrolls with text content

---

### 6. Implement 'Save As' dialog
**Labels**: `good first issue`, `easy`, `enhancement`
**Description**: Add explicit Save As menu option with default `.txt` extension.
**Acceptance Criteria**:
- Save As menu item works
- File saved with chosen filename
- Default extension is `.txt`
- Updates window title with new filename

---

### 7. Add About dialog
**Labels**: `good first issue`, `easy`, `enhancement`
**Description**: Implement `Help -> About` with app name and version.
**Acceptance Criteria**:
- About dialog opens from Help menu
- Shows app name, version, and description
- Includes credits/acknowledgments
- Modal dialog with OK button

---

### 8. Add basic README.md
**Labels**: `good first issue`, `easy`, `documentation`
**Description**: Create a friendly README with setup and run instructions.
**Acceptance Criteria**:
- README in repo root
- Includes quickstart instructions
- Lists features
- Includes badges and links

---

### 9. Add CONTRIBUTING.md
**Labels**: `good first issue`, `easy`, `documentation`
**Description**: Short contribution guide for contributors.
**Acceptance Criteria**:
- CONTRIBUTING.md exists
- Clarifies labels and PR flow
- Includes branch naming conventions
- Explains contribution process

---

### 10. Add recent files menu
**Labels**: `easy`, `enhancement`
**Description**: Keep a list of the 5 most recently opened files.
**Acceptance Criteria**:
- Recent files menu shows paths
- Displays up to 5 files
- Clicking opens the file
- Updates when new files are opened

---

### 11. Add status bar time saved indicator
**Labels**: `easy`, `enhancement`
**Description**: Show `Saved` indicator when autosave runs.
**Acceptance Criteria**:
- Indicator appears for 2 seconds after save
- Shows "Saved" text or icon
- Doesn't interfere with other status bar info

---

### 12. Add configurable tab size
**Labels**: `easy`, `enhancement`
**Description**: Add a setting for tab width (2/4/8 spaces).
**Acceptance Criteria**:
- Setting available in preferences
- Pressing Tab inserts configured number of spaces
- Setting persists across sessions

---

### 13. Add simple preferences dialog
**Labels**: `easy`, `enhancement`
**Description**: Allow toggling autosave and theme.
**Acceptance Criteria**:
- Preferences dialog accessible from menu
- Can toggle autosave on/off
- Can select theme (light/dark)
- Preferences persist to `settings.json`

---

### 14. Add find (Ctrl+F) basic dialog
**Labels**: `easy`, `enhancement`
**Description**: Search text, highlight first match.
**Acceptance Criteria**:
- Ctrl+F opens find dialog
- Found term highlighted and focused
- Can navigate to next/previous matches
- Case-sensitive option

---

### 15. Add keyboard shortcut list in Help
**Labels**: `easy`, `documentation`
**Description**: Short key guide in Help menu.
**Acceptance Criteria**:
- Help dialog lists common shortcuts
- Organized by category
- Shows platform-specific shortcuts if applicable

---

### 16. Add `.gitignore`
**Labels**: `good first issue`, `easy`, `enhancement`
**Description**: Ignore venv, pyc, etc.
**Acceptance Criteria**:
- .gitignore file added
- Ignores Python cache files
- Ignores virtual environments
- Ignores IDE files

---

### 17. Add license file (MIT)
**Labels**: `good first issue`, `easy`, `documentation`
**Description**: Add MIT LICENSE to repo.
**Acceptance Criteria**:
- LICENSE present with MIT text
- Copyright year and holder correct
- Standard MIT license format

---

### 18. Add icons & basic branding
**Labels**: `easy`, `enhancement`, `design`
**Description**: Add 128x128 app icon to `assets/`.
**Acceptance Criteria**:
- Icon included in repo
- Icon displayed in window (if supported)
- Icon file in appropriate format (PNG/ICO)

---

### 19. Add basic unit test for utility function
**Labels**: `easy`, `test`
**Description**: Add a test in `tests/`.
**Acceptance Criteria**:
- Test file in `tests/` directory
- `pytest` passes
- Tests cover utility functions

---

### 20. Add keyboard shortcut to toggle status bar
**Labels**: `easy`, `enhancement`
**Description**: Let users hide/show status bar.
**Acceptance Criteria**:
- Shortcut toggles visibility
- State persists across sessions
- Menu item reflects current state

---

## Medium Issues

### 1. Implement tabbed editing
**Labels**: `medium`, `enhancement`
**Description**: Convert editor to support multiple open files via tabs.
**Acceptance Criteria**:
- Open multiple files in tabs
- Switching preserves cursor and content
- Close tab button works
- Unsaved changes warning per tab

---

### 2. Find & Replace (with regex support)
**Labels**: `medium`, `enhancement`
**Description**: Make a robust dialog with replace all.
**Acceptance Criteria**:
- Find & Replace dialog
- Replace works across file
- Replace All option
- Regex option toggles regex behavior
- Case-sensitive option

---

### 3. Autosave with configurable interval
**Labels**: `medium`, `enhancement`
**Description**: Save in background at a user-configurable interval.
**Acceptance Criteria**:
- Autosaves without UI blocking
- Configurable interval (seconds)
- Saves to original file or prompts if unsaved
- Shows indicator when autosave occurs

---

### 4. Syntax highlighting engine
**Labels**: `medium`, `enhancement`
**Description**: Implement highlighters for Python and JS using tags.
**Acceptance Criteria**:
- Keywords, strings, comments get different tags/colors
- Works for Python and JavaScript
- Detects language from file extension
- Real-time highlighting as user types

---

### 5. Add file encoding detection
**Labels**: `medium`, `enhancement`
**Description**: Detect UTF-8 vs others and open files accordingly.
**Acceptance Criteria**:
- Files with UTF-8 BOM open correctly
- Fallback shown if encoding fails
- Encoding displayed in status bar
- Can manually select encoding

---

### 6. Add spellchecking toggle
**Labels**: `medium`, `enhancement`
**Description**: Integrate `pyspellchecker` to underline misspelled words.
**Acceptance Criteria**:
- Misspelled words get underlined
- Right-click suggests corrections
- Can add words to dictionary
- Toggle on/off in preferences

---

### 7. Implement settings saved to JSON
**Labels**: `medium`, `enhancement`
**Description**: Persist window size, theme, last opened files.
**Acceptance Criteria**:
- Settings saved to `settings.json`
- Window size/position restored
- Theme preference saved
- Recent files list saved

---

### 8. Add print preview / print support
**Labels**: `medium`, `enhancement`
**Description**: Allow printing the current document.
**Acceptance Criteria**:
- Print menu item
- OS print dialog appears
- Prints content correctly
- Page breaks handled appropriately

---

### 9. Add drag-and-drop file open
**Labels**: `medium`, `enhancement`
**Description**: User can drop a file onto the editor to open it.
**Acceptance Criteria**:
- Dropped files open in new tab
- Shows visual feedback during drag
- Handles multiple files
- Validates file types

---

### 10. Implement mini-map (basic)
**Labels**: `medium`, `enhancement`, `design`
**Description**: Vertical scaled preview of file with click-to-jump.
**Acceptance Criteria**:
- Mini-map shows proportion of file
- Clicking jumps to that location
- Updates as user scrolls
- Toggle visibility option

---

### 11. Add a plugin API skeleton
**Labels**: `medium`, `enhancement`
**Description**: Simple plugin loader that discovers `plugins/`.
**Acceptance Criteria**:
- Plugins can register a menu item
- Menu item triggers a function
- Plugin discovery works
- Basic plugin example included

---

### 12. Add Markdown preview split view
**Labels**: `medium`, `enhancement`
**Description**: Render Markdown to HTML and show side-by-side.
**Acceptance Criteria**:
- Live preview updates while editing
- Split view (editor | preview)
- Renders Markdown correctly
- Toggle preview on/off

---

### 13. Add 'Go to Line' dialog
**Labels**: `medium`, `enhancement`
**Description**: Quickly navigate to a given line number.
**Acceptance Criteria**:
- Dialog opens with Ctrl+G
- Cursor moves to specified line
- Validates line number range
- Scrolls to show target line

---

### 14. Implement autosave crash recovery
**Labels**: `medium`, `enhancement`
**Description**: Reopen unsaved content after a crash.
**Acceptance Criteria**:
- If crash occurred, prompt to recover on next start
- Shows list of recoverable files
- Can restore or discard
- Cleans up old recovery files

---

### 15. Implement customizable keybindings UI
**Labels**: `medium`, `enhancement`
**Description**: Allow remapping common shortcuts.
**Acceptance Criteria**:
- Keybinding changes saved
- Take effect immediately
- Shows current bindings
- Can reset to defaults

---

## Hard Issues

### 1. Implement an incremental syntax tokenizer
**Labels**: `hard`, `enhancement`
**Description**: Tokenize as user types to enable fast highlighting.
**Acceptance Criteria**:
- Large files still highlight without UI freezing
- Incremental updates as user types
- Efficient memory usage
- Supports multiple languages

---

### 2. Add real-time collaborative editing demo (local LAN)
**Labels**: `hard`, `enhancement`
**Description**: Simple peer-to-peer syncing for two users.
**Acceptance Criteria**:
- Two instances on LAN edit the same file
- Visible updates in real-time
- Handles conflicts gracefully
- Shows other user's cursor (optional)

---

### 3. Implement a plugin marketplace UI
**Labels**: `hard`, `enhancement`
**Description**: Browse & install plugins from a manifest file.
**Acceptance Criteria**:
- Install/uninstall works
- Plugins activated without restart
- Manifest file format defined
- Plugin validation

---

### 4. Build a mini-language server (LS) client
**Labels**: `hard`, `enhancement`
**Description**: Integrate a simple LSP for Python to show hover info.
**Acceptance Criteria**:
- Hovering symbols shows docstring info
- Works with simple Python server
- Error highlighting
- Auto-complete integration

---

### 5. Implement code folding
**Labels**: `hard`, `enhancement`
**Description**: Collapse/expand blocks (Python indentation-based).
**Acceptance Criteria**:
- Folding markers show
- Fold/unfold works
- Indentation-based for Python
- Keyboard shortcuts for fold/unfold

---

### 6. Add a performant rope data structure for large files
**Labels**: `hard`, `enhancement`
**Description**: Replace Tkinter Text with rope-backed model.
**Acceptance Criteria**:
- Opening & editing >100k lines remains responsive
- Rope data structure implemented
- Seamless integration with UI
- Performance benchmarks

---

### 7. Implement syntax-aware autocomplete
**Labels**: `hard`, `enhancement`
**Description**: Suggest completions based on context for Python.
**Acceptance Criteria**:
- Autocomplete dropdown shows suggestions
- Inserts selected suggestion
- Context-aware (imports, variables, etc.)
- Keyboard navigation

---

### 8. Add full-text search across project folder
**Labels**: `hard`, `enhancement`
**Description**: Search across opened project directory with results panel.
**Acceptance Criteria**:
- Results clickable
- Opens file at the match
- Shows context around matches
- Filters by file type

---

## Issue Creation Template

When creating issues in GitHub, use this format:

```markdown
## Description
[Issue description]

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Difficulty
[Easy/Medium/Hard]

## Labels
[Add appropriate labels]
```

---

*This list is a reference for maintainers creating GitHub issues. Each issue should be created individually with full details.*

