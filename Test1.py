import glob
import math
import operator
import os
import shutil
from functools import reduce
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageFilter
from robot.api.deco import library, keyword
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


@keyword
def hello_world(self):
    print("hello")


@keyword('Compare Images')
def compare_images1(file1, file2):
    h1 = Image.open(file1).histogram()
    h2 = Image.open(file2).histogram()
    rms = math.sqrt(reduce(operator.add, map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))
    rms = math.sqrt(reduce(operator.add, map(lambda a,b: (a-b)**2, h1, h2))/len(h1))

    rms = math.sqrt(reduce(operator.add, map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))
    return rms


@keyword('Compare Images By Rotateting First Image')
def compare_images2(img1, img2):
    img2 = Image.open(img2)
    img1 = (Image.open(img1))
    # img1 = (Image.open(img1)).resize(img2.size).rotate(90)
    img1.save("rotated.png")

    diff = ImageChops.difference(img1, img2).histogram()
    sq = (value * (i % 256) ** 2 for i, value in enumerate(diff))
    sum_squares = sum(sq)
    rms = math.sqrt(sum_squares / float(img1.size[0] * img1.size[1]))

    # Error is an arbitrary value, based on values when
    # comparing 2 rotated images & 2 different images.
    return rms

@keyword('Compare Images By finding Edge')
def compare_images3(img1, img2):
    img1 = Image.open(img1)
    img2 = Image.open(img2)

    img1 = img1.filter(ImageFilter.FIND_EDGES)
    img2 = img2.filter(ImageFilter.FIND_EDGES)
    # img1 = (Image.open(img1)).resize(img2.size).rotate(90)
    img1.save("img1.png")
    img2.save("img2.png")

    diff = ImageChops.difference(img1, img2).histogram()
    sq = (value * (i % 256) ** 2 for i, value in enumerate(diff))
    sum_squares = sum(sq)
    rms = math.sqrt(sum_squares / float(img1.size[0] * img1.size[1]))

    # Error is an arbitrary value, based on values when
    # comparing 2 rotated images & 2 different images.
    return rms


@keyword('Delete Image Files in directory')
def delete_images(path):
    shutil.rmtree(path)


@keyword('Sekil Ciz')
def sekil():
    driver = BuiltIn().get_library_instance('SeleniumLibrary').driver

    action = ActionChains(driver)

    body_element = driver.find_element(By.XPATH, '//canvas')

    actions = ActionChains(driver)
    ss = body_element.size
    x = ss['width']
    y = ss['height']
    (actions.move_to_element_with_offset(body_element, 0, 0).
     click_and_hold(body_element).
     move_to_element_with_offset(body_element, -x / 2, -y / 2).
     move_to_element_with_offset(body_element, 0, 0).
     move_to_element_with_offset(body_element, -x / 2, y / 2).
     move_to_element_with_offset(body_element, 0, 0).
     move_to_element_with_offset(body_element, x / 2, -y / 2).
     move_to_element_with_offset(body_element, 0, 0).
     move_to_element_with_offset(body_element, x / 2, y / 2).
     release().perform())


def press_left(self):
    self.get_action_chain().key_down(Keys.LEFT_CONTROL)
    self.get_action_chain().perform()
