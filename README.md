# AerialViewGenerator
Download satellite tiles and emulate the view from a camera mounted on a UAV pointing down ([nadir](https://en.wikipedia.org/wiki/Nadir)). All the images downloaded are cached locally to preserve the remote server (so you don't get banned!).


## Install it:
```
$ pip install git+https://github.com/ricardodeazambuja/AerialViewGenerator
```

## If you don't know which tile server to use, install `xyzservices`:
```
$ pip install -q xyzservices
```
and
```
from aerialviewgenerator import AerialView
basemaps = AerialView.getBasemaps()

# check available free tile servers
print(basemaps.keys())
```
The available maps vary the zoom levels offered. Examples of tile server URL (you need to fill any field besides the `z`, `x`, and `y` ones):
* `basemaps['OpenStreetMap.Mapnik']` : `https://tile.openstreetmap.org/{z}/{x}/{y}.png`
* `basemaps['GeoportailFrance.orthos']` : `https://wxs.ign.fr/{apikey}/geoportail/wmts?REQUEST=GetTile&SERVICE=WMTS&VERSION=1.0.0&STYLE={style}&TILEMATRIXSET={TileMatrixSet}&FORMAT={format}&LAYER={variant}&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}`
* `basemaps['USGS.USImagery']` : `https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}`
* `basemaps['Esri.WorldImagery']`: `https://server.arcgisonline.com/ArcGIS/rest/services/{variant}/MapServer/tile/{z}/{y}/{x}`

Another place to check online is the [Leaflet providers preview](https://leaflet-extras.github.io/leaflet-providers/preview/index.html)

Finally, search online and you will find other map tile servers that are available.

## How to use it

Depending on your tile server, certain zoom levels will be available. Usually some non-free providers will offer a maximum of up to 20, but for the free ones the zoom goes up to 19. Below is an example for image from France:
```
from aerialviewgenerator.aerialview import AerialView

baseurl = 'https://wxs.ign.fr/choisirgeoportail/geoportail/wmts?REQUEST=GetTile&SERVICE=WMTS&VERSION=1.0.0&STYLE=normal&TILEMATRIXSET=PM&FORMAT=image/jpeg&LAYER=ORTHOIMAGERY.ORTHOPHOTOS&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}'
avg = AerialView(zoom=20, baseurl=baseurl)

altitude = 300
bearing = 0 # world map, not local coordinates
fov = 60
lat, lon = 48.858327718853104, 2.294309636169546
img = avg.getAerialImage(lat, lon, bearing, altitude, fov, output_size=(512,512))
img.show()
```
![image](https://github.com/ricardodeazambuja/AerialViewGenerator/assets/6606382/4b598c88-4857-4c13-912c-f8316f24205c)

## Examples
The only example available, so far, is [this notebook](https://github.com/ricardodeazambuja/AerialViewGenerator/blob/main/Example.ipynb). You can test it directly on google colab: 
[![Example](https://camo.githubusercontent.com/84f0493939e0c4de4e6dbe113251b4bfb5353e57134ffd9fcab6b8714514d4d1/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/github/ricardodeazambuja/AerialViewGenerator/blob/main/Example.ipynb)
