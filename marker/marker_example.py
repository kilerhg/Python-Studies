from pathlib import Path
from glob import glob

from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered


ROOT_PATH = Path('.temp')
PATH_INPUT = ROOT_PATH / 'input'
PATH_OUTPUT = ROOT_PATH / 'output'

PATH_INPUT_TEMPLATE = str(PATH_INPUT / '**/*.pdf')

list_all_files = glob(PATH_INPUT_TEMPLATE, recursive=True)

list_all_files = ['.temp/input/Historico Faculdade.pdf']

for pos, file in enumerate(list_all_files):

    converter = PdfConverter(
        artifact_dict=create_model_dict(),
    )
    rendered = converter(file)
    text, _, images = text_from_rendered(rendered)
    # print(type(text))

    with open(str(PATH_OUTPUT / f'{pos}.md'), 'w+') as file:
        file.write(text)