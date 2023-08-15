import pytest
import json
import os

from colors_api.color_extractor import ColorExtractor


def test_color_extractor_should_load_the_input_image():
    test_image_path = os.path.join('tests', 'utils', 'sky-7622960_1280.jpg')
    colorExtractor = ColorExtractor()
    colorExtractor.load(test_image_path)
    assert colorExtractor.image is not None

def test_color_extractor_should_should_extract_colors():
    test_image_path = os.path.join('tests', 'utils', 'sky-7622960_1280.jpg')
    colorExtractor = ColorExtractor()

    result_json = colorExtractor.load(test_image_path).extract(n_colors=3)
    result_dict = json.loads(result_json)
    assert len(result_dict['palette']) == 3
