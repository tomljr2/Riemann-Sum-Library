def RiemannSum(f,a,b,n=1000,type='l',plot=False):
   rSum = 0
   flip = False

   # For now, just flip a and b if b < a
   # and then make the final result negative
   if(b < a):
      flip = True
      a,b = b,a

   # Plot the original function on the graph in the
   # given range, if the user specified to plot.
   if(plot):
      import numpy as np
      import matplotlib.pyplot as plt
      fig,ax = plt.subplots(1)
      r = np.arange(a,b,0.025*abs(b-a))
      ax.plot(r,f(r))

   # If a == b, then there is no area, so the Riemann sum
   # approximation is just 0. So don't even bother plotting.
   if(a == b):
      return 0

   # Calculate the delta x
   dx = ((b-a)*1.0)/n

   # Perform the Riemann sum approximation based on where
   # the user specified the rectangles to be positioned
   for i in range(1,n+1):
      if(type == 'l'):
         x = f(a+(i-1)*dx)
      elif(type == 'm'):
         x = f(((a+i*dx)+(a+(i-1)*dx))/2)
      elif(type == 'r'):
         x = f(a+i*dx)
      else:
         raise Exception("Invalid Riemann sum type")

      if(plot):
         ax.add_patch(plt.Rectangle((a+(i-1)*dx,0),dx,x, \
                                    facecolor="none", edgecolor="red"))
      rSum += x
   rSum *= dx

   # Show the graph if the user wanted it
   if(plot):
      plt.show()

   # Multiply the final result by -1 if b < a
   if(flip):
      rSum *= -1

   return rSum
