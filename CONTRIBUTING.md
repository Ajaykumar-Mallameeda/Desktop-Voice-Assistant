# Contributing to Desktop Voice Assistant

## Getting Started

1. Fork the repository.
2. Create a branch: `git checkout -b feature/your-feature-name`.
3. Make your changes.
4. Test that the assistant runs: `python Desktop\ voice\ assistant/Allen.py`.
5. Push and open a Pull Request.

## Code Style

- Follow PEP 8 for Python code.
- Keep modules focused: STT, TTS, and action routing are separate modules.
- Add docstrings to new functions.

## Pull Request Checklist

- [ ] Code runs without errors
- [ ] No hardcoded absolute paths
- [ ] No module-level side effects (function calls at module level)
- [ ] New commands added to `action.py` follow existing pattern

## Reporting Issues

Open an issue on GitHub with:
- Steps to reproduce
- Expected behavior
- Actual behavior
- Python version and OS
