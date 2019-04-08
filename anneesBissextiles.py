#!/usr/bin/env python3
# -*-coding:Utf-8 -*

annee=input("Saisissez un année : ")
annee=int(annee)
if annee%400==0 or (annee%4==0 and annee%100!=0):
    print(annee,"est bissextile.")
else:
    print(annee,"n'est pas bissextile.")
