from time import perf_counter
import statistics
import turtle

turtle.setup(1200, 600)
screen = turtle.Screen()
print(type(screen))
print(screen)

ANGLES = (0, 3.695220532)  # 直線和斜線的角度
NUM_RUNS = 20
SPEED = 0

for angle in ANGLES:
    times = []
    for _ in range(NUM_RUNS):
        line = turtle.Turtle()
        line.speed(SPEED)  
        line.hideturtle()
        line.penup()
        line.lt(angle)
        line.setpos(-470, 0)
        line.pendown()
        line.showturtle()
        start_time = perf_counter()
        line.fd(962)
        end_time = perf_counter()
        times.append(end_time - start_time)
        
    line_ave = statistics.mean(times)
    print("Angle {} degrees: average time for {} runs at speed {} = {:.5f}"
          .format(angle, NUM_RUNS, SPEED, line_ave))
