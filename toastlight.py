#!/usr/bin/env python
import time
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219

# Configuration for a single 8x8 matrix
serial = spi(port=0, device=0, cs_high=False)
device = max7219(serial, cascaded=1, block_orientation=0, rotate=0, pcb_layout=1)

# Set the display brightness (0-15)
device.brightness(5) # Adjust as needed

# Define the pixel art for the toast silhouette from your image (8x8)
# 1 represents an LED on, 0 represents an LED off
toast_silhouette_image_pixels = [
    [0, 0, 1, 1, 1, 1, 0, 0], # Rounded top
    [0, 1, 1, 1, 1, 1, 1, 0], # Slight curve
    [1, 1, 1, 1, 1, 1, 1, 1], # Full width
    [1, 1, 1, 1, 1, 1, 1, 1], #
    [1, 1, 1, 1, 1, 1, 1, 1], # Main body
    [1, 1, 1, 1, 1, 1, 1, 1], #
    [1, 1, 1, 1, 1, 1, 1, 1], #
    [1, 1, 1, 1, 1, 1, 1, 1]  # Flat bottom
]


def display_specific_toast_silhouette():
    print("Displaying the specific toast silhouette on the MAX7219 matrix...")

    # Use a canvas to draw the pixels
    with canvas(device) as draw:
        for y, row in enumerate(toast_silhouette_image_pixels):
            for x, pixel_on in enumerate(row):
                if pixel_on:
                    draw.point((x, y), fill="white") # Turn on the LED at (x,y)

    print("Toast silhouette displayed. Holding for 5 seconds...")
    time.sleep(5) # Display for 5 seconds

if __name__ == "__main__":
    try:
        display_specific_toast_silhouette()
    except KeyboardInterrupt:
        print("\nExiting.")
    finally:
        # Clear the display when the script exits
        device.clear()