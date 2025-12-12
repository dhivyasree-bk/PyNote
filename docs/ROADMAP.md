# PyNote Roadmap

This document outlines the development roadmap for PyNote, organized by milestones.

## Milestones

### v0.1 - MVP (Current)
**Status**: ✅ In Progress

Core functionality for a basic text editor:
- [x] Open / Save / Save As
- [x] Undo / Redo
- [x] Status bar (line/column)
- [x] Basic keyboard shortcuts (Ctrl+S, Ctrl+O, Ctrl+Z, Ctrl+N)
- [x] Menu system
- [ ] Line numbers
- [ ] Light / Dark theme toggle
- [ ] Autosave (configurable)

**Target**: Basic usable editor

---

### v0.2 - UX Improvements
**Status**: 🔜 Planned

Enhanced user experience:
- [ ] Line numbers gutter
- [ ] Theme system (light/dark)
- [ ] Autosave with configurable interval
- [ ] Word/character count in status bar
- [ ] Recent files menu
- [ ] About dialog
- [ ] Preferences dialog
- [ ] Settings persistence (JSON)

**Target**: Polished, user-friendly editor

---

### v0.3 - Power Features
**Status**: 🔜 Planned

Advanced editing capabilities:
- [ ] Tabbed editing (multiple files)
- [ ] Find & Replace dialog
- [ ] Find & Replace with regex support
- [ ] Syntax highlighting (Python, JavaScript, HTML)
- [ ] Go to Line dialog
- [ ] Drag-and-drop file opening
- [ ] Print support
- [ ] File encoding detection

**Target**: Feature-rich editor

---

### v0.4 - Advanced Features
**Status**: 🔜 Planned

Professional features:
- [ ] Markdown preview (split view)
- [ ] Mini-map (scaled preview)
- [ ] Spell checking (pyspellchecker integration)
- [ ] Code folding (Python indentation-based)
- [ ] Syntax-aware autocomplete
- [ ] Plugin system (hook-based)
- [ ] Plugin marketplace UI
- [ ] Customizable keybindings UI

**Target**: Extensible, professional editor

---

### v1.0 - Release
**Status**: 🔜 Planned

Stable release with:
- [ ] Comprehensive test coverage
- [ ] Complete documentation
- [ ] Performance optimizations
- [ ] Cross-platform testing
- [ ] Installer/packaging
- [ ] User guide
- [ ] Developer documentation

**Target**: Production-ready release

---

## Future Considerations

### Performance
- [ ] Incremental syntax tokenizer for large files
- [ ] Rope data structure for >100k line files
- [ ] Optimized rendering

### Collaboration
- [ ] Real-time collaborative editing (local LAN)
- [ ] Simple peer-to-peer syncing

### Developer Tools
- [ ] Mini-language server (LS) client
- [ ] Hover documentation
- [ ] Full-text search across project folder

---

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for how to contribute. Issues are tagged with milestones and difficulty levels.

**Current Focus**: Complete v0.1 MVP features

---

*Last updated: 2024*

