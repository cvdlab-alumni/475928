function doorsWindows() {
  var struct = new THREE.Object3D();

     extDoor = mkExtDoor (10,1,17.5);
     extDoor.position.x = 49.6;
     extDoor.position.y = .4;
     extDoor.position.z = 1.1;
     struct.add(extDoor);

     var intDoor1 = mkIntDoor123 (10.5,.8,17.45);
     intDoor1.rotation.z = Math.PI/2;
     intDoor1.position.x = 36.5;
     intDoor1.position.y = 6;
     intDoor1.position.z = 1;
     struct.add(intDoor1);     

     var intDoor2 = mkIntDoor123 (10,.8,17.45);
     intDoor2.rotation.z = Math.PI/2;
     intDoor2.position.x = 36.5;
     intDoor2.position.y = 32;
     intDoor2.position.z = 1;
     struct.add(intDoor2);

     var intDoor3 = mkIntDoor123 (10,.8,17.45);
     intDoor3.rotation.z = Math.PI/2;
     intDoor3.position.x = 36.5;
     intDoor3.position.y = 56.7;
     intDoor3.position.z = 1;
     struct.add(intDoor3);

     var intDoor4 = mkIntDoor45 (10,.8,17.45);
     intDoor4.rotation.z = -3 * Math.PI/2;
     intDoor4.position.x = 52.5;
     intDoor4.position.y = 56.5;
     intDoor4.position.z = 1;
     struct.add(intDoor4);

     var intDoor5 = mkIntDoor45 (10.5,.8,17.45);
     intDoor5.rotation.z = - 3 * Math.PI/2;
     intDoor5.position.x = 52.5;
     intDoor5.position.y = 32;
     intDoor5.position.z = 1;
     struct.add(intDoor5);

     var intDoor6 = mkIntDoorScrigno (16,.8,17.45);
     intDoor6.position.x = 65.5;
     intDoor6.position.y = 21.5;
     intDoor6.position.z = 1;
     struct.add(intDoor6);


     //finestre
     var window1 = mkBigWindow (15,.8,10);
     window1.position.x = 11.1;
     window1.position.y = 0.5;
     window1.position.z = 7.1;
     struct.add(window1);

     var window2 = mkSmallWindowC (7.5,.8,8.4);
     window2.rotation.z = Math.PI/2;
     window2.position.x = 0.4;
     window2.position.y = 8.54;
     window2.position.z = 9.4;
     struct.add(window2);

     var window3 = mkSmallWindow2 (7.6,.8,10.1);
     window3.rotation.z = Math.PI/2;
     window3.position.x = 0.4;
     window3.position.y = 34.4;
     window3.position.z = 7;
     struct.add(window3);

     var window4 = mkSmallWindow1 (7.5,.8,8.5);
     window4.rotation.z = Math.PI/2;
     window4.position.x = 0.4;
     window4.position.y = 57.9;
     window4.position.z = 9.2;
     struct.add(window4);

     var window5 = mkBigWindow (21,.8,10);
     window5.position.x = 15.8;
     window5.position.y = 84.5;
     window5.position.z = 7.1;
     struct.add(window5);

     var window6 = mkBigWindow (20,.8,10);
     window6.position.x = 63;
     window6.position.y = 84.5;
     window6.position.z = 7;
     struct.add(window6); 

     var window7 = mkBigWindow (10.65,.5,10);
     window7.rotation.z = Math.PI/2;
     window7.position.x = 93.5;
     window7.position.y = 56.5;
     window7.position.z = 7.2;
     struct.add(window7);

     var window8 = mkSmallWindow1 (7.3,.8,10);
     window8.rotation.z = Math.PI/2;
     window8.position.x = 93.5;
     window8.position.y = 33.7;
     window8.position.z = 7.5;
     struct.add(window8);

     var window9 = mkBigWindow (15.5,.5,8.5);
     window9.position.x = 65.45;
     window9.position.y = 0.5;
     window9.position.z = 9.1;
     struct.add(window9);


  function mkExtDoor (x, y, z) {
    var perno = new THREE.Object3D();
    var portaGeometry = new THREE.BoxGeometry(x,y,z);
    var porta = createMesh(portaGeometry,"ext_door.jpg");
    porta.position.set(x/2,0,(z/2-.1));

    porta.azione = function (){
     if (porta.parent.rotation.z == 0){
     porta.parent.rotation.z = -Math.PI/2;
    }
    else
     porta.parent.rotation.z = 0;
    };

    perno.add(porta);
    // perno.position.set(x,y,z);
    porta.position.x = -x/2;

    return perno;
  }

  function mkSmallWindow1 (x, y, z) {
    var win = createMesh(new THREE.BoxGeometry(x, y, z), "finestrapiccola.jpg");
    win.position.set(x/2,0,(z/2-.1));

    var cubeGeometry = new THREE.BoxGeometry(.01, .01, .01);
    var cubeMaterial = new THREE.MeshLambertMaterial({color: Math.random() * 0xc0c0c0});
    var perno = new THREE.Mesh(cubeGeometry, cubeMaterial);

    win.azione = function (){
      if (win.parent.rotation.z == Math.PI/2){
      win.parent.rotation.z = Math.PI;
    }
    else
      win.parent.rotation.z = Math.PI/2;
    };

    perno.add(win);

    return perno;
  }


  function mkSmallWindowM (x, y, z) {
    var win = createMesh(new THREE.BoxGeometry(x, y, z), "finestrapiccola.jpg");
    win.position.set(x/2,0,(z/2-.1));

    var cubeGeometry = new THREE.BoxGeometry(.01, .01, .01);
    var cubeMaterial = new THREE.MeshLambertMaterial({color: Math.random() * 0xc0c0c0});
    var perno = new THREE.Mesh(cubeGeometry, cubeMaterial);

    win.azione = function (){
      if (win.parent.rotation.z == Math.PI/2){
      win.parent.rotation.z = Math.PI;
      }
      else
      win.parent.rotation.z = Math.PI/2;
    };

    perno.add(win);
    
    return perno;
  }


  function mkSmallWindowC (x, y, z) {
    var win = createMesh(new THREE.BoxGeometry(x, y, z), "finestrapiccola.jpg");
    win.position.set(x/2,0,(z/2-.1));

    var cubeGeometry = new THREE.BoxGeometry(.01, .01, .01);
    var cubeMaterial = new THREE.MeshLambertMaterial({color: Math.random() * 0xc0c0c0});
    var perno = new THREE.Mesh(cubeGeometry, cubeMaterial);

    win.azione = function (){
      if (win.parent.rotation.z == Math.PI/2){
        win.parent.rotation.z = Math.PI/4;
      }
      else
      win.parent.rotation.z = Math.PI/2;
    };

    perno.add(win);
    
    return perno;
  }

  function mkSmallWindow2 (x, y, z) {
    var win = createMesh(new THREE.BoxGeometry(x, y, z), "finestrapiccola.jpg");
    win.position.set(x/2,0,(z/2-.1));

    var cubeGeometry = new THREE.BoxGeometry(.01, .01, .01);
    var cubeMaterial = new THREE.MeshLambertMaterial({color: Math.random() * 0xc0c0c0});
    var perno = new THREE.Mesh(cubeGeometry, cubeMaterial);

    win.azione = function (){
    if (win.parent.rotation.y == 0){
      win.parent.rotation.y = Math.PI/8;
    }
    else
    win.parent.rotation.y = 0;
    };

    perno.add(win);
    
    return perno;
  }

  function mkBigWindow (x, y, z) {
    var win = createMesh(new THREE.BoxGeometry(x, y, z), "finestragrande.jpg");
    win.position.set(x/2,0,(z/2-.1));

    var cubeGeometry = new THREE.BoxGeometry(.01, .01, .01);
    var cubeMaterial = new THREE.MeshLambertMaterial({color: Math.random() * 0xc0c0c0});
    var perno = new THREE.Mesh(cubeGeometry, cubeMaterial);
    perno.add(win);
    
    return perno;
  }

  function mkIntDoor123 (x, y, z) {
    var perno = new THREE.Object3D();
    var portaGeometry = new THREE.BoxGeometry(x,y,z);
    var porta = createMesh(portaGeometry,"door.png");
    porta.position.set(x/2,0,(z/2-.1));

    porta.azione = function (){
      if (porta.parent.rotation.z == Math.PI/2){
        porta.parent.rotation.z = 2*Math.PI/2;
      }
      else
      porta.parent.rotation.z = Math.PI/2;
    };

    perno.add(porta);

    return perno;
  }

  function mkIntDoor45 (x, y, z) {
    var perno = new THREE.Object3D();
    var portaGeometry = new THREE.BoxGeometry(x,y,z);
    var porta = createMesh(portaGeometry,"door.jpg");
    porta.position.set(x/2,0,(z/2-.1));

    porta.azione = function (){
      if (porta.parent.rotation.z == - 3 * Math.PI/2){
        porta.parent.rotation.z = - Math.PI/6;
      }
      else
      porta.parent.rotation.z = -3 * Math.PI/2;
    };

    perno.add(porta);

    return perno;
  }

  function mkIntDoorScrigno (x, y, z) {
    var perno = new THREE.Object3D();
    var portaGeometry = new THREE.BoxGeometry(x,y,z);
    var porta = createMesh(portaGeometry,"sc_door.jpg");
    porta.position.set(x/2,0,(z/2-.1));

    porta.azione = function (){
      if (porta.position.x == x/2){
        var tweenDoor = new TWEEN.Tween( porta.position )
        .to( { x: -5.5 }, 1000 )
        .easing( TWEEN.Easing.Linear.None )
        tweenDoor.start();
      }
      else {
        var tweenDoor = new TWEEN.Tween( porta.position )
        .to( { x: x/2 }, 1000 )
        .easing( TWEEN.Easing.Linear.None )
        tweenDoor.start();
      }
    };
    perno.add(porta);

    return perno;
  };

  var projector = new THREE.Projector();
  document.addEventListener('mousedown', onDocumentMouseDown, false);


  function onDocumentMouseDown (event) {
    event.preventDefault();
    var vector = new THREE.Vector3(( event.clientX / window.innerWidth ) * 2 - 1, -( event.clientY / window.innerHeight ) * 2 + 1, 0.5);
    projector.unprojectVector(vector, camera);
    var raycaster = new THREE.Raycaster(camera.position, vector.sub(camera.position).normalize());
    var intersects = raycaster.intersectObjects([ extDoor.children[0], intDoor1.children[0], intDoor2.children[0], intDoor3.children[0], intDoor4.children[0], intDoor5.children[0], intDoor6.children[0], window2.children[0], window8.children[0], window3.children[0]]);

    if (intersects.length > 0) {
      intersects[ 0 ].object.azione && intersects[ 0 ].object.azione() ;
    }
  }

  var cube1;
  cube1 = createMesh2(new THREE.BoxGeometry(11,7.6,.5));
  cube1.rotation.z = Math.PI/2;
  cube1.rotation.x = - Math.PI/2;
  cube1.rotation.y = - Math.PI/2;
  cube1.position.x = 93.5;
  cube1.position.y = 36.65;
  cube1.position.z = 11.7;
  struct.add(cube1);

  var cube;
  cube = createMesh1(new THREE.BoxGeometry(15, 10, 1));
  cube.position.set(73,52,10);
  cube.rotation.x = Math.PI/2;
  struct.add(cube);

  return struct;
}