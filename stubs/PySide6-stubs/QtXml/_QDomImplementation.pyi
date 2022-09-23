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
PySide6.QtXml, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from enum import IntFlag
from typing import overload

import PySide6.QtCore
import PySide6.QtXml

class QDomImplementation:
    """
    https://doc.qt.io/qt-6/qdomimplementation.html

    **Detailed Description**

    This class describes the features that are supported by the DOM
    implementation. Currently the XML subset of DOM Level 1 and DOM Level 2 Core
    are supported.

    Normally you will use the function **QDomDocument::implementation** () to
    get the implementation object.

    You can create a new document type with **createDocumentType** () and a new
    document with **createDocument** ().

    For further information about the Document Object Model see **Level 1**  and
    **Level 2 Core** . For a more general introduction of the DOM implementation
    see the **QDomDocument**  documentation.

    The QDom classes have a few issues of nonconformance with the XML
    specifications that cannot be fixed in Qt 4 without breaking backward
    compatibility. The Qt XML Patterns module and the **QXmlStreamReader**  and
    **QXmlStreamWriter**  classes have a higher degree of a conformance.

    **See also** **hasFeature** ().
    """

    AcceptInvalidChars: QDomImplementation.InvalidDataPolicy = ...
    DropInvalidChars: QDomImplementation.InvalidDataPolicy = ...
    ReturnNullNode: QDomImplementation.InvalidDataPolicy = ...

    class InvalidDataPolicy(IntFlag):
        AcceptInvalidChars: QDomImplementation.InvalidDataPolicy = ...
        DropInvalidChars: QDomImplementation.InvalidDataPolicy = ...
        ReturnNullNode: QDomImplementation.InvalidDataPolicy = ...
    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qdomimplementation.html#QDomImplementation

        **QDomImplementation::QDomImplementation()**

        Constructs a QDomImplementation object.
        """
        ...
    @overload
    def __init__(self, arg__1: PySide6.QtXml.QDomImplementation) -> None:
        """
        https://doc.qt.io/qt-6/qdomimplementation.html#QDomImplementation-1

        **QDomImplementation::QDomImplementation(const QDomImplementation & x
        )**

        Constructs a copy of **x**.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def createDocument(
        self, nsURI: str, qName: str, doctype: PySide6.QtXml.QDomDocumentType
    ) -> PySide6.QtXml.QDomDocument:
        """
        https://doc.qt.io/qt-6/qdomimplementation.html#createDocument

        **QDomDocument QDomImplementation::createDocument(const QString & nsURI
        , const QString & qName , const QDomDocumentType & doctype )**

        Creates a DOM document with the document type **doctype**. This function
        also adds a root element node with the qualified name **qName** and the
        namespace URI **nsURI**.
        """
        ...
    def createDocumentType(
        self, qName: str, publicId: str, systemId: str
    ) -> PySide6.QtXml.QDomDocumentType:
        """
        https://doc.qt.io/qt-6/qdomimplementation.html#createDocumentType

        **QDomDocumentType QDomImplementation::createDocumentType(const QString
        & qName , const QString & publicId , const QString & systemId )**

        Creates a document type node for the name **qName**.

        **publicId** specifies the public identifier of the external subset. If
        you specify an empty string (QString()) as the **publicId** , this means
        that the document type has no public identifier.

        **systemId** specifies the system identifier of the external subset. If
        you specify an empty string as the **systemId** , this means that the
        document type has no system identifier.

        Since you cannot have a public identifier without a system identifier,
        the public identifier is set to an empty string if there is no system
        identifier.

        DOM level 2 does not support any other document type declaration
        features.

        The only way you can use a document type that was created this way, is
        in combination with the **createDocument** () function to create a
        **QDomDocument**  with this document type.

        In the DOM specification, this is the only way to create a non-null
        document. For historical reasons, Qt also allows to create the document
        using the default empty constructor. The resulting document is null, but
        becomes non-null when a factory function, for example
        **QDomDocument::createElement** (), is called. The document also becomes
        non-null when setContent() is called.

        **See also** **createDocument** ().
        """
        ...
    def hasFeature(self, feature: str, version: str) -> bool:
        """
        https://doc.qt.io/qt-6/qdomimplementation.html#hasFeature

        **bool QDomImplementation::hasFeature(const QString & feature , const
        QString & version ) const**

        The function returns `true` if QDom implements the requested **version**
        of a **feature** ; otherwise returns `false`.

        The currently supported features and their versions:

        FeatureVersion
        XML1.0
        """
        ...
    @staticmethod
    def invalidDataPolicy() -> PySide6.QtXml.QDomImplementation.InvalidDataPolicy:
        """
        https://doc.qt.io/qt-6/qdomimplementation.html#invalidDataPolicy

        **[static] QDomImplementation::InvalidDataPolicy
        QDomImplementation::invalidDataPolicy()**

        Returns the invalid data policy, which specifies what should be done
        when a factory function in **QDomDocument**  is passed invalid data.

        **Warning:** This function is not **reentrant** .

        **See also** **setInvalidDataPolicy** () and **InvalidDataPolicy** .
        """
        ...
    def isNull(self) -> bool:
        """
        https://doc.qt.io/qt-6/qdomimplementation.html#isNull

        **bool QDomImplementation::isNull()**

        Returns `false` if the object was created by
        **QDomDocument::implementation** (); otherwise returns `true`.
        """
        ...
    @staticmethod
    def setInvalidDataPolicy(
        policy: PySide6.QtXml.QDomImplementation.InvalidDataPolicy,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qdomimplementation.html#setInvalidDataPolicy

        **[static] void QDomImplementation::setInvalidDataPolicy(QDomImplementat
        ion::InvalidDataPolicy policy )**

        Sets the invalid data policy, which specifies what should be done when a
        factory function in **QDomDocument**  is passed invalid data.

        The **policy** is set for all instances of **QDomDocument**  which
        already exist and which will be created in the future.

        void XML_snippet_main()
            {
            **QDomDocument**  doc;
        **QDomImplementation**  impl;
            // This will create the element, but
        the resulting XML document will
            // be invalid, because '~' is not a
        valid character in a tag name.
        impl.setInvalidDataPolicy(**QDomImplementation** ::AcceptInvalidChars);
        **QDomElement**  elt1 = doc.createElement("foo~bar");

            // This
        will create an element with the tag name "foobar".
        impl.setInvalidDataPolicy(**QDomImplementation** ::DropInvalidChars);
        **QDomElement**  elt2 = doc.createElement("foo~bar");

            // This
        will create a null element.
        impl.setInvalidDataPolicy(**QDomImplementation** ::ReturnNullNode);
        **QDomElement**  elt3 = doc.createElement("foo~bar");
            }

        **Warning:** This function is not **reentrant** .

        **See also** **invalidDataPolicy** () and **InvalidDataPolicy** .
        """
        ...
