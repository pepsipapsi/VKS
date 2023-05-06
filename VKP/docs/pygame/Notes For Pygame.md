## What are some problems that arise when dealing with a program built using pygame?
The first thing to notice, is how the engine is built considering frame rates. A good computer would run a game slower than a very good computer, but we always want to have consistent run time on both. How do we deal with this problem? 

1. Ceiling - easy to tell the computer to pause between frames
2. Floor - really hard to get a computer to run faster (need to change the game to ensure it runs well)

We need a clock object. (Helps us with time and frames)

```python
clock = pygame.time.Clock()

... #while loop

pygame.display.update()
clock.tick(60)
```

clock.tick(60), tells the program to update the while loop 60 times per second. 

## Displaying images

- Surface (Display surface)
	- The game window. Anything displayed.
* Surface (regular)
	* Essentially a single image (something imported, rendered text or a plain color)
	* Needs to be put on diplay surface.

Display surface always comes empty, and regular surfaces fill the display surface. We can only have one display surface, but many regular surfaces. 

## Why is the Bezier Curve needed to be implemented?

To answer this question, we need too see what "C-C avstand" formula is about. C-C Avstand or CC disctance is the distance (in cm) that a heating cable has to itself, objects and walls. For objects and walls the CC distance is half a CC. This will be implemented gradually. 

Bezier Curve is a mathematical function to calculate how a curve will, in this case, be drawn on the window program. CC distance uses curves all the time with only the starting and ending points being fixed by the balance of the middle point between them. What I mean by that is that the curve itself won't go more to the left or the right. By giving it a fixed integer (cm in this case), the program will have a dynamical function to expand or shrink the fixed middle point of the bezier curve and will take in consideration the walls that it is given, to better adapt the cable representation and the calculation in itself.
![[Pasted image 20230503194036.png | 500]]
This picture is a great example of how the Bezier Curve functions. To obtain this visual curve, one linear function and two quadratic functions is needed to implement it. The first linear function is to represent the starting point to the middle point. 
##### Step 1

![[Pasted image 20230503195646.png | 100]]
The linear function goes like this:
$$
L_0(t) = (1 - t) P_0 + tP_1
$$
==t varies between 0 to 1==

![[Pasted image 20230503200116.png | 200]]

##### Step 2
To draw the curve, we need three points. The two first points are already established, and we know we need two quadratic functions. 

The fist quadratic function:
$$
L_1(t) = (1 - t)P_1 + P_2
$$
![[Pasted image 20230503200748.png | 200]]
Point P1 to P2 is created with a linear L1.

##### Step 3
To finalize the Bezier Curve:

The second quadratic function:
$$
Q_0(t) = (1-t)L_0(t) + tL_1(t)
$$

![[Pasted image 20230503201034.png | 200]]