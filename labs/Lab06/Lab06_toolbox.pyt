# -*- coding: utf-8 -*-

import arcpy
import time

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [RenderTool]

class RenderTool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName="Your working project",
            name="workProject",
            datatype="DEFile",
            parameterType="Required",
            direction="Input"
        )

        param1 = arcpy.Parameter(
            displayName="Name of layer you want to render",
            name="layername",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )

        param2 = arcpy.Parameter(
            displayName="Folder of the new project for saving the render layer",
            name="newprojectfolder",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input"
        )

        param3 = arcpy.Parameter(
            displayName="Name of the new project for saving the render layer",
            name="newprojectname",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        params = [param0, param1, param2, param3]
        return params
    
    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return
    
    def execute(self, parameters, messages):
        """The source code of the tool."""
        # define progressor variables
        readTime = 2.5
        start = 0
        maximum = 100
        step = 25

        # set up the progressor
        arcpy.SetProgressor("step", "Checking project and layer...", start, maximum, step)
        time.sleep(readTime)
        # add message to results pane
        arcpy.AddMessage("Checking project and layer...")

        # reference to .aprx
        aprxFileAddress = parameters[0].valueAsText
        project = arcpy.mp.ArcGISProject(aprxFileAddress)
        layername = parameters[1].valueAsText
        # grab layer in . aprx
        if layername == 'GarageParking':
            layer = project.listMaps('Map')[0].listLayers()[1]
            symbology = layer.symbology
        
            # increment progressor and change label + add message
            arcpy.SetProgressorPosition(start + step)
            arcpy.SetProgressorLabel("start to update render...")
            time.sleep(readTime)
            arcpy.AddMessage("start to update render...")

            # update copy's renderer to be 'GraduatedColorsRenderer"
            symbology.updateRenderer('GraduatedColorsRenderer')
            # field for choropleth
            symbology.renderer.classificationField = "Shape_Area"

            # increment progressor and change label + add message
            arcpy.SetProgressorPosition(start + step + step)
            arcpy.SetProgressorLabel("setting render...")
            time.sleep(readTime)
            arcpy.AddMessage("setting render...")       

            # set how many classes
            symbology.renderer.breakCount = 5
            # set color map
            symbology.renderer.colorRamp = project.listColorRamps('Oranges (5 Classes)')[0]
            # set the layer's actual symbology equal to the copy
            layer.symbology = symbology

            # increment progressor and change label + add message
            arcpy.SetProgressorPosition(maximum)
            arcpy.SetProgressorLabel("saving project...")
            time.sleep(readTime)
            arcpy.AddMessage("saving project...") 

        if layername == 'Structures':
            layer = project.listMaps('Map')[0].listLayers()[0]
            symbology = layer.symbology

            # increment progressor and change label + add message
            arcpy.SetProgressorPosition(start + step)
            arcpy.SetProgressorLabel("start to update render...")
            time.sleep(readTime)
            arcpy.AddMessage("start to update render...")

            # update copy's renderer to be 'UniqueValuesRenderer"
            symbology.updateRenderer('UniqueValueRenderer')

            # increment progressor and change label + add message
            arcpy.SetProgressorPosition(start + step + step)
            arcpy.SetProgressorLabel("setting render...")
            time.sleep(readTime)
            arcpy.AddMessage("setting render...")       

            # use 'Type' as unique value
            symbology.renderer.fields = ["Type"]
            # set the layer's actual symbology equal to the copy
            layer.symbology = symbology

            # increment progressor and change label + add message
            arcpy.SetProgressorPosition(maximum)
            arcpy.SetProgressorLabel("saving project...")
            time.sleep(readTime)
            arcpy.AddMessage("saving project...") 

        else:
            arcpy.AddMessage("We can't work with this layer.")

        newprojectpath = parameters[2].valueAsText + "\\" + parameters[3].valueAsText
        project.saveACopy(newprojectpath)
        arcpy.AddMessage("Done!")
        return
    
    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return