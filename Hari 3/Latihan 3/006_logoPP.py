import turtle

# Membuat objek Turtle
t = turtle.Turtle()

# Fungsi untuk menggambar lingkaran
def draw_circle(radius, fill_color, pen_color):
    t.fillcolor(fill_color)
    t.pencolor(pen_color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_rectangle(width, height, fill_color):
    t.fillcolor(fill_color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Fungsi utama
def main():
    # Setel latar belakang menjadi hitam
    turtle.bgcolor("white")

    # Setel kecepatan tampilan Turtle
    t.speed(7)  # Anda dapat mengubah kecepatan sesuai keinginan

    radius_outerr = 310
    t.penup()
    t.goto(0, -310)  # Pindah ke posisi bawah lingkaran luar
    t.pendown()
    draw_circle(radius_outerr, "black", "black")

    # Lingkaran luar (putih)
    radius_outer = 300
    t.penup()
    t.goto(0, -300)  # Pindah ke posisi bawah lingkaran luar
    t.pendown()
    draw_circle(radius_outer, "white", "white")

    # Lingkaran dalam (biru tua)
    radius_inner = 230
    t.penup()
    t.goto(0, -230)  # Pindah ke posisi bawah lingkaran luar
    t.pendown()
    draw_circle(radius_inner, "darkblue", "darkblue")
    
    t.pencolor("white")
    width = 120
    height = 80
    t.penup()
    t.goto(-35, -200)
    t.pendown()
    draw_rectangle(width, height, "white")
    
    t.pencolor("red")
    width = 110
    height = 70
    t.penup()
    t.goto(-30,-195)
    t.pendown()
    draw_rectangle(width, height, "red")

    radius_inner = 80
    t.penup()
    t.goto(15, -165)  # Pindah ke posisi bawah lingkaran luar
    t.pendown()
    draw_circle(radius_inner, "white", "white")
#kelingking
    t.pencolor("white")
    width = 35
    height = 175
    t.penup()
    t.goto(60, -95)
    t.pendown()
    draw_rectangle(width, height, "white")
#jari manis  
    width = 35
    height = 175
    t.penup()
    t.goto(25, -85)
    t.pendown()
    draw_rectangle(width, height, "white")
#jari tengah
    width = 35
    height = 175
    t.penup()
    t.goto(-10, -85)
    t.pendown()
    draw_rectangle(width, height, "white")
#tombol hitam putih
    radius_innerr = 55
    t.penup()
    t.goto(-35, 75) 
    t.pendown()
    draw_circle(radius_innerr, "white", "white")

    radius_innerr = 50
    t.penup()
    t.goto(-35, 80) 
    t.pendown()
    draw_circle(radius_innerr, "black", "black")
#tari telunjuk
    t.pencolor("white")
    width = 45
    height = 210
    t.penup()
    t.goto(-55, -60)
    t.pendown()
    draw_rectangle(width, height, "white")

    t.pencolor("white")
    t.fillcolor("white")
    t.begin_fill()
    t.penup()
    t.goto(-50, -25)
    t.pendown()
    t.goto(-105, 15)
    t.goto(-140, -35)
    t.goto(-55, -100)
    t.goto(-50, -25)
    t.end_fill()
#merah
    radius_inner = 75
    t.penup()
    t.goto(15, -160)  # Pindah ke posisi bawah lingkaran luar
    t.pendown()
    draw_circle(radius_inner, "red", "red")
    radius_inner = 75
    t.penup()
    t.goto(15, -145)  # Pindah ke posisi bawah lingkaran luar
    t.pendown()
    draw_circle(radius_inner, "red", "red")

    t.pencolor("red")
    width = 30
    height = 170
    t.penup()
    t.goto(60, -95)
    t.pendown()
    draw_rectangle(width, height, "red")
    t.hideturtle()

    width = 30
    height = 170
    t.penup()
    t.goto(25, -85)
    t.pendown()
    draw_rectangle(width, height, "red")

    width = 30
    height = 170
    t.penup()
    t.goto(-10, -85)
    t.pendown()
    draw_rectangle(width, height, "red")

    width = 35
    height = 205
    t.penup()
    t.goto(-50, -60)
    t.pendown()
    draw_rectangle(width, height, "red")
    
    t.pencolor("red")
    t.fillcolor("red")
    t.begin_fill()
    t.penup()
    t.goto(-35, -42)
    t.pendown()
    t.goto(-103, 7)
    t.goto(-132, -33)
    t.goto(-55, -93)
    t.goto(-35, -42)
    t.end_fill()

    t.pencolor("black")
    t.penup()
    t.goto(-275, -85)
    t.pendown()

    t.fillcolor("black")
    t.begin_fill()
    for _ in range(5):
        t.forward(50)
        t.right(144)
        
    t.end_fill()

    t.penup()
    t.goto(225, -85)
    t.pendown()

    t.fillcolor("black")
    t.begin_fill()
    for _ in range(5):
        t.forward(50)
        t.right(144)
        
    t.end_fill()

    teks1="S E K O L A H   M E N E N G A H   K E J U R U A N"
    t.penup()
    t.goto(0, 320)
    t.pendown()
    t.write(teks1, align="center", font=("Arial", 30, "bold"))
    teks2="P R E S T A S I    P R I M A"
    t.penup()
    t.goto(0, -370)
    t.pendown()
    t.write(teks2, align="center", font=("Arial", 30, "bold"))
    # Menutup jendela saat diklik
    turtle.exitonclick()

if __name__ == "__main__":
    main()