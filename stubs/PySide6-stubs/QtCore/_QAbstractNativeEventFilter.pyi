"""
PySide stub files generated by **IceSpringPySideStubs**

Home: https://baijifeilong.github.io/2022/01/06/ice-spring-pyside-stubs/index.html

Github: https://github.com/baijifeilong/IceSpringPySideStubs

PyPI(PySide2): https://pypi.org/project/IceSpringPySideStubs-PySide2

PyPI(PySide6): https://pypi.org/project/IceSpringPySideStubs-PySide6

PyPI(PyQt5): https://pypi.org/project/IceSpringPySideStubs-PyQt5

PyPI(PyQt6): https://pypi.org/project/IceSpringPySideStubs-PyQt6

Generated by BaiJiFeiLong@gmail.com

License: MIT
"""
"""
This file contains the exact signatures for all functions in module
PySide6.QtCore, except for defaults which are replaced by "...".
"""

from __future__ import annotations

import PySide6.QtCore

class QAbstractNativeEventFilter:
    """
    https://doc.qt.io/qt-6/qabstractnativeeventfilter.html

    **Detailed Description**
    """

    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qabstractnativeeventfilter.html#QAbstractNativeEv
        entFilter

        **QAbstractNativeEventFilter::QAbstractNativeEventFilter()**

        Creates a native event filter.

        By default this doesn't do anything. Remember to install it on the
        application object.
        """
        ...
    def nativeEventFilter(
        self, eventType: PySide6.QtCore.QByteArray | bytes, message: int
    ) -> tuple[object, int]:
        """
        https://doc.qt.io/qt-6/qabstractnativeeventfilter.html#nativeEventFilter

        **[pure virtual] bool
        QAbstractNativeEventFilter::nativeEventFilter(const QByteArray &
        eventType , void * message , qintptr * result )**

        This method is called for every native event.

        **Note:** The filter function here receives native messages, for
        example, MSG or XCB event structs.

        It is called by the QPA platform plugin. On Windows, it is called by the
        event dispatcher.

        The type of event **eventType** is specific to the platform plugin
        chosen at run-time, and can be used to cast **message** to the right
        type.

        On X11, **eventType** is set to "xcb_generic_event_t", and the
        **message** can be casted to a xcb_generic_event_t pointer.

        On Windows, **eventType** is set to "windows_generic_MSG" for messages
        sent to toplevel windows, and "windows_dispatcher_MSG" for system-wide
        messages such as messages from a registered hot key. In both cases, the
        **message** can be casted to a MSG pointer. The **result** pointer is
        only used on Windows, and corresponds to the LRESULT pointer.

        On macOS, **eventType** is set to "mac_generic_NSEvent", and the
        **message** can be casted to an NSEvent pointer.

        In your reimplementation of this function, if you want to filter the
        **message** out, i.e. stop it being handled further, return true;
        otherwise return false.

        **Linux example**

        class MyXcbEventFilter : public **QAbstractNativeEventFilter**
            {
        public:
                bool nativeEventFilter(const **QByteArray**  &eventType,
        void *message, long *) override
                {
                    if (eventType ==
        "xcb_generic_event_t") {
                        xcb_generic_event_t* ev =
        static_cast<xcb_generic_event_t \\*>(message);
                        // ...
        }
                    return false;
                }
            };

        **macOS example**

        mycocoaeventfilter.h:

        #include <QAbstractNativeEventFilter>

            class MyCocoaEventFilter
        : public **QAbstractNativeEventFilter**
            {
            public:
                bool
        nativeEventFilter(const **QByteArray**  &eventType, void *message, long
        *) override;
            };

        mycocoaeventfilter.mm:

        #include "mycocoaeventfilter.h"

            #import <AppKit/AppKit.h>
        bool CocoaNativeEventFilter::nativeEventFilter(const QByteArray
        &eventType, void *message, long *)
            {
                if (eventType ==
        "mac_generic_NSEvent") {
                    NSEvent *event =
        static_cast<NSEvent \\*>(message);
                    if ([event type] ==
        NSKeyDown) {
                        // Handle key event
        qDebug() << QString::fromNSString([event characters]);
                    }
        }
                return false;
            }

        myapp.pro:

        HEADERS += mycocoaeventfilter.h
            OBJECTIVE_SOURCES +=
        mycocoaeventfilter.mm
            LIBS += -framework AppKit
        """
        ...
