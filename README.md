# App Store Screenshot Analyzer

A Python tool that analyzes App Store screenshots and generates analysis reports without requiring any external API keys.

## Features

- Scrapes screenshots from App Store listings
- Analyzes image properties:
  - Resolution and aspect ratio
  - Color distribution
  - Brightness levels
- Generates PDF reports with technical insights
- No API keys required

## Installation

1. Clone the repository:
```bash
git clone https://github.com/robertredbox/appstore-screenshot-analyzer.git
cd appstore-screenshot-analyzer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```python
from screenshot_analyzer import analyze_app_screenshots

# Analyze app screenshots
analyze_app_screenshots("https://apps.apple.com/app/your-app-id")
```

The script will generate a PDF report with analysis of each screenshot.

## Requirements

See `requirements.txt` for full list of dependencies.

## License

MIT License - see LICENSE file for details.