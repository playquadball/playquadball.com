# Contributing to How to play Quadball

Thank you for your interest in improving this quadball educational resource! This guide explains how to contribute effectively.

## Ways to Contribute

### 🐛 Report Issues
- **Factual errors**: Rule misstatements, incorrect scoring, outdated information
- **Typos and grammar**: Writing issues that affect clarity
- **Broken links**: Dead or incorrect links to external resources
- **Formatting problems**: Display issues, broken lists, or rendering errors

**How to report**: Open an [issue](https://github.com/playquadball/playquadball.com/issues) with:
- Clear description of the problem
- Page URL where the issue appears
- Expected vs. actual behavior
- Screenshots if applicable

### ✏️ Quick Edits
For small fixes (typos, grammar, minor clarifications):

1. **Use the "Edit this page" button** (✏️ icon) on any website page
2. **Make your changes** in the GitHub web editor
3. **Submit directly** as a pull request
4. **Add a clear commit message** describing your change

### 🔧 Larger Contributions
For substantial improvements, new sections, or major updates:

1. **Fork the repository** to your GitHub account
2. **Clone locally**: `git clone https://github.com/YOUR_USERNAME/playquadball.com.git`
3. **Create a feature branch**: `git checkout -b improve-content`
4. **Make your changes** in the `docs/` directory
5. **Test locally** (see [Local Development](#local-development))
6. **Commit with clear messages**: `git commit -m "Add examples to beater positioning"`
7. **Push and create pull request**

## Content Guidelines

### ✅ What We Accept
- **Accuracy improvements** based on official IQA rulebook
- **Clarity enhancements** for better understanding
- **Additional examples** or practical applications
- **Better organization** of existing content
- **Accessibility improvements** for screen readers
- **SEO enhancements** for better discoverability

### ❌ What We Don't Accept
- **Promotional content** for specific teams, leagues, or products
- **Commercial links** or sponsorship content
- **Personal opinions** on rule interpretations (stick to official sources)
- **Non-educational content** that doesn't serve learning goals
- **Copyrighted material** without proper attribution

### 📏 Content Standards
- **Follow the official IQA rulebook** as the authoritative source
- **Write for beginners** - assume readers are new to quadball
- **Use clear, simple language** - avoid unnecessary jargon
- **Include examples** where helpful for understanding
- **Maintain consistent formatting** with existing content
- **Reference rule numbers** when citing specific regulations

## Local Development

### Prerequisites
- Python 3.11+
- [uv](https://docs.astral.sh/uv/) package manager

### Setup
```bash
git clone https://github.com/playquadball/playquadball.com.git
cd playquadball.com
uv sync
```

### Preview Changes
```bash
uv run mkdocs serve
```

Visit `http://localhost:8000` to see your changes live.

### Build for Production
```bash
uv run mkdocs build
```

## File Structure

```
docs/
├── getting-started/          # Beginner-friendly introductions
├── players/                  # Position-specific guides
├── officials/               # Referee and tournament resources
├── resources/               # Reference materials
└── index.md                 # Homepage

overrides/                   # Custom templates for SEO
mkdocs.yml                  # Site configuration
```

## Pull Request Process

### Before Submitting
- [ ] **Test locally** to ensure changes display correctly
- [ ] **Check spelling and grammar**
- [ ] **Verify all links work**
- [ ] **Ensure content matches official rules**
- [ ] **Follow existing formatting patterns**

### PR Description Template
```markdown
## Summary
Brief description of your changes

## Changes Made
- [ ] Fixed typo in section X
- [ ] Added example for concept Y
- [ ] Updated rule reference from A to B

## Checklist
- [ ] Content is factually accurate
- [ ] Writing is clear and beginner-friendly
- [ ] Formatting is consistent
- [ ] All links work correctly
- [ ] Changes tested locally
```

## Review Process

1. **Automated checks** run for formatting and links
2. **Maintainer review** for accuracy and style
3. **Community feedback** on significant changes
4. **Merge** once approved
5. **Automatic deployment** to playquadball.com

## Questions?

- **General questions**: Start a [Discussion](https://github.com/playquadball/playquadball.com/discussions)
- **Rule clarifications**: Reference the [official IQA rulebook](https://iqasport.org)
- **Technical issues**: Open an [Issue](https://github.com/playquadball/playquadball.com/issues)

## License

By contributing, you agree that your contributions will be licensed under the same [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) license that covers the project.

---

Thank you for helping make quadball more accessible to everyone! 🏆