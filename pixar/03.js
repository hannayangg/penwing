// [2차원 스프링]
// y축을 움직이도록 했던 것을 x축으로 똑같이 추가해줌
// 주의** x축으로 작용하는 힘: 중력없음

var gravity = 10;
var mass = 30;
var timeStep = 0.1;
var k = 7;
var damping = 10;
var anchorX = 100;
var anchorY = 200;

var velocityY = 0;
var velocityX = 0;

var positionY = 100;
var positionX = 200;

draw = function(){
    var springForceY = -k * (positionY - anchorY);
    var springForceX = -k * (positionX - anchorX);

    var dampingForceY = damping * velocityY;
    var dampingForceX = damping * velocityX;

    var forceY = springForceY - dampingForceY + (mass*gravity);
    var forceX = springForceX - dampingForceX;

    var accelerationY = forceY / mass;
    var accelerationX = forceX / mass;

    velocityY = velocityY + (accelerationY*timeStep);
    velocityX = velocityX + (accelerationX*timeStep);

    positionY = positionY + (velocityY*timeStep);
    positionX = positionX + (velocityX*timeStep);

    background(255, 255, 255);
    ellipse(positionX, positionY, 20, 20);
    line(positionX, positionY, anchorX, anchorY);
    rect(anchorX-5, anchorY-5, 10,10);

};