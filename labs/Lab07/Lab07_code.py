
import arcpy

data_input = r'C:\\Users\\canov\\OneDrive\\Desktop\\GIS_676\\Canova-GIS-676\\labs\\Lab07\\Lab07_Data\\'
data_output = r'C:\\Users\\canov\\OneDrive\\Desktop\\GIS_676\\Canova-GIS-676\\labs\\Lab07\\Lab07_Results\\'
band1 = arcpy.sa.Raster(data_input + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B1.TIF") # blue
band2 = arcpy.sa.Raster(data_input + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B2.TIF") # green
band3 = arcpy.sa.Raster(data_input + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B3.TIF") # red
band4 = arcpy.sa.Raster(data_input + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B4.TIF") # NIR

# composite bands
composite = arcpy.CompositeBands_management([band1,band2,band3,band4], data_output + "combined.tif")

# hillshade from DEM
azimuth = 315
altitude = 45
shadows = "NO_SHADOWS"
z_factor = 1
arcpy.ddd.HillShade(data_input + r'\n30_w097_1arc_v3.tif', data_output + r'\hillshade.tif', azimuth, altitude, shadows, z_factor)

# slope from DEM
output_measurement = "DEGREE"
z_factor = 1
arcpy.ddd.Slope(data_input + r'\n30_w097_1arc_v3.tif', data_output + r'\slopes.tif', output_measurement, z_factor)