# Tilemap-backgraund-move-easy-camera-
in this project i use pygame, to create a simple tilemap background.

Here I will describe some concepts, useful for understanding how my code works:
each tile has a position (x,y), that i load immediately and don't change anymore.
when i move the camera, i update the coordinates of camera (x camera, y camera). When i draw the background, i draw only the tiles in the region: (x camera to x camera + width screen, y camera to y camera + height screen).
