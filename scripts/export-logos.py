"""Build fixed cream-backed logos from the original SVG sources.

Requires Python 3 and rsvg-convert (librsvg). Run from any directory.
"""
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SVG = 'http://www.w3.org/2000/svg'
ET.register_namespace('', SVG)

for name, padding, export_width in [('symbol', 16, 512), ('wordmark', 24, 2400)]:
    source = ROOT / 'assets' / f'latent-paths-{name}.svg'
    logo = ET.parse(source).getroot()
    width, height = (int(logo.attrib[key]) for key in ('width', 'height'))
    canvas_width, canvas_height = width + 2 * padding, height + 2 * padding
    canvas = ET.Element(f'{{{SVG}}}svg', {
        'width': str(canvas_width), 'height': str(canvas_height),
        'viewBox': f'0 0 {canvas_width} {canvas_height}',
        'role': 'img', 'aria-label': f'Latent Paths {name}',
    })
    ET.SubElement(canvas, f'{{{SVG}}}title').text = f'Latent Paths {name}'
    ET.SubElement(canvas, f'{{{SVG}}}rect', {
        'width': str(canvas_width), 'height': str(canvas_height),
        'rx': '8', 'fill': '#F1EBDD',
    })
    logo.set('x', str(padding))
    logo.set('y', str(padding))
    canvas.append(logo)
    output = source.with_stem(f'{source.stem}-cream')
    ET.ElementTree(canvas).write(output, encoding='unicode', xml_declaration=True)
    subprocess.run([
        'rsvg-convert', '--width', str(export_width),
        '--output', str(output.with_suffix('.png')), str(output),
    ], check=True)
