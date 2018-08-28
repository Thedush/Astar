import cv2
import numpy as np
from heapq import *
x=87
y=232
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
     
      #print path[1]
      cs1=gs
       
    gval[current]=g
    fval[current]=f
    heappush(s,(fval[current],current))



img=cv2.imread('test_images/test_image21.png')  #read the image 
b=[]
a=[]
gorow=[0]*4
gocol=[0]*4
p=q=0
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
         gorow[p]=i
         gocol[q]=j
         p=p+1
         q=q+1
      if (img[i1,j1,0]==0):
         a[i].append(100)
        
for i in range (10):
    print a[i]





start=(strow,stcol)
goal=(gorow[0],gocol[0])
astar(start,goal)
start=(gorow[0],gocol[0])
goal=(gorow[1],gocol[1])
astar(start,goal)

cv2.imshow('nav',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
