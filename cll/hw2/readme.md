# HW2 for BE002
Run `hw2.py`
**Major Function:** 
```python
def drawCircle(event,x,y,flags,param):
    if event==cv2.EVENT_RBUTTONDBLCLK:
        radius=param[0]
        color=param[1]
        thickness=param[2] # If thickness=-1, draw solid circles
        cv2.circle(img,(x,y),radius,color,thickness)
```
## Task 1
__Output__
<img src="https://github.com/ophwsjtu18/ohw21f/blob/main/cll/hw2/Task1_hollowCircle.png" alt="Cow" align=center />

## Task 2
- __Input__
<img src="https://github.com/ophwsjtu18/ohw21f/blob/main/cll/hw2/cow.jpg" alt="Cow" align=center />

- __Output__
<img src="https://github.com/ophwsjtu18/ohw21f/blob/main/cll/hw2/Task2_solidCircle.png" alt="Cow" align=center />
