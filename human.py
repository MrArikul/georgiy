from tkinter import Tk, Canvas, ARC, SE, W


class Human():
    
        def __init__(self, canvas, x, y):
            self.canvas = canvas
            self.x = x
            self.y = y 
           
        
        def display(self):
            self.__drawHead()
            #self.__drawBody()
            self.__drawLeggs()
            self.__drawFace()
            self.__drawName()
            
            
        def __drawLeggs(self):
            self.canvas.create_line(self.x, self.y, self.x+50, self.y-50, self.x+100, self.y, width=2)
            self.canvas.create_line(self.x+50, self.y-190, self.x+50, self.y-50, self.x+100, self.y, width=2)
            self.canvas.create_line(self.x, self.y-110, self.x+50, self.y-150, self.x+100, self.y-110, width=2)
        def __drawHead(self):
            self.canvas.create_oval(self.x, self.y-290, self.x+100, self.y-190, width=2)
            self.canvas.create_arc(self.x+10,self.x+25, self.y-210, self.x+96, start=0, extent=-180,
                style=ARC, outline="red", width=3)
        
        def __drawFace(self):
            self.canvas.create_oval(self.x+30, self.y-260, self.x+20, self.y-280, width=0, fill="red")
            self.canvas.create_oval(self.x+70, self.y-260, self.x+60, self.y-280, width=0, fill="red")

        
        def __drawName(self):
       
            self.canvas.create_text(self.x+50, self.y-330, fill="black", font="Times 20 italic bold", text ="Это Олег, хорошая работа!")
        
        def __drawBody(self):
            self.canvas.create_line(50, 460, 50, 550, width=2)
            self.canvas.create_line(10, 640, 50, 546, width=2)
            self.canvas.create_line(100, 670, 50, 546, width=2)
            self.canvas.create_line(-110, 400, 50, 500, width=2)
            self.canvas.create_line(110, 460, 50, 500, width=2)
       
       