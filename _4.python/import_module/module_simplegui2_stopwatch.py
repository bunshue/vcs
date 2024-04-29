import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # type: ignore

simplegui.Frame._hide_status = True  # pylint: disable=protected-access
simplegui.Frame._keep_timers = False  # pylint: disable=protected-access


# Global constants
CANVAS_WIDTH = 350
CANVAS_HEIGHT = 220


# Global variables
NB_ATTEMPTS = 0
NB_SUCCESS = 0

TIME = 0


# Helper function
def format_time(decisecond):  # type: (int) -> str
    """
    Convert time in tenths of seconds
    into formatted string m:ss.t

    :param decisecond: int >= 0

    :return: str
    """
    assert isinstance(decisecond, int)
    assert decisecond >= 0

    decisecond, tenths = decisecond // 10, decisecond % 10
    minutes, seconds = decisecond // 60, decisecond % 60

    return "%d:%02d.%d" % (minutes, seconds, tenths)


# Event handlers for buttons
def quit_prog():  # type: () -> None
    """Stop timer and quit."""
    TIMER.stop()
    FRAME.stop()


def reset():  # type: () -> None
    """
    Reinit NB_ATTEMPTS, NB_SUCCESS and time
    and stop timer
    """
    global NB_ATTEMPTS  # pylint: disable=global-statement
    global NB_SUCCESS  # pylint: disable=global-statement
    global TIME  # pylint: disable=global-statement

    TIMER.stop()

    NB_ATTEMPTS = 0
    NB_SUCCESS = 0

    TIME = 0


def start():  # type: () -> None
    """Start timer"""
    TIMER.start()


def stop():  # type: () -> None
    """
    If timer is running
    then stop timer
    and increment NB_ATTEMPTS
    and if time is multiple of 10 then increment NB_SUCCESS
    """
    global NB_ATTEMPTS  # pylint: disable=global-statement
    global NB_SUCCESS  # pylint: disable=global-statement

    if TIMER.is_running():
        TIMER.stop()

        NB_ATTEMPTS += 1
        if TIME % 10 == 0:
            NB_SUCCESS += 1


# Event handler for timer
def tick():  # type: () -> None
    """Increment TIME"""
    global TIME  # pylint: disable=global-statement

    TIME += 1


# Draw handler
def draw(canvas):  # type: (simplegui.Canvas) -> None
    """
    Display TIME in center
    and display NB_SUCCESS / NB_ATTEMPTS on upper-right

    :param canvas: simplegui.Canvas
    """
    text = format_time(TIME)
    size = 60
    width = FRAME.get_canvas_textwidth(text, size, "monospace")
    canvas.draw_text(
        text,
        (
            (CANVAS_WIDTH - width) // 2,
            # (CANVAS_HEIGHT - size) // 2 + size * 3 // 4
            (CANVAS_HEIGHT * 2 + size) // 4,
        ),
        size,
        "Lime",
        "monospace",
    )

    if NB_ATTEMPTS > 0:
        text = "%d/%d" % (NB_SUCCESS, NB_ATTEMPTS)
        percent_success = NB_SUCCESS * 100 // NB_ATTEMPTS
        size = 30 if NB_SUCCESS == NB_ATTEMPTS else 20
        width = FRAME.get_canvas_textwidth(text, size, "monospace")
        canvas.draw_text(
            text,
            (CANVAS_WIDTH - width * 5 // 4, size),
            size,
            (
                "Red"
                if percent_success < 25
                else ("Yellow" if percent_success >= 75 else "White")
            ),
            "monospace",
        )

    if TIMER.is_running():
        text = "Stop the timer when 0 decisecond."
        size = 20
        width = FRAME.get_canvas_textwidth(text, size)
        canvas.draw_text(
            text, ((CANVAS_WIDTH - width) // 2, (CANVAS_HEIGHT - size)), size, "White"
        )


# Create frame
FRAME = simplegui.create_frame(
    "Stopwatch (Stop the timer when 0 decisecond)", CANVAS_WIDTH, CANVAS_HEIGHT, 100
)


# Register event handlers
FRAME.add_button("Start", start, 100)
FRAME.add_label("")
FRAME.add_button("Stop", stop, 100)
FRAME.add_label("")
FRAME.add_button("Reset", reset, 100)
FRAME.add_label("")
FRAME.add_button("Quit", quit_prog)

FRAME.set_draw_handler(draw)

TIMER = simplegui.create_timer(100, tick)


# Main
assert format_time(0) == "0:00.0"
assert format_time(3) == "0:00.3"
assert format_time(11) == "0:01.1"
assert format_time(321) == "0:32.1"
assert format_time(613) == "1:01.3"
assert format_time(1234) == "2:03.4"

FRAME.start()
