var cpx = 20,
    cpy = 150; // position of the first charge (the one on the left)
var cnx = 300,
    cny = 350; // position of the second charge (the one on the right)
var qp;// = 1000;//createSlider(0,1000,50);
    qn = 1000; // values of the charges; try qn=1000 and different combinations (e.g. qp=10, qn=1000)

var x, y, dx, dy, dxn, dyn;
var d1, E1, E1x, E1y, d2, E2, E2x, E2y;
var EEx, EEy, EE, ll, deltaX, deltaY;
var lines = 90; // number of lines
var density;


function setup() {
   // createCanvas(windowWidth, 700);
   qpSlide = createSlider(-1000,2000,500);
   linesSlider = createSlider(0,300, 60);
   densitySlider = createSlider(4,24,12);

   qnSlider = createSlider(-1000,2000,500);


}

function draw() {
  createCanvas(windowWidth, 700);
      cnx = width/2;
    cny = height/2;

    background(128);
    smooth();

    qpSlide.position(width/2 - 66,height + 20);
linesSlider.position(width/2 - 220, height+20);
densitySlider.position(width/2 + 86, height+20);
qnSlider.position(width/2 + 230, height+20);

    qp = qpSlide.value();
    lines = linesSlider.value();
    density = densitySlider.value();
    qn = qnSlider.value();


    fill(0);
    lineLen = 2; // grains of semolina dimension (try lineLen=10, lineLen=20)
    drawLines(createVector(cpx,cpy));
    drawLines(createVector(cnx,cny));


    fill(0);
    ellipse(cpx, cpy, 8, 8);

    fill(120);
    ellipse(cnx, cny, 8, 8);

    //noLoop();

}

function mouseDragged() {
    if ( mouseX < width && mouseY < height) {
        // loop();
        cpx = mouseX;
        cpy = mouseY;
    }

}

function newPnt(pnt){
    dx = pnt.x - cpx; // diff between field line point and charge point
    dy = pnt.y - cpy;
    d1 = sqrt(dx * dx + dy * dy); // pythagorean theorem
    E1 = qp / (d1 * d1); // inverse square law
    E1x = dx * E1 / d1; // dx:d1 = E1x:E1
    E1y = dy * E1 / d1;

    dxn = pnt.x - cnx;
    dyn = pnt.y - cny;
    d2 = sqrt(dxn * dxn + dyn * dyn);
    E2 = qn / (d2 * d2);
    E2x = dxn * E2 / d2;
    E2y = dyn * E2 / d2;

    EEx = E1x + E2x;
    EEy = E1y + E2y;
    EE = sqrt(EEx * EEx + EEy * EEy); // pythagorean theorem or root sum square


    deltaX = lineLen * EEx / EE;
    deltaY = lineLen * EEy / EE;
    var npnt = createVector(pnt.x+deltaX,pnt.y+deltaY);

    return(npnt);
}

function drawLines(chrgPnt){ // charge Point

    var theta = 0;
    for (var j = 0; j < density; j++) {
        x = chrgPnt.x + lineLen * cos(theta);
        y = chrgPnt.y + lineLen * sin(theta);
        for (var i = 0; i < lines; i++) {


        var nPnt = newPnt(createVector(x,y));
        stroke("#ffa700");
        line(x,y, nPnt.x, nPnt.y);
        x = nPnt.x;
        y = nPnt.y;
        }
    theta += TAU/density
    }

}
