from demo import Demo


def test_demo(qtbot):
    window = Demo()
    window.show()
    qtbot.addWidget(window)
