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

    Dial {
        id: dial
        x: 240
        y: 260
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.5}
}
##^##*/
