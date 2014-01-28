Flask-Color
===========

![](http://i.imgur.com/u5tLLho.png)

flask-color is an extension for Flask that improves the built-in web server with colors when debugging. Unnecessary clutter such as time or IP are hidden.

Installing
----------

You can install this using pip.

````$ pip install flask-color````

How to use
----------

There's an example of use in sample.py. Add two lines to your code:

```python
# Import this extension
import flask.ext.color

# Initialize extension with your app.
flask.ext.color.init_app(app)
```

Flask configuration *DEBUG* must be True for this extension to function. You can override this by setting *COLOR_ALWAYS_ON* true.

Configuration
-------------

- *COLOR_ALWAYS_ON*: Force extension on even if not in DEBUG mode
- *COLOR_PATTERN_GRAY*: Regular expression that matches static file requests (these requests are marked with gray color)
