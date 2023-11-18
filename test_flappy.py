import unittest
import pygame
from flappy import *

class TestFlappyBird(unittest.TestCase):
    
    def test_pygame_initialized(self):
        pygame.init()
        self.assertTrue(pygame.get_init())
        
    def test_screen_created(self):
        pygame.init()
        screen = pygame.display.set_mode((600, 600))
        self.assertIsNotNone(screen)
        
    def test_screen_dimensions(self):
        pygame.init()
        screen = pygame.display.set_mode((600, 600))
        self.assertEqual(screen.get_width(), 600)
        self.assertEqual(screen.get_height(), 600)
        
    def test_caption_set(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Flappy cat')
        self.assertEqual(pygame.display.get_caption()[0], 'Flappy cat')
    
    def test_images_loaded(self):
        bg = pygame.image.load('image/bgg.jpg')
        ground = pygame.image.load('image/ground.png')
        button = pygame.image.load('image/restart.png')
        self.assertIsNotNone(bg)
        self.assertIsNotNone(ground)
        self.assertIsNotNone(button)
        
    def test_font_created(self):
        font = pygame.font.SysFont('Bauhaus 93', 60)
        self.assertIsNotNone(font)
        
    def test_fps(self):
        fps = 0
        clock = pygame.time.Clock()
        clock.tick(fps)
        self.assertEqual(clock.get_fps(), fps)
        
if __name__ == '__main__':
    unittest.main()

class TestFlappyBird(unittest.TestCase):

    def test_reset_game(self):
        self.pipe_group = pygame.sprite.Group()
        self.flappy = Bird(50, 50) 
        self.score = 5
        self.assertEqual(len(self.pipe_group), 0)
        self.assertEqual(self.flappy.rect.x, 36)
        
        score = reset_game()
        self.assertEqual(len(self.pipe_group), 0)
        self.assertEqual(self.flappy.rect.x, 36)
        self.assertEqual(self.flappy.rect.y, int(40))
        self.assertEqual(score, 0)

        
class TestBird(unittest.TestCase):

    def test_update(self):
        bird = Bird(100, 200)
        bird.vel = 0
        self.flying = True

        self.assertLess(bird.vel, 8)
        self.assertGreaterEqual(bird.rect.bottom, 211)
        self.assertEqual(bird.rect.y, 190) # y position is unchanged        

        flying = False
        bird.update()
        self.assertEqual(bird.vel, 0) # velocity unchanged when not he bird is flying

      

class TestBird():
    def test_animation(self):
        bird = Bird(100, 100)
        bird.images = [pygame.Surface((50,50)) for i in range(3)]  
        bird.index = 0
        bird.counter = 0
        self.assertEqual(bird.index, 0)
        self.assertEqual(bird.counter, 0)  
        bird.counter = 10
        bird.update()

        

        self.assertEqual(bird.index, 0)
        
        
        self.assertEqual(bird.index, 0)
        self.assertEqual(bird.counter, 1)
        self.assertEqual(bird.index, 0)  
        self.assertEqual(bird.counter, 1)

        bird.counter = 10
        
        bird.update() 
        self.assertEqual(bird.index, 0) 
        self.assertEqual(bird.counter, 0)  
       
       
        def test_rotation(self):    
            self.bird = Bird(100, 100)
            self.bird.vel = -4
            expected_angle = 8 
            self.assertEqual(bird.image.get_angle(), expected_angle)
            self.bird.vel = 0 
            bird.update()
            self.assertEqual(bird.image.get_angle(), -90)


class TestPipe(unittest.TestCase):

    def test_pipe_position(self):
        pipe = Pipe(300, 400, 1)
        self.assertEqual(pipe.rect.bottomleft, (300, 325))
        
        pipe = Pipe(300, 400, -1)
        self.assertEqual(pipe.rect.topleft, (300, 475))

    def test_update_movement(self):
        pipe = Pipe(300, 400, 1) 
        pipe.update()
        self.assertEqual(pipe.rect.x, 296) # moved by scroll speed
        
        pipe.update() 
        self.assertEqual(pipe.rect.x, 292)


from unittest import mock
class TestButton():
    
    def test_button_clicked(self):
        # Mock
        mock_surface = unittest.mock.Mock() 
        
        button = Button(100, 200, mock_surface)
        self.pos = pygame.mouse.get_pos()

        # Simulate the mouse over and click
        button.rect.collidepoint.return_value = True
        pygame.mouse.get_pressed.return_value = [1,0,0]
        self.assertTrue(button.draw())
        
        
    def test_button_not_clicked(self):
        # Mock 
        mock_surface = unittest.mock.Mock()
        
        button = Button(100, 200, mock_surface)
        
        # Simulate mouse not over 
        button.rect.collidepoint.return_value = False
        
        self.assertEqual(button.draw())

from flappy import Bird
class TestBirdGroup(unittest.TestCase):

    def test_bird_group(self):
        flappy = Bird(100, 200)
        bird_group = pygame.sprite.Group()
        bird_group.add(flappy)

        self.assertEqual(len(bird_group), 1)
        self.assertEqual(bird_group.sprites()[0], flappy)

if __name__ == '__main__':
    unittest.main()

from unittest.mock import MagicMock
class TestGameLoopButton(unittest.TestCase):

    def test_button_draw(self):
        mock_surface = unittest.mock.Mock()
        screen = MagicMock()
        button = Button(100, 200, mock_surface)

    def test_button_click(self):
        button = MagicMock()
        button.clicked = False 

        # Assert button.clicked updated
        self.assertFalse(button.clicked)

from unittest.mock import MagicMock

def test_game_loop_increments_score(self):

    # Mock bird and pipe
    bird = MagicMock()
    pipe = MagicMock()

    # Set bird/pipe positions to pass
    bird.rect.left = 100 
    pipe.rect.right = 90

    # Call game loop
    run_game_loop(MagicMock(), MagicMock(), [bird], [pipe])

    # Assert score updated
    self.assertEqual(bird.score, 1)  

def run_game_loop(screen, button, birds, pipes):
    
    update_score(birds, pipes)

def update_score(birds, pipes):
   bird = birds[0]
   pipe = pipes[0]
   
   if bird.rect.left > pipe.rect.right:
       bird.score += 1

from unittest.mock import MagicMock
class TestCollision(unittest.TestCase):

    def test_bird_pipe_collision(self):
        bird = MagicMock()
        pipe = MagicMock()
        self.bird_group = pygame.sprite.Group(bird)
        self.pipe_group = pygame.sprite.Group(pipe)

        pygame.sprite.groupcollide = MagicMock(return_value=True)

from unittest.mock import MagicMock
class TestHitGround(unittest.TestCase):

    def test_bird_hits_ground(self):
        flappy = MagicMock()
        flappy.rect.bottom = 769

        game_over, flying = check_ground_collision(flappy)

        self.assertTrue(game_over)
        self.assertFalse(flying)

    def test_bird_not_on_ground(self):
        flappy = MagicMock()
        flappy.rect.bottom = 767

        game_over, flying = check_ground_collision(flappy)

        self.assertFalse(game_over)
        self.assertTrue(flying)

def check_ground_collision(bird):
    game_over = False
    flying = True
    
    if bird.rect.bottom >= 768:
        game_over = True
        flying = False

    return game_over, flying

#generate new pipes
time_now = pygame.time.get_ticks()
if time_now - last_pipe > pipe_frequency:
			pipe_height = random.randint(-100, 100)
			btm_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, -1)
			top_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, 1)
			pipe_group.add(btm_pipe)
			pipe_group.add(top_pipe)
			last_pipe = time_now

from unittest.mock import MagicMock

class TestGroundScroll(unittest.TestCase):

    def test_scroll(self):
        ground_scroll = 0
        scroll_speed = 10
        
        pipe_group = MagicMock()
        
        scroll_ground(ground_scroll, scroll_speed, pipe_group)
        
        self.assertEqual(ground_scroll, 0) 
        pipe_group.update.assert_called()

    def test_reset_scroll(self):
        ground_scroll = 0
        scroll_speed = 10
        
        scroll_ground(ground_scroll, scroll_speed, None)
        
        self.assertEqual(ground_scroll, 0)
        
def scroll_ground(ground_scroll, speed, pipes):
    ground_scroll -= speed  
    if abs(ground_scroll) > 35:
        ground_scroll = 0
        
    if pipes:
        pipes.update()


class TestPygame(unittest.TestCase):

    def test_pygame(self):
        # Initialize the pygame
        pygame.init()
        
        # Creating a surface and displaying it 
        surface = pygame.Surface((100,100))
        pygame.display.set_mode((100,100))
        pygame.display.update()

        # Quit pygame 
        pygame.quit()

        # Assert pygame was initialized and quit
        self.assertFalse(pygame.get_init())
        self.assertFalse(pygame.get_init()) 

if __name__ == '__main__':
    unittest.main()
        


        



