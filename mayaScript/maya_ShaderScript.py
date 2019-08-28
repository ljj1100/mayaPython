import maya.cmds as mc
from maya.cmds import hyperShade


class Error(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt


class ShaderSetting():
    def __init__(self):
        self.f_GeoList = []
        self.s_GeoList = []
        self.selectedGEOFirst()

        # print(self.shaderAndList(self.selected_GEO))

    def selectedGEOFirst(self):
        self.window_ = mc.window("First Selected", resizeToFitChildren=1)
        mc.columnLayout(adjustableColumn=True)

        mc.button(label='First Select', command=(self.firstButton))
        mc.button(label='Second Select', command=(self.secondButton))
        mc.button(label='close', command=(self.closeButton))

        mc.showWindow(self.window_)

    def firstButton(self, evt):
        selected_GEO = mc.ls(dag=1, o=1, s=1, sl=1)
        mc.warning("{}".format(selected_GEO))
        self.f_GeoList.append(selected_GEO)
        self.f_GeoList = self.f_GeoList[-1]

    def secondButton(self, evt):
        selected_GEO = mc.ls(dag=1, o=1, s=1, sl=1)
        mc.warning("{}".format(selected_GEO))
        self.s_GeoList.append(selected_GEO)
        self.s_GeoList = self.s_GeoList[-1]

        if len(self.f_GeoList) <= len(self.s_GeoList):
            for num, i in enumerate(self.s_GeoList):
                self.shaderAndList(self.f_GeoList[num], i)

        else:
            raise Error("This is not same that object number")

    def closeButton(self, evt):

        mc.deleteUI(self.window_)

    def shaderAndList(self, first_selectedGeo, second_selectedGeo):
        geo_shaderList = mc.listConnections(first_selectedGeo, type='shadingEngine')
        geo_shader = mc.ls(mc.listConnections(geo_shaderList), materials=1)

        mc.select(second_selectedGeo)
        mc.hyperShade(assign=geo_shader[0])


show = ShaderSetting()