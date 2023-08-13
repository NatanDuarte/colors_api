import pytest
import os

from colors_api.color_extractor import ColorExtractor


def test_color_extractor_should_load_the_input_image():
    test_image_path = os.path.join('tests', 'utils', 'sky-7622960_1280.jpg')
    colorExtractor = ColorExtractor()
    colorExtractor.load(test_image_path)
    assert colorExtractor.image is not None

def test_color_extractor_should_only_accept_colorful_images():
    test_image_path = os.path.join('tests', 'utils', 'sky-7622960_1280-BW.jpg')
    colorExtractor = ColorExtractor()
    colorExtractor.load(test_image_path)
    assert colorExtractor.image is not None
