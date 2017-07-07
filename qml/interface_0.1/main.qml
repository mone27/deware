import QtQuick 2.6
import QtQuick.Window 2.2

Window {
    id: window1
    visible: true
    height: 480
    width: 800
    color: 'red'
    MouseArea {
        anchors.top: parent
        onClicked: {
            Qt.quit();
        }
    }
    Item{
        id: liveValues
        anchors.top: parent.top
        anchors.left: parent.left
        width: parent.width/2
        height: parent.height/2
        anchors.leftMargin: 0
        anchors.topMargin: 0
        Grid {

            id: rowTemp
            anchors.fill: parent
            Label {
                x: 79
                y: 43
                text: qsTr("Text")
                font.pixelSize: 12
            }

            Label {
                id: temp_txt
                x: 180
                y: 43
                text: qsTr("Text")
                font.pixelSize: 12
            }
        }
        Text {
            id: hum_lab
            x: 79
            y: 100
            text: qsTr("Text")
            font.pixelSize: 12
        }

        Text {
                id: hum_txt
                x: 180
                y: 100
                text: qsTr("Text")
                font.pixelSize: 12
            }
        }
    

}
