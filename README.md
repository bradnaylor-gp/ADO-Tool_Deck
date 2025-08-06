# Reveal.js Template System

A flexible templating system for creating reveal.js presentations using Jinja2 templates and YAML configuration.

## Features

- 🎨 Modular CSS with theme support
- 📦 Reusable slide components and layouts
- 🛠️ YAML-based presentation configuration
- 🔧 Jinja2 templating for dynamic content
- 📱 Responsive design with mobile support
- 🎯 PowerPoint master slide style templates

## Installation

1. Install uv if not already installed:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone the repository:
```bash
git clone <repository-url>
cd reveal-template
```

3. Create virtual environment and install dependencies:
```bash
uv venv
uv pip install .
```

## Usage

1. Create a YAML configuration file for your presentation (see `examples/ado-tool.yaml` for reference)

2. Build your presentation:
```bash
python build.py your-config.yaml output.html
```

## Directory Structure

```
reveal-template/
├── static/
│   ├── css/
│   │   ├── base/          # Core CSS files
│   │   ├── themes/        # Theme variations
│   │   └── components/    # Reusable components
│   ├── js/               # Custom JavaScript
│   └── img/              # Image assets
├── templates/
│   ├── base.html         # Base template
│   ├── macros/          # Reusable template macros
│   └── slides/          # Slide templates
├── examples/            # Example configurations
└── config/             # Theme configurations
```

## Creating Presentations

### Basic YAML Structure

```yaml
title: "Your Presentation"
subtitle: "Optional Subtitle"
theme: "default"  # or any custom theme
date: "YYYY-MM-DD"
presenters:
  - name: "Your Name"
    title: "Your Title"

slides:
  - type: "section"
    title: "Section Title"
    
  - type: "content"
    title: "Slide Title"
    layout: "two-columns"
    content:
      left: "Left column content"
      right: "Right column content"
```

### Available Layouts

- `default`: Standard slide layout
- `two-columns`: Split content into two columns
- `grid`: Grid-based layout (2-4 columns)
- `centered`: Centered content
- Custom layouts can be added via CSS

### Components

- Title slides
- Section headers
- Feature lists
- Code blocks
- Note boxes
- Workflow diagrams
- Comparison blocks
- Contact information

### Themes

1. **Default Theme**
   - Clean, minimal design
   - Customizable colors and typography

2. **GuidePoint Theme**
   - Corporate branding colors
   - Professional dark theme
   - Custom components

Custom themes can be created by:
1. Adding a new CSS file in `static/css/themes/`
2. Extending the default theme variables
3. Customizing component styles as needed

## Development

### Adding New Components

1. Create component CSS in `static/css/components/`
2. Add Jinja2 macro in `templates/slides/content.html`
3. Register macro in `build.py`
4. Document usage in examples

### Creating Themes

1. Create theme CSS file in `static/css/themes/`
2. Override CSS variables for customization
3. Add theme-specific components if needed
4. Document theme in examples

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - See LICENSE file for details
