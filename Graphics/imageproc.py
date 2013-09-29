import math

def reverseRotatePoint(point, center, angle):
	x = point['x']*math.cos(angle) + point['y']*math.sin(angle) \
		+ center['x'] - center['x']*math.cos(angle) \
		- center['y']*math.sin(angle)
	y = point['y']*math.cos(angle) - point['x']*math.sin(angle) \
		+ center['y'] - center['y']*math.cos(angle) \
		+ center['x']*math.sin(angle)
	point['x'] = x
	point['y'] = y
	return point

def rotatePoint(point, center, angle):
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
	print "Step 01-center", center
	x = rect['left'] + rect['width']
	y = rect['top'] + rect['height']
	downRightPoint = {'x':x, 'y':y}
	print "Step 02-down-right point:", downRightPoint
	rotatedDownRightPoint = rotatePoint(downRightPoint, center, rect['rot'])
	print "Step 1-Rotated Down-right point:", rotatedDownRightPoint

#Calculate delta of size
	deltaSize = deltaCoorToDeltaSize4(deltaCoor, rect['rot'])
	print "Step 2-Delta Size:", deltaSize
	
#Calculate resized and rotated top-left point
	w = rect['width'] + deltaSize['width']
	h = rect['height'] + deltaSize['height']
	x = rotatedDownRightPoint['x'] - (w*math.cos(rect['rot']) - h*math.sin(rect['rot'])) 
	y = rotatedDownRightPoint['y'] - (h*math.cos(rect['rot']) + w*math.sin(rect['rot']))
	rotatedTopLeftPoint = {'x':x, 'y':y}
	print "Step 3-Resized and rotated top-left point:", rotatedTopLeftPoint 

#Calculate new center
	center = {'x': (rotatedTopLeftPoint['x']+rotatedDownRightPoint['x']) / 2, 'y': (rotatedTopLeftPoint['y']+rotatedDownRightPoint['y'])/2} 
	print "Step 4-New Center:", center

#Reverse resized and rotated top-left point to unrotated 
	topLeftPoint = reverseRotatePoint(rotatedTopLeftPoint, center, rect['rot']) 
	print "Step 5-New Top-left Point:", topLeftPoint

#Return new rectangle
	newRect = {'top':topLeftPoint['y'], 'left':topLeftPoint['x'], 'rot':rect['rot'], 'width':w, 'height':h}
	return newRect 

#main function 2
def topleftDrag2(rect, deltaCoor):
	left = (math.cos(rect['rot'])+1)*deltaCoor['x']/2.0 + math.sin(rect['rot'])*deltaCoor['y']/2.0 + rect['left']
	top = -math.sin(rect['rot'])*deltaCoor['x']/2.0 + (math.cos(rect['rot'])+1)*deltaCoor['y']/2.0 + rect['top'] 
	width = rect['width'] - deltaCoor['x']*math.cos(rect['rot']) - deltaCoor['y']*math.sin(rect['rot'])
	height = rect['height'] - deltaCoor['y']*math.cos(rect['rot']) + deltaCoor['x']*math.sin(rect['rot'])
	newRect={'top':top, 'left':left, 'width':width, 'height':height, 'rot':rect['rot']}
	return newRect 

originRect={'top':100, 'left':100, 'width':80, 'height':150, 'rot':math.pi/4.0}
deltaCoor={'x':40, 'y':10}
print topleftDrag1(originRect, deltaCoor)
print topleftDrag2(originRect, deltaCoor)
