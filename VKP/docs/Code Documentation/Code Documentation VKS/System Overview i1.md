## File Overview: main.py
The initial executed function setups the whole program. What is initialized?
```python
class Simulation:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Varmekabel Simulator")
        self.clock = pygame.time.Clock()
        self.view = View()
```
1. pygame
2. fonts using pygame
3. the 'window', were everyting that is rendered will be seen
4. caption, aka the name of the program
5. in-built pygame clock function (for delta time and ticks)
6. Getting access to the View.py as self.view

```python
def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.view.checkB1:
                        self.view.setPdf()
                self.view.manager.process_events(event)
            dt = self.clock.tick() / 1000
            self.view.run(dt)
            self.view.manager.update(dt)
            self.view.manager.draw_ui(self.screen)
            pygame.display.update()
```
