// [감폭기 변수]
// 1. 감폭기 자체의 힘 (damping)
// 2. 공의 운동 속도 (velocityY)
// (공의 변화 속도 빠르면 저항힘 커지고, 변화 속도 0이면 저항할 필요X)
// dampingForceY = dampint * valocityY
// 이 힘은 스프링력에 저항하는 힘이기 때문에 힘을 계산할 때 빼주어야 함!!!

var gravity = 10;
var mass = 30;
var timeStep = 0.1;
var k = 7;
var damping = 10;
var anchorX = 100;
var anchorY = 200;

var velocityY = 0;
var positionY = 100;

draw = function(){
    var springForceY = -k * (positionY - anchorY);
    var dampingForceY = damping * velocityY;
    var forceY = springForceY - dampingForceY + (mass*gravity);
    var accelerationY = forceY / mass;

    velocityY = velocityY + (accelerationY*timeStep);
    positionY = positionY + (velocityY*timeStep);

    background(255, 255, 255);
    ellipse(100, positionY, 20, 20);
    line(100, positionY, anchorX, anchorY);
    rect(anchorX-5, anchorY-5, 10,10);

};