```python
def cc_avstand(kvadratmeter, kabellengde):
    return (kvadratmeter / kabellengde) * 100
```
This is the code that generates an accurate CC Distance. With this, the program can manipulate how the dawing on the "Boxes", representing each room, will layout.

- [ ] Function needs:
	- [ ] What room is it on?
	- [ ] What is the m^2 total of the room (rooms)
		- [ ] Contained just in the space given (Total Area)
	- [ ] cc_avstand --> will be halfed on objects and walls
		- [ ] Are there som "fixed" elements that have fixed distance?
		- [ ] Should everything be halfed?
	* [ ] If all requirements met: then, set starting point and ending point (P1) to be in distance between cc-avstand
	* [ ] render

