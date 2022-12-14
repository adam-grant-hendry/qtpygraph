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
PySide6.QtQuick, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from enum import IntFlag
from typing import overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtOpenGL
import PySide6.QtQml
import PySide6.QtQuick

class QSGNode:
    """
    https://doc.qt.io/qt-6/qsgnode.html

    **Detailed Description**

    The QSGNode class can be used as a child container. Children are added with
    the **appendChildNode** (), **prependChildNode** (),
    **insertChildNodeBefore** () and **insertChildNodeAfter** (). The order of
    nodes is important as geometry nodes are rendered according to their
    ordering in the scene graph.

    The scene graph nodes contains a mechanism to describe which parts of the
    scene has changed. This includes the combined matrices, accumulated opacity,
    changes to the node hierarchy, and so on. This information can be used for
    optimizations inside the scene graph renderer. For the renderer to properly
    render the nodes, it is important that users call **QSGNode::markDirty** ()
    with the correct flags when nodes are changed. Most of the functions on the
    node classes will implicitly call **markDirty** (). For example,
    **QSGNode::appendChildNode** () will call **markDirty** () passing in
    **QSGNode::DirtyNodeAdded** .

    If nodes change every frame, the **preprocess** () function can be used to
    apply changes to a node for every frame it is rendered. The use of
    **preprocess** () must be explicitly enabled by setting the
    **QSGNode::UsePreprocess**  flag on the node.

    The virtual **isSubtreeBlocked** () function can be used to disable a
    subtree all together. Nodes in a blocked subtree will not be preprocessed()
    and not rendered.

    **Note:** All classes with QSG prefix should be used solely on the scene
    graph's rendering thread. See **Scene Graph and Rendering**  for more
    information.
    """

    DirtyUsePreprocess: QSGNode.DirtyStateBit = ...
    DirtySubtreeBlocked: QSGNode.DirtyStateBit = ...
    DirtyMatrix: QSGNode.DirtyStateBit = ...
    DirtyNodeAdded: QSGNode.DirtyStateBit = ...
    DirtyNodeRemoved: QSGNode.DirtyStateBit = ...
    DirtyGeometry: QSGNode.DirtyStateBit = ...
    DirtyMaterial: QSGNode.DirtyStateBit = ...
    DirtyOpacity: QSGNode.DirtyStateBit = ...
    DirtyForceUpdate: QSGNode.DirtyStateBit = ...
    DirtyPropagationMask: QSGNode.DirtyStateBit = ...
    OwnedByParent: QSGNode.Flag = ...
    UsePreprocess: QSGNode.Flag = ...
    OwnsGeometry: QSGNode.Flag = ...
    OwnsMaterial: QSGNode.Flag = ...
    OwnsOpaqueMaterial: QSGNode.Flag = ...
    IsVisitableNode: QSGNode.Flag = ...
    BasicNodeType: QSGNode.NodeType = ...
    GeometryNodeType: QSGNode.NodeType = ...
    TransformNodeType: QSGNode.NodeType = ...
    ClipNodeType: QSGNode.NodeType = ...
    OpacityNodeType: QSGNode.NodeType = ...
    RootNodeType: QSGNode.NodeType = ...
    RenderNodeType: QSGNode.NodeType = ...

    class DirtyState: ...

    class DirtyStateBit(IntFlag):
        DirtyUsePreprocess: QSGNode.DirtyStateBit = ...
        DirtySubtreeBlocked: QSGNode.DirtyStateBit = ...
        DirtyMatrix: QSGNode.DirtyStateBit = ...
        DirtyNodeAdded: QSGNode.DirtyStateBit = ...
        DirtyNodeRemoved: QSGNode.DirtyStateBit = ...
        DirtyGeometry: QSGNode.DirtyStateBit = ...
        DirtyMaterial: QSGNode.DirtyStateBit = ...
        DirtyOpacity: QSGNode.DirtyStateBit = ...
        DirtyForceUpdate: QSGNode.DirtyStateBit = ...
        DirtyPropagationMask: QSGNode.DirtyStateBit = ...

    class Flag(IntFlag):
        OwnedByParent: QSGNode.Flag = ...
        UsePreprocess: QSGNode.Flag = ...
        OwnsGeometry: QSGNode.Flag = ...
        OwnsMaterial: QSGNode.Flag = ...
        OwnsOpaqueMaterial: QSGNode.Flag = ...
        IsVisitableNode: QSGNode.Flag = ...

    class Flags: ...

    class NodeType(IntFlag):
        BasicNodeType: QSGNode.NodeType = ...
        GeometryNodeType: QSGNode.NodeType = ...
        TransformNodeType: QSGNode.NodeType = ...
        ClipNodeType: QSGNode.NodeType = ...
        OpacityNodeType: QSGNode.NodeType = ...
        RootNodeType: QSGNode.NodeType = ...
        RenderNodeType: QSGNode.NodeType = ...
    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qsgnode.html#QSGNode

        **QSGNode::QSGNode()**

        Constructs a new node
        """
        ...
    @overload
    def __init__(self, type: PySide6.QtQuick.QSGNode.NodeType) -> None:
        """
        https://doc.qt.io/qt-6/qsgnode.html#QSGNode

        **QSGNode::QSGNode()**

        Constructs a new node
        """
        ...
    def appendChildNode(self, node: PySide6.QtQuick.QSGNode) -> None:
        """
        https://doc.qt.io/qt-6/qsgnode.html#appendChildNode

        **void QSGNode::appendChildNode(QSGNode * node )**

        Appends **node** to this node's list of children.

        Ordering of nodes is important as geometry nodes will be rendered in the
        order they are added to the scene graph.
        """
        ...
    def childAtIndex(self, i: int) -> PySide6.QtQuick.QSGNode:
        """
        https://doc.qt.io/qt-6/qsgnode.html#childAtIndex

        **QSGNode *QSGNode::childAtIndex(int i ) const**

        Returns the child at index **i**.

        Children are stored internally as a linked list, so iterating over the
        children via the index is suboptimal.
        """
        ...
    def childCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qsgnode.html#childCount

        **int QSGNode::childCount() const**

        Returns the number of child nodes.
        """
        ...
    def clearDirty(self) -> None: ...
    def dirtyState(self) -> PySide6.QtQuick.QSGNode.DirtyState: ...
    def firstChild(self) -> PySide6.QtQuick.QSGNode:
        """
        https://doc.qt.io/qt-6/qsgnode.html#firstChild

        **QSGNode *QSGNode::firstChild() const**

        Returns the first child of this node.

        The children are stored in a linked list.
        """
        ...
    def flags(self) -> PySide6.QtQuick.QSGNode.Flags:
        """
        https://doc.qt.io/qt-6/qsgnode.html#flags

        **QSGNode::Flags QSGNode::flags() const**

        Returns the set of flags for this node.

        **See also** **setFlags** ().
        """
        ...
    def insertChildNodeAfter(
        self, node: PySide6.QtQuick.QSGNode, after: PySide6.QtQuick.QSGNode
    ) -> None:
        """
        https://doc.qt.io/qt-6/qsgnode.html#insertChildNodeAfter

        **void QSGNode::insertChildNodeAfter(QSGNode * node , QSGNode * after
        )**

        Inserts **node** to this node's list of children after the node
        specified with **after**.

        Ordering of nodes is important as geometry nodes will be rendered in the
        order they are added to the scene graph.
        """
        ...
    def insertChildNodeBefore(
        self, node: PySide6.QtQuick.QSGNode, before: PySide6.QtQuick.QSGNode
    ) -> None:
        """
        https://doc.qt.io/qt-6/qsgnode.html#insertChildNodeBefore

        **void QSGNode::insertChildNodeBefore(QSGNode * node , QSGNode * before
        )**

        Inserts **node** to this node's list of children before the node
        specified with **before**.

        Ordering of nodes is important as geometry nodes will be rendered in the
        order they are added to the scene graph.
        """
        ...
    def isSubtreeBlocked(self) -> bool:
        """
        https://doc.qt.io/qt-6/qsgnode.html#isSubtreeBlocked

        **[virtual] bool QSGNode::isSubtreeBlocked() const**

        Returns whether this node and its subtree is available for use.

        Blocked subtrees will not get their dirty states updated and they will
        not be rendered.

        The **QSGOpacityNode**  will return a blocked subtree when accumulated
        opacity is 0, for instance.
        """
        ...
    def lastChild(self) -> PySide6.QtQuick.QSGNode:
        """
        https://doc.qt.io/qt-6/qsgnode.html#lastChild

        **QSGNode *QSGNode::lastChild() const**

        Returns the last child of this node.

        The children are stored as a linked list.
        """
        ...
    def markDirty(self, bits: PySide6.QtQuick.QSGNode.DirtyState) -> None:
        """
        https://doc.qt.io/qt-6/qsgnode.html#markDirty

        **void QSGNode::markDirty(QSGNode::DirtyState bits )**

        Notifies all connected renderers that the node has dirty **bits**.
        """
        ...
    def nextSibling(self) -> PySide6.QtQuick.QSGNode:
        """
        https://doc.qt.io/qt-6/qsgnode.html#nextSibling

        **QSGNode *QSGNode::nextSibling() const**

        Returns the node after this in the parent's list of children.

        The children are stored as a linked list.
        """
        ...
    def parent(self) -> PySide6.QtQuick.QSGNode:
        """
        https://doc.qt.io/qt-6/qsgnode.html#parent

        **QSGNode *QSGNode::parent() const**

        Returns the parent node of this node.
        """
        ...
    def prependChildNode(self, node: PySide6.QtQuick.QSGNode) -> None:
        """
        https://doc.qt.io/qt-6/qsgnode.html#prependChildNode

        **void QSGNode::prependChildNode(QSGNode * node )**

        Prepends **node** to this node's the list of children.

        Ordering of nodes is important as geometry nodes will be rendered in the
        order they are added to the scene graph.
        """
        ...
    def preprocess(self) -> None:
        """
        https://doc.qt.io/qt-6/qsgnode.html#preprocess

        **[virtual] void QSGNode::preprocess()**

        Override this function to do processing on the node before it is
        rendered.

        Preprocessing needs to be explicitly enabled by setting the flag
        **QSGNode::UsePreprocess** . The flag needs to be set before the node is
        added to the scene graph and will cause the preprocess() function to be
        called for every frame the node is rendered.

        **Warning:** Beware of deleting nodes while they are being preprocessed.
        It is possible, with a small performance hit, to delete a single node
        during its own preprocess call. Deleting a subtree which has nodes that
        also use preprocessing may result in a segmentation fault. This is done
        for performance reasons.
        """
        ...
    def previousSibling(self) -> PySide6.QtQuick.QSGNode:
        """
        https://doc.qt.io/qt-6/qsgnode.html#previousSibling

        **QSGNode *QSGNode::previousSibling() const**

        Returns the node before this in the parent's list of children.

        The children are stored as a linked list.
        """
        ...
    def removeAllChildNodes(self) -> None:
        """
        https://doc.qt.io/qt-6/qsgnode.html#removeAllChildNodes

        **void QSGNode::removeAllChildNodes()**

        Removes all child nodes from this node's list of children.
        """
        ...
    def removeChildNode(self, node: PySide6.QtQuick.QSGNode) -> None:
        """
        https://doc.qt.io/qt-6/qsgnode.html#removeChildNode

        **void QSGNode::removeChildNode(QSGNode * node )**

        Removes **node** from this node's list of children.
        """
        ...
    def reparentChildNodesTo(self, newParent: PySide6.QtQuick.QSGNode) -> None: ...
    def setFlag(self, arg__1: PySide6.QtQuick.QSGNode.Flag, arg__2: bool = ...) -> None:
        """
        https://doc.qt.io/qt-6/qsgnode.html#setFlag

        **void QSGNode::setFlag(QSGNode::Flag f , bool enabled = true)**

        Sets the flag **f** on this node if **enabled** is true; otherwise
        clears the flag.

        **See also** **flags** ().
        """
        ...
    def setFlags(self, arg__1: PySide6.QtQuick.QSGNode.Flags, arg__2: bool = ...) -> None:
        """
        https://doc.qt.io/qt-6/qsgnode.html#setFlags

        **void QSGNode::setFlags(QSGNode::Flags f , bool enabled = true)**

        Sets the flags **f** on this node if **enabled** is true; otherwise
        clears the flags.

        **See also** **flags** ().
        """
        ...
    def type(self) -> PySide6.QtQuick.QSGNode.NodeType:
        """
        https://doc.qt.io/qt-6/qsgnode.html#type

        **QSGNode::NodeType QSGNode::type() const**

        Returns the type of this node. The node type must be one of the
        predefined types defined in **QSGNode::NodeType**  and can safely be
        used to cast to the corresponding class.
        """
        ...
