import maya.cmds as cmds

class pyUI_():
    def __init__(self):
        self.filelist = cmds.ls(type="file")

        if (cmds.window('change Name', exists=True)):
            cmds.deleteUI('change Name', exists=True)

        # make UI
        self.window_ = cmds.window('change Name', resizeToFitChildren=True)
        cmds.columnLayout()
        cmds.text(label="This Tool is rename Tool for minju")

        # lineFiled
        cmds.textFieldGrp('obj1', label='Name', text="test")
        cmds.textFieldGrp('obj2', label='ChangeName')
        cmds.rowColumnLayout(numberOfColumns=3)
        # make Button
        cmds.button(label="Apply", command=self.textName)
        cmds.button(label="reFresh", command=self.texReload)
        cmds.showWindow(self.window_)

    def textName(self, evt):
        filelist = self.filelist

        empty_name = []
        or_ = cmds.textFieldGrp('obj1', query=True, tx=True)
        ch_ = cmds.textFieldGrp('obj2', query=True, tx=True)

        cmds.filePathEditor(refresh=True)
        for i in filelist:
            fPath = cmds.getAttr(i + ".fileTextureName")
            print
            fPath, i + ".fileTextureName"
            setName = cmds.filePathEditor(i + ".fileTextureName", replaceField="nameOnly", replaceString=(or_, ch_),
                                          replaceAll=True)
        self.texReload
        return setName

    def texReload(self):
        for tex in pm.ls(type='file'):
            filePath = tex.fileTextureName.get()
            if not filePath:
                continue
            tex.fileTextureName.set(filePath)


show = pyUI_()

