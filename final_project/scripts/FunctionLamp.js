function createLamps(){
	var lamps = new THREE.Object3D();
	
	var lampSala = createLamp();
	lampSala.rotation.x = Math.PI/2;
	lampSala.position.set(72.5,37.5,0);
	lamps.add(lampSala);
	
	var lampCucina = createLamp();
	lampCucina.rotation.x = Math.PI/2;
	lampCucina.position.set(72.5,12.5,0);
	lamps.add(lampCucina);	
	
	var lampCamera1 = createLamp();
	lampCamera1.rotation.x = Math.PI/2;
	lampCamera1.position.set(20,12.5,0);
	lamps.add(lampCamera1);	
	
	var lampCamera2 = createLamp();
	lampCamera2.rotation.x = Math.PI/2;
	lampCamera2.position.set(20,65,0);
	lamps.add(lampCamera2);
	
	var lampCamera3 = createLamp();
	lampCamera3.rotation.x = Math.PI/2;
	lampCamera3.position.set(72.5,65,0);
	lamps.add(lampCamera3);
	
	var lampIngresso1 = createLamp();
	lampIngresso1.rotation.x = Math.PI/2;
	lampIngresso1.position.set(45,20,0);
	lamps.add(lampIngresso1);
	
	var lampIngresso2 = createLamp();
	lampIngresso2.rotation.x = Math.PI/2;
	lampIngresso2.position.set(45,50,0);
	lamps.add(lampIngresso2);	
	
	var lampBagno = createLamp();
	lampBagno.rotation.x = Math.PI/2;
	lampBagno.position.set(20,35,0);
	lamps.add(lampBagno);			

	return lamps;
}

function createLamp(){
	var lamp = new THREE.Object3D();
	var baseGeometry = new THREE.CylinderGeometry(4, 4, 0.5, 20, 20, false);
	var baseMaterial = new THREE.MeshBasicMaterial({ color: 0x33234c, shading: THREE.FlatShading });
	var base = new THREE.Mesh(baseGeometry, baseMaterial);
	base.position.set(0, 25, 0);
	lamp.add(base);
	var half_sphereGeometry = new THREE.SphereGeometry(4, 20, 20, 0, Math.PI*2, -Math.PI/2, Math.PI/2);
	var half_sphereMaterial = new THREE.MeshBasicMaterial({ color: 0x4169e1, side: THREE.DoubleSide });
	var half_sphere = new THREE.Mesh(half_sphereGeometry, half_sphereMaterial);
	half_sphere.position.set(0, 21, 0);
	lamp.add(half_sphere);

	return lamp;
}

function createSphere(radius, pol1, pol2, colore,trasparente, opacita){
	var sphereGeometry = new THREE.SphereGeometry(radius, pol1, pol2);
	var sphereMaterial = new THREE.MeshBasicMaterial({ color: colore,transparent: trasparente, opacity: opacita});
	var sphere = new THREE.Mesh(sphereGeometry, sphereMaterial);
	return sphere;
}