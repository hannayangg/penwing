// [다수의 스프링]
// 1. mass1에 작용하는 힘 F1 = S1 - D1 + G1 - S2 + D2
// 2. mass2의 스프링력 S2 = -k * (P2-P1)
// 3. line:
// 위의 라인은 anchorX,Y에 연결되고,
// 밑의 라인은 mass1의 위치에 연결되어야 함!!

var gravity = 10;
var mass = 30;
var timeStep = 0.1;
var k = 7;
var damping = 10;
var anchorX = 100;
var anchorY = 200;
//mass1
var mass1velocityY = 0;
var mass1velocityX = 0;
var mass1positionY = 100;
var mass1positionX = 200;
//mass2
var mass2velocityY = 0;
var mass2velocityX = 0;
var mass2positionY = 80;
var mass2positionX = 100;


draw = function(){
    //mass1 springforce
    var mass1springForceY = -k * (mass1positionY - anchorY);
    var mass1springForceX = -k * (mass1positionX - anchorX);
    //mass2 springforce
    var mass2springForceY = -k * (mass2positionY - mass1positionY);
    var mass2springForceX = -k * (mass2positionX - mass1positionX);
    //mass1 dampingforce
    var mass1dampingForceY = damping * mass1velocityY;
    var mass1dampingForceX = damping * mass1velocityX;
    //mass2 dampingforce
    var mass2dampingForceY = damping * mass2velocityY;
    var mass2dampingForceX = damping * mass2velocityX;
    //mass1 netforce
    var mass1forceY = mass1springForceY - mass1dampingForceY + (mass*gravity) - mass2springForceY + mass2dampingForceY;
    var mass1forceX = mass1springForceX - mass1dampingForceX - mass2springForceX + mass2dampingForceX;
    //mass2 netforce
    var mass2forceY = mass2springForceY - mass2dampingForceY + (mass*gravity);
    var mass2forceX = mass2springForceX - mass2dampingForceX;
    //mass1 acceleration
    var mass1accelerationY = mass1forceY / mass;
    var mass1accelerationX = mass1forceX / mass;
    //mass2 acceleration
    var mass2accelerationY = mass2forceY / mass;
    var mass2accelerationX = mass2forceX / mass;
    //mass1 velocity
    mass1velocityY = mass1velocityY + (mass1accelerationY*timeStep);
    mass1velocityX = mass1velocityX + (mass1accelerationX*timeStep);
    //mass2 velocity
    mass2velocityY = mass2velocityY + (mass2accelerationY*timeStep);
    mass2velocityX = mass2velocityX + (mass2accelerationX*timeStep);
    //mass1 position
    mass1positionY = mass1positionY + (mass1velocityY*timeStep);
    mass1positionX = mass1positionX + (mass1velocityX*timeStep);
    //mass2 position
    mass2positionY = mass2positionY + (mass2velocityY*timeStep);
    mass2positionX = mass2positionX + (mass2velocityX*timeStep);

    background(255, 255, 255);
    ellipse(mass1positionX, mass1positionY, 20, 20);
    ellipse(mass2positionX, mass2positionY, 20,20);
    
    line(mass1positionX, mass1positionY, anchorX, anchorY);
    line(mass2positionX, mass2positionY, mass1positionX, mass1positionY);

    rect(anchorX-5, anchorY-5, 10,10);

};