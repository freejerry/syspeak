canvas_template = function(id){
  var html = '<canvas id="canvas_' + id + '" style="display:none;vertical-align: middle;"></canvas>' +
             '<canvas id="ocanvas_' + id + '" style="display:none;vertical-align: middle;"></canvas>';
  return html;
};

function initCanvas(target) {
  var canvas = document.getElementById('canvas_' + target);
  var ocanvas = document.getElementById('ocanvas_' + target);
  var ctx = canvas.getContext('2d');
  var octx = ocanvas.getContext('2d');
  canvas.width = 32;
  canvas.height = 32;
  canvas.style.width  = '400px';
  canvas.style.height  = '400px';
  ocanvas.width = 1000;
  ocanvas.height = 800;
  //ctx.scale(10, 10);
  return [ctx, octx, canvas, ocanvas];
}

gen_color_chips = function(){
  var colors = [];
  var chips = [];
  var method = chroma.scale(['navy','yellow']).mode('lch').colors(1024);
  method.forEach(function(f){
    colors.push(chroma(f).get("rgb"));
    chips.push(chroma(f).hex());
  });
  return [colors, chips];
};
/*
gen_color_chips = function(){
  var colors = [];
  var method = chroma.scale(['#000001','#ff0000']).mode('lch').colors(1024);
  method.forEach(function(f){
    colors.push(chroma(f).hex());
  });
  return colors;
};
*/
function drawPixel(ctx, data) {
  //console.log(colors);
  if(data == 0){
    ctx.rect(0,0,32,32);
    //ctx.fillStyle="#000000";
    ctx.fill();
  }else{
    ctx.clearRect(0, 0, 32, 32);
    for (var i = 0; i < 32; ++i) {
      for (var j = 0; j < 32; ++j)
      {
        x = Math.floor(i);
        y = Math.floor(j);
        r = Math.floor(colors[data[i][j]][0]);
        g = Math.floor(colors[data[i][j]][1]);
        b = Math.floor(colors[data[i][j]][2]);
        ctx.fillStyle = `rgb( ${r} , ${g} , ${b} )`;
        ctx.fillRect(x, y, 1, 1);
      }
    }
  }
}

