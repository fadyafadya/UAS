import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import streamlit as st
from PIL import Image
import json
import csv
from csv import DictReader
from operator import itemgetter, attrgetter
import statistics

st.set_page_config(layout="wide")  # this needs to be the first Streamlit command called

#--------------- HEADER ---------------
image = Image.open('3.png')
st.image(image)

#--------------- SIDEBAR ---------------
st.sidebar.caption("Fadya Zalfa Rahmanita")
st.sidebar.caption("12220152")
st.sidebar.caption("UAS IF2112 2021/2022")

## User inputs on the control panel #########
st.sidebar.title("SETTINGS")
singkatan_country = []
country = []
a = open('kode_negara_lengkap.json', 'r')
data = json.load(a)
for element in data['cantik']:
    country.append(element["name"])
    
######### GRAFIK 1.a. #########
st.sidebar.caption('Produksi Minyak Mentah Per Tahun')
list_country = st.sidebar.selectbox("Pilih Negara", country)
with open('kode_negara_lengkap.json', 'r') as ko:
    data = json.load(ko)
    for element in data['cantik']:
        if element['name'] == list_country:
            sing = element['alpha-3']
            break
            
######### GRAFIK 1.b. #########
st.sidebar.caption('Produksi Minyak Mentah Terbesar')
tah = st.sidebar.number_input("Jumlah negara terbesar", min_value=1, max_value=None, value=3)
tah2 = st.sidebar.number_input("Pilih tahun *1971--2015", min_value=1, max_value=None, value=1971)

## For Grafik 1.a ##
st.subheader("Produksi Minyak Mentah Per Tahun")
ot = pd.read_csv('produksi_minyak_mentah.csv')
ab = ot[ot.kode_negara == sing]
st.dataframe(ab)
tahunn = list(ab['tahun'].unique())
produksi = list(ab['produksi'])
cmap_name = 'tab20'
cmap = cm.get_cmap(cmap_name)
colors = cmap.colors[:len(tahunn)]
fig, ax = plt.subplots()
ax.bar(tahunn, produksi, color=colors)
ax.set_xlabel("Tahun", fontsize=10)
ax.set_ylabel("Jumlah Produksi", fontsize=10)
st.pyplot(fig)

## For Grafik 1.b. ##
st.subheader("Produksi Minyak Mentah Terbesar")
ap = ot[ot.tahun == tah2]
st.dataframe(ap)
tahunn2 = list(ap['kode_negara'].unique())
produksi2 = list(ap['produksi'])
sue = len(tahunn2)
tahunbe = []
with open('kode_negara_lengkap.json', 'r') as koo:
    data = json.load(koo)
    for element in data['cantik']:
        for i in range(0, sue):
            if element['alpha-3'] == tahunn2[0+i]:
                tahunbe.append(element['name'])
                break
ac = list(map(list, zip(tahunbe, produksi2)))
ase = sorted(ac, key=itemgetter(1), reverse=True)
ajee = ase[:tah]
lst_1_new, lst_2_new = zip(*ajee)

cmap_name = 'tab20'
cmap = cm.get_cmap(cmap_name)
colors = cmap.colors[:len(ajee)]
fig, ax = plt.subplots()
ax.bar(lst_1_new, lst_2_new, color=colors)
ax.set_xlabel("Negara", fontsize=10)
ax.set_ylabel("Jumlah Produksi", fontsize=10)
st.pyplot(fig)

######### Grafik 1.c. #########
st.sidebar.caption('Produksi Kumulatif Terbesar')
tah3 = st.sidebar.number_input("Pada tahun: *1971-2015", min_value=1, max_value=None, value=1978)
st.subheader("Produksi Kumulatif Terbesar")
abb = ot[ot.tahun == tah3]
st.dataframe(abb)
tahunn3 = list(abb['kode_negara'].unique())
produksi3 = list(abb['produksi'])
tahunbee = []
with open('kode_negara_lengkap.json', 'r') as koo:
    data = json.load(koo)
    for element in data['cantik']:
        for i in range(0, sue):
            if element['alpha-3'] == tahunn3[0+i]:
                tahunbee.append(element['name'])
                break
acc = list(zip(tahunbee, produksi3))
asee = sorted(acc, key=itemgetter(1), reverse=True)
lst_1_neww, lst_2_neww = zip(*asee)
suee = len(lst_2_neww)
assuiook = []
for element in lst_2_neww:
    for i in range(0, suee):
        if element != 0.0:
            assuiook.append(element)
            break
accuu = len(assuiook)
ajeee2 = lst_1_neww[:accuu]

cmap_name = 'tab20'
cmap = cm.get_cmap(cmap_name)
colors = cmap.colors[:len(assuiook)]
fig, ax = plt.subplots()
ax.bar(ajeee2, assuiook, color=colors)
ax.set_xlabel("Negara", fontsize=10)
ax.set_ylabel("Jumlah Produksi", fontsize=10)
st.pyplot(fig)

######### 1.d. #########
left_col, mind_col, right_col = st.columns(3)
left_col.subheader("Negara Dengan Produksi Minyak Tertinggi")
left_col.text("Nama Negara: Saudi Arabia")
left_col.text("Kode Negara: SAU")
left_col.text("Region: Asia")
left_col.text("Sub Region: Western Asia")
left_col.text("Pada Tahun: 2015")
ot = pd.read_csv('produksi_minyak_mentah.csv')
absau = ot[ot.kode_negara == 'SAU']
left_col.dataframe(absau)

mind_col.subheader("Negara Dengan Produksi Minyak Terendah")
mind_col.text("Nama Negara: Slovenia")
mind_col.text("Kode Negara: SVN")
mind_col.text("Region: Europe")
mind_col.text("Sub Region: Southern Europe")
mind_col.text("Pada Tahun: 2000")
ot = pd.read_csv('produksi_minyak_mentah.csv')
abssvn = ot[ot.kode_negara == 'SVN']
mind_col.dataframe(abssvn)

right_col.subheader("Negara Dengan Produksi Minyak Nol")
right_col.text("Nama Negara: Belgium")
right_col.text("Kode Negara: BEL")
right_col.text("Region: Europe")
right_col.text("Sub Region: Western Europe")
right_col.text("Pada Tahun: -")
ot = pd.read_csv('produksi_minyak_mentah.csv')
absblr = ot[ot.kode_negara == 'BEL']
right_col.dataframe(absblr)
