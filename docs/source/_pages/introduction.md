# Introduction 📈

## `Qt` Graphics View Framework

The [Qt Graphics View Framework] consists of the following hierarchy:

```
View -> Scene -> Item
```

where `Views` are scroll area widgets for observing `Scenes` and `Scenes` contain `Items`. Each object has its own coordinate system.

```{eval-rst}
.. list-table::

   * - .. figure:: ../_resources/img/item_coordinates.png

       **Item Coordinates**

     -
     -
```

[qt graphics view framework]: https://doc.qt.io/qt-6/graphicsview.html
