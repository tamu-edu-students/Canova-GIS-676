
import arcpy
import os

### geodatabase ###
folder_path = r'C:\Users\canov\OneDrive\Desktop\GIS_676\Canova-GIS-676'
gdb_name = 'GIS_676_Lab04.gdb'
gdb_path = folder_path + '\\' + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)

### read csv file, convert to layer, put in gdb ###
csv_path = r'C:\Users\canov\OneDrive\Desktop\GIS_676\Canova-GIS-676\labs\Lab04\Lab04_Data\garages.csv'
garage_layer_name = 'GaragePoints'
garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layer_name)

### add garages to gdb ###
input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)

### add GaragePoints layer to gdb ###
garage_points = gdb_path + '\\' + garage_layer_name

##### copy building feature in Campus.gdb to lab4 gdb #####

### open campus gdb and obtain building feature ###
campus = r'C:\Users\canov\OneDrive\Desktop\GIS_676\Canova-GIS-676\labs\Lab04\Lab04_Data\Campus.gdb'
buildings_campus = campus + '\\' + 'Structures'

### destination path for building feature A
buildings = gdb_path + '\\' + 'Buildings'

### copy ###
arcpy.Copy_management(buildings_campus, buildings)

##### project GaragePoints layer tobuilding layer #####

### building layer projection ###
spatial_ref = arcpy.Describe(buildings).spatialReference

### garage layer projection ###
arcpy.Project_management(garage_points, os.path.join(gdb_path, 'Garage_Points_reprojected'), spatial_ref)

##### spatial analysis on building and garage points #####

### garage buffer ###
garageBuffered = arcpy.Buffer_analysis(gdb_path + '\\' + 'Garage_Points_reprojected', gdb_path + '\\' + 'Garage_Points_buffered', 150)

### intersect buffer with buildings ###
arcpy.Intersect_analysis([garageBuffered, buildings], gdb_path + '\Garage_Building_Intersection', 'ALL')

### output to csv ###
arcpy.TableToTable_conversion(gdb_path + '\Garage_Building_Intersection.dbf', r'C:\Users\canov\OneDrive\Desktop\GIS_676\Canova-GIS-676\labs\Lab04\Lab04_Data', 'nearbyBuildings.csv')