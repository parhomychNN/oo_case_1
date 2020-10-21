from math import floor, sqrt
from tkinter import *

from Point import Point
from Quadratic_equation import Quadratic_equation


def draw_a_point(c: Canvas, point: Point, color: str):
    thickness = 0
    x1, y1 = point.x + thickness, point.y + thickness
    x2, y2 = point.x - thickness, point.y - thickness
    c.create_oval(x1, y1, x2, y2, fill=color)


def update_canvas(c: Canvas, p1: Point, p2: Point, circle_center: Point, radius: float):
    # c.delete(ALL)

    # scale calculation
    width = c.winfo_width()
    height = c.winfo_height()
    circle_right = circle_center.x + radius
    circle_top = circle_center.y + radius
    # cells drawing
    for i in range(0, width, 1):
        c.create_line(i, 0, i, height, fill="#c2c3c4")
    for i in range(0, width, 1):
        c.create_line(0, i, width, i, fill="#c2c3c4")

    scale = width / circle_right if (width / circle_right < height / circle_top) else height / circle_top
    scale = floor(scale * 0.9)
    if p2 is not None:
        c.create_line(p1.x, p1.y, p2.x, p2.y)
    c.create_oval(circle_center.x - radius,
                  circle_center.y - radius,
                  circle_center.x + radius,
                  circle_center.y + radius,
                  outline="red")

    draw_a_point(c, p1, "#03fc77")
    if p2 is not None:
        draw_a_point(c, p2, "#03fc77")
    draw_a_point(c, circle_center, "#1a255c")

    c.scale(ALL, 0, 0, scale, scale)
    print("scale = " + str(scale))


def calculate_intersections(x1, y1, xc, yc, radius, canvas):
    canvas.delete(ALL)

    x1 = float(x1.get())
    y1 = float(y1.get())
    xc = float(xc.get())
    yc = float(yc.get())
    radius = float(radius.get())

    num_of_dec = 4
    zero_point = Point(0, 0)
    ray_point = Point(x1, y1)

    # tilt angle calculation
    k_orig = ray_point.y / ray_point.x
    k_perpend = - (1 / k_orig)
    print("k_orig = " + str(k_orig) + ", k_perpend = " + str(k_perpend))

    # (x - a) ** 2 + (y - b) ** 2 = R ** 2 - circle equation
    # if R == 1, a = 0, b = 0:
    x_perp = sqrt(1 / (1 + k_orig ** 2))
    y_perp = k_orig * x_perp
    perp_point = Point(x_perp, y_perp)
    # y=kx+b; b=y-kx
    b_perp = perp_point.y - perp_point.x * x_perp
    canvas.create_line(0, b_perp, 10, 10 * k_perpend + b_perp, fill="#f72b02")
    print("Perp point: " + str(perp_point) + ", b_perp = " + str(b_perp))

    # todo: вынести это вычисление в другую функцию и пройтись по перпендикуляру y_perp = x_perp * k_perpend + b_perp
    a = round(x1 ** 2 + y1 ** 2, num_of_dec)
    b = round((-2 * x1 * xc) - 2 * y1 * yc, num_of_dec)
    c = round(xc ** 2 + yc ** 2 - radius ** 2, num_of_dec)
    print(str(a) + "d2 + " + str(b) + "d + " + str(c))
    quad_eq = Quadratic_equation(a, b, c)
    # decided on d
    quad_res = quad_eq.solve_quad_equation()
    print("Decided on d: " + quad_res.__str__())
    point_n1: Point
    circle_center = Point(xc, yc)
    if quad_res.status == "No roots":
        update_canvas(canvas, zero_point, Point(x1 * 100, y1 * 100), circle_center, radius)
    elif quad_res.status == "1 root":
        # 1 intersection
        xn = x1 * quad_res.x1
        yn = y1 * quad_res.x1
        print("Points of intersection: (" + str(xn) + ", " + str(yn) + ")")
        point_n2 = Point(xn, yn)
        update_canvas(canvas, zero_point, point_n2, circle_center, radius)
    else:
        # 2 intersections
        xn = x1 * quad_res.x1
        yn = y1 * quad_res.x1
        point_n1 = Point(xn, yn)
        print("Root #1: " + str(point_n1) + ", distance: " + str(point_n1.get_distance_to(zero_point)))
        xn = x1 * quad_res.x2
        yn = y1 * quad_res.x2
        point_n2 = Point(xn, yn)
        print("Root #2: " + str(point_n2) + ", distance: " + str(point_n2.get_distance_to(zero_point)))
        nearest_point = point_n1 if point_n1.get_distance_to(zero_point) < point_n2.get_distance_to(
            zero_point) else point_n2
        update_canvas(canvas, zero_point, nearest_point, circle_center, radius)


def fill_the_appearance():
    root = Tk()
    root.title("CASE-технологии. Пересечения")
    root.geometry("500x300")
    # frames
    frame_top = Frame(root)
    frame_left = Frame(root)
    frame_right = Frame(root)

    # top elements
    label_name = Label(frame_top, text="CASE-технологии. Пересечения")

    # left elements
    entry_width = 7
    # the 1st dot coordinates entry
    lbl_frm_dot_1 = LabelFrame(frame_left, text="Первая точка")
    label_x1 = Label(lbl_frm_dot_1, text="x1")
    x1 = Entry(lbl_frm_dot_1, width=entry_width)
    label_y1 = Label(lbl_frm_dot_1, text="y1")
    y1 = Entry(lbl_frm_dot_1, width=entry_width)

    # circle center entry
    lbl_frm_circle_center = LabelFrame(frame_left, text="Центр окружности")
    label_xc = Label(lbl_frm_circle_center, text="xс")
    xc = Entry(lbl_frm_circle_center, width=entry_width)
    label_yc = Label(lbl_frm_circle_center, text="yc")
    yc = Entry(lbl_frm_circle_center, width=entry_width)

    # circle radius entry
    lbl_frm_circle_radius = LabelFrame(frame_left, text="Радиус окружности")
    label_radius = Label(lbl_frm_circle_radius, text="радиус")
    radius = Entry(lbl_frm_circle_radius, width=entry_width)

    # canvas
    canvas = Canvas(frame_right, bg='#ccc')

    # button for calculation
    btn_calculate = Button(frame_left, text="Вычислить пересечение",
                           command=lambda: calculate_intersections(x1, y1, xc, yc, radius, canvas))

    # packs
    frame_top.pack(side=TOP)
    frame_left.pack(side=LEFT, padx=10, pady=10)
    frame_right.pack(side=RIGHT)

    label_name.pack()

    # pack for 1st point
    lbl_frm_dot_1.pack(side=TOP, fill=X)
    label_x1.pack(side=LEFT)
    x1.pack(side=LEFT)
    label_y1.pack(side=LEFT)
    y1.pack(side=LEFT)

    # pack for circle center
    lbl_frm_circle_center.pack(side=TOP, fill=X)
    label_xc.pack(side=LEFT)
    xc.pack(side=LEFT)
    label_yc.pack(side=LEFT)
    yc.pack(side=LEFT)

    # pack for circle radius
    lbl_frm_circle_radius.pack(side=TOP, fill=X)
    label_radius.pack(side=LEFT)
    radius.pack(side=LEFT)

    # pack for button
    btn_calculate.pack(side=TOP)

    # pack for canvas
    canvas.pack()

    root.mainloop()
