import QtQuick 2.15
import QtQuick.Controls 2.15


ApplicationWindow {
    id: mapEdit

    // 窗口标题设置
    title: "MapEdit"
    // 窗口大小设置
    width: 1600
    height: 1000


    // Window默认不可见，需要进行设置为可见
    visible: true

    Rectangle{
        id: test
        objectName: "test"
        width: 200
        height: 200
        color: 'green'
        anchors.centerIn: parent
    }

    Text {
        id: helloText
        text: "hello world"
        y: 30
        anchors.centerIn: parent
        font.pointSize: 24
        font.bold: true
    }

    Grid {
        id: colorPicker
        x: 4
        y: 800
        
        rows: 2
        columns: 3
        spacing: 3

        Chip{ cellColor: "red"; onClicked: helloText.color = cellColor }
        Chip{ cellColor: "green"; onClicked: helloText.color = cellColor }
        Chip{ cellColor: "blue"; onClicked: helloText.color = cellColor }
        Chip{ cellColor: "yellow"; onClicked: helloText.color = cellColor }
        Chip{ cellColor: "steelblue"; onClicked: helloText.color = cellColor }
        Chip{ cellColor: "black"; onClicked: helloText.color = cellColor }
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.5}
}
##^##*/
