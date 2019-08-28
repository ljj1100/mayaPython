import sys
# Qt Import
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

import maya.cmds as mc
import json
import os

#### environ script path ####
script_path = os.environ['MAYA_APP_DIR'] + "/scripts"

class FindFolderTxt(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        global script_path

        self.main_layout = QBoxLayout(QBoxLayout.TopToBottom,self)
        self.initWidget()

    def initWidget(self):
        self.setWindowTitle("Hey")
        # combobox
        self.makeLineEdit()
        self.makeComboBox()
        self.makePushButton()

    def makeLineEdit(self):
        grp_1 = QGroupBox("Make .txt File")
        self.main_layout.addWidget(grp_1)

        base = QBoxLayout(QBoxLayout.TopToBottom,self)
        base_button_layout = QBoxLayout(QBoxLayout.TopToBottom,self)
        base_layout = QBoxLayout(QBoxLayout.TopToBottom,self)
        # push button
        qb_4 = QPushButton()
        qb_4.setText("save")
        qb_4.clicked.connect(self.save)
        base_button_layout.addWidget(qb_4)
        # LineEidt
        qle = QLineEdit()
        # connect
        qle.textChanged.connect(self.changedText)
        base_layout.addWidget(qle)

        base.addLayout(base_layout)
        base.addLayout(base_button_layout)

        grp_1.setLayout(base)

    def makeComboBox(self):
        grp_1 = QGroupBox("Select ile")
        self.main_layout.addWidget(grp_1)

        self.base = QBoxLayout(QBoxLayout.TopToBottom, self)
        base_button_layout = QBoxLayout(QBoxLayout.LeftToRight, self)
        self.base_combo_layout = QBoxLayout(QBoxLayout.LeftToRight, self)
        # push Button
        qb_3 = QPushButton()
        # setText
        qb_3.setText("refresh")
        qb_3.clicked.connect(self.refresh)
        base_button_layout.addWidget(qb_3)
        # comboBox
        self.qb_1 = QComboBox()
        self.refresh()
        self.base.addLayout(base_button_layout)

        grp_1.setLayout(self.base)

    def makePushButton(self):
        grp_1 = QGroupBox()
        self.main_layout.addWidget(grp_1)

        base =QBoxLayout(QBoxLayout.TopToBottom, self)
        base_layout = QBoxLayout(QBoxLayout.LeftToRight, self)
        base_layout1 = QBoxLayout(QBoxLayout.LeftToRight, self)
        # button
        self.qp_1 = QPushButton()
        qb_2 = QPushButton()
        # setText
        self.qp_1.setText("Select")
        qb_2.setText("Close")
        # connect
        self.qp_1.clicked.connect(self.selectButton)
        qb_2.clicked.connect(self.close)
        # set Layout
        base_layout.addWidget(self.qp_1)
        base_layout.addWidget(qb_2)

        base.addLayout(base_layout)

        grp_1.setLayout(base)

    def selectButton(self):
        self.comboBox_text = self.comboBoxText()
        self.close()

    def changedText(self):
        return_text = self.sender().text()
        self.return_text = return_text

    def comboBoxText(self):
        return self.qb_1.currentText()

    def save(self):
        with open("{}/{}.txt".format(script_path,self.return_text),'w') as f:
            f.write("a")

    def refresh(self):
        file_txt = [i for i in os.listdir(script_path) if i.endswith('.txt')]
        self.qb_1.clear()
        for i in file_txt:
            self.qb_1.addItem(i)
        self.qb_1.currentIndexChanged.connect(self.comboBoxText)
        self.base_combo_layout.addWidget(self.qb_1)
        self.base.addLayout(self.base_combo_layout)

class ImportSelectedNode():
    def test(self):
        selected_object = mc.ls(selection=True)
        return selected_object

class Form(QWidget):
#  main Widget
    def __init__(self):
        QWidget.__init__(self)

        dlg = FindFolderTxt()
        dlg.exec_()
        comboBox_text = dlg.comboBox_text
        self.findTxtFile = comboBox_text

        self.selected_object = ImportSelectedNode().test()

        global script_path

        self.main_layout = QBoxLayout(QBoxLayout.TopToBottom,self)
        self.initWidget()

    def initWidget(self):
        self.setWindowTitle("I'm really love you")
        # setName
        self.makeLineEdit()
        # comboBox
        self.text_list = []
        self.makeComboB()
        # pushButton
        self.makePushButton()

    def makeLineEdit(self):
        grp_1 = QGroupBox("Set Name")
        self.main_layout.addWidget(grp_1)

        base_layout = QBoxLayout(QBoxLayout.LeftToRight,self)

        qle = QLineEdit()
        qle.textChanged.connect(self.saveLineEidt)
        base_layout.addWidget(qle)

        grp_1.setLayout(base_layout)

    def makeComboB(self):
        grp_1 = QGroupBox("List")
        self.main_layout.addWidget(grp_1)

        self.base = QBoxLayout(QBoxLayout.TopToBottom,self)
        base_layout = QBoxLayout(QBoxLayout.TopToBottom,self)
        base_layout_1 = QBoxLayout(QBoxLayout.LeftToRight, self)

        self.qCb = QComboBox()
        self.loadDict()

        qb_1 = QPushButton()
        qb_2 = QPushButton()
        qb_3 = QPushButton()
        qb_1.setText("save")
        qb_3.setText("refresh")
        qb_2.setText("delete")
        qb_1.clicked.connect(self.jsonSave)
        qb_2.clicked.connect(self.jsonDelete)
        qb_3.clicked.connect(self.jsonRefresh)

        base_layout.addWidget(self.qCb)
        base_layout_1.addWidget(qb_1)
        base_layout_1.addWidget(qb_3)
        base_layout_1.addWidget(qb_2)

        self.base.addLayout(base_layout)
        self.base.addLayout(base_layout_1)

        grp_1.setLayout(self.base)

    def makePushButton(self):
        grp_1 = QGroupBox("Button")
        self.main_layout.addWidget(grp_1)

        base_layout = QBoxLayout(QBoxLayout.LeftToRight,self)
        # make Button
        qb_3 = QPushButton()
        qb_1 = QPushButton()
        # Button Name
        qb_3.setText("close")
        qb_1.setText("set")
        # button connect
        qb_1.clicked.connect(self.setPosition)
        qb_3.clicked.connect(self.close)
        # set button layout
        base_layout.addWidget(qb_1)
        base_layout.addWidget(qb_3)

        grp_1.setLayout(base_layout)

    def saveLineEidt(self):
        self.saveName_text = self.sender().text()

#### attrib ###

    def findSelNode(self,node_text={}):
        node_text = self.jsonLoad()
        for i in self.selected_object:
            t = mc.xform(i, t=1, ws=1, q=1)
            ro = mc.xform(i, ro=1, ws=1, q=1)
            node_text[self.saveName_text] = t , ro
        return node_text

    def loadDict(self):
        for i in self.jsonLoad():
            self.qCb.addItem(i)

    def jsonRefresh(self):
        self.qCb.clear()
        for i in self.jsonLoad():
            self.qCb.addItem(i)

    def jsonSave(self):
        save_text =  self.findSelNode()
        with open("{}{}{}".format(script_path, "/", self.findTxtFile), "w") as f:
            jason_string = json.dumps(save_text, indent=2)
            f.write(jason_string)

    def jsonDelete(self):
        self.cur_text = self.qCb.currentText()
        load_json = self.jsonLoad()
        del load_json[self.cur_text]
        with open("{}{}{}".format(script_path, "/", self.findTxtFile), "w") as f:
            jason_string = json.dumps(load_json, indent=2)
            f.write(jason_string)

    def jsonLoad(self):
        findTxt_path = self.findTxtFile.split(".")[:-1][0]
        try:
            with open("{}{}{}.txt".format(script_path, "/", findTxt_path)) as f:
                data = json.load(f)
        except:
            a = {}
            data = a
        return data

    def setPosition(self):
        cur_text = self.qCb.currentText()
        attribs  = self.jsonLoad()[cur_text]

        a = ImportSelectedNode()
        sel_obj = a.test()
        print sel_obj
        for i in sel_obj:
            mc.setAttr("{}.{}".format(str(i), "t"), attribs[0][0], attribs[0][1], attribs[0][2])
            mc.setAttr("{}.{}".format(str(i), "r"), attribs[1][0], attribs[1][1],attribs[1][2])
        # a = Form()
        # a.update()
        # self.close()

ex = Form()
ex.show()
