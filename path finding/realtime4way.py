import cv2
import numpy as np
from heapq import *

img=cv2.imread('test_images/test_image7.png')  #read the image 
def h(a,b):
   return (b[0]-a[0])+(b[1]-a[1])
def astar(start,goal):
  cs1=cs=start
  gs=goal
  close=set()
  parent={}
  gval={(start):0}
  fval={(start):gval[start]+h(start,goal)}
  s=[]
  axis={(0,1),(0,-1),(1,0),(-1,0)}
  heappush(s,(fval[start],start))
  fu=0
  close.add(cs)


  while cs !=gs and cs1 !=gs:
   cs=heappop(s)[1]
   for i,j in axis:
    current=cs[0]+i,cs[1]+j
    if 0<= current[0] <10 and 0<= current[1] <10:
      
       if a[current[0]][current[1]] ==100:
           continue
    else:
       continue
   
    if i==0 or j ==0:
      g=(gval[cs]+10)
    elif i !=0 and j != 0:
      g=(gval[cs]+14)
    
    f=g+h(current,goal)
    
    if current in close :
          continue
    parent[current]=cs
    close.add(current)
    
    if current ==gs:
      path=[]
      loop=0
      while current in parent:
         loop=loop+1
         path.append(current)
         fuck=current
         current=parent[current]
         cv2.line(img,(((fuck[1]+1)*40)-20,((fuck[0]+1)*40)-20),(((current[1]+1)*40)-20,((current[0]+1)*40)-20),(255,255,0),3)
      path.append(start)
      print path
      for f in range(0,loop+1):
         print path[loop]
         loop=loop-1
      cs1=gs
       
    gval[current]=g
    fval[current]=f
    heappush(s,(fval[current],current))

def center(lw,hi):
    mask = cv2.inRange(img, np.array([0,lw,0]), np.array([255,hi,255]))
    contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    M = cv2.moments(contours[0])
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])    
    return (cx,cy)
strow,stcol = center(120,130)
gorow,gocol= center(160,170)

b=[]
a=[]

p=q=0
for i1 in xrange (20,400,40):     ##coverting the image into a matrix
     
  i=(((i1-20)/40))
  a.append([])
 
  for j1 in xrange (20,400,40):
      j=(((j1-20)/40))
       
      if (img[i1,j1,0]==0):
         a[i].append(100)
        
      else:
         a[i].append(0)
        
for i in range (10):
    print a[i]




start=(((stcol-20)/40),((strow-20)/40))
goal=(((gocol-20)/40),((gorow-20)/40))

astar(start,goal)

cv2.imshow('nav',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
