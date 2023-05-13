// [고정된 값]
// 1. 중력가속도 2. 질량 3. 시간변화량
// 4. 용수철계수 5. 닻의 x축좌표, 6. 닻의 y축 좌표

// [변화하는 값]
// 1. 공의 속력 변화 2. 공의 위치 변화
// 초기화해줌

// [공의 위치 변화를 나타내는 것이 관건]
// 5. 위치 변화 s' = s + vt 를 알려면 속력 변화를 알아야 함.
// 4. 속력 변화 v' = v + at 를 알려면 가속도를 알아야 함.
// 3. 가속도 a = F/m 를 알려면 공에 작용하는 힘을 알아야 함.
// 2. 힘 F = 탄성력 + 중력(m*g) 을 알려면 탄성력을 알아야 함.
// 1. 탄성력 = -k*(변위)

var gravity = 10;
var mass = 30;
var timeStep = 0.1;
var k = 7;
var anchorX = 100;
var anchorY = 200;

var velocityY = 0;
var positionY = 100;

draw = function(){
    var springForceY = -k * (positionY - anchorY);
    var forceY = springForceY + (mass*gravity);
    var accelerationY = forceY / mass;

    velocityY = velocityY + (accelerationY*timeStep);
    positionY = positionY + (velocityY*timeStep);

    background(255, 255, 255);
    ellipse(100, positionY, 20, 20);
    line(100, positionY, anchorX, anchorY);
    rect(anchorX-5, anchorY-5, 10,10);

};