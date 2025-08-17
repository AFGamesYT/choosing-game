import pygame
import os
import threading
from time import sleep as wait

# file strucure
#
#  files/
#    anim1/
#       idle.png
#       walking.png
#       greet.png
#    anim2/       
#       idle.png
#       running.png
#       hello_world.png
#
# 
# usage
#  animated_image_path = "files/anim1"
#  anim1 = AnimatedImage(animated_image_path)
#  anim1.add_animations(["idle", "walking", "greet"])
#  anim1.config_anim("idle", loop=True, time_between_frames=15)
#  
#  anim1.play_animation("greet")

class AnimatedImage:
    def __init__(self, screen: pygame.Surface, position: tuple[int, int], path) -> None:
        """
        :param position: Where the animated image is drawn. The size is determined by the config.
        :param path: Path to the animation sheet.

        Example usage:
            animated_image_path = "files/anim1"\n
            anim1 = AnimatedImage(animated_image_path)  # initialize the animation sheet.\n
            anim1.add_animations(["idle", "walking", "greet"])  # add the animations to the image (there has to be a file with the same name as the animation.)\n
            anim1.config_anim("idle", loop=True, time_between_frames=15, default=True)  # configure the animation\n

            anim1.play_animation("greet")  # play an animation\n
        \n
        ====\n
        \n
        Animation configs:
            "loop": Whether the animation is looping or not. If set to True, then will not stop until stopped.\n
            "time_between_frames": How fast the animation will run.\n
            "default": Instantly plays the animation, starts playing when no other animation is playing. Good for an idle animation.\n
            "height": Height of one sprite within the entire animation sheet.\n
            "width": Width of one sprite within the entire animation sheet.\n
            "frames": The amount of frames in the animation sheet.
        \n
        ====\n
        \n
        """
        self.path = path

        self.file_format = ".png"

        self.screen = screen
        self.pos = position

        self.anims = []

        self.animation_playing = False

        self.CONFIGS = ["time_between_frames", "loop", "default", "height", "width", "frames"]

    def add_animation(self, anim: str):
        if anim not in self.anims:
            if os.path.exists(f"{self.path}/{anim}{self.file_format}"):
                self.anims.append(
                    {"anim": anim, "loop": False, "time_between_frames": 1, "default": False, "height": 0, "width": 0, "frames": 0}
                )
            else:
                print(f"AnimatedImage: path {self.path}/{anim}{self.file_format} does not exist.")
        else:
            print(f"AnimatedImage: Animation '{anim}' already exists.")

    def add_animations(self, anims: list[str] | tuple[str]):
        for anim in anims:
            if anim not in self.anims:
                if os.path.exists(f"{self.path}/{anim}{self.file_format}"):
                    self.anims.append(
                        {"anim": anim, "loop": False, "time_between_frames": 1, "default": False, "height": 0, "width": 0, "frames": 0}
                    )
                else:
                    print(f"AnimatedImage: path {self.path}/{anim}{self.file_format} does not exist.")
            else:
                print(f"AnimatedImage: Animation '{anim}' already exists.")

    def config_anim(self, anim, **kwargs):
        for key in kwargs:
            if key.lower() not in self.CONFIGS:
                print(f"Animated Image: {key} is not a valid config. Avaliable configs: {self.CONFIGS}")
                return
            else:
                for a in self.anims:
                    if a['anim'] == anim:
                        animation = a
                        break
                else:
                    print(f"AnimatedImage: Animation '{anim}' doesn't exist.")
                    return
                animation[key] = kwargs[key]



    def play_animation(self, anim: str):
        for a in self.anims:
            if a['anim'] == anim:
                animation = a
                break
        else:
            print(f"AnimatedImage: Animation '{anim}' doesn't exist.")
            return


        def play_anim():
            nonlocal anim

            frames = animation['frames']
            if frames < 1:
                print(f"AnimatedImage: Cannot play animation '{anim}' because has less than 1 frame.")
                return

            if animation['height'] < 1 or animation['width'] < 1:
                print(f"AnimatedImage: Cannot play animation '{anim}' because the width or the height is not set.")
                return


            images_per_row = pygame.image.load(f"{self.path}/{animation["anim"]}{self.file_format}").get_rect().width // animation['width']

            new_frame = False

            def draw_surface():
                nonlocal new_frame
                while True:
                    if new_frame:
                        self.screen.fill(pygame.Color(0, 0, 0, 0))
                        new_frame = False
                    pygame.display.get_surface().blit(
                        self.screen,
                        (0, 0)
                    )

            draw_thread = threading.Thread(target=draw_surface, daemon=True)

            draw_thread.start()
            if animation['loop']:
                while True:
                    for frame in range(frames):
                        new_frame = True
                        self.screen.blit(
                            pygame.image.load(f"{self.path}/{animation["anim"]}{self.file_format}"),
                            self.pos,
                            area=pygame.Rect(frame % images_per_row * animation["width"],
                                             animation["height"]*(frame//images_per_row),
                                             animation["width"], animation["height"])
                        )

                        wait(animation['time_between_frames'])

            else:
                for frame in range(frames):
                    new_frame = True
                    self.screen.blit(
                        pygame.image.load(f"{self.path}/{animation["anim"]}{self.file_format}"),
                        self.pos,
                        area=pygame.Rect(frame % images_per_row * animation["width"],
                                         animation["height"] * (frame // images_per_row),
                                         animation["width"], animation["height"])
                    )

                    wait(animation['time_between_frames'])

        thread = threading.Thread(target=play_anim, daemon=True)
        thread.start()


if __name__ == "__main__":
    pygame.init()

    WIDTH = 1920
    HEIGHT = 1080

    FPS = 120

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Animated Image Test")

    clock = pygame.time.Clock()
    run = True
    fullscreen = True

    def background():
        global run
        while run:
            screen.fill((255, 255, 255))
            wait(0.1)

    background_thread = threading.Thread(target=background, daemon=True)
    background_thread.start()

    animations_screen = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

    animated_image_path = "textures/test_stick_figure"
    anim1 = AnimatedImage(screen=animations_screen, position=(100, 100), path=animated_image_path)
    anim1.add_animations(["idle", "wave"])
    anim1.config_anim("idle", loop=True, time_between_frames=0.2, height=20, width=10, frames=10, default=True)
    anim1.config_anim("wave", loop=True, time_between_frames=0.2, height=32, width=32, frames=10)


    anim1.play_animation("wave")

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                if event.key == pygame.K_r:
                    anim1.play_animation("wave")


        try:
            pygame.display.update()
        except KeyboardInterrupt:
            print("Quitting...")
            run = False
        clock.tick(FPS)

    pygame.quit()
