---
title: "assimp"
date: 2022-06-15T08:56:33+02:00
status: "open"
draft: false
tags: ["Beginner", "Tutorial", "assimp", "3D"]
menu: 
  main:
    identifier: "assimp"
    title: "Asset-Importer-Lib (assimp)"
    weight: 870
    parent: "thirdparty"
---
# Asset-Importer-Lib (assimp) {#assimp}
## Introduction
[Assimp](http://www.assimp.org "assimp") (Asset-Importer-Lib) is a library to load and process geometric scenes from various 3D data formats.

This chapter provides some examples of how 3D formats can be imported into MeVisLab. In general you always need a `SoSceneLoader` module. The `SoSceneLoader` allows to load meshes as Open Inventor points/lines/triangles/faces using the Open Asset Import Library.

![SoSceneLoader](/images/tutorials/thirdparty/SoSceneLoader.png "SoSceneLoader")

You can also use the `SoSceneWriter` module to export your 3D scenes from MeVisLab into any of the output formats listed below.

## File formats
The Assimp-Lib currently supports the following [file formats](https://assimp-docs.readthedocs.io/en/v5.1.0/about/introduction.html):

* 3D Manufacturing Format (.3mf)
* Collada (.dae, .xml)
* Blender (.blend)
* Biovision BVH (.bvh)
* 3D Studio Max 3DS (.3ds)
* 3D Studio Max ASE (.ase)
* glTF (.glTF)
* glTF2.0 (.glTF)
* KHR_lights_punctual ( 5.0 )
* KHR_materials_pbrSpecularGlossiness ( 5.0 )
* KHR_materials_unlit ( 5.0 )
* KHR_texture_transform ( 5.1 under test )
* FBX-Format, as ASCII and binary (.fbx)
* Stanford Polygon Library (.ply)
* AutoCAD DXF (.dxf)
* IFC-STEP (.ifc)
* Neutral File Format (.nff)
* Sense8 WorldToolkit (.nff)
* Valve Model (.smd, .vta)
* Quake I (.mdl)
* Quake II (.md2)
* Quake III (.md3)
* Quake 3 BSP (.pk3)
* RtCW (.mdc)
* Doom 3 (.md5mesh, .md5anim, .md5camera)
* DirectX X (.x)
* Quick3D (.q3o, .q3s)
* Raw Triangles (.raw)
* AC3D (.ac, .ac3d)
* Stereolithography (.stl)
* Autodesk DXF (.dxf)
* Irrlicht Mesh (.irrmesh, .xml)
* Irrlicht Scene (.irr, .xml)
* Object File Format ( .off )
* Wavefront Object (.obj)
* Terragen Terrain ( .ter )
* 3D GameStudio Model ( .mdl )
* 3D GameStudio Terrain ( .hmp )
* Ogre ( .mesh.xml, .skeleton.xml, .material )
* OpenGEX-Fomat (.ogex)
* Milkshape 3D ( .ms3d )
* LightWave Model ( .lwo )
* LightWave Scene ( .lws )
* Modo Model ( .lxo )
* CharacterStudio Motion ( .csm )
* Stanford Ply ( .ply )
* TrueSpace (.cob, .scn)
* XGL-3D-Format (.xgl)
