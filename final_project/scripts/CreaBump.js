function creaQuadro (nome) {
  var quadro = new THREE.Object3D();
  var plane = createMesh(new THREE.BoxGeometry(10, 5, .1), nome + ".jpg", nome + "-bump.jpg");  //si sceglie la texture da inserire
  quadro.add(plane);

  return quadro;
};

function createMesh(geom, imageFile, bump) {
  var texture = THREE.ImageUtils.loadTexture("textures/" + imageFile)
  var mat = new THREE.MeshPhongMaterial();
  mat.map = texture;
  
  if(bump){
    var bump = THREE.ImageUtils.loadTexture("textures/" + bump)
    mat.bumpMap = bump;
    mat.bumpScale = 80;
  }

  var mesh = new THREE.Mesh(geom, mat);
  return mesh;
}