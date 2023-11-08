
import arcpy
import os

### geodatabase ###
folder_path = r'C:\Users\canov\OneDrive\Desktop\GIS_676\Canova-GIS-676'
gdb_name = 'GIS_676_Lab05.gdb'
gdb_path = folder_path + '\\' + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)