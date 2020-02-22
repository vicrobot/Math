from math import pi, cos, sin
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

class Integrate:
    def __init__(self, p, f, a, b):
        """
        #Class for definite integral, assuming f is continuous in range [a,b]
        
        p is error level, we've to get area with error upto or below that level.
        f is given continuous function in [a,b] range.
        """
        self.f = f
        self.p = p #error allowed.
        self.lim = a, b #lower and upper limits.
        self.bins = 10

    def getBins(self):
        """
        Decides how many parts to make in curve to get accuracy of 100*(1- errorallowed) %. 
        """
        avg = float('inf')
        a,b= self.lim
        n = self.bins
        f = self.f
        count = 0
        while avg -1-2*self.p > 0:
            count += 1
            n += n//2
            c =  (b-a)/n
            s = 0
            for i in range(1, n):
                s += abs(f(a +(i+1)*c)/f(a + i*c)) #absolute since we don't want differences
                                                   #to cancel each other but support together.
            avg = s/n #at ideal integration, avg is 0. As n increases, avg decreases.
            print(f"Error: {(avg-1)/2:>8.7}%, bins: {n:>8}, Iteration: {count:>3}")
        return n

    def getArea(self,i):
        """
        Returns slit's area on x =i. Slit's width is self.c which is (upper lim - lower lim)/parts made in graph
        slit is a rectangle sitting on x = i and x = i+self.c and height is f(i) and f(i+self.c)
        """
        a,b = self.lim
        area = self.c*self.f(a + i*self.c)
        return area

    def run(self):
        """
        Executes area calculation, does animation
        """
        self.bins = self.getBins()
        print('\nNumber of bins got for {0} or less error is : {1}'.format(self.p, self.bins))
        self.c = (self.lim[1] - self.lim[0])/self.bins
        
        #anim -----------------
        self.area = self.getArea(self.lim[0])
        print(f"Area: {self.area:>5.5}")
        
        self.x = np.linspace(self.lim[0], self.lim[1], self.bins)[1:]
        self.y = [f(i) for i in self.x]
        
        fig, self.ax = plt.subplots()
        plt.xlabel('X')
        plt.ylabel(r'$sin^2(x)$')
        plt.grid('True')
        def init():
            ax_obj, = self.ax.plot(self.x, self.y)
            return [ax_obj]
        polygon_list = []
        def animate(j):
            self.area += self.getArea(j)
            print(f"Area: {self.area:>5.5}")
            self.ax.title.set_text(f"Area: {self.area:>5.5} sq. units")
            i = j*self.c
            polygon_obj,=self.ax.fill([i,i+self.c, i+self.c, i],[0,0,f(i+self.c), f(i)], 'k')
            polygon_list.append(polygon_obj)
            return polygon_list
        
        ani = anim.FuncAnimation(fig, animate, frames = range(self.bins), init_func = init,interval = 1,
                                blit = False, repeat = False)
        plt.title(f"Area: {self.area:>5.5} sq. units")
        plt.show()
        print(f"Area: {self.area:>5.5} sq. units")



if __name__ == "__main__":
    f = lambda x: sin(x)**2   #function specified.
    Integrate(1e-2,f,  0, pi).run()
