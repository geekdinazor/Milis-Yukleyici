#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QCheckBox, QComboBox, QHBoxLayout

class HosgeldinizPencere(QWidget):
    def __init__(self, ebeveyn=None):
        super(HosgeldinizPencere, self).__init__(ebeveyn)
        self.ebeveyn = ebeveyn

        hosgedinizKutu=QVBoxLayout()
        self.setLayout(hosgedinizKutu)

        hosgeldinizYazi=QLabel(self.tr("<h1>Milis Linux Yükleyiciye Hoşgeldiniz</h1>"))
        hosgeldinizYazi.setAlignment(Qt.AlignCenter)
        hosgedinizKutu.addWidget(hosgeldinizYazi)

        dillerKutu=QHBoxLayout()
        hosgedinizKutu.addLayout(dillerKutu)

        dillerKutu.addWidget(QLabel(self.tr("Lütfen Sistem Ve Yükleyici İçin Bir Dil Seçiniz")))

        self.dillerCombo = QComboBox()
        dillerKutu.addWidget(self.dillerCombo)
        self.dillerCombo.currentTextChanged.connect(self.dillerComboDegisti)
        self.dillerComboDoldur()

        kullanimSartlari = QTextEdit()
        hosgedinizKutu.addWidget(kullanimSartlari)
        kullanimSartlari.setText(self.tr("""Milis Linux (Milli İşletim Sistemi) sıfır kaynak koddan üretilen,\n
        kendine has paket yöneticisine sahip,\n
        bağımsız tabanlı yerli linux işletim sistemi projesidir.\n
        Genel felsefe olarak ülkemizdeki bilgisayar kullanıcıları için linuxu kolaylaştırıp\n
        Milis İşletim Sisteminin sorunsuz bir işletim sistemi olmasını sağlamayı ve yazılımsal\n
        olarak dışa bağımlı olmaktan kurtarmayı esas alır. Ayrıca her türlü katkıda bulunmak\n
        isteyenler için bulunmaz bir Türkçe açık kaynak projesidir.\n"""))

        self.sartKabulKutusu=QCheckBox("Kullanım Şartlarını Kabul Ediyorum.")
        self.sartKabulKutusu.stateChanged.connect(self.sartKabulFonksiyon)
        hosgedinizKutu.addWidget(self.sartKabulKutusu)

    def sartKabulFonksiyon(self):
        if self.sartKabulKutusu.isChecked():
            self.ebeveyn.ileriDugme.setDisabled(False)
        else:
            self.ebeveyn.ileriDugme.setDisabled(True)

    def dillerComboDoldur(self):
        dillerListe = self.ebeveyn.komutCalistirFonksiyon("localectl list-locales")
        dillerListe = dillerListe.split("\n")
        for dil in dillerListe:
            if dil != "":
                self.dillerCombo.addItem(dil)
        self.dillerCombo.setCurrentText("tr_TR.utf8")

    def dillerComboDegisti(self,dil):
        self.ebeveyn.sistemDili = dil