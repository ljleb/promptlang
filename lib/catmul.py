from bezier import compute_on_curve_with_points as compute_bezier
import numpy
import math

def linear_interpolation(t, control_points):
    return control_points[0] + (control_points[1] - control_points[0]) * t

def compute_catmul(t, control_points):
    if len(control_points) == 1:
        return control_points[0]
    elif len(control_points) == 2:
        return linear_interpolation(t, control_points)
    else:
        target_curve = min(int(t * (len(control_points) - 1)), len(control_points) - 1)
        g0 = control_points[target_curve - 1] if target_curve > 0 else control_points[0] + control_points[0] - control_points[1]
        cp0 = control_points[target_curve]
        cp1 = control_points[target_curve + 1]
        g1 = control_points[target_curve + 2] if target_curve + 2 < len(control_points) else cp1 + cp1 - cp0
        ip0 = (cp1 + g0) / 2
        ip1 = (cp0 + g1) / 2
        ip0 = cp0 + cp1 - ip0
        ip1 = cp1 + cp0 - ip1
        return compute_bezier(math.fmod(t * (len(control_points) - 1), 1.), [cp0, ip0, ip1, cp1])


if __name__ == '__main__':
    import turtle as tr
    size = 30
    turtle_tool = tr.Turtle()
    turtle_tool.speed(10)
    turtle_tool.up()

    points = numpy.array([[0., 1.], [1, -1], [2, -3], [3, -1]])*100

    for point in points:
        turtle_tool.goto(point)
        turtle_tool.dot(5, "red")

    for i in range(size):
        t = i/size
        point = compute_catmul(t, points)
        turtle_tool.goto(point)
        turtle_tool.dot()
        print(point)

    turtle_tool.goto(100000, 100000)
    turtle_tool.dot()
    tr.done()
