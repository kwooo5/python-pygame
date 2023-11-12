import pytest
import pygame
from flappy import *

def test_pygame_initialized():
    pygame.init()
    assert pygame.get_init()
    
def test_screen_created():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    assert screen
    
def test_screen_dimensions():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    assert screen.get_width() == 600
    assert screen.get_height() == 600
    
def test_caption_set():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Flappy cat')
    assert pygame.display.get_caption()[0] == 'Flappy cat'

def test_images_loaded():
    bg = pygame.image.load('image/bgg.jpg')
    ground = pygame.image.load('image/ground.png')
    button = pygame.image.load('image/restart.png')
    assert bg != None
    assert ground != None 
    assert button != None
    
def test_font_created():
    font = pygame.font.SysFont('Bauhaus 93', 60)
    assert font != None
def test_fps():
    