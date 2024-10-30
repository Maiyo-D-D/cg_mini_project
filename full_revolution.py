import math
import cairo
from PIL import Image
import random

WIDTH, HEIGHT = 800, 800

def draw_stars(context, num_stars=100):
    """Draw random stars in the background."""
    context.set_source_rgb(1, 1, 1)  # White stars
    for _ in range(num_stars):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        radius = random.uniform(0.5, 1.5)  # Random small size for stars
        context.arc(x, y, radius, 0, 2 * math.pi)
        context.fill()

def draw_glow(context, center_x, center_y, radius, color):
    """Draw a glowing effect using a radial gradient."""
    gradient = cairo.RadialGradient(center_x, center_y, radius * 0.5,
                                    center_x, center_y, radius * 1.5)
    gradient.add_color_stop_rgba(0, *color, 1)  # Core of the glow (solid)
    gradient.add_color_stop_rgba(1, *color, 0)  # Fade out to transparent
    context.set_source(gradient)
    context.arc(center_x, center_y, radius * 1.5, 0, 2 * math.pi)
    context.fill()

def draw_sphere_with_shading(context, center_x, center_y, radius, color):
    """Draw a 3D-like sphere with lighting and shading."""
    gradient = cairo.RadialGradient(center_x - radius * 0.3, center_y - radius * 0.3, radius * 0.2,
                                    center_x, center_y, radius)
    gradient.add_color_stop_rgb(0, *color)  # Lighted side
    gradient.add_color_stop_rgb(0.7, color[0] * 0.5, color[1] * 0.5, color[2] * 0.5)  # Mid shading
    gradient.add_color_stop_rgb(1, 0.1, 0.1, 0.1)  # Dark shadow
    context.set_source(gradient)
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)
    context.fill()

def create_frame(planets_positions, sun_position, frame_num):
    """Create a frame with the sun, glowing effect, planets with shading, and stars."""
    # Create surface and context
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    context = cairo.Context(surface)

    # Background (deep space, black)
    context.set_source_rgb(0, 0, 0)  # Space background
    context.paint()

    # Draw stars in the background
    draw_stars(context, num_stars=200)

    # Draw the glow around the sun
    draw_glow(context, sun_position[0], sun_position[1], 100, (1, 0.8, 0.1))  # Glowing sun effect

    # Draw the sun (a large 3D sphere in the center)
    draw_sphere_with_shading(context, sun_position[0], sun_position[1], 50, (1, 1, 0))  # Yellow sun with shading

    # Draw planets (smaller spheres)
    for planet in planets_positions:
        x, y, radius, color = planet
        draw_sphere_with_shading(context, x, y, radius, color)

    # Return the frame as a PIL image
    return Image.frombuffer("RGBA", (WIDTH, HEIGHT), surface.get_data(), "raw", "BGRA", 0, 1)

def create_solar_system_gif(num_frames=60):
    frames = []
    sun_position = (WIDTH // 2, HEIGHT // 2)  # Sun in the center

    # Planet configuration: (distance from sun, radius, color)
    planets_info = [
        (120, 10, (0.5, 0.5, 1)),  # Blue planet, closest to sun
        (160, 15, (0.8, 0.3, 0.2)),  # Reddish planet
        (200, 20, (0.2, 0.8, 0.3)),  # Greenish planet
        (240, 25, (0.8, 0.8, 0.2)),  # Yellowish planet
    ]

    # Orbital speeds (different for each planet)
    orbital_speeds = [0.05, 0.03, 0.02, 0.01]

    # Generate frames
    for frame_num in range(num_frames):
        planets_positions = []
        for i, planet_info in enumerate(planets_info):
            distance, radius, color = planet_info

            # Calculate angle for full revolution, looping every 360 degrees
            angle = (frame_num * orbital_speeds[i]) % (2 * math.pi)

            # Calculate new position of planet in orbit (revolve around the sun)
            planet_x = sun_position[0] + distance * math.cos(angle)
            planet_y = sun_position[1] + distance * math.sin(angle)

            planets_positions.append((planet_x, planet_y, radius, color))

        # Create the frame
        frames.append(create_frame(planets_positions, sun_position, frame_num))

    # Save the frames as a GIF
    frames[0].save("solar_system_full_revolution.gif", save_all=True, append_images=frames[1:], duration=100, loop=0)
    print("GIF created: solar_system_full_revolution.gif")

if __name__ == "__main__":
    create_solar_system_gif()