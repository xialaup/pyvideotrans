# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

from videotrans.configure import config
from videotrans.util import tools


class Ui_zhipuaiform(object):
    def setupUi(self, zhipuaiform):
        self.has_done = False
        zhipuaiform.setObjectName("zhipuaiform")
        zhipuaiform.setWindowModality(QtCore.Qt.NonModal)
        zhipuaiform.resize(600, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(zhipuaiform.sizePolicy().hasHeightForWidth())
        zhipuaiform.setSizePolicy(sizePolicy)
        zhipuaiform.setMaximumSize(QtCore.QSize(600, 600))

        v1=QtWidgets.QVBoxLayout(zhipuaiform)
        h2=QtWidgets.QHBoxLayout()

        
        h4=QtWidgets.QHBoxLayout()


        self.label_0 = QtWidgets.QPushButton()
        self.label_0.setGeometry(QtCore.QRect(10, 10, 580, 35))
        self.label_0.setStyleSheet("background-color: rgba(255, 255, 255,0);text-align:left")
        self.label_0.setText(
            '智谱AI在此填写api key')
        v1.addWidget(self.label_0)


        self.label_2 = QtWidgets.QLabel(zhipuaiform)
        self.label_2.setMinimumSize(QtCore.QSize(0, 35))
        self.label_2.setSizeIncrement(QtCore.QSize(0, 35))
        self.label_2.setObjectName("label_2")
        self.zhipu_key = QtWidgets.QLineEdit(zhipuaiform)
        self.zhipu_key.setMinimumSize(QtCore.QSize(0, 35))
        self.zhipu_key.setObjectName("zhipu_key")
        h2.addWidget(self.label_2)
        h2.addWidget(self.zhipu_key)
        v1.addLayout(h2)
        
        h_model=QtWidgets.QHBoxLayout()
        self.label_selectmodel = QtWidgets.QLabel()
        self.label_selectmodel.setObjectName("label_selectmodel")
        self.label_selectmodel.setText("选择使用模型")
        self.zhipu_model = QtWidgets.QComboBox()
        self.zhipu_model.setMinimumSize(QtCore.QSize(0, 35))
        self.zhipu_model.setObjectName("zhipu_model")
        h_model.addWidget(self.label_selectmodel)
        h_model.addWidget(self.zhipu_model)
        v1.addLayout(h_model)

        self.label_allmodels = QtWidgets.QLabel()
        self.label_allmodels.setObjectName("label_allmodels")
        self.label_allmodels.setText(
            '填写所有可用模型，以英文逗号分隔，填写后可在上方选择' if config.defaulelang == 'zh' else 'Fill in all available models, separated by commas. After filling in, you can select them above')
        v1.addWidget(self.label_allmodels)

        self.edit_allmodels = QtWidgets.QPlainTextEdit()
        self.edit_allmodels.setObjectName("edit_allmodels")
        v1.addWidget(self.edit_allmodels)





        self.label_4 = QtWidgets.QLabel(zhipuaiform)
        self.label_4.setObjectName("label_4")

        self.template = QtWidgets.QPlainTextEdit(zhipuaiform)
        self.template.setObjectName("template")
        v1.addWidget(self.label_4)
        v1.addWidget(self.template)


        self.set = QtWidgets.QPushButton(zhipuaiform)
        self.set.setMinimumSize(QtCore.QSize(0, 35))
        self.set.setObjectName("set")
        
        self.test = QtWidgets.QPushButton()
        self.test.setMinimumSize(QtCore.QSize(0, 30))
        self.test.setObjectName("test")
        self.test.setText("Test")

        help_btn = QtWidgets.QPushButton()
        help_btn.setMinimumSize(QtCore.QSize(0, 35))
        help_btn.setStyleSheet("background-color: rgba(255, 255, 255,0)")
        help_btn.setObjectName("help_btn")
        help_btn.setCursor(Qt.PointingHandCursor)
        help_btn.setText("查看填写教程" if config.defaulelang == 'zh' else "Fill out the tutorial")
        help_btn.clicked.connect(lambda: tools.open_url(url='https://pyvideotrans.com/zhipuai-ai'))

        h4.addWidget(self.set)
        h4.addWidget(self.test)
        h4.addWidget(help_btn)
        v1.addLayout(h4)

        self.retranslateUi(zhipuaiform)
        QtCore.QMetaObject.connectSlotsByName(zhipuaiform)

    def retranslateUi(self, zhipuaiform):
        zhipuaiform.setWindowTitle("智谱AI")
        self.label_2.setText("智谱AI API Key")
        self.template.setPlaceholderText("prompt")
        self.label_4.setText(
            "{lang}代表目标语言名称，不要删除。")
        self.set.setText('保存' )
        self.zhipu_key.setPlaceholderText("在此填写智谱AI的 API Key")

