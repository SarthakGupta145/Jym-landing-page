import turtle
angle = 90
void setup(){
    size(900, 900)
}

void draw(){
    background(0)
    translate(width/2, height/2)
    stroke(255)
    strokeWeight(3)
    for(int i=0
        i < 280
        i += 10){
        pushMatrix()
        rotate(radians(i) *
               cos(radians(angle)))
        line(200*sin(
            radians(angle)), 0, 0, 200)
        popMatrix()
    }
    angle + 1
}
