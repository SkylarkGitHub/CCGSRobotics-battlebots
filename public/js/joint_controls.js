var prevPacket;
//var socket = new WebSocket('ws://'+location.hostname+':8888');

function joint(jointName) {
    this.name = jointName;
    this.changeValue = 0



    this.sendPacket = function () {
        sendPacket("Joint,'" + this.name + "', " + this.changeValue)
    }
}


function jointKey(keyID, jointPacket) {
    this.keyID = keyID;
    this.currentlyPressed = false,
    this.jointPacket = jointPacket

    this.onPress = function () {
        this.currentlyPressed = true;
    },
    this.onRelease = function () {
        this.currentlyPressed = false;
    }
    this.sendPacket = function () {
        if(this.currentlyPressed) {
            sendPacket
        }
    }
}

var jointKeys = [
    ]


// "sendPacket(packet)" will send a packet along the websocket, provided it doesn't match the previous data. 
// This prevents the websocket being clogged with unnecessary data packets.
function sendPacket(packet){
    if(packet != prevPacket) {
        console.log(packet)
        //socket.send(packet)
        prevPacket = packet
    }
}

document.addEventListener("keydown", function onEvent(event) {
    jointKeys.forEach(function (key, index) {
        if(event.key === key.keyID) {
            key.onPress();
        }
    })
});

document.addEventListener("keyup", function onEvent(event) {
    jointKeys.forEach(function (key, index) {
        if(event.key === key.keyID) {
            key.onRelease();
        }
    })
});

setInterval(function(){
    jointKeys.forEach(function (key, index) {
        if(event.key === key.keyID) {
            key.sendPacket();
        }
    })
    
}, 10);