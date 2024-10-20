import streamlit as st
import numpy as np
import random
from PIL import Image, ImageDraw

# Define game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 50
ENEMY_SIZE = 60
PLAYER_SPEED = 20

# Initialize game state
player_pos = [100, 100]
enemies = [[random.randint(0, SCREEN_WIDTH - ENEMY_SIZE), random.randint(0, SCREEN_HEIGHT - ENEMY_SIZE)] for _ in range(3)]

# Create a function to draw the game state
def draw_game(player_pos, enemies):
    # Create a blank image
    img = Image.new("RGB", (SCREEN_WIDTH, SCREEN_HEIGHT), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw the player (yellow square)
    draw.rectangle(
        [player_pos[0], player_pos[1], player_pos[0] + PLAYER_SIZE, player_pos[1] + PLAYER_SIZE],
        fill=(255, 255, 0)
    )
    
    # Draw enemies (red squares)
    for enemy_pos in enemies:
        draw.rectangle(
            [enemy_pos[0], enemy_pos[1], enemy_pos[0] + ENEMY_SIZE, enemy_pos[1] + ENEMY_SIZE],
            fill=(255, 0, 0)
        )
    
    return img

# Streamlit app setup
st.title("Pac-Man Inspired Game with Streamlit")

# Display the game
st.write("Use the buttons below to move your character.")
col1, col2, col3, col4 = st.columns(4)

if col1.button("Left"):
    player_pos[0] = max(player_pos[0] - PLAYER_SPEED, 0)
if col2.button("Right"):
    player_pos[0] = min(player_pos[0] + PLAYER_SPEED, SCREEN_WIDTH - PLAYER_SIZE)
if col3.button("Up"):
    player_pos[1] = max(player_pos[1] - PLAYER_SPEED, 0)
if col4.button("Down"):
    player_pos[1] = min(player_pos[1] + PLAYER_SPEED, SCREEN_HEIGHT - PLAYER_SIZE)

# Check for collisions (simple demonstration)
collision = False
for enemy_pos in enemies:
    if (
        player_pos[0] < enemy_pos[0] + ENEMY_SIZE and
        player_pos[0] + PLAYER_SIZE > enemy_pos[0] and
        player_pos[1] < enemy_pos[1] + ENEMY_SIZE and
        player_pos[1] + PLAYER_SIZE > enemy_pos[1]
    ):
        collision = True

if collision:
    st.write("You got caught!")
else:
    st.image(draw_game(player_pos, enemies))