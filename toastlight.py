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
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1, 1, 0], 
    [0, 1, 1, 1, 1, 1, 1, 0], 
    [0, 0, 1, 1, 1, 1, 0, 0], 
    [0, 0, 1, 1, 1, 1, 0, 0], 
    [0, 0, 1, 1, 1, 1, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0]  
]


def animate_toast_levitate(duration_seconds=15, loop_count=None, speed=0.1):
    print(f"Animating toast levitating for {duration_seconds} seconds (or {loop_count} loops)...")

    levitation_offsets = [
        0,
        1,
        0,
        -1,
        0
    ]
    
    start_time = time.time()
    num_loops = 0

    while True:
        if loop_count is not None and num_loops >= loop_count:
            break
        if loop_count is None and (time.time() - start_time > duration_seconds):
            break

        for y_offset in levitation_offsets:
            with canvas(device) as draw:
                for y_row, row_pixels in enumerate(toast_base_pixels):
                    for x_col, pixel_on in enumerate(row_pixels):
                        if pixel_on:
                            display_y = y_row + y_offset
                            if 0 <= display_y < 8:
                                draw.point((x_col, display_y), fill="white")
            time.sleep(speed)
        
        num_loops += 1

    print("Animation finished.")


if __name__ == "__main__":
    try:
        animate_toast_levitate(duration_seconds=15, speed=0.15)
    except KeyboardInterrupt:
        print("\nAnimation stopped by user.")
    finally:
        device.clear()