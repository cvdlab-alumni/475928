/*
* Functions Muri
*/
function createWalls(){
	var walls = new THREE.Object3D();

	var muroCortoPorta = createMuroCortoPorta("ingresso.jpg");
		muroCortoPorta.position.set(37,1,-4.1);

	var muroPortaCameraDx = createMuroPortaCameraDx("camera.jpg");
		muroPortaCameraDx.rotation.y = Math.PI/2;
		muroPortaCameraDx.position.set(54.1,1,-56.1);		

	var muroFinestraCameraDx = createMuroFinestraCameraDx("camera.jpg");
		muroFinestraCameraDx.rotation.y = Math.PI/2;
		muroFinestraCameraDx.position.set(93.8,1,-56.1);

	var muroFinestraCucina = createMuroFinestraCucina("cucina.jpg");
		muroFinestraCucina.position.set(54.2,1,-4.1);

	var muroScrignoCucina = createMuroScrigno("cucina.jpg");
		muroScrignoCucina.position.set(54.2,1,-23.8);

	var muroScrignoSalone = createMuroScrigno("salone.jpg");
		muroScrignoSalone.position.set(54.2,1,-25.1);

	var muroSxSalone = createMuroSxSalone("salone.jpg");
		muroSxSalone.rotation.y = Math.PI/2;
		muroSxSalone.position.set(54.1,1,-25);

	var muroPiccoloCucina1 = createMuroPiccoloCucina("cucina.jpg");
		muroPiccoloCucina1.rotation.y = Math.PI/2;
	    muroPiccoloCucina1.position.set(54.1,1,-4);

	var muroPiccoloCucina2 = createMuroPiccoloCucina("cucina.jpg");
		muroPiccoloCucina2.rotation.y = Math.PI/2;
	    muroPiccoloCucina2.position.set(93.9,1,-4);

	var muroCameraPorta = createMuroCameraPorta("camera.jpg");
	    muroCameraPorta.position.set(.9,1,-4.1);

	var muroBagnoPorta = createMuroBagnoPorta("piastr_bagno.jpg");
		muroBagnoPorta.rotation.y = Math.PI/2;
		muroBagnoPorta.position.set(36.88,1,-25)

	var muroSupCamera = createMuroSxLarge("camera.jpg");
		muroSupCamera.position.set(.9,1,-23.7);	

	var muroCortoCamera1 = createMuroCortoCamera("camera.jpg");
		muroCortoCamera1.rotation.y = Math.PI/2;
		muroCortoCamera1.position.set(52.7,1,-74.6);

	var muroCortoCamera2 = createMuroCortoIngresso("camera.jpg");
		muroCortoCamera2.position.set(37,1,-74.6);

	var muroCortoIngresso = createMuroCortoIngresso("ingresso.jpg");
		muroCortoIngresso.position.set(37,1,-73.4);

	var muroIngressoSalone = createMuroIngressoSalone("ingresso.jpg");
		muroIngressoSalone.position.set(52.8,1,-3)

	var muroDxSalone = createMuroDxSalone("salone.jpg");
		muroDxSalone.rotation.y = Math.PI/2;
		muroDxSalone.position.set(93.8,1,-25.2);			

	var muroSupSalone = createMuroDxLarge("salone.jpg");
		muroSupSalone.position.set(53,1,-54.7);

	var muroInfBagno = createMuroSxLarge("piastr_bagno.jpg");
		muroInfBagno.position.set(.9,1,-25.1);

	var muroSupBagno = createMuroSxLarge("piastr_bagno.jpg");
		muroSupBagno.position.set(.9,1,-54.7);		

	var muroGrandeCamereSx = createMuroGrandeCamereSx("camera.jpg");
		muroGrandeCamereSx.position.set(.9,1,-56.5);

	var muroCamereSinistraCorridoio = createMuroCamereSinistraCorridoio("camera.jpg");
		muroCamereSinistraCorridoio.position.set(36.9,1,-2.95);

	var muroCamereSinistra = createMuroCamereSinistra("camera.jpg");
		muroCamereSinistra.rotation.y=3*Math.PI/2;
		muroCamereSinistra.position.set(2.1,1,-88);	

	var muroCamereRetro = createMuroCamereRetro("camera.jpg");
		muroCamereRetro.position.set(.9,1,-86.9);

	var muroIngressoBagno = createMuroIngressoBagno("ingresso.jpg");
		muroIngressoBagno.position.set(38.1,1,-2.95);

	var muroEsternoFrontale = createMuroEsternoFrontale("muro_esterno.jpg");
		muroEsternoFrontale.position.set(.9,1,-2.96);

	var muroEsternoDestra = createMuroEsternoDestra("muro_esterno.jpg", "muro_esterno-bump.jpg");
		muroEsternoDestra.rotation.y = Math.PI/2;
		muroEsternoDestra.position.set(95.1,1,-3);

	var muroEsternoRetro = createMuroEsternoRetro("muro_esterno.jpg", "muro_esterno-bump.jpg");
		muroEsternoRetro.position.set(.9,1,-88.1);

	var muroEsternoSinistra = createMuroEsternoSinistra("muro_esterno.jpg", "muro_esterno-bump.jpg");
		muroEsternoSinistra.position.set(.9,1,-88);
		muroEsternoSinistra.rotation.y=3*Math.PI/2;

	var muroSxBagno = createMuroSxBagno("piastr_bagno.jpg");
		muroSxBagno.rotation.y = Math.PI/2;
		muroSxBagno.position.set(2.15,1,-24.5);

	walls.add(muroSxBagno);
	walls.add(muroCortoPorta);
	walls.add(muroPortaCameraDx);
	walls.add(muroFinestraCameraDx);
	walls.add(muroFinestraCucina);
	walls.add(muroScrignoCucina);
	walls.add(muroScrignoSalone);
	walls.add(muroSxSalone);
	walls.add(muroPiccoloCucina1);
	walls.add(muroPiccoloCucina2);
	walls.add(muroCameraPorta);
	walls.add(muroBagnoPorta);
	walls.add(muroSupCamera);
	walls.add(muroCortoCamera1);
	walls.add(muroCortoCamera2);
	walls.add(muroCortoIngresso);
	walls.add(muroIngressoSalone);
	walls.add(muroDxSalone);
	walls.add(muroSupSalone);
	walls.add(muroInfBagno);
	walls.add(muroSupBagno);
	walls.add(muroGrandeCamereSx);
	walls.add(muroCamereSinistraCorridoio);
	walls.add(muroCamereSinistra);
	walls.add(muroCamereRetro);
	walls.add(muroIngressoBagno);
	walls.add(muroEsternoFrontale);
	walls.add(muroEsternoDestra);
	walls.add(muroEsternoRetro);
	walls.add(muroEsternoSinistra);
	return walls
}

function createMeshM(geom, imageFile) {
	var texture = THREE.ImageUtils.loadTexture("textures/" + imageFile)
	texture.wrapS = THREE.RepeatWrapping;
	texture.wrapT = THREE.RepeatWrapping;

	var mat = new THREE.MeshPhongMaterial({side: THREE.DoubleSide});
		mat.map = texture;
		mat.map.repeat.set(.1, .1);
	var mesh = new THREE.Mesh(geom, mat);

	return mesh;
}

function createMuroEsternoSinistra(texture) {
	function drawShape() {
		var shape = new THREE.Shape();
			shape.moveTo(0,0);
			shape.lineTo(85,0);
			shape.lineTo(85,21);
			shape.lineTo(0,21);
			shape.lineTo(0,0);
		var hole1 = new THREE.Path();
			hole1.moveTo(19.6,17.45);
			hole1.lineTo(27.1,17.45);
			hole1.lineTo(27.1,9.1);
			hole1.lineTo(19.6,9.1);
			hole1.lineTo(19.6,17.45);
			shape.holes.push(hole1);
		var hole2 = new THREE.Path();
			hole2.moveTo(43,17.1);
			hole2.lineTo(50.6,17.1);
			hole2.lineTo(50.6,7);
			hole2.lineTo(43,7);
			hole2.lineTo(43,17.1);
			shape.holes.push(hole2);
		var hole3 = new THREE.Path();
			hole3.moveTo(68.96,17.7);
			hole3.lineTo(76.46,17.7);
			hole3.lineTo(76.46,9.2);
			hole3.lineTo(68.96,9.2);
			hole3.lineTo(68.96,17.7);
			shape.holes.push(hole3);
	
		return shape;

	}
	
	var shape1 = createMeshM(new THREE.ShapeGeometry(drawShape()),texture);
    shape1.material.map.wrapS = THREE.RepeatWrapping;
    shape1.material.map.wrapT = THREE.RepeatWrapping;

	return shape1;	
}

function createMuroEsternoRetro(texture) {
	function drawShape() {
		var shape = new THREE.Shape();
			shape.moveTo(0,0);
			shape.lineTo(94,0);
			shape.lineTo(94,21);
			shape.lineTo(0,21);
			shape.lineTo(0,0);
		var hole1 = new THREE.Path();
			hole1.moveTo(16,7);
			hole1.lineTo(16,17);
			hole1.lineTo(36,17);
			hole1.lineTo(36,7);
			hole1.lineTo(16,7);
			shape.holes.push(hole1);
		var hole2 = new THREE.Path();
			hole2.moveTo(63,7);
			hole2.lineTo(63,17);
			hole2.lineTo(83,17);
			hole2.lineTo(83,7);
			hole2.lineTo(63,7);
			shape.holes.push(hole2);
		
			return shape;
		}

	var shape1 = createMeshM(new THREE.ShapeGeometry(drawShape()), texture);
	// shape1.rotation.y = Math.PI/2;

        shape1.material.map.wrapS = THREE.RepeatWrapping;
        shape1.material.map.wrapT = THREE.RepeatWrapping;

		return shape1;	
}

function createMuroEsternoDestra(texture) {
		function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,0);
				shape.lineTo(85,0);
				shape.lineTo(85,21);
				shape.lineTo(0,21);
				shape.lineTo(0,0);
			var hole1 = new THREE.Path();
				hole1.moveTo(33.15,7);
				hole1.lineTo(40.7,7);
				hole1.lineTo(40.7,17);
				hole1.lineTo(33.15,17);
				hole1.lineTo(33.15,7);
				shape.holes.push(hole1);
			var hole2 = new THREE.Path();
				hole2.moveTo(56.5,7);
				hole2.lineTo(67.15,7);
				hole2.lineTo(67.15,17);
				hole2.lineTo(56.5,17);
				hole2.lineTo(56.5,7);
				shape.holes.push(hole2);

		return shape;
		}
		var shape1 = createMeshM(new THREE.ShapeGeometry(drawShape()), texture);
		shape1.material.map.wrapS = THREE.RepeatWrapping;
        shape1.material.map.wrapT = THREE.RepeatWrapping;

	return shape1;		
}

function createMuroEsternoFrontale(texture) {
		function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,0);
				shape.lineTo(94.1,0);
				shape.lineTo(94.1,21);
				shape.lineTo(0,21);
				shape.lineTo(0,0);
			var hole1 = new THREE.Path();
				hole1.moveTo(11.35,7.1);
				hole1.lineTo(25.9,7.1);
				hole1.lineTo(25.9,16.9);
				hole1.lineTo(11.35,16.9)
				hole1.lineTo(11.35,7.1);
				shape.holes.push(hole1);
			var hole2 = new THREE.Path(); 
				hole2.moveTo(39.7,1);
				hole2.lineTo(49.7,1);
				hole2.lineTo(49.7,18.5);
				hole2.lineTo(39.7,18.5);
				hole2.lineTo(39.7,1);
				shape.holes.push(hole2);
			var hole3 = new THREE.Path();
				hole3.moveTo(65.65,9.5);
				hole3.lineTo(80.35,9.5);
				hole3.lineTo(80.35,17.4);
				hole3.lineTo(65.65,17.4);
				hole3.lineTo(65.65,9.5);
				shape.holes.push(hole3);
		return shape;
		}
		var shape1 = createMeshM(new THREE.ShapeGeometry(drawShape()),texture);
        shape1.material.map.wrapS = THREE.RepeatWrapping;
        shape1.material.map.wrapT = THREE.RepeatWrapping;

	return shape1;		
}

function createMuroIngressoBagno(texture) {
	function drawShape() {
		var shape = new THREE.Shape();
			shape.moveTo(0,0);
			shape.lineTo(71.3,0);
			shape.lineTo(71.3,21);
			shape.lineTo(0,21);
			shape.lineTo(0,0);
		var hole1 = new THREE.Path();
			hole1.moveTo(6.2,1);
			hole1.lineTo(16,1);
			hole1.lineTo(16,18.4);
			hole1.lineTo(6.2,18.4);
			hole1.lineTo(6.2,1);
			shape.holes.push(hole1);	
		var hole2 = new THREE.Path();
			hole2.moveTo(32.1,1);
			hole2.lineTo(42,1);
			hole2.lineTo(42,18.4);
			hole2.lineTo(32.1,18.4);
			hole2.lineTo(32.1,1);
			shape.holes.push(hole2);
		var hole3 = new THREE.Path();
			hole3.moveTo(56.8,1);
			hole3.lineTo(66.7,1);
			hole3.lineTo(66.7,18.4);
			hole3.lineTo(56.8,18.4);
			hole3.lineTo(56.8,21);
			shape.holes.push(hole3);
	return shape;
	}

	var shape1 = createMeshM(new THREE.ShapeGeometry(drawShape()), texture);
        shape1.material.map.wrapS = THREE.RepeatWrapping;
        shape1.material.map.wrapT = THREE.RepeatWrapping;
		shape1.rotation.y = Math.PI/2;

	return shape1;
}


function createMuroIngressoSalone(texture) {
	function drawShape() {
		var shape = new THREE.Shape();
			shape.moveTo(0,0);
			shape.lineTo(70.5,0);
			shape.lineTo(70.5,21);
			shape.lineTo(0,21);
			shape.lineTo(0,0);
		var hole1 = new THREE.Path();
			hole1.moveTo(32,1);
			hole1.lineTo(42,1);
			hole1.lineTo(42,18);
			hole1.lineTo(32,18);
			hole1.lineTo(32,1);
			shape.holes.push(hole1);	
		var hole2 = new THREE.Path();
			hole2.moveTo(56.854,1);
			hole2.lineTo(65.754,1);
			hole2.lineTo(65.754,18);
			hole2.lineTo(56.854,18);
			hole2.lineTo(56.854,1);
			shape.holes.push(hole2);
	return shape;
		}

	var shape1 = createMeshM(new THREE.ShapeGeometry(drawShape()), texture);
        shape1.material.map.wrapS = THREE.RepeatWrapping;
        shape1.material.map.wrapT = THREE.RepeatWrapping;
		shape1.rotation.y = Math.PI/2;

	return shape1;
}


function createMuroCamereRetro(texture) {
	function drawShape() {
		var shape = new THREE.Shape();
			shape.moveTo(0,0);
			shape.lineTo(94,0);
			shape.lineTo(94,21);
			shape.lineTo(0,21);
			shape.lineTo(0,0);
		var hole1 = new THREE.Path();
			hole1.moveTo(16,7);
			hole1.lineTo(16,17);
			hole1.lineTo(36,17);
			hole1.lineTo(36,7);
			hole1.lineTo(16,7);
			shape.holes.push(hole1);
		var hole2 = new THREE.Path();
			hole2.moveTo(63,7);
			hole2.lineTo(63,17);
			hole2.lineTo(83,17);
			hole2.lineTo(83,7);
			hole2.lineTo(63,7);
			shape.holes.push(hole2);
	return shape;
	}

	var shape1 = createMeshM(new THREE.ShapeGeometry(drawShape()), texture);

        shape1.material.map.wrapS = THREE.RepeatWrapping;
        shape1.material.map.wrapT = THREE.RepeatWrapping;

		return shape1;	
}


function createMuroCamereSinistra(texture) {
		function drawShape() {
		var shape = new THREE.Shape();
			shape.moveTo(0,0);
			shape.lineTo(85,0);
			shape.lineTo(85,21);
			shape.lineTo(0,21);
			shape.lineTo(0,0);
		var hole1 = new THREE.Path();
			hole1.moveTo(19.6,17.45);
			hole1.lineTo(27.1,17.45);
			hole1.lineTo(27.1,9.4);
			hole1.lineTo(19.6,9.4);
			hole1.lineTo(19.6,17.45);
			shape.holes.push(hole1);
		var hole2 = new THREE.Path();
			hole2.moveTo(43,17.1);
			hole2.lineTo(50.6,17.1);
			hole2.lineTo(50.6,7);
			hole2.lineTo(43,7);
			hole2.lineTo(43,17.1);
			shape.holes.push(hole2);
		var hole3 = new THREE.Path();
			hole3.moveTo(68.96,17.7);
			hole3.lineTo(76.46,17.7);
			hole3.lineTo(76.46,9.4);
			hole3.lineTo(68.96,9.4);
			hole3.lineTo(68.96,17.7);
			shape.holes.push(hole3);
	
	return shape;
	}

	var shape1 = createMeshM(new THREE.ShapeGeometry(drawShape()),texture);
    shape1.material.map.wrapS = THREE.RepeatWrapping;
    shape1.material.map.wrapT = THREE.RepeatWrapping;

	return shape1;	
}


function createMuroCamereSinistraCorridoio(texture) {
	function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,0);
				shape.lineTo(71.75,0);
				shape.lineTo(71.75,21);
				shape.lineTo(0,21);
				shape.lineTo(0,0);
			var hole1 = new THREE.Path();
				hole1.moveTo(6.2,1);
				hole1.lineTo(16.3,1);
				hole1.lineTo(16.3,18.45);
				hole1.lineTo(6.2,18.45);
				hole1.lineTo(6.2,1);
				shape.holes.push(hole1);	
			var hole2 = new THREE.Path();
				hole2.moveTo(32.1,1);
				hole2.lineTo(42.1,1);
				hole2.lineTo(42.1,18.45);
				hole2.lineTo(32.1,18.45);
				hole2.lineTo(32.1,1);
				shape.holes.push(hole2);
			var hole3 = new THREE.Path();
				hole3.moveTo(56.8,1);
				hole3.lineTo(66.8,1);
				hole3.lineTo(66.8,18.45);
				hole3.lineTo(56.8,18.45);
				hole3.lineTo(56.8,21);
				shape.holes.push(hole3);
		return shape;
		}

	var shape1 = createMeshM(new THREE.ShapeGeometry(drawShape()), texture);
        shape1.material.map.wrapS = THREE.RepeatWrapping;
        shape1.material.map.wrapT = THREE.RepeatWrapping;
		shape1.rotation.y = Math.PI/2;

	return shape1;
}


function createMuroGrandeCamereSx(texture) {
		function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,0);
				shape.lineTo(94,0);
				shape.lineTo(94,21);
				shape.lineTo(0,21);
				shape.lineTo(0,0);
			var hole1 = new THREE.Path();
				hole1.moveTo(36,.5);
				hole1.lineTo(36,21);
				hole1.lineTo(52,21);
				hole1.lineTo(52,.5);
				hole1.lineTo(36,.5);
				shape.holes.push(hole1);
		return shape;
		}		

		var shape1 = createMeshM(new THREE.ShapeGeometry(drawShape()),texture);
        shape1.material.map.wrapS = THREE.RepeatWrapping;
        shape1.material.map.wrapT = THREE.RepeatWrapping;

		return shape1;	

}

function createMuroCortoIngresso(texture) {
		function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,0);
				shape.lineTo(17,0);
				shape.lineTo(17,21);
				shape.lineTo(0,21);
				shape.lineTo(0,0);
			var hole1 = new THREE.Path();
				hole1.moveTo(8,.1);
				hole1.lineTo(10,.1);
				hole1.lineTo(10,.4);
				hole1.lineTo(8,.4);
				hole1.lineTo(8,.1);
				shape.holes.push(hole1);
		return shape;
		}		

		var shape1 = createMeshM(new THREE.ShapeGeometry(drawShape()),texture);
        shape1.material.map.wrapS = THREE.RepeatWrapping;
        shape1.material.map.wrapT = THREE.RepeatWrapping;

		return shape1;	
}

function createMuroCortoCamera(texture) {
		function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,0);
				shape.lineTo(13,0);
				shape.lineTo(13,21);
				shape.lineTo(0,21);
				shape.lineTo(0,0);
			var hole1 = new THREE.Path();
				hole1.moveTo(8,.1);
				hole1.lineTo(10,.1);
				hole1.lineTo(10,.4);
				hole1.lineTo(8,.4);
				hole1.lineTo(8,.1);
				shape.holes.push(hole1);
		return shape;
		}		

		var shape1 = createMeshM(new THREE.ShapeGeometry(drawShape()),texture);
        shape1.material.map.wrapS = THREE.RepeatWrapping;
        shape1.material.map.wrapT = THREE.RepeatWrapping;

		return shape1;	

}

function createMuroSxLarge(texture) {
		function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,0);
				shape.lineTo(36,0);
				shape.lineTo(36,21);
				shape.lineTo(0,21);
				shape.lineTo(0,0);
			var hole1 = new THREE.Path();
				hole1.moveTo(0,0);
				hole1.lineTo(0,2);
				hole1.lineTo(.2,2);
				hole1.lineTo(.2,0);
				hole1.lineTo(0,0);
				shape.holes.push(hole1);
		return shape;
		}		

		var shape1 = createMeshM(new THREE.ShapeGeometry(drawShape()),texture);
        shape1.material.map.wrapS = THREE.RepeatWrapping;
        shape1.material.map.wrapT = THREE.RepeatWrapping;

		return shape1;	
}


function createMuroDxLarge(texture) {
		function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,0);
				shape.lineTo(41,0);
				shape.lineTo(41,21);
				shape.lineTo(0,21);
				shape.lineTo(0,0);
			var hole1 = new THREE.Path();
				hole1.moveTo(0,0);
				hole1.lineTo(0,2);
				hole1.lineTo(.2,2);
				hole1.lineTo(.2,0);
				hole1.lineTo(0,0);
				shape.holes.push(hole1);
		return shape;
		}		

		var shape1 = createMeshM(new THREE.ShapeGeometry(drawShape()),texture);
        shape1.material.map.wrapS = THREE.RepeatWrapping;
        shape1.material.map.wrapT = THREE.RepeatWrapping;

		return shape1;	
}

function createMuroDxSalone(texture) {
		function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,0);
				shape.lineTo(30,0);
				shape.lineTo(30,21);
				shape.lineTo(0,21);
				shape.lineTo(0,0);
			var hole1 = new THREE.Path();
				hole1.moveTo(11.65,7.5);
				hole1.lineTo(18.2,7.5);
				hole1.lineTo(18.2,17);
				hole1.lineTo(11.65,17);
				hole1.lineTo(11.65,7.5);
				shape.holes.push(hole1);
		return shape;
		}		

		var shape1 = createMeshM(new THREE.ShapeGeometry(drawShape()),texture);
        shape1.material.map.wrapS = THREE.RepeatWrapping;
        shape1.material.map.wrapT = THREE.RepeatWrapping;

		return shape1;	
}

function createMuroBagnoPorta(texture) {
	function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,0);
				shape.lineTo(30,0);
				shape.lineTo(30,21);
				shape.lineTo(0,21);
				shape.lineTo(0,0);
			var hole1 = new THREE.Path();
				hole1.moveTo(10,1);
				hole1.lineTo(20,1);
				hole1.lineTo(20,18.45);
				hole1.lineTo(10,18.45);
				hole1.lineTo(10,1);
				shape.holes.push(hole1);	
		return shape;
		}

	var shape1 = createMeshM(new THREE.ShapeGeometry(drawShape()), texture);
        shape1.material.map.wrapS = THREE.RepeatWrapping;
        shape1.material.map.wrapT = THREE.RepeatWrapping;
	shape1.rotation.y = Math.PI/2;

	return shape1;
}

function createMuroCameraPorta(texture) {
		function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,0);
				shape.lineTo(37,0);
				shape.lineTo(37,21);
				shape.lineTo(0,21);
				shape.lineTo(0,0);
			var hole1 = new THREE.Path();
				hole1.moveTo(11.5,7);
				hole1.lineTo(26,7);
				hole1.lineTo(26,17);
				hole1.lineTo(11.5,17)
				hole1.lineTo(11.5,7);
				shape.holes.push(hole1);
			
		return shape;
		}
		var shape1 = createMeshM(new THREE.ShapeGeometry(drawShape()),texture);
        shape1.material.map.wrapS = THREE.RepeatWrapping;
        shape1.material.map.wrapT = THREE.RepeatWrapping;

	return shape1;		
}

function createMuroPiccoloCucina(texture) {
		function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,0);
				shape.lineTo(20,0);
				shape.lineTo(20,21);
				shape.lineTo(0,21);
				shape.lineTo(0,0);
			var hole1 = new THREE.Path();
				hole1.moveTo(0,0);
				hole1.lineTo(0,2);
				hole1.lineTo(.2,2);
				hole1.lineTo(.2,0);
				hole1.lineTo(0,0);
				shape.holes.push(hole1);
		return shape;
		}		

		var shape1 = createMeshM(new THREE.ShapeGeometry(drawShape()),texture);
        shape1.material.map.wrapS = THREE.RepeatWrapping;
        shape1.material.map.wrapT = THREE.RepeatWrapping;

		return shape1;	

}

function createMuroSxSalone(texture) {
	function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,0);
				shape.lineTo(30,0);
				shape.lineTo(30,21);
				shape.lineTo(0,21);
				shape.lineTo(0,0);

			var hole1 = new THREE.Path();
				hole1.moveTo(10,1);
				hole1.lineTo(19.8,1);
				hole1.lineTo(19.8,18.45);
				hole1.lineTo(10.2,18.45);
				hole1.lineTo(10.2,1);
				shape.holes.push(hole1);

		return shape;
		}

	var shape1 = createMeshM(new THREE.ShapeGeometry(drawShape()), texture);
	shape1.rotation.y = Math.PI/2;

	return shape1;
}

function createMuroScrigno(texture) {
	function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,0);
				shape.lineTo(40,0);
				shape.lineTo(40,21);
				shape.lineTo(0,21);
				shape.lineTo(0,0);
			var hole1 = new THREE.Path();
				hole1.moveTo(12.3,1);
				hole1.lineTo(27.3,1);
				hole1.lineTo(27.3,18.45);
				hole1.lineTo(12.3,18.45);
				hole1.lineTo(12.3,1);
				shape.holes.push(hole1);		
		return shape;
		}

	var shape1 = createMeshM(new THREE.ShapeGeometry(drawShape()), texture);

	return shape1;
}

function createMuroFinestraCucina(texture) {
		function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,0);
				shape.lineTo(40,0);
				shape.lineTo(40,21);
				shape.lineTo(0,21);
				shape.lineTo(0,0);
			var hole1 = new THREE.Path();
				hole1.moveTo(12.5,9.4);
				hole1.lineTo(27,9.4);
				hole1.lineTo(27,17);
				hole1.lineTo(12.5,17)
				hole1.lineTo(12.5,9.4);
				shape.holes.push(hole1);
		return shape;
		}
		var shape1 = createMeshM(new THREE.ShapeGeometry(drawShape()),texture);
        shape1.material.map.wrapS = THREE.RepeatWrapping;
        shape1.material.map.wrapT = THREE.RepeatWrapping;

	return shape1;		
}


function createMuroFinestraCameraDx(texture) {
		function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,0);
				shape.lineTo(31,0);
				shape.lineTo(31,21);
				shape.lineTo(0,21);
				shape.lineTo(0,0);
			var hole1 = new THREE.Path();
				hole1.moveTo(3.6,7.1);
				hole1.lineTo(13.8,7.1);
				hole1.lineTo(13.8,16.9);
				hole1.lineTo(3.6,16.9);
				hole1.lineTo(3.6,7.1);
				shape.holes.push(hole1);

		return shape;
		}
		var shape1 = createMeshM(new THREE.ShapeGeometry(drawShape()), texture);
		shape1.material.map.wrapS = THREE.RepeatWrapping;
        shape1.material.map.wrapT = THREE.RepeatWrapping;

	return shape1;		
}

function createMuroPortaCameraDx(texture) {
	function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,0);
				shape.lineTo(31,0);
				shape.lineTo(31,21);
				shape.lineTo(0,21);
				shape.lineTo(0,0);
			var hole1 = new THREE.Path();
				hole1.moveTo(3.7,1);
				hole1.lineTo(13,1);
				hole1.lineTo(13,18.45);
				hole1.lineTo(3.7,18.45);
				hole1.lineTo(3.7,1);
				shape.holes.push(hole1);
		return shape;
		}

	var shape1 = createMeshM(new THREE.ShapeGeometry(drawShape()), texture);
        shape1.material.map.wrapS = THREE.RepeatWrapping;
        shape1.material.map.wrapT = THREE.RepeatWrapping;
	return shape1;
}

function createMuroCortoPorta(texture) {
		function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,0);
				shape.lineTo(17,0);
				shape.lineTo(17,21);
				shape.lineTo(0,21);
				shape.lineTo(0,0);
			var hole1 = new THREE.Path();
				hole1.moveTo(3.5,1);
				hole1.lineTo(13.5,1);
				hole1.lineTo(13.5,18.5);
				hole1.lineTo(3.5,18.5);
				hole1.lineTo(3.5,1);
				shape.holes.push(hole1);
		return shape;
		}		

		var shape1 = createMeshM(new THREE.ShapeGeometry(drawShape()),texture);
        shape1.material.map.wrapS = THREE.RepeatWrapping;
        shape1.material.map.wrapT = THREE.RepeatWrapping;

		return shape1;	
}

function createMuroSxBagno(texture) {
		function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,0);
				shape.lineTo(31,0);
				shape.lineTo(31,21);
				shape.lineTo(0,21);
				shape.lineTo(0,0);
			var hole1 = new THREE.Path();
				hole1.moveTo(13,17.1);
				hole1.lineTo(20.5,17.1);
				hole1.lineTo(20.5,7);
				hole1.lineTo(13,7);
				hole1.lineTo(13,17.1);
				shape.holes.push(hole1);
		
		return shape;

		}
	
		var shape1 = createMeshM(new THREE.ShapeGeometry(drawShape()),texture);
        shape1.material.map.wrapS = THREE.RepeatWrapping;
        shape1.material.map.wrapT = THREE.RepeatWrapping;

		return shape1;	
}