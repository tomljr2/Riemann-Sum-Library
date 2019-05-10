def RiemannSum(f,a,b,n=100,dx=None,type='l',plot=False):
   rSum = 0

   if(b < a):
      raise ValueError("a should be less than or equal to b")

   # Plot the original function on the graph in the
   # given range, if the user specified to plot.
   if(plot):
      import numpy as np
      import matplotlib.pyplot as plt
      fig,ax = plt.subplots(1)
      r = np.arange(a,b,0.025*abs(b-a))
      ax.plot(r,f(r))

   if(a == b):
      return 0

   # Set dx to be equal width rectangles. Multiplying by
   # 1.0 is done to force dx to be a floating point value.
   if(dx == None):
      dx = ((b-a)*1.0)/n

   if(type == 'l'):
      for i in range(0,n):
         if(plot):
            ax.add_patch(plt.Rectangle((a+i*dx,0),dx,f(a+i*dx), \
                         facecolor="none",edgecolor="red"))
         rSum += f(a+i*dx)
      rSum *= dx
   elif(type == 'm'):
      for i in range(0,n):
         if(plot):
            ax.add_patch(plt.Rectangle((a+(i-1)*dx,0),dx,(f(a+i*dx)+f(a+(i+1)*dx))/2, \
                         facecolor="none",edgecolor="red"))
         rSum+= (f(a+i*dx)+f(a+(i+1)*dx))/2
      rSum *= dx
   elif(type == 'r'):
      for i in range(1,n+1):
         if(plot):
            ax.add_patch(plt.Rectangle((a+(i-1)*dx,0),dx,f(a+i*dx), \
                         facecolor="none",edgecolor="red"))
         rSum+= f(a+i*dx)
      rSum *= dx
   elif(type == 't'):
      pass
   else:
      raise Exception('Invalid Riemann sum type: {}'.format(type))

   if(plot):
      plt.show()
   return rSum
