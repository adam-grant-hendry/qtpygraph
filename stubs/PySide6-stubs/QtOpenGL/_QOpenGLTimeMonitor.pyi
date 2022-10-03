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
PySide6.QtOpenGL, except for defaults which are replaced by "...".
"""

from __future__ import annotations

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtOpenGL

class QOpenGLTimeMonitor(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qopengltimemonitor.html

    **Detailed Description**

    The QOpenGLTimeMonitor class is a convenience wrapper around a collection of
    OpenGL timer query objects used to measure intervals of time on the GPU to
    the level of granularity required by your rendering application.

    The OpenGL timer queries objects are queried in sequence to record the GPU
    timestamps at positions of interest in your rendering code. Once the results
    for all issues timer queries become available, the results can be fetched
    and QOpenGLTimerMonitor will calculate the recorded time intervals for you.

    The typical use case of this class is to either profile your application's
    rendering algorithms or to adjust those algorithms in real-time for dynamic
    performance/quality balancing.

    Prior to using QOpenGLTimeMonitor in your rendering function you should set
    the required number of sample points that you wish to record by calling
    setSamples(). Note that measuring N sample points will produce N-1 time
    intervals. Once you have set the number of sample points, call the
    **create** () function with a valid current OpenGL context to create the
    necessary query timer objects. These steps are usually performed just once
    in an initialization function.

    Use the **recordSample** () function to delimit blocks of code containing
    OpenGL commands that you wish to time. You can check availability of the
    resulting time samples and time intervals with **isResultAvailable** (). The
    calculated time intervals and the raw timestamp samples can be retrieved
    with the blocking **waitForIntervals** () and **waitForSamples** ()
    functions respectively.

    After retrieving the results and before starting a new round of taking
    samples (for example, in the next frame) be sure to call the **reset** ()
    function which will clear the cached results and reset the timer index back
    to the first timer object.

    **See also** **QOpenGLTimerQuery** .
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qopengltimemonitor.html#QOpenGLTimeMonitor

        **QOpenGLTimeMonitor::QOpenGLTimeMonitor(QObject * parent = nullptr)**

        Creates a QOpenGLTimeMonitor instance with the given **parent**. You
        must call **create** () with a valid OpenGL context before using.

        **See also** **setSampleCount** () and **create** ().
        """
        ...
    def create(self) -> bool:
        """
        https://doc.qt.io/qt-6/qopengltimemonitor.html#create

        **bool QOpenGLTimeMonitor::create()**

        Instantiate **sampleCount** () OpenGL timer query objects that will be
        used to track the amount of time taken to execute OpenGL commands
        between successive calls to **recordSample** ().

        Returns `true` if the OpenGL timer query objects could be created.

        **See also** **destroy** (), **setSampleCount** (), and **recordSample**
        ().
        """
        ...
    def destroy(self) -> None:
        """
        https://doc.qt.io/qt-6/qopengltimemonitor.html#destroy

        **void QOpenGLTimeMonitor::destroy()**

        Destroys any OpenGL timer query objects used within this instance.

        **See also** **create** ().
        """
        ...
    def isCreated(self) -> bool:
        """
        https://doc.qt.io/qt-6/qopengltimemonitor.html#isCreated

        **bool QOpenGLTimeMonitor::isCreated() const**

        Returns `true` if the underlying OpenGL query objects have been created.
        If this returns `true` and the associated OpenGL context is current,
        then you are able to record time samples with this object.
        """
        ...
    def isResultAvailable(self) -> bool:
        """
        https://doc.qt.io/qt-6/qopengltimemonitor.html#isResultAvailable

        **bool QOpenGLTimeMonitor::isResultAvailable() const**

        Returns `true` if the OpenGL timer query results are available.

        **See also** **waitForSamples** () and **waitForIntervals** ().
        """
        ...
    def objectIds(self) -> list[int]:
        """
        https://doc.qt.io/qt-6/qopengltimemonitor.html#objectIds

        **QList<GLuint> QOpenGLTimeMonitor::objectIds() const**

        Returns a **QList**  containing the object Ids of the OpenGL timer query
        objects.
        """
        ...
    def recordSample(self) -> int:
        """
        https://doc.qt.io/qt-6/qopengltimemonitor.html#recordSample

        **int QOpenGLTimeMonitor::recordSample()**

        Issues an OpenGL timer query at this point in the OpenGL command queue.
        Calling this function in a sequence in your application's rendering
        function, will build up details of the GPU time taken to execute the
        OpenGL commands between successive calls to this function.

        **See also** **setSampleCount** (), **isResultAvailable** (),
        **waitForSamples** (), and **waitForIntervals** ().
        """
        ...
    def reset(self) -> None:
        """
        https://doc.qt.io/qt-6/qopengltimemonitor.html#reset

        **void QOpenGLTimeMonitor::reset()**

        Resets the time monitor ready for use in another frame of rendering.
        Call this once you have obtained the previous results and before calling
        **recordSample** () for the first time on the next frame.

        **See also** **recordSample** ().
        """
        ...
    def sampleCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qopengltimemonitor.html#sampleCount

        **int QOpenGLTimeMonitor::sampleCount() const**

        Returns the number of sample points that have been requested with
        **setSampleCount** (). If create was successfully called following
        **setSampleCount** (), then the value returned will be the actual number
        of sample points that can be used.

        The default value for sample count is 2, leading to the measurement of a
        single interval.

        **See also** **setSampleCount** ().
        """
        ...
    def setSampleCount(self, sampleCount: int) -> None:
        """
        https://doc.qt.io/qt-6/qopengltimemonitor.html#setSampleCount

        **void QOpenGLTimeMonitor::setSampleCount(int sampleCount )**

        Sets the number of sample points to **sampleCount**. After setting the
        number of samples with this function, you must call **create** () to
        instantiate the underlying OpenGL timer query objects.

        The new **sampleCount** must be at least 2.

        **See also** **sampleCount** (), **create** (), and **recordSample** ().
        """
        ...
    def waitForIntervals(self) -> list[int]:
        """
        https://doc.qt.io/qt-6/qopengltimemonitor.html#waitForIntervals

        **QList<GLuint64> QOpenGLTimeMonitor::waitForIntervals() const**

        Returns a **QList**  containing the time intervals delimited by the
        calls to **recordSample** (). The resulting vector will contain one
        fewer element as this represents the intervening intervals rather than
        the actual timestamp samples.

        This function will block until OpenGL indicates the results are
        available. It is recommended to check the availability of the result
        prior to calling this function with **isResultAvailable** ().

        **See also** **waitForSamples** () and **isResultAvailable** ().
        """
        ...
    def waitForSamples(self) -> list[int]:
        """
        https://doc.qt.io/qt-6/qopengltimemonitor.html#waitForSamples

        **QList<GLuint64> QOpenGLTimeMonitor::waitForSamples() const**

        Returns a **QList**  containing the GPU timestamps taken with
        **recordSample** ().

        This function will block until OpenGL indicates the results are
        available. It is recommended to check the availability of the result
        prior to calling this function with **isResultAvailable** ().

        **Note:** This function only works on systems that have OpenGL >=3.3 or
        the ARB_timer_query extension. See **QOpenGLTimerQuery**  for more
        details.

        **See also** **waitForIntervals** () and **isResultAvailable** ().
        """
        ...