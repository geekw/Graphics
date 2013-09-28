import math

def rotatePoint(point, center, angle):
	x = point['x']*math.cos(angle) + point['y']*math.sin(angle) \
		+ center['x'] - center['x']*math.cos(angle) \
		- center['y']*math.sin(angle)
	y = point['y']*math.cos(angle) - point['x']*math.sin(angle) \
		+ center['y'] - center['y']*math.cos(angle) \
		+ center['x']*math.sin(angle)
	point['x'] = x
	point['y'] = y
	return point

def reverseRotatePoint(point, center, angle):
	x = point['x']*math.cos(angle) - point['y']*math.sin(angle) \
		+ center['x'] - center['x']*math.cos(angle) \
		+ center['y']*math.sin(angle)
	y = point['y']*math.cos(angle) + point['x']*math.sin(angle) \
		+ center['y'] - center['y']*math.cos(angle) \
		- center['x']*math.sin(angle)
	point['x'] = x
	point['y'] = y
	return point

def deltaCoorToDeltaSize4(deltaCoor, angle):
#For down-right point fixed only
	dw = -deltaCoor['x']*math.cos(angle) - deltaCoor['y']*math.sin(angle)
	dh = -deltaCoor['y']*math.cos(angle) + deltaCoor['x']*math.sin(angle)
	deltaSize={'width':dw, 'height':dh}	
	return deltaSize

#main function 1
def topleftDrag1(rect,deltaCoor):
#Calculate rotated down-right point
	x = rect['left'] + rect['width']/2.0 
	y = rect['top'] + rect['height']/2.0 
	center = {'x':x, 'y':y}
	x = rect['left'] + rect['width']
	y = rect['top'] + rect['height']
	downRightPoint = {'x':x, 'y':y}
	rotatedDownRightPoint = rotatePoint(downRightPoint, center, rect['rot'])

#Calculate delta of size
	deltaSize = deltaCoorToDeltaSize4(deltaCoor, rect['rot'])
	
#Calculate resized and rotated top-left point
	w = rect['width'] + deltaSize['width']
	h = rect['height'] + deltaSize['height']
	x = downRightPoint['x'] - (w*math.cos(rect['rot']) - h*math.sin(rect['rot'])) 
	y = downRightPoint['y'] - (h*math.cos(rect['rot']) + w*math.sin(rect['rot']))
	topLeftPoint = {'x':x, 'y':y}

#Calculate new center
	center = {'x': (topLeftPoint['x']+downRightPoint['x']) / 2, 'y': (topLeftPoint['y']+downRightPoint['y'])/2} 

#Reverse resized and rotated top-left point to unrotated 
	topLeftPoint = reverseRotatePoint(topLeftPoint, center, rect['rot']) 

#Return new rectangle
	newRect = {'top':topLeftPoint['y'], 'left':topLeftPoint['x'], 'rot':rect['rot'], 'width':w, 'height':h}
	return newRect 

#main function 2
def topleftDrag2(rect, deltaCoor):
	left = (math.cos(2*rect['rot'])+math.cos(rect['rot']))*deltaCoor['x']/2.0 + (math.sin(2*rect['rot'])+math.sin(rect['rot']))*deltaCoor['y']/2.0 + rect['left']
	top = -(math.sin(2*rect['rot'])+math.sin(rect['rot']))*deltaCoor['x']/2.0 + (math.cos(2*rect['rot'])+math.cos(rect['rot']))*deltaCoor['y']/2.0 + rect['top'] 
	width = rect['width'] - deltaCoor['x']*math.cos(rect['rot']) - deltaCoor['y']*math.sin(rect['rot'])
	height = rect['height'] - deltaCoor['y']*math.cos(rect['rot']) + deltaCoor['x']*math.sin(rect['rot'])
	newRect={'top':top, 'left':left, 'width':width, 'height':height, 'rot':rect['rot']}
	return newRect 

originRect={'top':100, 'left':100, 'width':50, 'height':150, 'rot':math.pi/4}
deltaCoor={'x':20, 'y':30}
print topleftDrag1(originRect, deltaCoor)
print topleftDrag2(originRect, deltaCoor)
