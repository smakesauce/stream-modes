# TODO


* Implement a command that transitions to focus mode.
    - Start the countdown timer.
    - Change the mode display on the statusline.
- Implement a command that transitions to vibe mode.
    - Hide timer.
    - Change the mode display.
- Implement a command that updates the statusline text.
- Automatically push state changes to widget.

## MVP spec

The MVP for this project is an HTML widget that possesses the features
enumerated below. The widget will be connected via a websocket to a
backend service that provides an API for cool stuff.

* mode name
    - for now, just "focus" and "vibe" mode
* timer
    - would be nice if it made a noise upon expiration so that i notice
* display arbitrary text
    - just something to provide whatever context i feel necessary
    - im thinking sometimes ill input a ! chat command that further
      explains the task and project being worked on.

* technology
    - client
        * curl
    - api backend
        * flask
            - lightweight
            - theoretically accessible to more people on twitch than ruby (disaster_robot's primary proficiency)
    - widget ui
        * vanilla js
            - the widget is a pretty minor js implementation, prob
              doesnt warrent much more than vanilla js
### MVP API spec

* POST /widget
    - Create a widget
    - Args:
        * default_mode
        * timer_enabled
        * text

* POST /widgets/:widget_uuid
    - Update a widget
    - Args:
        * text
        * mode

* POST /widgets/:widget_uuid/timer/start
* POST /widgets/:widget_uuid/timer/stop

## 1.0+ ideas

* Analytics on widget state change
* Web sockets
* Automatic mode transitions
* for things like !project, allow viewers to hover the command to see the
command's actual text output without sending it in chat. for an example
of a plugin that allows viewers to interact with the stream window
see cardboardlive for magic the gathering which allows viewers to hover
their mouse over a card on the stream and see a popup showing an
enlarged version of the card.
* Somehow encourage chat to converse amongst themselves similar to what happens in a Bob Ross stream.
