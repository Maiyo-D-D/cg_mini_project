# Solar System Animation Project

This project generates an animated GIF of a solar system with a sun and orbiting planets. The animation includes stars in the background, a glowing effect around the sun, and shaded spheres representing the sun and planets.

## Code Explanation

### Imports
```python
import math
import cairo
from PIL import Image
import random
```
- `math`: Provides mathematical functions.
- `cairo`: Used for 2D graphics rendering.
- `PIL.Image`: Part of the Pillow library, used for image processing.
- `random`: Generates random numbers.

### Constants
```python
WIDTH, HEIGHT = 800, 800
```
Defines the dimensions of the canvas.

### Functions

#### `draw_stars(context, num_stars=100)`
Draws random stars in the background.
- `context.set_source_rgb(1, 1, 1)`: Sets the color to white.
- Loops `num_stars` times to draw stars at random positions with random sizes.

#### `draw_glow(context, center_x, center_y, radius, color)`
Draws a glowing effect using a radial gradient.
- Creates a radial gradient centered at `(center_x, center_y)`.
- Adds color stops to create a glow effect that fades out to transparent.

#### `draw_sphere_with_shading(context, center_x, center_y, radius, color)`
Draws a 3D-like sphere with lighting and shading.
- Creates a radial gradient to simulate lighting and shading on the sphere.
- Adds color stops to create a gradient from light to dark.

#### `create_frame(planets_positions, sun_position, frame_num)`
Creates a frame with the sun, glowing effect, planets with shading, and stars.
- Creates a surface and context for drawing.
- Sets the background to black.
- Draws stars, the sun's glow, the sun, and the planets.
- Returns the frame as a PIL image.

#### `create_solar_system_gif(num_frames=60)`
Generates an animated GIF of the solar system.
- Initializes the sun's position.
- Defines planet configurations (distance from the sun, radius, color).
- Defines orbital speeds for each planet.
- Generates frames by calculating the position of each planet in its orbit.
- Saves the frames as a GIF.

### Main Execution
```python
if __name__ == "__main__":
    create_solar_system_gif()
```
Calls the `create_solar_system_gif` function to generate the GIF.

## Output
The output is an animated GIF named `solar_system_full_revolution.gif` that shows a solar system with a sun and orbiting planets.

## Usage
Run the script to generate the GIF:
```bash
python revolution.py
```
Replace `revolution.py` with the actual name of the script file.
