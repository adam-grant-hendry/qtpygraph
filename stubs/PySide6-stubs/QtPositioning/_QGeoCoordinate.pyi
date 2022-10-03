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
PySide6.QtPositioning, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from enum import IntFlag
from typing import overload

import PySide6.QtCore
import PySide6.QtPositioning

class QGeoCoordinate:
    """
    https://doc.qt.io/qt-6/qgeocoordinate.html

    **Detailed Description**

    A QGeoCoordinate is defined by latitude, longitude, and optionally,
    altitude.

    Use **type** () to determine whether a coordinate is a 2D coordinate (has
    latitude and longitude only) or 3D coordinate (has latitude, longitude and
    altitude). Use **distanceTo** () and **azimuthTo** () to calculate the
    distance and bearing between coordinates.

    The coordinate values should be specified using the WGS84 datum. For more
    information on geographical terms see this article on **coordinates**  and
    another on **geodetic systems**  including WGS84.

    Azimuth in this context is equivalent to a compass bearing based on true
    north.

    This class is a **Q_GADGET**  since Qt 5.5. It can be **directly used from
    C++ and QML** .
    """

    Degrees: QGeoCoordinate.CoordinateFormat = ...
    DegreesWithHemisphere: QGeoCoordinate.CoordinateFormat = ...
    DegreesMinutes: QGeoCoordinate.CoordinateFormat = ...
    DegreesMinutesWithHemisphere: QGeoCoordinate.CoordinateFormat = ...
    DegreesMinutesSeconds: QGeoCoordinate.CoordinateFormat = ...
    DegreesMinutesSecondsWithHemisphere: QGeoCoordinate.CoordinateFormat = ...
    InvalidCoordinate: QGeoCoordinate.CoordinateType = ...
    Coordinate2D: QGeoCoordinate.CoordinateType = ...
    Coordinate3D: QGeoCoordinate.CoordinateType = ...

    class CoordinateFormat(IntFlag):
        Degrees: QGeoCoordinate.CoordinateFormat = ...
        DegreesWithHemisphere: QGeoCoordinate.CoordinateFormat = ...
        DegreesMinutes: QGeoCoordinate.CoordinateFormat = ...
        DegreesMinutesWithHemisphere: QGeoCoordinate.CoordinateFormat = ...
        DegreesMinutesSeconds: QGeoCoordinate.CoordinateFormat = ...
        DegreesMinutesSecondsWithHemisphere: QGeoCoordinate.CoordinateFormat = ...

    class CoordinateType(IntFlag):
        InvalidCoordinate: QGeoCoordinate.CoordinateType = ...
        Coordinate2D: QGeoCoordinate.CoordinateType = ...
        Coordinate3D: QGeoCoordinate.CoordinateType = ...
    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qgeocoordinate.html#QGeoCoordinate

        **QGeoCoordinate::QGeoCoordinate()**

        Constructs a coordinate. The coordinate will be invalid until
        **setLatitude** () and **setLongitude** () have been called.
        """
        ...
    @overload
    def __init__(self, latitude: float, longitude: float) -> None:
        """
        https://doc.qt.io/qt-6/qgeocoordinate.html#QGeoCoordinate-1

        **QGeoCoordinate::QGeoCoordinate(double latitude , double longitude )**

        Constructs a coordinate with the given **latitude** and **longitude**.

        If the latitude is not between -90 to 90 inclusive, or the longitude is
        not between -180 to 180 inclusive, none of the values are set and the
        **type** () will be **QGeoCoordinate::InvalidCoordinate** .

        **See also** **isValid** ().
        """
        ...
    @overload
    def __init__(self, latitude: float, longitude: float, altitude: float) -> None:
        """
        https://doc.qt.io/qt-6/qgeocoordinate.html#QGeoCoordinate-2

        **QGeoCoordinate::QGeoCoordinate(double latitude , double longitude ,
        double altitude )**

        Constructs a coordinate with the given **latitude** , **longitude** and
        **altitude**.

        If the latitude is not between -90 to 90 inclusive, or the longitude is
        not between -180 to 180 inclusive, none of the values are set and the
        **type** () will be **QGeoCoordinate::InvalidCoordinate** .

        Note that **altitude** specifies the meters above sea level.

        **See also** **isValid** ().
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtPositioning.QGeoCoordinate) -> None:
        """
        https://doc.qt.io/qt-6/qgeocoordinate.html#QGeoCoordinate-3

        **QGeoCoordinate::QGeoCoordinate(const QGeoCoordinate & other )**

        Constructs a coordinate from the contents of **other**.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def __lshift__(
        self, stream: PySide6.QtCore.QDataStream
    ) -> PySide6.QtCore.QDataStream: ...
    def __rshift__(
        self, stream: PySide6.QtCore.QDataStream
    ) -> PySide6.QtCore.QDataStream: ...
    def altitude(self) -> float:
        """
        https://doc.qt.io/qt-6/qgeocoordinate.html#altitude

        **double QGeoCoordinate::altitude() const**

        Returns the altitude (meters above sea level).

        The return value is undefined if the altitude has not been set.

        **Note:** Getter function for property **altitude** .

        **See also** **setAltitude** () and **type** ().
        """
        ...
    def atDistanceAndAzimuth(
        self, distance: float, azimuth: float, distanceUp: float = ...
    ) -> PySide6.QtPositioning.QGeoCoordinate:
        """
        https://doc.qt.io/qt-6/qgeocoordinate.html#atDistanceAndAzimuth

        **[invokable] QGeoCoordinate QGeoCoordinate::atDistanceAndAzimuth(qreal
        distance , qreal azimuth , qreal distanceUp = 0.0) const**

        Returns the coordinate that is reached by traveling **distance** meters
        from the current coordinate at **azimuth** (or bearing) along a great-
        circle. There is an assumption that the Earth is spherical for the
        purpose of this calculation.

        The altitude will have **distanceUp** added to it.

        Returns an invalid coordinate if this coordinate is invalid.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def azimuthTo(self, other: PySide6.QtPositioning.QGeoCoordinate) -> float:
        """
        https://doc.qt.io/qt-6/qgeocoordinate.html#azimuthTo

        **[invokable] qreal QGeoCoordinate::azimuthTo(const QGeoCoordinate &
        other ) const**

        Returns the azimuth (or bearing) in degrees from this coordinate to the
        coordinate specified by **other**. Altitude is not used in the
        calculation.

        The bearing returned is the bearing from the origin to **other** along
        the great-circle between the two coordinates. There is an assumption
        that the Earth is spherical for the purpose of this calculation.

        Returns 0 if the type of this coordinate or the type of **other** is
        **QGeoCoordinate::InvalidCoordinate** .

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def distanceTo(self, other: PySide6.QtPositioning.QGeoCoordinate) -> float:
        """
        https://doc.qt.io/qt-6/qgeocoordinate.html#distanceTo

        **[invokable] qreal QGeoCoordinate::distanceTo(const QGeoCoordinate &
        other ) const**

        Returns the distance (in meters) from this coordinate to the coordinate
        specified by **other**. Altitude is not used in the calculation.

        This calculation returns the great-circle distance between the two
        coordinates, with an assumption that the Earth is spherical for the
        purpose of this calculation.

        Returns 0 if the type of this coordinate or the type of **other** is
        **QGeoCoordinate::InvalidCoordinate** .

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def isValid(self) -> bool:
        """
        https://doc.qt.io/qt-6/qgeocoordinate.html#isValid

        **bool QGeoCoordinate::isValid() const**

        Returns `true` if the **longitude**  and **latitude**  are valid.

        **Note:** Getter function for property **isValid** .
        """
        ...
    def latitude(self) -> float:
        """
        https://doc.qt.io/qt-6/qgeocoordinate.html#latitude

        **double QGeoCoordinate::latitude() const**

        Returns the latitude, in decimal degrees. The return value is undefined
        if the latitude has not been set.

        A positive latitude indicates the Northern Hemisphere, and a negative
        latitude indicates the Southern Hemisphere.

        **Note:** Getter function for property **latitude** .

        **See also** **setLatitude** () and **type** ().
        """
        ...
    def longitude(self) -> float:
        """
        https://doc.qt.io/qt-6/qgeocoordinate.html#longitude

        **double QGeoCoordinate::longitude() const**

        Returns the longitude, in decimal degrees. The return value is undefined
        if the longitude has not been set.

        A positive longitude indicates the Eastern Hemisphere, and a negative
        longitude indicates the Western Hemisphere.

        **Note:** Getter function for property **longitude** .

        **See also** **setLongitude** () and **type** ().
        """
        ...
    def setAltitude(self, altitude: float) -> None:
        """
        https://doc.qt.io/qt-6/qgeocoordinate.html#setAltitude

        **void QGeoCoordinate::setAltitude(double altitude )**

        Sets the altitude (meters above sea level) to **altitude**.

        **Note:** Setter function for property **altitude** .

        **See also** **altitude** ().
        """
        ...
    def setLatitude(self, latitude: float) -> None:
        """
        https://doc.qt.io/qt-6/qgeocoordinate.html#setLatitude

        **void QGeoCoordinate::setLatitude(double latitude )**

        Sets the latitude (in decimal degrees) to **latitude**. The value should
        be in the WGS84 datum.

        To be valid, the latitude must be between -90 to 90 inclusive.

        **Note:** Setter function for property **latitude** .

        **See also** **latitude** ().
        """
        ...
    def setLongitude(self, longitude: float) -> None:
        """
        https://doc.qt.io/qt-6/qgeocoordinate.html#setLongitude

        **void QGeoCoordinate::setLongitude(double longitude )**

        Sets the longitude (in decimal degrees) to **longitude**. The value
        should be in the WGS84 datum.

        To be valid, the longitude must be between -180 to 180 inclusive.

        **Note:** Setter function for property **longitude** .

        **See also** **longitude** ().
        """
        ...
    def swap(self, other: PySide6.QtPositioning.QGeoCoordinate) -> None: ...
    def toString(
        self, format: PySide6.QtPositioning.QGeoCoordinate.CoordinateFormat = ...
    ) -> str:
        """
        https://doc.qt.io/qt-6/qgeocoordinate.html#toString

        **[invokable] QString
        QGeoCoordinate::toString(QGeoCoordinate::CoordinateFormat format =
        DegreesMinutesSecondsWithHemisphere) const**

        Returns this coordinate as a string in the specified **format**.

        For example, if this coordinate has a latitude of -27.46758, a longitude
        of 153.027892 and an altitude of 28.1, these are the strings returned
        depending on **format** :

        **format** valueReturned string
        **Degrees** -27.46758°, 153.02789°,
        28.1m
        **DegreesWithHemisphere** 27.46758° S, 153.02789° E, 28.1m
        **DegreesMinutes** -27° 28.054', 153° 1.673', 28.1m
        **DegreesMinutesWithHemisphere** 27° 28.054 S', 153° 1.673' E, 28.1m
        **DegreesMinutesSeconds** -27° 28' 3.2", 153° 1' 40.4", 28.1m
        **DegreesMinutesSecondsWithHemisphere** 27° 28' 3.2" S, 153° 1' 40.4" E,
        28.1m

        The altitude field is omitted if no altitude is set.

        If the coordinate is invalid, an empty string is returned.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def type(self) -> PySide6.QtPositioning.QGeoCoordinate.CoordinateType:
        """
        https://doc.qt.io/qt-6/qgeocoordinate.html#type

        **QGeoCoordinate::CoordinateType QGeoCoordinate::type() const**

        Returns the type of this coordinate.
        """
        ...