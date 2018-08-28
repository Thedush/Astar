import cv2
import numpy as np
from heapq import *
x=87
y=232
def h(a,b):
   return (b[0]-a[0])+(b[1]-a[1])
          


img=cv2.imread('test_images/test_image1.png')  #read the image 
b=[]
a=[]
for i1 in xrange (20,400,40):     ##coverting the image into a matrix
     
  i=(((i1-20)/40))
  a.append([])
 
  for j1 in xrange (20,400,40):
      j=(((j1-20)/40))
       
      if (img[i1,j1,0]==255):
         a[i].append(0)
        
      if (img[i1,j1,0]==x ):
         a[i].append(0)
         
         strow=i
         stcol=j
      if (img[i1,j1,0]==y):
         a[i].append(0)
         
         gorow=i
         gocol=j
      if (img[i1,j1,0]==0):
         a[i].append(100)
        
for i in range (10):
    print a[i]
start=(strow,stcol)
cs1=cs=start
goal=(gorow,gocol)
gs=goal
close=set()
parent={}
gval={(start):0}
fval={(start):gval[start]+h(start,goal)}
s=[]
axis={(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)}
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
      while current in parent:
         path.append(current)
         fuck=current
         current=parent[current]
         cv2.line(img,(((fuck[1]+1)*40)-20,((fuck[0]+1)*40)-20),(((current[1]+1)*40)-20,((current[0]+1)*40)-20),(255,255,0),3)
      path.append(start)
      print path
      cs1=gs
       
    gval[current]=g
    fval[current]=f
    heappush(s,(fval[current],current))
        
cv2.imshow('nav',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
