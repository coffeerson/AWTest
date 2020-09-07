import QtQuick 2.15

Item{
    id: chips
    property alias cellColor: rectangle.color
    signal clicked(cellColor: color)
    width: 40
    height: 20

    Rectangle {
        id: rectangle
        border.color: "black"
        anchors.fill: parent
    }

    MouseArea {
        anchors.fill: parent
        onClicked: chips.clicked(chips.cellColor)
    }
}