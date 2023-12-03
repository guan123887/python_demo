from qgis.analysis import QgsNativeAlgorithms
from qgis.core import QgsApplication
import sys
#相对路径
# gis_path = sys.executable
# process_path = qgis_path.split('apps')[0] + 'apps\qgis\python\plugins'
# sys.path.append(process_path)
#绝对路径
sys.path.append(r'D:\QGIS\apps\qgis\python\plugins')  # processing是插件！！
import processing
from processing.core.Processing import Processing
qgs = QgsApplication([], False)
qgs.initQgis()
Processing.initialize()
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())

parameters={'INPUT':r'C:\Users\gzk\Desktop\QGIS_DATA\rainbi.shp','OVERLAY':r'C:\Users\gzk\Desktop\QGIS_DATA\first_data.shp','OUTPUT':r'C:\Users\gzk\Desktop\QGIS_DATA\output.shp'}
processing.run('native:clip',parameters)

qgs.exitQgis()