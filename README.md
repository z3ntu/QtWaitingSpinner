# QtWaitingSpinner

QtWaitingSpinner is a highly configurable, custom Qt widget for showing "waiting" or "loading" spinner icons in Qt applications, e.g. the spinners below are all QtWaitingSpinner widgets differing only in their configuration:

![waiting spinner](https://github.com/z3ntu/QtWaitingSpinner/blob/gh-pages/waiting-spinners.gif)

### Configuration

The following properties can all be controlled directly through their corresponding setters:

* Color of the widget
* "Roundness" of the lines
* Speed (rotations per second)
* Number of lines to be drawn
* Line length
* Line width
* Radius of the spinner's "dead space" or inner circle
* The percentage fade of the "trail"
* The minimum opacity of the "trail"

This project uses the [qtpy](https://github.com/spyder-ide/qtpy) abstraction layer to support PyQt6, PyQt5, PySide6, and PySide2 backends.

### Usage

Despite being highly configurable, QtWaitingSpinner is extremely easy to use and, to make things even easier, the "QtWaitingSpinnerTest" application can assist you in determining the exact shape, size and color you'd like your spinner to have.

For example, the embedded spinner in the QtWaitingSpinnerTest screenshot below can be created as follows:

```python
from waitingspinnerwidget import QtWaitingSpinner

spinner = QtWaitingSpinner(self)

spinner.setRoundness(70.0)
spinner.setMinimumTrailOpacity(15.0)
spinner.setTrailFadePercentage(70.0)
spinner.setNumberOfLines(12)
spinner.setLineLength(10)
spinner.setLineWidth(5)
spinner.setInnerRadius(10)
spinner.setRevolutionsPerSecond(1)
spinner.setColor(QColor(81, 4, 71))

spinner.start()
```

A demo is included with the `demo.py` file.

![demo dialog](https://github.com/z3ntu/QtWaitingSpinner/blob/gh-pages/test-dialog.png)

As an alternative example, the code below will create a spinner that (1) blocks all user input to the main application for as long as the spinner is active, (2) automatically centers itself on its parent widget every time "start" is called and (3) makes use of the default shape, size and color settings.

```python
spinner = QtWaitingSpinner(self, True, True, Qt.ApplicationModal)
spinner.start() # starts spinning
```

Please use [use this link](https://github.com/z3ntu/QtWaitingSpinner/issues) for feedback, requests or issues.

Enjoy!

### Thanks:
to [@snowwlex](https://github.com/snowwlex) for the base of my port (and this README)!

QtWaitingSpinner was inspired by the [spin.js](http://fgnass.github.io/spin.js/)  project.
