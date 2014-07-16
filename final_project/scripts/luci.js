function luci () {
var lampade = new THREE.Object3D();

var pointColor = "#ffffff";
var lightSala = new THREE.PointLight( pointColor, 1, 40 );
lightSala.position.set( 72.5,37.5,0 );
lampade.add( lightSala );

var lightCucina = new THREE.PointLight( pointColor, 1, 40 );
lightCucina.position.set( 72.5,12.5,0 );
lampade.add( lightCucina );

var lightCamera1 = new THREE.PointLight( pointColor, 1, 40 );
lightCamera1.position.set( 20,12.5,0 );
lampade.add( lightCamera1 );

var lightCamera2 = new THREE.PointLight( pointColor, 1, 40 );
lightCamera2.position.set( 20,65,0 );
lampade.add( lightCamera2 );

var lightCamera3 = new THREE.PointLight( pointColor, 1, 40 );
lightCamera3.position.set( 72.5,65,0 );
lampade.add( lightCamera3 );

var lightBagno = new THREE.PointLight( pointColor, 1, 40 );
lightBagno.position.set( 20,35,0 );
lampade.add( lightBagno );

var lightIngresso1 = new THREE.PointLight( pointColor, 1, 40 );
lightIngresso1.position.set( 45,20,0 );
lampade.add( lightIngresso1 );
var lightIngresso2 = new THREE.PointLight( pointColor, 1, 40 );
lightIngresso2.position.set( 45,50,0 );
lampade.add( lightIngresso2 );

 var gui = new dat.GUI();

 var controls = new function () {
        this.LuceSala = true;
        this.LuceCucina = true;
        this.LuceCamera1 = true; 
        this.LuceCamera2 = true; 
        this.LuceCamera3 = true; 
        this.LuceBagno = true;
        this.LuceIngresso = true;
  };

 gui.add(controls, 'LuceSala').onChange(function (value) {
      if(value) {
        lampade.add(lightSala);
        lightSala.castShadow = true;
        lightSala.receiveShadow = true;
       }
     else {
        lampade.remove(lightSala);
        lightSala.castShadow = false;
        lightSala.receiveShadow = false;
      }
    });

  gui.add(controls, 'LuceCucina').onChange(function (value) {
      if(value) {
        lampade.add(lightCucina);
        lightCucina.castShadow = true;
        lightCucina.receiveShadow = true;
       }
     else {
        lampade.remove(lightCucina);
        lightCucina.castShadow = false;
        lightCucina.receiveShadow = false;
      }
    });

    gui.add(controls, 'LuceCamera1').onChange(function (value) {
      if(value) {
        lampade.add(lightCamera1);
        lightCamera1.castShadow = true;
        lightCamera1.receiveShadow = true;
       }
     else {
        lampade.remove(lightCamera1);
        lightCamera1.castShadow = false;
        lightCamera1.receiveShadow = false;
      }
    });

        gui.add(controls, 'LuceCamera2').onChange(function (value) {
      if(value) {
        lampade.add(lightCamera2);
        lightCamera2.castShadow = true;
        lightCamera2.receiveShadow = true;
       }
     else {
        lampade.remove(lightCamera2);
        lightCamera2.castShadow = false;
        lightCamera2.receiveShadow = false;
      }
    });

  gui.add(controls, 'LuceCamera3').onChange(function (value) {
      if(value) {
        lampade.add(lightCamera3);
        lightCamera3.castShadow = true;
        lightCamera3.receiveShadow = true;
       }
     else {
        lampade.remove(lightCamera3);
        lightCamera3.castShadow = false;
        lightCamera3.receiveShadow = false;
      }
    });

    gui.add(controls, 'LuceBagno').onChange(function (value) {
      if(value) {
        lampade.add(lightBagno);
        lightBagno.castShadow = true;
        lightBagno.receiveShadow = true;
       }
     else {
        lampade.remove(lightBagno);
        lightBagno.castShadow = false;
        lightBagno.receiveShadow = false;
      }
    });

  gui.add(controls, 'LuceIngresso').onChange(function (value) {
      if(value) {
        lampade.add(lightIngresso1);
        lightIngresso1.castShadow = true;
        lightIngresso1.receiveShadow = true;
        lampade.add(lightIngresso2);
        lightIngresso2.castShadow = true;
        lightIngresso2.receiveShadow = true;
       }
     else {
        lampade.remove(lightIngresso1);
        lightIngresso1.castShadow = false;
        lightIngresso1.receiveShadow = false;
        lampade.remove(lightIngresso2);
        lightIngresso2.castShadow = false;
        lightIngresso2.receiveShadow = false;
      }
    });

  return lampade;

}