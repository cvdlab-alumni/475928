function insert3Dobj () {
  var obj = new THREE.Object3D();

  // SALONE
  var divano = loadObj("couchPoofyPillows");
  divano.scale.set(3,3,3);
  divano.rotation.y = Math.PI/4;
  divano.position.set(55,4,-17.5);
  obj.add(divano);

  var tavolo = loadObj("table4");
  tavolo.rotation.y = Math.PI/4;
  tavolo.scale.set(.05,.05,.05);
  tavolo.position.set(69,1.5,-41);
  obj.add(tavolo);

  var tappeto = loadObj("kleed_grieks");
  tappeto.rotation.y = - Math.PI/8;
  tappeto.scale.set(.1,.1,.1);
  tappeto.position.set(66.5,1.5,-45);
  obj.add(tappeto);

  // CUCINA
  var cucina1 = loadObj("2DoorLowerCabinet");
  cucina1.rotation.y = Math.PI;
  cucina1.scale.set(1,1,1);
  cucina1.position.set(89.5,5,-5);
  obj.add(cucina1);

  var cucina2 = loadObj("2DoorLowerCabinet");
  cucina2.rotation.y = Math.PI;
  cucina2.scale.set(1,1,1);
  cucina2.position.set(76.5,5,-5);
  obj.add(cucina2);

  var cucina3 = loadObj("kitchenSinkWithMarble");
  cucina3.rotation.y = Math.PI;
  cucina3.scale.set(1.7,1.6,2);
  cucina3.position.set(83,4.45,-4.23);
  obj.add(cucina3);

  var cucina4 = loadObj("gasHob");
  cucina4.rotation.y = Math.PI;
  cucina4.scale.set(.1,.1,.1);
  cucina4.position.set(76.5,-.75,-4.35);
  obj.add(cucina4);

  var cucina5 = loadObj("percolateur");
  cucina5.rotation.y = - Math.PI;
  cucina5.scale.set(.1,.1,.1);
  cucina5.position.set(90,9.5,-3.7);
  obj.add(cucina5);

  // BAGNO
  var water = loadObj("water");
  water.scale.set(.08,.08,.08);
  water.position.set(5,3,-48);
  obj.add(water);

  var bidet = loadObj("bidet");
  bidet.scale.set(.08,.08,.08);
  bidet.position.set(18,3,-48);
  obj.add(bidet);

  var c_igienica = loadObj("bathroom-tissue");
  c_igienica.scale.set(3,3,3);
  c_igienica.rotation.y = Math.PI/2;
  c_igienica.position.set(2,7,-46);
  obj.add(c_igienica);

  var lavandino = loadObj("washbasin");
  lavandino.scale.set(.11,.11,.11);
  lavandino.rotation.y = Math.PI;
  lavandino.position.set(10,0,-22.5);
  obj.add(lavandino);

  var bilancia = loadObj("pesePersonne");
  bilancia.scale.set(.1,.1,.1);
  bilancia.rotation.y = Math.PI;
  bilancia.position.set(13.5,4.5,-25.5);
  obj.add(bilancia);

  var vasca = loadObj("bath_jay_hardy");
  vasca.scale.set(.08,.08,.08);
  vasca.position.set(28.5,1.5,-28);
  obj.add(vasca);

  var specchio = loadObj("mirror");
  specchio.scale.set(.2,.2,.2);
  specchio.position.set(10,13,-22.5);
  specchio.rotation.y = Math.PI;
  obj.add(specchio);

  // CAMERA 1
  var letto = loadObj("lettoAzzurro");
  letto.scale.set(.08,.08,.08);
  letto.rotation.y = Math.PI/2;
  letto.position.set(-28.5,.3,1.5);
  obj.add(letto);

  var comodino = loadObj("comodinoAzzurro");
  comodino.scale.set(.07,.07,.07);
  comodino.rotation.y = Math.PI/2;
  comodino.position.set(-27,1.8,10);
  obj.add(comodino);

  var scrivania = loadObj("biurko3");
  scrivania.scale.set(.09,.09,.09);
  scrivania.rotation.y = Math.PI;
  scrivania.position.set(12,6.5,-3);
  obj.add(scrivania);

  var sedia = loadObj("officeChair");
  sedia.scale.set(.07,.07,.07);
  sedia.position.set(-12.5,10.2,-22.5);
  obj.add(sedia);

  var armadio1 = loadObj("mobileAzzurro");
  armadio1.scale.set(.07,.07,.07);
  armadio1.position.set(17,1.5,-17);
  obj.add(armadio1);

  var armadio2 = loadObj("mobileAzzurro");
  armadio2.scale.set(.07,.07,.07);
  armadio2.position.set(10,1.5,-17);
  obj.add(armadio2);

  var lamp = loadObj("desk_lamp1");
  lamp.scale.set(.5,.5,.5);
  lamp.rotation.y = 3 * Math.PI/4;
  lamp.position.set(9,6.5,-3);
  obj.add(lamp);

  var pc = loadObj("imac");
  pc.scale.set(10,10,10);
  pc.rotation.y = Math.PI;
  pc.position.set(13,6.5,-3);
  obj.add(pc);

  var scarpe = loadObj("sneakers");
  scarpe.scale.set(.05,.05,.05);
  scarpe.position.set(17,2,-13);
  obj.add(scarpe);

  var iphone = loadObj("iphone");
  iphone.scale.set(.09,.09,.09);
  iphone.rotation.x = - Math.PI/2;
  iphone.rotation.z = Math.PI/6;
  iphone.position.set(3.5,5.2,-11);
  obj.add(iphone);

  var car = loadObj("concept-sedan-01v1");
  car.rotation.y = - Math.PI/2;
  car.position.set(80,0,8);
  obj.add(car);

  var cubeGeometry = new THREE.BoxGeometry(10, 10, 10);
  var cubeMaterial = new THREE.MeshLambertMaterial({color: 0xeeeeee, opacity: 0, transparent:true});
  var cube1 = new THREE.Mesh(cubeGeometry, cubeMaterial);
  cube1.position.set(70,2,9);
  obj.add(cube1);

  var cube2 = new THREE.Mesh(cubeGeometry, cubeMaterial);
  cube2.position.set(17,2,-18);
  obj.add(cube2);

  cube1.azione = function () {
    var tween1car = new TWEEN.Tween( car.position )
    .to( { x: -10 }, 2000 )
    .easing( TWEEN.Easing.Linear.None )
    tween1car.start();  
  };

  cube2.azione = function (){
    var tween1scarpe = new TWEEN.Tween( scarpe.position )
    .to( { x: 10 }, 2000 )
    .easing( TWEEN.Easing.Linear.None )
    tween1scarpe.start();

    var tween2scarpe = new TWEEN.Tween( scarpe.rotation )
    .to( { y: 4 * Math.PI/3 }, 2500 )
    .easing( TWEEN.Easing.Linear.None )
    tween2scarpe.start();
  };


  var projector = new THREE.Projector();
  document.addEventListener('mousedown', onDocumentMouseDown, false);

  function onDocumentMouseDown (event) {
    event.preventDefault();
    var vector = new THREE.Vector3(( event.clientX / window.innerWidth ) * 2 - 1, -( event.clientY / window.innerHeight ) * 2 + 1, 0.5);
    projector.unprojectVector(vector, camera);
    var raycaster = new THREE.Raycaster(camera.position, vector.sub(camera.position).normalize());
    var intersects = raycaster.intersectObjects([ cube1, cube2 ]);

    if (intersects.length > 0) {
      intersects[ 0 ].object.azione && intersects[ 0 ].object.azione() ;
    }
  }

  // CAMERA 2
  var lettoGrande = loadObj("lit");
  lettoGrande.scale.set(.08,.08,.08);
  lettoGrande.rotation.y = Math.PI;
  lettoGrande.position.set(18,3,-71);
  obj.add(lettoGrande);

  return obj;
}


function loadObj (name) {
  var obj = new THREE.Object3D();
  var loader = new THREE.OBJMTLLoader();
  loader.addEventListener('load', function (event) {
    var object = event.content;
    obj.add(object);
  });

  loader.load(
    'models/'+ name + '.obj', 
    'models/' + name + '.mtl', 
    {side: THREE.DoubleSide}
  );
return obj;
};