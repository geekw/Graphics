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

def deltaCoorToDeltaSize(deltaCoor, angle):
#For down-right point fixed only
	dw = -deltaCoor['x']*math.cos(angle) - deltaCoor['y']*math.sin(angle)
	dh = -deltaCoor['y']*math.cos(angle) + deltaCoor['x']*math.sin(angle)
	deltaSize={'width':dw, 'height':dh}	
	return deltaSize

#main function
def topleftDrag(rect,deltaCoor):
#Calculate rotated down-right point
	x = rect['left'] + rect['width'] 
	y = rect['top'] + rect['height'] 
	downRightPoint = {'x':x, 'y':y}

#Calculate delta of size
	deltaSize = deltaCoorToDeltaSize(deltaCoor, rect['rot'])
	
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
	rect = {'top':topLeftPoint['y'], 'left':topLeftPoint['x'], 'rot':rect['rot'], 'width':w, 'height':h}
	return rect

originRect={'top':100, 'left':100, 'width':150, 'height':150, 'rot':20}
deltaCoor={'x':23, 'y':54}
print topleftDrag(originRect, deltaCoor)

