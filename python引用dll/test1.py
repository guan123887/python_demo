import clr
clr.FindAssembly('MapControlApplication1')
clr.FindAssembly('ESRI.ArcGIS.ADF.Local')
clr.FindAssembly('ESRI.ArcGIS.AxControls')
clr.FindAssembly('ESRI.ArcGIS.Carto')
clr.FindAssembly('ESRI.ArcGIS.Controls')
clr.FindAssembly('ESRI.ArcGIS.Display')
clr.FindAssembly('ESRI.ArcGIS.System')
clr.FindAssembly('ESRI.ArcGIS.SystemUI')
clr.FindAssembly('ESRI.ArcGIS.Version')
from MapControlApplication1 import *
# from ESRI.ArcGIS.ADF.Local import *
# from ESRI.ArcGIS.AxControls import *
# from ESRI.ArcGIS.Carto import *
# from ESRI.ArcGIS.Controls import *
# from ESRI.ArcGIS.Display import *
# from ESRI.ArcGIS.System import *
# from ESRI.ArcGIS.SystemUI import *
# from ESRI.ArcGIS.Version import *
ins=Program()
print(ins.add(6,10))
print(ins.Main())