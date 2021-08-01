import pygame
import time
import random
import numpy as np
import os
import tkinter as tk
from tkinter import*

#requirments
'''
pip install pygame
pip install numpy
pip install tkinter
'''
#commands
#"Esc" to close the window

os.environ["SDL_VIDEO_CENTERED"]='1'

#resolution
width, height = 1080,100
size = (width, height)

pygame.init()
pygame.display.set_caption("vinay jakkena's grid")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 30

black = (0, 0, 0)
blue = (0, 121, 150)
blue1 = (0,14,71)
white = (255, 255, 255)
green = (124,252,0)
red = (255,0,0)

scaler = 30
offset = 2
#inputval = int(0)
#newgridArchieve = np.ndarray()

class Grid:
    def __init__(self, width, height, scale, offset):
        self.scale = scale
        #cell columns and rows randomly placing by using height and width
        self.rows = int(width/scale)
        self.columns = int(height/scale)

        #grid size
        self.size = (self.rows, self.columns)
        
        #numpy ndarray gives inter connection to one end to another end like rubic shape
        self.grid_array = np.ndarray(shape=(self.size))
        self.offset = offset

        # UI changes
        self.window = tk.Tk()
        self.window.title("Game of life and death input and output screen")

        self.window.configure(background='snow')

        

        lb1 = tk.Label(self.window, text="enter a number in the multipes of 20 utmost 100 to append to grid",pady=20, bg='deep pink').pack()
        self.cells_entry = Entry(self.window)
        self.cells_entry.place(x=200, y=310)
        self.cells_entry.pack(pady=30)

        Button(self.window,text="Click to add cells", padx=10, pady=5,command=self.printValue).pack()

        lb2 = tk.Label(self.window, text="searching a cell for its state", width=20, height=1, fg="black", bg="deep pink", font=('times', 20, ' bold ')) 
        self.cells_entry1 = Entry(self.window)
        self.cells_entry1.place(x=400, y=310)
        self.cells_entry1.pack(pady=30)

        Button(self.window,text="Enter searching cell", padx=10, pady=5,command=self.printValue1).pack()

        #Create a listbox
        self.listbox= Listbox(self.window)
        self.listbox.pack(side =LEFT, fill = BOTH)

        #Create a Scrollbar
        scrollbar = Scrollbar(self.window)
        scrollbar.pack(side = RIGHT, fill = BOTH)

        Label(self.window, text=f'History', pady=20, bg='#ffbf00').pack()
        #Insert Values in listbox
        #self.listbox.insert(END, Label)
        self.listbox.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = self.listbox.yview)


    def printValue(self):
        additionalCells = int(self.cells_entry.get())
        # input value from UI is assigned to inputval
        #inputval = 20
        #2d array is converted to 1d array and preserved
        
        oldGridsize = (grid.rows * grid.columns)
        newRowSize = grid.rows
        newColumnize = grid.columns + additionalCells/20
        # grid size is updated with the new cells count
        grid.update_grid_size(newRowSize, newColumnize)
        grid.update_random2d_array(self.gridArchieve, oldGridsize)
        screen.fill(black)
        # grid.Conway is used for applying our logic
        grid.Conway(off_color=red, on_color=green, surface=screen)
        pygame.display.update()
        Label(self.window, text=f'{additionalCells} cells appended to grid', pady=20, bg='#ffbf00').pack()
        #Insert Values in listbox
        self.listbox.insert(END, Label)
    
    
    def printValue1(self):
        searchId = int(self.cells_entry1.get())
        SearchedCellValue = self.gridArchieve[searchId - 1]
        status = "Alive" if SearchedCellValue == 1 else "Dead"
        Label(self.window, text=f'the cell{searchId} is {status}', pady=20, bg='yellow').pack()
        #Insert Values in listbox
        self.listbox.insert(END, Label)



    def random2d_array(self):
        #random number from 0,1 is assigned to the grid
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0,1)


    def Conway(self, off_color, on_color, surface):
        next = np.ndarray(shape=(self.size))
        for x in range(self.rows):
            for y in range(self.columns):
                state = self.grid_array[x][y]
                neighbours = self.get_neighbours( x, y)
                if state == 0 and neighbours == 3:
                    next[x][y] = 1
                elif state == 1 and (neighbours < 2 or neighbours > 3):
                    next[x][y] = 0
                else:
                    next[x][y] = state
        self.grid_array = next  
        for x in range(self.rows):
            for y in range(self.columns):
                y_pos = y * self.scale
                x_pos = x * self.scale
                if self.grid_array[x][y] == 1:
                    pygame.draw.rect(surface, on_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                else:
                    pygame.draw.rect(surface, off_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
        
        self.gridArchieve = grid.grid_array.flatten()

           

    #used for finding the neighbours of the specific cell
    def get_neighbours(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x+n+self.rows) % self.rows
                y_edge = (y+m+self.columns) % self.columns
                total += self.grid_array[x_edge][y_edge]

        total -= self.grid_array[x][y]
        return total

    #used for updating the existing grid
    def update_grid_size(self, newx, newy):
        #cell columns and rows randomly placing by using height and width
        self.columns = int(newy)
        self.rows = int(newx)

        #grid size
        self.size = (self.rows, self.columns)
        
        #numpy ndarray gives inter connection to one end to another end like rubic shape
        self.grid_array = np.ndarray(shape=(self.size))

    #used for updating the existing grid values
    def update_random2d_array(self, gridSize):
        count = 0
        for x in range(self.rows):
            for y in range(self.columns):
                if(count < gridSize):
                    self.grid_array[x][y] = self.gridArchieve[count]
                    count = count + 1
                else:
                    self.grid_array[x][y] = random.randint(0,1)
                    
# grid is initializing the grid with rows 20 and columns 25
grid = Grid(width,height, scaler, offset)
grid.random2d_array()
screen.fill(black)
grid.Conway(off_color=red, on_color=green, surface=screen)
pygame.display.update()


#window.mainloop()


run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
    grid.window.update_idletasks()
    grid.window.update()
    pygame.display.update()
pygame.quit()