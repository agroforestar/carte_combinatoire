# Parseur

**Sequence diagram:**

```plantuml
@startuml

top to bottom direction
skinparam linetype ortho

class node2 as "Parseur.Plant" {
   yMin: 
   uCode: 
   yMax: 
   x: 
   y: 
   xMax: 
   type: 
   xMin: 
   __init__(self, data): 
}
class object {
   __doc__: 
   __dict__: 
   __slots__: 
   __module__: 
   __annotations__: 
   __class__(self: _T): 
   __class__(self, __type: Type[object]): 
   __init__(self): 
   __new__(cls: Type[_T]): 
   __setattr__(self, name: str, value: Any): 
   __eq__(self, o: object): 
   __ne__(self, o: object): 
   __str__(self): 
   __repr__(self): 
   __hash__(self): 
   __format__(self, format_spec: str): 
   __getattribute__(self, name: str): 
   __delattr__(self, name: str): 
   __sizeof__(self): 
   __reduce__(self): 
   __reduce_ex__(self, protocol: SupportsIndex): 
   __reduce_ex__(self, protocol: int): 
   __dir__(self): 
   __init_subclass__(cls): 
}

node2   ^-[#595959,plain]-  object 
@enduml
````

# Fonctions

### ReadTxt(path)

#### Donne les lignes d'un fichier .txt

<blockquote>

_paramètres_ :\
&emsp; path : le fichier .txt visé
    
_returns_ :\
&emsp; list[] : lignes du fichier

</blockquote>

<p>&nbsp;</p>

### GetPointsFromPoint(point_central, distance)
#### Donne 4 autre points autour du point central à partir d'une distance 

<blockquote>

_paramètres_ :\
&emsp; point_central : (x, y)

&emsp; distance : distance voulu entre les points

_returns_ :\
&emsp; points[] : liste qui comporte 4 tuple (x, y)

</blockquote>

<p>&nbsp;</p>

### GetPointsFromArea(plant)
#### Donne les 4 extrémités de la surface

<blockquote>

_paramètres_ :\
&emsp; plante : l'objet plante qui est une surface

_returns_ :\
&emsp; points[] : liste qui comporte 4 tuple (x, y)

</blockquote>

<p>&nbsp;</p>

### Convert(plants, map)
#### Met à jour la map (Graph) à partir des plantes

<blockquote>

_paramètres_ :\
&emsp; plants : plants[]

&emsp; map : map

_returns_ :\
&emsp; map : map passée en paramètres mise à jour

</blockquote>

<p>&nbsp;</p>

### Parse(path, map)
#### Fonction principale qui gère la mise à jour de la map et la création des plantes

<blockquote>

_paramètres_ :\
&emsp; path : chemin d'accès du fichier .txt

&emsp; map : map crée au préalable ```nMap()```

_returns_ :\
&emsp; map : map passée en paramètres mise à jour

</blockquote>

