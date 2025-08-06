#!/usr/bin/env python3
import os
import sys
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

class PresentationBuilder:
    def __init__(self, config_path):
        self.config_path = config_path
        self.env = Environment(
            loader=FileSystemLoader(['templates']),
            autoescape=select_autoescape(['html', 'xml'])
        )
        
        # Load macros
        self.title_macro = self.env.get_template('slides/title.html')
        self.content_macro = self.env.get_template('slides/content.html')
        
        # Register macros as globals
        self.env.globals.update({
            'title_slide': self.title_macro.module.title_slide,
            'section_header': self.content_macro.module.section_header,
            'content_slide': self.content_macro.module.content_slide,
            'feature_list': self.content_macro.module.feature_list,
            'code_block': self.content_macro.module.code_block,
            'note_box': self.content_macro.module.note_box,
            'workflow': self.content_macro.module.workflow,
            'comparison': self.content_macro.module.comparison,
        })

    def load_config(self):
        """Load the presentation configuration from YAML."""
        with open(self.config_path, 'r') as f:
            return yaml.safe_load(f)

    def build_slides(self, config):
        """Build the slides content from configuration."""
        slides = []
        
        # Add title slide if configured
        if 'title' in config:
            slides.append(self.title_macro.module.title_slide(
                title=config['title'],
                subtitle=config.get('subtitle'),
                presenters=config.get('presenters'),
                date=config.get('date'),
                logos=config.get('logos', {})
            ))
        
        # Add content slides
        for slide in config.get('slides', []):
            slide_type = slide.get('type', 'content')
            
            if slide_type == 'section':
                slides.append(self.content_macro.module.section_header(
                    title=slide['title'],
                    subtitle=slide.get('subtitle'),
                    background=slide.get('background'),
                    transition=slide.get('transition')
                ))
            
            elif slide_type == 'content':
                slides.append(self.content_macro.module.content_slide(
                    title=slide.get('title'),
                    content=slide.get('content'),
                    layout=slide.get('layout', 'default'),
                    background=slide.get('background'),
                    transition=slide.get('transition')
                ))
        
        return '\n'.join(slides)

    def build_presentation(self):
        """Build the complete presentation."""
        config = self.load_config()
        
        # Load base template
        template = self.env.get_template('base.html')
        
        # Build slides content
        slides_content = self.build_slides(config)
        
        # Render complete presentation
        html = template.render(
            title=config.get('title', 'Presentation'),
            theme=config.get('theme', 'default'),
            favicon=config.get('favicon'),
            center=config.get('center', True),
            transition=config.get('transition', 'slide'),
            slide_number=config.get('slide_number', 'c/t'),
            show_slide_number=config.get('show_slide_number', 'all'),
            config=config.get('reveal_config', {}),
            slides=slides_content
        )
        
        return html

    def write_output(self, html, output_path):
        """Write the presentation HTML to file."""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as f:
            f.write(html)

def main():
    if len(sys.argv) != 3:
        print("Usage: build.py <config.yaml> <output.html>")
        sys.exit(1)
    
    config_path = sys.argv[1]
    output_path = sys.argv[2]
    
    builder = PresentationBuilder(config_path)
    html = builder.build_presentation()
    builder.write_output(html, output_path)
    print(f"Presentation built successfully: {output_path}")

if __name__ == '__main__':
    main()
