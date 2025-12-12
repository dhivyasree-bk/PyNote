# PyNote Design Document

## Architecture Overview

PyNote is built using Python 3.10+ and Tkinter, following a modular architecture for maintainability and extensibility.

## Project Structure

```
src/pynote/
├── __init__.py      # Package initialization
├── main.py          # Application entry point and main window
├── editor.py        # Editor widget wrapper
├── ui.py            # UI components (dialogs, menus)
├── themes.py        # Theme definitions and application
└── utils.py         # Utility functions (settings, file I/O helpers)
```

## Component Design

### Main Application (`main.py`)

**Responsibilities:**
- Application initialization
- Window management
- Menu creation
- Keyboard shortcut binding
- File operations (open/save)
- Status bar updates

**Key Classes:**
- `PyNoteApp`: Main application class inheriting from `tk.Tk`

### Editor Widget (`editor.py`)

**Responsibilities:**
- Text widget wrapper
- Cursor position management
- Content manipulation
- Line navigation

**Key Classes:**
- `EditorWidget`: Wrapper around `tk.Text` with convenience methods

### UI Components (`ui.py`)

**Responsibilities:**
- Dialog windows (About, Go to Line, etc.)
- Menu helpers
- User interaction components

**Key Classes:**
- `AboutDialog`: About window
- `GoToLineDialog`: Line navigation dialog

### Themes (`themes.py`)

**Responsibilities:**
- Theme definitions (light/dark)
- Theme application to widgets
- Theme management

**Key Functions:**
- `get_theme(name)`: Retrieve theme configuration
- `apply_theme(widget, theme)`: Apply theme to widget

### Utilities (`utils.py`)

**Responsibilities:**
- Settings management (load/save JSON)
- File operations helpers
- Text analysis (word/char count)
- Encoding detection

**Key Functions:**
- `load_settings()`: Load user settings
- `save_settings(settings)`: Save user settings
- `count_words(text)`: Count words in text
- `count_chars(text)`: Count characters in text

## Design Patterns

### MVC-like Structure
- **Model**: File content, settings state
- **View**: Tkinter widgets (Text, Menu, etc.)
- **Controller**: Event handlers in `PyNoteApp`

### Separation of Concerns
- UI logic separated from business logic
- Theme system isolated from widget creation
- Utilities kept independent and reusable

## Theme System

Themes are defined as dictionaries with color keys:
- `bg`: Background color
- `fg`: Foreground/text color
- `select_bg`: Selection background
- `select_fg`: Selection foreground
- `insert_bg`: Cursor color
- `gutter_bg`: Line number gutter background
- `gutter_fg`: Line number gutter foreground
- `status_bg`: Status bar background
- `status_fg`: Status bar foreground

## Settings System

Settings are stored in JSON format:
- **Location**: Platform-specific config directory
  - Windows: `%APPDATA%/PyNote/settings.json`
  - macOS/Linux: `~/.config/pynote/settings.json`

**Default Settings:**
```json
{
  "theme": "light",
  "autosave": false,
  "autosave_interval": 300,
  "tab_size": 4,
  "font_family": "Courier New",
  "font_size": 12,
  "recent_files": []
}
```

## Extension Points

### Plugin System (Future)
- Plugin discovery in `plugins/` directory
- Hook-based registration
- Menu item injection
- Event system

### Syntax Highlighting (Future)
- Tokenizer-based highlighting
- Language-specific rules
- Tag-based coloring in Tkinter Text widget

## UI Guidelines

### Layout
- Main text area fills available space
- Status bar at bottom
- Scrollbar on right side
- Menu bar at top

### Keyboard Shortcuts
- Standard editor shortcuts (Ctrl+S, Ctrl+O, etc.)
- Consistent with platform conventions
- Customizable (future feature)

### Dialogs
- Modal dialogs for user input
- Clear labels and instructions
- Cancel/OK buttons
- Error handling with user-friendly messages

## File Handling

### Supported Formats
- Text files (`.txt`)
- Markdown (`.md`)
- Python (`.py`)
- All files (`*.*`)

### Encoding
- Default: UTF-8
- Fallback: Latin-1
- BOM detection (future)

## Performance Considerations

### Current
- Tkinter Text widget handles moderate file sizes well
- No performance optimizations yet

### Future
- Incremental tokenization for syntax highlighting
- Rope data structure for large files (>100k lines)
- Lazy rendering for very long files

## Testing Strategy

### Unit Tests
- Utility functions (`test_utils.py`)
- Theme application
- Settings load/save

### Integration Tests
- File operations
- UI interactions
- Keyboard shortcuts

### Manual Testing
- Cross-platform compatibility
- Theme switching
- File operations

## Future Architecture Considerations

### Multi-file Editing
- Tab widget or notebook
- File manager component
- Tab state management

### Plugin Architecture
- Plugin loader
- Hook registration system
- API for plugins

### Syntax Highlighting
- Tokenizer engine
- Language definitions
- Real-time highlighting

---

*This document is a living document and will be updated as the project evolves.*

