#!/usr/bin/env python
# -*- coding: cp1252  -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Sat Jul 21 15:09:12 2018
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, QtSql
from configparser import ConfigParser
import sys,os
reload(sys)
if hasattr(sys,"setdefaultencoding"):
    sys.setdefaultencoding("cp1252")

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

#20/11/2018
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(730, 450)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 301, 430))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 51, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.loginEdit = QtGui.QLineEdit(self.groupBox)
        self.loginEdit.setGeometry(QtCore.QRect(90, 18, 200, 20))
        self.loginEdit.setObjectName(_fromUtf8("loginEdit"))
        self.passwordEdit = QtGui.QLineEdit(self.groupBox)
        self.passwordEdit.setGeometry(QtCore.QRect(90, 50, 150, 20))
        self.passwordEdit.setInputMask(_fromUtf8(""))
        self.passwordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordEdit.setObjectName(_fromUtf8("passwordEdit"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 51, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.traiterButton = QtGui.QPushButton(self.groupBox)
        self.traiterButton.setGeometry(QtCore.QRect(90, 80, 75, 23))
        self.traiterButton.setObjectName(_fromUtf8("traiterButton"))
        self.traiterButton.clicked.connect(self.traiterButton_clicked)
        self.tableWidget = QtGui.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(5, 130, 288, 192))
        self.tableWidget.setMaximumSize(QtCore.QSize(391, 16777215))
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        # item.setSizeHint(QSize=)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()

        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        # size_width=item.sizeHint()
        # size_width.setWidth(0)
        # item.setSizeHint(QSize(100,32))
        self.tableWidget.setItem(0, 1, item)

        self.tableWidget.setColumnWidth(0,270)
        self.tableWidget.setColumnWidth(1,1)
        self.tableWidget.cellClicked.connect(self.tableWidget_cellClicked)

        # self.loginEdit2 = QtGui.QLineEdit(self.groupBox)
        # self.loginEdit2.setGeometry(QtCore.QRect(110, 18, 71, 20))
        # # self.loginEdit2.setEnabled()
        # self.loginEdit2.setObjectName(_fromUtf8("loginEdit2"))
        # self.loginEdit2.hide()

        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(243, 52, 70, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox.stateChanged.connect(self.checkBox_stateChanged)

        self.supprimerButton = QtGui.QPushButton(self.groupBox)
        self.supprimerButton.setGeometry(QtCore.QRect(170, 80, 75, 23))
        self.supprimerButton.setObjectName(_fromUtf8("supprimerButton"))
        self.supprimerButton.clicked.connect(self.supprimerButton_clicked)

        self.initButton = QtGui.QPushButton(self.groupBox)
        self.initButton.setGeometry(QtCore.QRect(250, 80, 41, 23))
        self.initButton.setObjectName(_fromUtf8("initButton"))
        self.initButton.clicked.connect(self.initButton_clicked)

        #Ajout liste campagne
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 347, 71, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.campagneBox = QtGui.QComboBox(self.groupBox)
        self.campagneBox.setGeometry(QtCore.QRect(80, 345, 215, 22))
        self.campagneBox.setObjectName(_fromUtf8("campagneBox"))
        self.campagneBox.addItem(_fromUtf8(""))
        self.campagneBox.setItemText(0, _fromUtf8(""))
        # self.campagneBox.addItem(_fromUtf8(""))
        # self.campagneBox.addItem(_fromUtf8(""))
        self.campagneBox.setEnabled(True)
        self.campagneBox.setEditable(True)

        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(330, 10, 391, 430))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.traitementBox = QtGui.QComboBox(self.groupBox_2)
        self.traitementBox.setEnabled(False)
        self.traitementBox.setGeometry(QtCore.QRect(112, 20, 191, 22))
        self.traitementBox.setObjectName(_fromUtf8("traitementBox"))
        self.traitementBox.addItem(_fromUtf8(""))
        self.traitementBox.setItemText(0, _fromUtf8(""))
        self.traitementBox.addItem(_fromUtf8(""))
        self.traitementBox.addItem(_fromUtf8(""))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 23, 91, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.checkBoxActiverTraitement = QtGui.QCheckBox(self.groupBox_2)
        self.checkBoxActiverTraitement.setGeometry(QtCore.QRect(310, 22, 70, 17))
        self.checkBoxActiverTraitement.setObjectName(_fromUtf8("checkBoxActiverTraitement"))
        self.checkBoxActiverTraitement.stateChanged.connect(self.checkBoxActiverTraitement_stateChanged)

        self.num_compte_en_coursEdit = QtGui.QLineEdit(self.groupBox_2)
        self.num_compte_en_coursEdit.setEnabled(False)
        self.num_compte_en_coursEdit.setGeometry(QtCore.QRect(137, 53, 41, 20))
        self.num_compte_en_coursEdit.setObjectName(_fromUtf8("num_compte_en_coursEdit"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 56, 121, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.checkBoxActivercompte_en_cours = QtGui.QCheckBox(self.groupBox_2)
        self.checkBoxActivercompte_en_cours.setGeometry(QtCore.QRect(185, 55, 70, 17))
        self.checkBoxActivercompte_en_cours.setObjectName(_fromUtf8("checkBoxActivercompte_en_cours"))
        self.checkBoxActivercompte_en_cours.stateChanged.connect(self.checkBoxActivercompte_en_cours_stateChanged)

        self.nombreTraiteEdit = QtGui.QLineEdit(self.groupBox_2)
        self.nombreTraiteEdit.setEnabled(False)
        self.nombreTraiteEdit.setGeometry(QtCore.QRect(113, 84, 81, 20))
        self.nombreTraiteEdit.setObjectName(_fromUtf8("nombreTraiteEdit"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(11, 86, 71, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.plainTextAenvoyer = QtGui.QPlainTextEdit(self.groupBox_2)
        self.plainTextAenvoyer.setGeometry(QtCore.QRect(110, 120, 271, 121))
        self.plainTextAenvoyer.setTabChangesFocus(True)
        self.plainTextAenvoyer.setObjectName(_fromUtf8("plainTextAenvoyer"))
        self.plainTextAenvoyer.textChanged.connect(self.plainTextAenvoyer_textChanged)

        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 119, 81, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.mettreajourButton = QtGui.QPushButton(self.groupBox_2)
        self.mettreajourButton.setGeometry(QtCore.QRect(110, 401, 75, 23))
        self.mettreajourButton.setObjectName(_fromUtf8("mettreajourButton"))
        self.mettreajourButton.clicked.connect(self.mettreajourButton_clicked)

        self.commencerButton = QtGui.QPushButton(self.groupBox_2)
        self.commencerButton.setGeometry(QtCore.QRect(190, 401, 75, 23))
        self.commencerButton.setObjectName(_fromUtf8("commencerButton"))
        self.commencerButton.clicked.connect(self.commencerButton_clicked)

        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(270, 401, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.pushButton_clicked)

        self.rafraichirButton = QtGui.QPushButton(self.groupBox_2)
        self.rafraichirButton.setGeometry(QtCore.QRect(269, 83, 61, 23))
        self.rafraichirButton.setObjectName(_fromUtf8("rafraichirButton"))
        self.rafraichirButton.clicked.connect(self.rafraichirButton_clicked)

        self.rechercheEdit = QtGui.QLineEdit(self.groupBox_2)
        self.rechercheEdit.setGeometry(QtCore.QRect(110, 274, 271, 20))
        self.rechercheEdit.setObjectName(_fromUtf8("rechercheEdit"))
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(11, 277, 61, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        #--10/11/2018 Ajout region
        #self.rechercheRegion = QtGui.QPlainTextEdit(self.groupBox_2)
        self.rechercheRegion = QtGui.QLineEdit(self.groupBox_2)
        self.rechercheRegion.setGeometry(QtCore.QRect(110, 307, 271, 20))
        #self.rechercheRegion.setTabChangesFocus(True)
        self.rechercheRegion.setObjectName(_fromUtf8("rechercheRegion"))
        self.label_7_1 = QtGui.QLabel(self.groupBox_2)
        self.label_7_1.setGeometry(QtCore.QRect(11, 310, 61, 16))
        self.label_7_1.setObjectName(_fromUtf8("label_7_1"))

        self.compteCarEdit = QtGui.QLineEdit(self.groupBox_2)
        self.compteCarEdit.setGeometry(QtCore.QRect(343, 242, 38, 20))
        self.compteCarEdit.setObjectName(_fromUtf8("compteCarEdit"))
        self.compteCarEdit.setEnabled(False)
        self.checkBoxActiverPlain = QtGui.QCheckBox(self.groupBox_2)
        self.checkBoxActiverPlain.setGeometry(QtCore.QRect(257, 244, 70, 17))
        self.checkBoxActiverPlain.setObjectName(_fromUtf8("checkBoxActiverPlain"))
        self.checkBoxActiverPlain.stateChanged.connect(self.checkBoxActiverPlain_stateChanged)
        self.checkBoxActiverPlain.setChecked(True)

        self.nombreEnvoiEdit = QtGui.QLineEdit(self.groupBox_2)
        self.nombreEnvoiEdit.setGeometry(QtCore.QRect(146, 338, 50, 20))
        self.nombreEnvoiEdit.setObjectName(_fromUtf8("nombreEnvoiEdit"))

        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(11, 341, 131, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))

        #Ajout pagination
        self.paginationEditDebut = QtGui.QLineEdit(self.groupBox_2)
        self.paginationEditDebut.setGeometry(QtCore.QRect(146, 370, 50, 20))
        self.paginationEditDebut.setObjectName(_fromUtf8("paginationEditDebut"))
        self.paginationEditFin = QtGui.QLineEdit(self.groupBox_2)
        self.paginationEditFin.setGeometry(QtCore.QRect(200, 370, 50, 20))
        self.paginationEditFin.setObjectName(_fromUtf8("paginationEditFin"))

        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(11, 373, 131, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))

        self.checkBoxNombreEnvoi = QtGui.QCheckBox(self.groupBox_2)
        self.checkBoxNombreEnvoi.setGeometry(QtCore.QRect(207, 340, 141, 17))
        self.checkBoxNombreEnvoi.setObjectName(_fromUtf8("checkBoxNombreEnvoi"))
        self.checkBoxNombreEnvoi.stateChanged.connect(self.checkBoxNombreEnvoi_stateChanged)

        self.initialiserButton = QtGui.QPushButton(self.groupBox_2)
        self.initialiserButton.setGeometry(QtCore.QRect(200, 83, 51, 23))
        self.initialiserButton.setObjectName(_fromUtf8("initialiserButton"))
        self.initialiserButton.clicked.connect(self.initialiserButton_clicked)

        MainWindow.setCentralWidget(self.centralwidget)

        destinataire=""
        with open(r"destinataire.txt", "r") as f :
            destinataire = f.read()
            # if destinataire.strip()=="":
            #     MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Le fichier destinataire.txt est vide", None, QtGui.QApplication.UnicodeUTF8))
            #     return
        self.rechercheEdit.setText(str(destinataire).strip())

        region=""
        with open(r"region.txt", "r") as f :
            region = f.read()
        self.rechercheRegion.setText(str(region).strip())

        activer_nombre_envoi=""
        with open(r"activer_nombre_envoi.txt", "r") as f :
            activer_nombre_envoi = f.read()
        if str(activer_nombre_envoi).strip()=="2":
            self.checkBoxNombreEnvoi.setChecked(True)
            self.nombreEnvoiEdit.setEnabled(True)
        else:
            self.checkBoxNombreEnvoi.setChecked(False)
            self.nombreEnvoiEdit.setEnabled(False)

        nombre_envoi=""
        with open(r"nombre_envoi.txt", "r") as f :
            nombre_envoi = f.read()
            # if str(nombre_envoi).strip()=="" and str(activer_nombre_envoi).strip()!="":
            #     MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Le nombre_envoi est vide", None, QtGui.QApplication.UnicodeUTF8))
            #     return
        self.nombreEnvoiEdit.setText(str(nombre_envoi).strip())

        traitement=""
        with open(r"traitement.txt", "r") as f :
            traitement = f.read()

        num_compte_en_cours=""
        with open(r"num_compte_en_cours.txt", "r") as f :
            num_compte_en_cours = f.read()

        self.retranslateUi(MainWindow)
        self.db=QtSql.QSqlDatabase.addDatabase("QPSQL")
        self.db.setHostName("127.0.0.1")
        self.db.setDatabaseName("saisie")
        self.db.setUserName("postgres")
        self.db.setPassword("123456")
        texte_a_afficher=""
        if self.db.open()==False:
            texte_a_afficher=str(self.db.lastError().text())
        else:
            texte_a_afficher="Connexion etablie !"

        #Charger liste campagne
        query_c=QtSql.QSqlQuery(self.db)
        if query_c.exec_("select campagne from table_campagne order by idenr")==False:
            MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", str(query_c.lastError().databaseText()), None, QtGui.QApplication.UnicodeUTF8))
            return
        v=1
        num_c = query_c.record().indexOf('campagne')
        while query_c.next():
            self.campagneBox.addItem(_fromUtf8(""))
            self.campagneBox.setItemText(v, QtGui.QApplication.translate("MainWindow", str(query_c.value(num_c).toString()), None, QtGui.QApplication.UnicodeUTF8))
            v=v+1
        #---------------------
        query=QtSql.QSqlQuery(self.db)
        query.exec_("select * from table_linkedin order by idenr")
        n=0

        # self.rafraichir()
        self.tableWidget.removeRow(0)

        while query.next():
            donnee=str(query.value(0).toString()).encode("cp1252").replace("\\\\","\\")
            motdepasse=str(query.value(1).toString()).encode("cp1252").replace("\\\\","\\")
            # print(donnee)
            self.tableWidget.insertRow(n)
            newItem = QtGui.QTableWidgetItem(str(donnee))
            self.tableWidget.setItem(n, 0, newItem)
            newItemPassword = QtGui.QTableWidgetItem(str(motdepasse))
            self.tableWidget.setItem(n, 1, newItemPassword)

            n=n+1
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", texte_a_afficher, None, QtGui.QApplication.UnicodeUTF8))

        index = self.traitementBox.findText(traitement, QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.traitementBox.setCurrentIndex(index)

        self.num_compte_en_coursEdit.setText(str(num_compte_en_cours))

        nombre_traite=""
        with open(r"nombre_traite.txt", "r") as f :
            nombre_traite = f.read()
        #self.nombreTraiteEdit.setText(str(nombre_traite).strip())
        self.nombreTraiteEdit.setText("0")

        texte=""
        with open(r"texte.txt", "r") as f :
            texte = f.read()
        self.plainTextAenvoyer.setPlainText(str(texte).strip())

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Envoi de message via linkedin", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Comptes", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Mot de passe", None, QtGui.QApplication.UnicodeUTF8))
        self.traiterButton.setText(QtGui.QApplication.translate("MainWindow", "Ajouter", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("MainWindow", "Login", None, QtGui.QApplication.UnicodeUTF8))

        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("MainWindow", "Mot de passe", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", "afficher", None, QtGui.QApplication.UnicodeUTF8))
        self.supprimerButton.setText(QtGui.QApplication.translate("MainWindow", "Supprimer", None, QtGui.QApplication.UnicodeUTF8))
        self.initButton.setText(QtGui.QApplication.translate("MainWindow", "init", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Parametres", None, QtGui.QApplication.UnicodeUTF8))
        self.traitementBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "commencer_page_1", None, QtGui.QApplication.UnicodeUTF8))
        self.traitementBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "continuer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Traitement", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxActiverTraitement.setText(QtGui.QApplication.translate("MainWindow", "activer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Numero compte en cours", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxActivercompte_en_cours.setText(QtGui.QApplication.translate("MainWindow", "activer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Nombre traite", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Texte a envoyer", None, QtGui.QApplication.UnicodeUTF8))
        self.mettreajourButton.setText(QtGui.QApplication.translate("MainWindow", "Mettre a jour", None, QtGui.QApplication.UnicodeUTF8))
        self.commencerButton.setText(QtGui.QApplication.translate("MainWindow", "Commencer", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Arreter", None, QtGui.QApplication.UnicodeUTF8))
        self.rafraichirButton.setText(QtGui.QApplication.translate("MainWindow", "Rafraichir", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Rechercher", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7_1.setText(QtGui.QApplication.translate("MainWindow", "Region", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxActiverPlain.setText(QtGui.QApplication.translate("MainWindow", "activer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Nombre envoi par compte", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxNombreEnvoi.setText(QtGui.QApplication.translate("MainWindow", "appliquer nombre d\'envoi", None, QtGui.QApplication.UnicodeUTF8))
        self.initialiserButton.setText(QtGui.QApplication.translate("MainWindow", "Initialiser", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Campagne", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Pagination", None, QtGui.QApplication.UnicodeUTF8))


    def traiterButton_clicked(self):
        if self.loginEdit.text()=="":
            self.loginEdit.setFocus()
            return
        if self.passwordEdit.text()=="":
            self.passwordEdit.setFocus()
            return

        query=QtSql.QSqlQuery(self.db)
        try:
            row = self.tableWidget.currentItem().row()
            query.prepare("select * from table_linkedin where login=?")
            query.addBindValue(str(self.tableWidget.item(row,0).text()).encode("cp1252"))
        except:
            if self.loginEdit.text()!="":
                query.prepare("select * from table_linkedin where login=?")
                query.addBindValue(self.loginEdit.text())
            else:
                query.prepare("select * from table_linkedin")
        if query.exec_()==False:
            MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", str(query.lastError().databaseText()), None, QtGui.QApplication.UnicodeUTF8))
            return
        if query.next():
            query.prepare("update table_linkedin  set login=?, password=? where login=?")
            query.addBindValue(self.loginEdit.text())
            query.addBindValue(self.passwordEdit.text())
            try:
                row = self.tableWidget.currentItem().row()
                query.addBindValue(str(self.tableWidget.item(row,0).text()).encode("cp1252"))
            except:
                query.addBindValue(self.loginEdit.text())
            query.exec_()
            # MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Deja existant", None, QtGui.QApplication.UnicodeUTF8))
            # return
        else:
            query.prepare("INSERT INTO table_linkedin (login, password) VALUES (?, ?)")
            query.addBindValue(self.loginEdit.text())
            query.addBindValue(self.passwordEdit.text())
            query.exec_()
            # n=0
            # while query.next():
            #     self.tableWidget.insertRow(n)
            #     n=+1
        self.rafraichir()
        self.loginEdit.setText("")
        self.passwordEdit.setText("")
        # self.loginEdit2.setText("")
        self.create_config()
        if self.traiterButton.text()=="Mettre a jour":
            self.traiterButton.setText(QtGui.QApplication.translate("MainWindow", "Ajouter", None, QtGui.QApplication.UnicodeUTF8))
            MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Mise a jour ok", None, QtGui.QApplication.UnicodeUTF8))
        else:
            MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Ajout ok", None, QtGui.QApplication.UnicodeUTF8))

    def rafraichir(self):
        query=QtSql.QSqlQuery(self.db)
        nbre_lignes=self.tableWidget.rowCount()+1

        for z in range(nbre_lignes):
            self.tableWidget.removeRow(0)

        query.exec_("select * from table_linkedin order by idenr")
        # print(query.size())

        n=0
        while query.next():
            donnee=str(query.value(0).toString()).encode("cp1252").replace("\\\\","\\")
            motdepasse=str(query.value(1).toString()).encode("cp1252").replace("\\\\","\\")
            # print(donnee)
            self.tableWidget.insertRow(n)
            newItem = QtGui.QTableWidgetItem(str(donnee))
            self.tableWidget.setItem(n, 0, newItem)
            newItemMotdepasse = QtGui.QTableWidgetItem(str(motdepasse))
            self.tableWidget.setItem(n, 1, newItemMotdepasse)

            n=n+1
            self.tableWidget.setRowCount(n)

    def tableWidget_cellClicked(self, arg1, arg2):
        self.loginEdit.setText(str(self.tableWidget.item(arg1,0).text()).encode("cp1252"))
        self.passwordEdit.setText(str(self.tableWidget.item(arg1,1).text()).encode("cp1252"))
        self.traiterButton.setText(QtGui.QApplication.translate("MainWindow", "Mettre a jour", None, QtGui.QApplication.UnicodeUTF8))

    def checkBox_stateChanged(self, arg1):
        if arg1==2:
            self.passwordEdit.setEchoMode(QtGui.QLineEdit.Normal)
        else:
            self.passwordEdit.setEchoMode(QtGui.QLineEdit.Password)

    def checkBoxActivercompte_en_cours_stateChanged(self, arg1):
        if arg1==2:
            self.num_compte_en_coursEdit.setEnabled(True)
        else:
            self.num_compte_en_coursEdit.setEnabled(False)

    def checkBoxActiverTraitement_stateChanged(self, arg1):
        if arg1==2:
            self.traitementBox.setEnabled(True)
        else:
            self.traitementBox.setEnabled(False)

    def supprimerButton_clicked(self):
        try:
            row = self.tableWidget.currentItem().row()
            # print(str(self.tableWidget.item(row,0).text()).encode("cp1252"))
            query=QtSql.QSqlQuery(self.db)
            query.prepare("delete from table_linkedin where login=?")
            query.addBindValue(str(self.tableWidget.item(row,0).text()).encode("cp1252"))
            query.exec_()
            self.tableWidget.removeRow(row)
            self.rafraichir()
            self.loginEdit.setText("")
            self.passwordEdit.setText("")
            self.traiterButton.setText(QtGui.QApplication.translate("MainWindow", "Ajouter", None, QtGui.QApplication.UnicodeUTF8))
            self.create_config()
            MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Suppression ok", None, QtGui.QApplication.UnicodeUTF8))
        except:
            self.traiterButton.setText(QtGui.QApplication.translate("MainWindow", "Ajouter", None, QtGui.QApplication.UnicodeUTF8))
            MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Envoi de message via linkedin", None, QtGui.QApplication.UnicodeUTF8))
            pass

    def create_config(self):
        cfg = open("c.ini", "w")
        config = ConfigParser()
        config.add_section('compte')

        query=QtSql.QSqlQuery(self.db)
        query.exec_("select * from table_linkedin order by idenr")
        n=0
        while query.next():
            n+=1
            login=str(query.value(0).toString()).encode("cp1252").replace("\\\\","\\")
            motdepasse=str(query.value(1).toString()).encode("cp1252").replace("\\\\","\\")
            config.set('compte','login'+str(n),login.encode("utf8"))
            config.set('compte','password'+str(n), motdepasse.encode("utf8"))
        config.write(cfg)
        cfg.close()

    def initButton_clicked(self):
        self.loginEdit.setText("")
        self.passwordEdit.setText("")
        self.traiterButton.setText(QtGui.QApplication.translate("MainWindow", "Ajouter", None, QtGui.QApplication.UnicodeUTF8))
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Envoi de message via linkedin", None, QtGui.QApplication.UnicodeUTF8))
        self.rafraichir()

    def mettreajourButton_clicked(self):
        # if str(self.rechercheEdit.text())=="":
        #     MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "La zone de recherche est vide", None, QtGui.QApplication.UnicodeUTF8))
        #     return

        if str(self.nombreEnvoiEdit.text())=="" and self.checkBoxNombreEnvoi.isChecked():
            MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Le nombre envoi est vide", None, QtGui.QApplication.UnicodeUTF8))
            return

        traitement = open("traitement.txt", "w")
        traitement.write(str(self.traitementBox.currentText()))
        traitement.close()
        num_compte_en_cours = open("num_compte_en_cours.txt", "w")
        num_compte_en_cours.write(str(self.num_compte_en_coursEdit.text()))
        num_compte_en_cours.close()
        destinataire = open("destinataire.txt", "w")
        destinataire.write(str(self.rechercheEdit.text()))
        destinataire.close()

        region = open("region.txt", "w")
        region.write(str(self.rechercheRegion.text()))
        region.close()

        nombre_envoi = open("nombre_envoi.txt", "w")
        nombre_envoi.write(str(self.nombreEnvoiEdit.text()))
        nombre_envoi.close()

        if self.checkBoxNombreEnvoi.isChecked():
            activer_nombre_envoi = open("activer_nombre_envoi.txt", "w")
            activer_nombre_envoi.write("2")
            activer_nombre_envoi.close()
        else:
            activer_nombre_envoi = open("activer_nombre_envoi.txt", "w")
            activer_nombre_envoi.close()

        texte = open("texte.txt", "w")
        texte.write(str(self.plainTextAenvoyer.toPlainText()))
        texte.close()
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Mise a jour ok", None, QtGui.QApplication.UnicodeUTF8))

    def commencerButton_clicked(self):
        # destinataire=""
        # with open(r"destinataire.txt", "r") as f :
        #     destinataire = f.read()
        #     if destinataire.strip()=="":
        #         MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Le fichier destinataire.txt est vide, pas de destinataire", None, QtGui.QApplication.UnicodeUTF8))
        #         return
        texte=""
        #Ajout campagne
        nom_nettoye=self.retour_chaine_nettoyee(str(self.campagneBox.currentText()).strip().encode("cp1252"))
        self.campagneBox.setEditText(nom_nettoye)
        query=QtSql.QSqlQuery(self.db)
        query.prepare("select * from table_campagne where campagne=?")
        query.addBindValue(str(self.campagneBox.currentText()).strip().encode("cp1252"))
        if query.exec_()==False:
            MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", str(query.lastError().databaseText()), None, QtGui.QApplication.UnicodeUTF8))
            return
        if str(self.campagneBox.currentText()).strip().encode("cp1252")=="":
            MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", str("Veuillez saisir le nom de campagne"), None, QtGui.QApplication.UnicodeUTF8))
            self.campagneBox.setFocus()
            return
        if query.next():
            pass
        else:
            query.prepare("INSERT INTO table_campagne (campagne) VALUES (?)")
            query.addBindValue(str(self.campagneBox.currentText()).strip().encode("cp1252"))
            query.exec_()
        #print(self.campagneBox.currentText())
        campagne = open("campagne.txt", "w")
        campagne.write(str(self.campagneBox.currentText()))
        campagne.close()
        #--------
        #Ajout pagination
        if str(self.paginationEditDebut.text()).strip().encode("cp1252")=="":
            MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", str("Veuillez saisir la page de debut"), None, QtGui.QApplication.UnicodeUTF8))
            self.paginationEditDebut.setFocus()
            return
        page_debut = open("page_debut.txt", "w")
        page_debut.write(str(self.paginationEditDebut.text()))
        page_debut.close()

        if str(self.paginationEditFin.text()).strip().encode("cp1252")=="":
            MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", str("Veuillez saisir la page de fin"), None, QtGui.QApplication.UnicodeUTF8))
            self.paginationEditFin.setFocus()
            return
        page_fin = open("page_fin.txt", "w")
        page_fin.write(str(self.paginationEditFin.text()))
        page_fin.close()

        #------------
        with open(r"texte.txt", "r") as f :
            texte = f.read()
            if texte.strip()=="":
                MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Le fichier texte.txt est vide, pas de message a envoyer", None, QtGui.QApplication.UnicodeUTF8))
                return

        if self.tableWidget.rowCount()==0:
            MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Pas de compte defini", None, QtGui.QApplication.UnicodeUTF8))
            return

        if os.path.exists('main.lock')==True:
            os.remove('main.lock')

        if os.path.exists('main2.lock')==True:
            os.remove('main2.lock')

        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Commencer ok", None, QtGui.QApplication.UnicodeUTF8))

    def retour_chaine_nettoyee(self, chaine):
        chaine=chaine.encode("cp1252")
        ListeAccents = "ËÉÊÈÄÀÂÜÙÛÏÎÖÔÇëéêèäàâüùûïîöôç'.-,"
        ReplaceListeAccents = "EEEEAAAUUUIIOOCeeeeaaauuuiiooc    "
        k=0
        bchiffreaccepter=True
        while(k<len(chaine)):
            chainenew=chaine
            bok=False
            if bchiffreaccepter==True:
                if (ord(chainenew[k].upper())>= 65 and ord(chainenew[k].upper()) <= 90) or (ord(chainenew[k].upper()) >= 48 and ord(chainenew[k].upper()) <= 57) or ord(chainenew[k].upper()) == 32:
                    bok=True
            else:
                if (ord(chainenew[k].upper())>= 65 and ord(chainenew[k].upper()) <= 90) or ord(chainenew[k].upper()) == 32:
                    bok=True

            if bok==False:
                j=0
                btrouve=False
                while(j<len(ListeAccents)):
                    if(ListeAccents[j]==chaine[k]):
                        chaine  = chaine.replace(chaine[k],ReplaceListeAccents[j])
                        btrouve=True
                        break
                    j=j+1
                if btrouve==False:
                    chaine  = chaine.replace(chaine[k]," ")

            k=k+1
        chaine = chaine.upper()
        chaine=self.ReplaceAllDoubleEspace(chaine)
        #chaine=chaine.replace(" ","").strip()
        return chaine

    def ReplaceAllDoubleEspace(self, chaine):
        newchaine = chaine
        while newchaine.find('  ') >= 0:
            newchaine = newchaine.replace('  ', ' ')
        return newchaine.lstrip().rstrip().lstrip()


    def pushButton_clicked(self):
        lock=open("main2.lock", "w")
        lock.close()
##        try:
##            browserExe = "chrome.exe"
##            os.system("taskkill /f /im "+browserExe)
##        except:
##            pass
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Arreter ok", None, QtGui.QApplication.UnicodeUTF8))

    def rafraichirButton_clicked(self):
        traitement=""
        with open(r"traitement.txt", "r") as f :
            traitement = f.read()

        num_compte_en_cours=""
        with open(r"num_compte_en_cours.txt", "r") as f :
            num_compte_en_cours = f.read()

        index = self.traitementBox.findText(traitement, QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.traitementBox.setCurrentIndex(index)
        self.num_compte_en_coursEdit.setText(str(num_compte_en_cours))
        # nombre_traite=""
        # with open(r"nombre_traite.txt", "r") as f :
        #     nombre_traite = f.read()
        # self.nombreTraiteEdit.setText(str(nombre_traite).strip())
        #Affichage nombre traite
        if str(self.campagneBox.currentText()).strip().encode("cp1252")=="":
            MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", str("Veuillez saisir le nom de campagne"), None, QtGui.QApplication.UnicodeUTF8))
            return
        query=QtSql.QSqlQuery(self.db)
        query.prepare("select * from table_tel where campagne=? and message_envoye='x'")
        query.addBindValue(str(self.campagneBox.currentText()).strip().encode("cp1252"))
        if query.exec_()==False:
            MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", str(query.lastError().databaseText()), None, QtGui.QApplication.UnicodeUTF8))
            return
        self.nombreTraiteEdit.setText(str(query.size()))

        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Affichage actualisee", None, QtGui.QApplication.UnicodeUTF8))

    def plainTextAenvoyer_textChanged(self):
        try:
            self.compteCarEdit.setText(str(len(self.plainTextAenvoyer.toPlainText())))
            if len(self.plainTextAenvoyer.toPlainText())>=300:
                texte_300=self.plainTextAenvoyer.toPlainText()[0:300]
                self.plainTextAenvoyer.setPlainText(texte_300)
                self.plainTextAenvoyer.setEnabled(False)
                self.checkBoxActiverPlain.setChecked(False)
        except:
            pass

    def checkBoxActiverPlain_stateChanged(self, arg1):
        if arg1==2:
            self.plainTextAenvoyer.setEnabled(True)
        else:
            self.plainTextAenvoyer.setEnabled(False)

    def checkBoxNombreEnvoi_stateChanged(self, arg1):
        if arg1==2:
            self.nombreEnvoiEdit.setEnabled(True)
        else:
            self.nombreEnvoiEdit.setEnabled(False)

    def initialiserButton_clicked(self):
        nombre_traite = open("nombre_traite.txt", "w")
        nombre_traite.write("0")
        nombre_traite.close()
        self.nombreTraiteEdit.setText("0")
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Nombre traite initialise", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

