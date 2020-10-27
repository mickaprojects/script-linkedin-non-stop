#!/usr/bin/env python
# -*- coding: cp1252 -*-


from selenium.webdriver.common.keys import Keys
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, uuid
from selenium.webdriver.common.action_chains import ActionChains
from distutils.version import StrictVersion
from numbers import Number
from configparser import ConfigParser
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from openpyxl.workbook import Workbook
import ast

from datetime import date
import time
import datetime
import sys
import os
import random
import glob
import re
import shutil
import traceback, wx
from bs4 import BeautifulSoup
import psycopg2
import psycopg2.extras
import urlparse

reload(sys)
sys.setdefaultencoding("cp1252")




class MainApp(wx.App):
    def OnInit(self):
        frame = menu()
        return True
#20/11/2018
class menu:
    def __init__(self,commande='',matricule=4546):
        if os.path.exists("main.lock")==False and os.path.exists("main2.lock")==False:
            self.dbname="saisie"
            try:
                local      = psycopg2.connect("dbname="+self.dbname+" user=postgres password=123456  host= localhost")
                local.set_client_encoding('WIN1252')
                local.set_isolation_level(0)
                curlocal  = local.cursor(cursor_factory=psycopg2.extras.DictCursor);

            except :
                print("serveur introuvable")
                return False

            try:
                lock=open("main.lock", "a")
                lock.close()
                k = 0
                print("debut")
                #31 07 2018 python27
                trace = open("trace.txt", "w")
                trace.close()
                date_jour1 = str(date.today())
                date_jour=self.date2fr(date_jour1,"/")

                nom_parametre = r"" + "parametres.ini"
                if (os.access(nom_parametre, os.F_OK) == False):
                    trace = open("trace.txt", "a")
                    trace.write("Le fichier parametres.ini est introuvable !\n")
                    trace.close()
                    # print("Le fichier parametres.ini est introuvable !")
                    sys.exit(0)

                c_fichier = r"" + "c.ini"
                if (os.access(c_fichier, os.F_OK) == False):
                    trace = open("trace.txt", "a")
                    trace.write("Le fichier c.ini est introuvable !\n")
                    trace.close()
                    # print("Le fichier parametres.ini est introuvable !")
                    sys.exit(0)

                destinataire=""
                with open(r"destinataire.txt", "r") as f :
                    destinataire = f.read()
                    if destinataire.strip()=="":
                        trace = open("trace.txt", "a")
                        trace.write("Le fichier destinataire.txt est vide" + "\n")
                        trace.close()
                        #sys.exit(0)

                texte=""
                with open(r"texte.txt", "r") as f :
                    texte = f.read()
                    if texte.strip()=="":
                        trace = open("trace.txt", "a")
                        trace.write("Le fichier texte.txt est vide" + "\n")
                        trace.close()
                        sys.exit(0)

                region=""
                with open(r"region.txt", "r") as f :
                    region = f.read()
                    region=region.strip()
                t_region=region.split("\n")

                traitement=""
                with open(r"traitement.txt", "r") as f :
                    traitement = f.read()
                    if traitement.strip()=="":
                        trace = open("trace.txt", "a")
                        trace.write("Le fichier traitement.txt est vide" + "\n")
                        trace.close()
                        sys.exit(0)

                campagne=""
                with open(r"campagne.txt", "r") as f :
                    campagne = f.read()
                    if campagne.strip()=="":
                        trace = open("trace.txt", "a")
                        trace.write("Le fichier campagne.txt est vide" + "\n")
                        trace.close()
                        sys.exit(0)

                num_compte_en_cours=""
                with open(r"num_compte_en_cours.txt", "r") as f :
                    num_compte_en_cours = f.read()
                    if num_compte_en_cours.strip()=="":
                        trace = open("trace.txt", "a")
                        trace.write("Le fichier num_compte_en_cours.txt est vide" + "\n")
                        trace.close()
                        sys.exit(0)

                nombre_envoi=""
                with open(r"nombre_envoi.txt", "r") as f :
                    nombre_envoi = f.read()
                    nombre_envoi=str(nombre_envoi).strip()

                lien_page=""
                with open(r"lien_page.txt", "r") as f :
                    lien_page = f.read()

                #--test page
                url = lien_page
                par = urlparse.parse_qs(urlparse.urlparse(url).query)
                page_encours=""
                try:
                    page_encours=par["page"][0]
                    print("page en cours "+str(page_encours))
                except:
                    print("page en cours vide")
                    pass

                page_debut=""
                with open(r"page_debut.txt", "r") as f :
                    page_debut = f.read()
                    if page_debut.strip()=="":
                        trace = open("trace.txt", "a")
                        trace.write("Le fichier page_debut.txt est vide" + "\n")
                        trace.close()
                        sys.exit(0)

                page_fin=""
                with open(r"page_fin.txt", "r") as f :
                    page_fin = f.read()
                    if page_fin.strip()=="":
                        trace = open("trace.txt", "a")
                        trace.write("Le fichier page_fin.txt est vide" + "\n")
                        trace.close()
                        sys.exit(0)

                if page_encours!="":
                    if traitement=="continuer":
                        if int(page_encours)>=int(page_fin)+1:
                            trace = open("trace.txt", "a")
                            trace.write("La page de fin est atteinte" + "\n")
                            trace.close()
                            sys.exit(0)


                #-------
                config = ConfigParser()
                config.read(nom_parametre)

                config2 = ConfigParser()
                config2.read(c_fichier)

                try:
                    login = u""+str(config2.get('compte', 'login'+str(num_compte_en_cours)))
                    password = u""+str(config2.get('compte', 'password'+str(num_compte_en_cours)))
                except Exception as inst:
                    login = u""+str(config2.get('compte', 'login1'))
                    password = u""+str(config2.get('compte', 'password1'))
                    num_compte_en_cours_fichier = open("num_compte_en_cours.txt", "w")
                    num_compte_en_cours_fichier.write("1")
                    num_compte_en_cours_fichier.close()
                    num_compte_en_cours="1"

                temps_recherche = int(config.get('parametre', 'temps_recherche'))
                temps_apres_authentification = int(config.get('parametre', 'temps_apres_authentification'))
                temps_affichage_resultat = int(config.get('parametre', 'temps_affichage_resultat'))
                scroll = int(config.get('parametre', 'scroll'))

                chromeOptions = webdriver.ChromeOptions()
                chromeOptions.add_argument("--start-maximized")

                prefs = {"profile.default_content_settings.popups": 0,
                         "download.default_directory": "", # IMPORTANT - ENDING SLASH V IMPORTANT
                         "directory_upgrade": True, "extensions_to_open": "", "plugins.plugins_disabled": ["Chrome PDF Viewer"], "plugins.plugins_list": [{"enabled":False,"name":"Chrome PDF Viewer"}]}

                chromeOptions.add_experimental_option("prefs",prefs)
                chromeOptions.add_argument("--disable-print-preview")
                chromedriver = r"chromedriver.exe"
                driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)

                driver.implicitly_wait(temps_recherche)

                wait = ui.WebDriverWait(driver,temps_recherche)

                driver.get("https://www.linkedin.com/uas/login?trk=hb_signin")

                # if traitement=="1":
                #     try:
                #         driver.get("https://www.linkedin.com/m/logout/")
                #         time.sleep(2)
                #     except:
                #         pass
                #     driver.get("https://www.linkedin.com/uas/login?trk=hb_signin")
                # else:
                #     if lien_page.strip()=="":
                #         trace = open("trace.txt", "a")
                #         trace.write("Le fichier lien_page.txt est vide" + "\n")
                #         trace.close()
                #         sys.exit(0)
                #
                #     driver.get(lien_page.strip())

                driver.maximize_window()

                s_script= "document.getElementById('username').setAttribute('value', '%s')"%(login)
                trace = open("trace.txt", "a")
                trace.write("entree login"+"\n")
                trace.close()
                # print("entree login")
                driver.execute_script(s_script)
                s_script= "document.getElementById('password').setAttribute('value', '%s')"%(password)
                trace = open("trace.txt", "a")
                trace.write("entree mdp"+"\n")
                trace.close()
                # print("entree mdp")
                driver.execute_script(s_script)

                #driver.find_element_by_id("btn-primary").click()
                auth_element=driver.find_element_by_xpath("//button[@class='btn__primary--large from__button--floating']")
                auth_element.click()
                trace = open("trace.txt", "a")
                trace.write("clic sur authentification"+"\n")
                trace.close()
                # print("clic sur authentification")
                time.sleep(temps_apres_authentification)

                if traitement=="continuer":
                    if lien_page.strip()=="":
                        trace = open("trace.txt", "a")
                        trace.write("Le fichier lien_page.txt est vide" + "\n")
                        trace.close()
                        sys.exit(0)
                    
                    if page_encours=="2":
                        url2=url.replace("&page=2", "&page="+str(page_debut))
                        driver.get(url2)
                        print("commencer debut page")
                    else:
                        if int(page_encours)<int(page_debut):
                            url2=url.replace("&page="+str(page_encours), "&page="+str(page_debut))
                            driver.get(url2)
                            print("commencer debut page aussi")
                        else:
                            driver.get(lien_page.strip())
                            print("continuer")

                desti=destinataire

                if len(texte)==0 or texte=="":
                    # print("Le texte a envoyer est vide !")
                    trace = open("trace.txt", "a")
                    trace.write("Le texte a envoyer est vide" + "\n")
                    trace.close()
                    sys.exit(0)
                if traitement=="commencer_page_1":
                    search=driver.find_element_by_xpath("//artdeco-typeahead-deprecated[@class='search-typeahead-v2 ember-view']/artdeco-typeahead-deprecated-input[@class='ember-view']/input")
                    search.clear()
                    #search.send_keys(u""+str(desti))
                    search.send_keys(u""+str(""))
                    search.send_keys(Keys.RETURN)
                    time.sleep(temps_affichage_resultat)

                print("1")
                nombre_traite_valeur="0"
                with open(r"nombre_traite.txt", "r") as f :
                    nombre_traite_valeur = f.read()
                    nombre_traite_valeur=str(nombre_traite_valeur).strip()
                try:
                    nombre_traite_valeur=int(nombre_traite_valeur)
                except:
                    nombre_traite_valeur=0
                xx=0+nombre_traite_valeur
                nbre_traite_encours=0
                v=0
                print("2")
                while True:
                    try:
                        driver.execute_script("window.scrollTo(0, 0);")
                        time.sleep(1)
                        #print("ok")
                        
                        # liste_trouve=driver.find_elements_by_xpath("//li[@class='search-result search-result__occluded-item ember-view']")
##                        try:
##                            #ul=driver.find_element_by_xpath("//ul[@class='search-results__list list-style-none']")
##                            ul=driver.find_element_by_xpath("//ul[@class='search-results__list list-style-none mt2']")
##                        except:
##                            try:
##                                ul=driver.find_element_by_xpath("//ul[@class='results-list ember-view']")
##                            except:
##                                try:
##                                    ul=driver.find_element_by_xpath("//ul[@class='search-results__list list-style-none']")
##                                except:
##                                    ul=driver.find_element_by_xpath("//ul[@class='results-list ember-view']")

                        print("3")
                        #liste_trouve=ul.find_elements_by_tag_name("li")
                        num_r=0
                        if len(t_region)>0:
                            v=v+1
                            print("4")
                            for r in t_region:
                                if traitement=="continuer":
                                    pass
                                else:
                                    if v==1:                                        
                                        try:                                                                            
                                            driver.find_element_by_xpath("//button[@data-control-name='clear_filters']").click()
                                            #if traitement=="continuer":
                                            #    driver.get(lien_page.strip())
                                                
                                        except:
                                            pass

                                        num_r+=1
                                        print("5")
                                        #clic tous les filtres
                                        time.sleep(3)
                                        tous_filtres=driver.find_element_by_xpath("//button[@data-control-name='all_filters']")
                                        tous_filtres.click()
                                        #saisie titre
                                        #input id search-advanced-title
                                        time.sleep(1)
                                        print("6")
                                        if str(desti).strip()!="":
                                            titre_reel=u""+chr(34)+str(desti)+chr(34)
                                            titre=driver.find_element_by_xpath("//input[@id='search-advanced-title']")
                                            titre.clear()
                                            titre.send_keys(titre_reel)
                                        print("7")
                                        #saisie region
                                        classes=driver.find_elements_by_xpath("//div[@class='type-ahead-wrapper type-ahead-theme-primary simple-type-ahead is-active']")
                                        elem2=classes[1]
                                        lieu=elem2.find_element_by_xpath("./div[@class='type-ahead-input-container']/div[@class='type-ahead-input-wrapper']/div[@class='type-ahead-input']/input[@class='ember-text-field ember-view']")
                                        print("8")
                                        lieu.clear()
                                        lieu.send_keys(u""+r)
                                        time.sleep(5)
                                        #lieu.send_keys(Keys.ARROW_DOWN)
                                        lieu.send_keys(Keys.RETURN)
                                        time.sleep(2)
                                        #cliquer appliquer filtre
                                        driver.find_element_by_xpath("//button[@data-control-name='all_filters_apply']").click()
                                        print("9")
                                        driver.execute_script("document.title = 'Parametrer les recherches'")
                                        print("Parametrer les recherches")
                                        #time.sleep(120)
                                        driver.execute_script("document.title = 'Traitement continue...'")
                                        print("Traitement continue")

                                #recherche
                                time.sleep(2)
                                print("10")
                                
                                try:
                                    #ul=driver.find_element_by_xpath("//ul[@class='search-results__list list-style-none']")
                                    #ul=driver.find_element_by_xpath("//ul[@class='search-results__list list-style-none mt2']")
                                    ul=driver.find_element_by_xpath("//div[@class='blended-srp-results-js pt0 pb4 ph0 container-with-shadow']/ul[@class='search-results__list list-style-none mt2']")
                                    print("ul 1")
                                except:
                                    try:
                                        ul=driver.find_element_by_xpath("//ul[@class='results-list ember-view']")
                                        print("ul 2")
                                    except:
                                        try:
                                            ul=driver.find_element_by_xpath("//ul[@class='search-results__list list-style-none']")
                                            print("ul 3")
                                        except:
                                            ul=driver.find_element_by_xpath("//ul[@class='results-list ember-view']")
                                            print("ul 4")

                                liste_trouve=ul.find_elements_by_tag_name("li")
                                print("a")
                                #liste_trouve=ul.find_elements_by_xpath("./li[@class='search-result search-result__occluded-item ember-view']")
                                if len(liste_trouve)>0:
                                    scroll_val=0
                                    val1=liste_trouve[0]
                                    tableau=val1.text.split("\n")
                                    region_val=tableau[len(tableau)-2]
                                    region_val2=tableau[len(tableau)-1]
                                    chaine_a_rechercher=str(r).encode("utf-8")
                                    print("b")
                                    print("a rechercher "+chaine_a_rechercher)
                                    print("region val "+region_val)
                                    if str(region_val).encode("utf-8").find(chaine_a_rechercher)==-1:
                                        if str(region_val2).encode("utf-8").find(chaine_a_rechercher)!=-1:
                                            print("c")
                                            pass
                                        else:
                                            print("d")
                                            pass
                                            #continue
                                    print("nbre de lignes: "+str(len(liste_trouve)))
                                    for x in range(len(liste_trouve)):
                                        # xx+=1
                                        # time.sleep(2)
                                        #print("*** "+liste_trouve[x].text.encode("cp1252", "ignore"))
                                        if liste_trouve[x].get_attribute("class")=="search-result search-result__occluded-item ember-view":
                                            print("debut boucle liste trouvee")
                                            #time.sleep(3600)
                                            try:
                                                driver.find_element_by_xpath("//button[@data-control-name='overlay.close_conversation_window']").click()
                                                time.sleep(1)
                                            except Exception as inst:
                                                pass

                                            scroll_val+=scroll
                                            desti1=liste_trouve[x]
                                            #print(dir(desti1))
                                            #print(desti1.get_attribute("class"))
                                                                                    
                                            #time.sleep(3600)
                                            text1=desti1.text
                                            text2=text1.split("\n")[0]
                                            nom_acteur_text=text2
                                            trace = open("trace.txt", "a")
                                            trace.write("--- "+nom_acteur_text.encode("utf-8")+"\n")
                                            trace.close()
                                            print("----- "+nom_acteur_text.encode("utf-8"))                                        
                                            tab1=text1.split("\n")
                                            region_text=tab1[len(tab1)-2]
                                            try:
                                                fonction_text=tab1[len(tab1)-3]
                                            except:
                                                fonction_text=""
                                            print("affichage fonction")
                                            nom_nettoye=self.retour_chaine_nettoyee(nom_acteur_text.encode("cp1252", "ignore"))
                                            curlocal.execute("select nom_nettoye from table_tel where campagne='"+campagne+"' and nom_nettoye='"+nom_nettoye+"'")
                                            t=curlocal.fetchall()                                        
                                            if len(t)==0:
                                                self.insertion("table_tel",["nom","nom_nettoye","fonction","region","fonction_recherche","campagne","compte"], [nom_acteur_text.encode("cp1252", "ignore"),nom_nettoye,fonction_text.encode("cp1252", "ignore"),region_text,desti,campagne,login],local)
                                                print("insertion")
                                            else:                                            
                                                driver.execute_script("window.scrollTo(0, "+str(scroll_val)+");")
                                                print("deja existant donc enregistrement suivant")
                                                continue
                                            try:
                                                bouton_connect=desti1.find_element_by_xpath(".//div[@class='ember-view']/button")
                                                text_bouton_connect=bouton_connect.text
                                                print("100")
                                                if text_bouton_connect.lower().find("connect")!=-1:
                                                    time.sleep(1)
                                                    print("101")
                                                    bouton_connect.click()
                                                    time.sleep(1)
                                                    print("102")
                                                    trace = open("trace.txt", "a")
                                                    trace.write("bouton connect trouve"+"\n")
                                                    trace.close()
                                                    print("103")
                                                    #ajout enlever blocage adresse email 20/07/2018
                                                    try:
                                                        connecter2=driver.find_element_by_xpath("//div[@role='document']/div[@class='ph4']/label[@for='email']/input[@id='email']")
                                                        driver.find_element_by_xpath("//header[@class='send-invite__header']/button[@name='cancel']").click()
                                                        time.sleep(1)
                                                        driver.execute_script("window.scrollTo(0, "+str(scroll_val)+");")
                                                        print("104")
                                                        continue
                                                    except Exception as inst:
                                                        log=open(date_jour.replace("/", "-")+".txt", "a")
                                                        traceback.print_exc(file=log)
                                                        log.close()
                                                        print("105")
                                                        pass
                                                    button_add_note=driver.find_element_by_xpath("//div[@class='send-invite__actions']/button[@class='button-secondary-large mr1']")
                                                    button_add_note.click()
                                                    custom_message=driver.find_element_by_xpath("//*[@id='custom-message']")
                                                    custom_message.send_keys(u""+texte)
                                                    time.sleep(1)
                                                    print("avant106")
                                                                                                 
                                                    button_done=driver.find_element_by_xpath("//div[@role='document']/div[@class='send-invite__actions']/button[@class='button-primary-large ml1']")
                                                    button_done.click()
                                                    time.sleep(1)
                                                    print("106")
                                                    bPass=False
                                                    try:                                                    
                                                        custom_message=driver.find_element_by_xpath("//*[@id='custom-message']")
                                                        custom_message.send_keys(u""+texte)
                                                        bPass=True
                                                        print("bpass true")
                                                    except:
                                                        print("exception bpass")
                                                        pass
    ##                                                try:
    ##                                                    for z in range(10):
    ##                                                        custom_message=driver.find_element_by_xpath("//*[@id='custom-message']")
    ##                                                        custom_message.send_keys(u""+texte)
    ##                                                        time.sleep(1)                                                    
    ##                                                                                                     
    ##                                                        button_done=driver.find_element_by_xpath("//div[@role='document']/div[@class='send-invite__actions']/button[@class='button-primary-large ml1']")
    ##                                                        button_done.click()
    ##                                                        time.sleep(2)
    ##                                                        print("suite 106")
    ##                                                except:
    ##                                                    pass
                                                    if bPass==True:                                                        
                                                        print("verif bpass true")
                                                        #time.sleep(3600)
                                                        trace = open("trace.txt", "a")
                                                        trace.write("compte ne pouvant plus envoyer de message"+"\n")
                                                        trace.close()
                                                        try:
                                                            driver.close()
                                                        except:
                                                            pass

                                                        sys.exit(0)
                                                        
                                                    xx+=1
                                                    # nom_acteur=desti1.find_element_by_xpath("//span[@class='name-and-icon']/span[@class='name actor-name']")

                                                    trace = open("trace.txt", "a")
                                                    trace.write("message envoye a {}".format(nom_acteur_text)+"\n")
                                                    trace.close()
                                                    curlocal.execute("update table_tel set message_envoye='x' where campagne='"+campagne+"' and nom_nettoye='"+nom_nettoye+"'")
                                                    local.commit()
                                                    print("message envoye")
                                                    nbre_traite_encours=nbre_traite_encours+1
                                                    nombre_traite = open("nombre_traite.txt", "w")
                                                    nombre_traite.write(str(xx))
                                                    nombre_traite.close()
                                                    print("106a")
    ##                                            elif text_bouton_connect.lower().find("message")!=-1:
    ##                                                print("bouton message")
    ##                                                #time.sleep(3600)
    ##                                                try:
    ##                                                    #bouton_message=desti1.find_element_by_xpath(".//div[@data-control-name='message']/button")
    ##                                                    bouton_message=desti1.find_element_by_xpath(".//div[@data-control-name='srp_profile_actions']/button")
    ##                                                    bouton_message.click()
    ##                                                    time.sleep(3)
    ##                                                    print("clic sur bouton message")
    ##                                                    time.sleep(3600)
    ##                                                    message=driver.find_element_by_xpath("//form[@class='msg-form msg-form--overlay msg-overlay-conversation-bubble__form relative ember-view']/div[@class='msg-form__compose-area relative ember-view']/textarea[@name='message']")
    ##                                                    text_message=texte
    ##                                                    message.send_keys(u""+text_message)
    ##                                                    time.sleep(2)
    ##                                                    driver.find_element_by_xpath("//div[@class='msg-form__right-actions display-flex']/div[@class='ember-view']/button").click()
    ##                                                    time.sleep(2)
    ##                                                    xx+=1
    ##                                                    print("5")
    ##                                                    # print("destinataire: {}".format(nombre_destinataire))
    ##                                                    nombre_traite = open("nombre_traite.txt", "w")
    ##                                                    nombre_traite.write(str(xx))
    ##                                                    nombre_traite.close()
    ##
    ##                                                    # nom_acteur=desti1.find_element_by_xpath("//span[@class='name-and-icon']/span[@class='name actor-name']")
    ##                                                    # nom_acteur_text=nom_acteur.text
    ##                                                    # text1=desti1.text
    ##                                                    # text2=text1.split("\n")[0]
    ##                                                    # nom_acteur_text=text2
    ##
    ##                                                    trace = open("trace.txt", "a")
    ##                                                    trace.write("message envoye a {}".format(nom_acteur_text)+"\n")
    ##                                                    trace.close()
    ##
    ##                                                    fermer_boite_message=driver.find_element_by_xpath("//button[@data-control-name='overlay.close_conversation_window']/li-icon[@type='cancel-icon']")
    ##                                                    fermer_boite_message.click()
    ##                                                    print("6")
    ##                                                except Exception as inst:
    ##                                                    log=open(date_jour.replace("/", "-")+".txt", "a")
    ##                                                    traceback.print_exc(file=log)
    ##                                                    log.close()
    ##
    ##                                                    nombre_traite = open("nombre_traite.txt", "w")
    ##                                                    nombre_traite.write(str(xx))
    ##                                                    nombre_traite.close()
    ##                                                    print("7")
                                                else:
                                                    trace = open("trace.txt", "a")
                                                    trace.write("bouton connect non trouve"+"\n")
                                                    trace.close()

                                                    nombre_traite = open("nombre_traite.txt", "w")
                                                    nombre_traite.write(str(xx))
                                                    nombre_traite.close()
                                                    print("autre cas")
                                            except Exception as inst:
                                                log=open(date_jour.replace("/", "-")+".txt", "a")
                                                traceback.print_exc(file=log)
                                                log.close()
                                                print("107")
                                                continue
    ##                                            try:
    ##                                                bouton_message=desti1.find_element_by_xpath(".//div[@data-control-name='message']/button")
    ##                                                bouton_message.click()
    ##                                                time.sleep(3)
    ##                                                print("108")
    ##                                                message=driver.find_element_by_xpath("//form[@class='msg-form msg-form--overlay msg-overlay-conversation-bubble__form relative ember-view']/div[@class='msg-form__compose-area relative ember-view']/textarea[@name='message']")
    ##                                                text_message=texte
    ##                                                message.send_keys(u""+text_message)
    ##                                                time.sleep(2)
    ##                                                driver.find_element_by_xpath("//div[@class='msg-form__right-actions display-flex']/div[@class='ember-view']/button").click()
    ##                                                time.sleep(2)
    ##                                                print("109")
    ##                                                # print("destinataire: {}".format(nombre_destinataire))
    ##                                                nombre_traite = open("nombre_traite.txt", "w")
    ##                                                nombre_traite.write(str(xx))
    ##                                                nombre_traite.close()
    ##
    ##                                                # nom_acteur=desti1.find_element_by_xpath("//span[@class='name-and-icon']/span[@class='name actor-name']")
    ##                                                # nom_acteur_text=nom_acteur.text
    ##                                                # text1=desti1.text
    ##                                                # text2=text1.split("\n")[0]
    ##                                                # nom_acteur_text=text2
    ##                                                trace = open("trace.txt", "a")
    ##                                                trace.write("message envoye a {}".format(nom_acteur_text)+"\n")
    ##                                                trace.close()
    ##                                                print("110")
    ##                                                fermer_boite_message=driver.find_element_by_xpath("//button[@data-control-name='overlay.close_conversation_window']/li-icon[@type='cancel-icon']")
    ##                                                fermer_boite_message.click()
    ##                                            except Exception as inst:
    ##                                                log=open(date_jour.replace("/", "-")+".txt", "a")
    ##                                                traceback.print_exc(file=log)
    ##                                                log.close()
    ##                                                print("111")
    ##                                                nombre_traite = open("nombre_traite.txt", "w")
    ##                                                nombre_traite.write(str(xx))
    ##                                                nombre_traite.close()
                                            if str(nbre_traite_encours)==nombre_envoi:
                                                page = open("lien_page.txt", "w")
                                                page.write(driver.current_url)
                                                page.close()
                                                try:
                                                    num_compte_en_cours_fichier = open("num_compte_en_cours.txt", "w")
                                                    num_compte_en_cours_fichier.write(str(int(num_compte_en_cours)+1))
                                                    num_compte_en_cours_fichier.close()
                                                except Exception as inst:
                                                    num_compte_en_cours_fichier = open("num_compte_en_cours.txt", "w")
                                                    num_compte_en_cours_fichier.write("1")
                                                    num_compte_en_cours_fichier.close()

                                                a=1/0
                                            driver.execute_script("window.scrollTo(0, "+str(scroll_val)+");")
                                else:
                                    trace = open("trace.txt", "a")
                                    trace.write("aucun resultat trouve"+"\n")
                                    trace.close()
                                #Next
                                
                                time.sleep(2)
                                try:
                                    bouton_next=driver.find_element_by_xpath("//li/button[@class='next']/div[@class='next-text']")
                                except:
                                    try:
                                        bouton_next=driver.find_element_by_xpath("//button[@class='artdeco-pagination__button artdeco-pagination__button--next artdeco-button artdeco-button--muted artdeco-button--icon-right artdeco-button--1 artdeco-button--tertiary ember-view']")
                                    except:
                                        trace = open("trace.txt", "a")
                                        trace.write("envoi termine, toutes les pages ont ete parcourues"+"\n")
                                        trace.close()
                                        try:
                                            driver.close()
                                        except:
                                            pass

                                        sys.exit(0)
                                try:
                                    url_suivant=""
                                    current_url=driver.current_url
                                    parse1 = urlparse.parse_qs(urlparse.urlparse(current_url).query)
                                    page1=parse1["page"][0]
                                    url_suivant=current_url.replace("&page="+str(page1), "&page="+str(int(page1)+1))
                                except:
                                    pass
                                bouton_next.click()
                                print("112")
                                time.sleep(1)
                                print("clic sur page suivante")
                                page = open("lien_page.txt", "w")
                                if url_suivant=="":
                                    url_suivant=current_url
                                page.write(url_suivant)
                                page.close()
                                print("url_suivant: "+str(url_suivant))

                                traitement_fichier = open("traitement.txt", "w")
                                traitement_fichier.write("continuer")
                                traitement_fichier.close()
                                print("113")
                                session_url = open("session_url.txt", "w")
                                session_url.write(str(driver.command_executor._url))
                                session_url.close()

                                session_id = open("session_id.txt", "w")
                                session_id.write(str(driver.session_id))
                                session_id.close()

                                #-----test page-------
                                lien_page2=""
                                with open(r"lien_page.txt", "r") as f :
                                    lien_page2 = f.read()
                                print("lien page apres page suivante "+lien_page2)
                                url = lien_page2
                                par = urlparse.parse_qs(urlparse.urlparse(url).query)
                                page_encours=""
                                try:
                                    page_encours=par["page"][0]
                                    print("apres page suivante, page en cours "+str(page_encours))
                                except:
                                    print("apres page suivante, page en cours vide")
                                    pass
                                
                                if page_encours!="":
                                    print("comparaison "+page_encours+" - "+page_fin)
                                    
                                    if int(page_encours)>=int(page_fin)+1:
                                                                                                                        
                                        trace = open("trace.txt", "a")
                                        trace.write("La page de fin est atteinte" + "\n")
                                        trace.close()
                                        try:
                                            driver.close()
                                        except:
                                            pass
                                        sys.exit(0)
                                #-----------------
                                print("arrive")
                                
                                if page_encours=="3":
                                    print("page encours 3")
                                    
                                    if int(page_debut)>2:
                                        print("ouverture page debut "+page_debut)
                                        url2=url.replace("&page=3", "&page="+str(page_debut))
                                        driver.get(url2)
                                        time.sleep(1)

                                print("114")
                                                                
                        else:
                            # liste_trouve=ul.find_elements_by_xpath(".//li[@class='search-result search-result__occluded-item ember-view']")
                            print("115")
                            if len(liste_trouve)>0:
                                scroll_val=0
                                print("116")
                                for x in range(len(liste_trouve)):
                                    # xx+=1
                                    # time.sleep(2)
                                    try:
                                        driver.find_element_by_xpath("//button[@data-control-name='overlay.close_conversation_window']").click()
                                        time.sleep(1)
                                    except Exception as inst:
                                        pass
                                    print("117")
                                    scroll_val+=scroll
                                    desti1=liste_trouve[x]

                                    text1=desti1.text
                                    text2=text1.split("\n")[0]
                                    nom_acteur_text=text2
                                    print("118")
                                    nom_nettoye=self.retour_chaine_nettoyee(nom_acteur_text.encode("cp1252", "ignore"))
                                    curlocal.execute("select nom_nettoye from table_tel where campagne='"+campagne+"' and nom_nettoye='"+nom_nettoye+"'")
                                    t=curlocal.fetchall()
                                    if len(t)==0:
                                        self.insertion("table_tel",["nom","nom_nettoye","campagne","compte"], [nom_acteur_text.encode("cp1252", "ignore"),nom_nettoye,campagne,login],local)
                                        print("partie 2 insertion")
                                    else:
                                        driver.execute_script("window.scrollTo(0, "+str(scroll_val)+");")
                                        print("partie 2 deja existant donc enregistrement suivant")
                                        continue
                                    try:
                                        bouton_connect=desti1.find_element_by_xpath(".//div[@class='ember-view']/button")
                                        text_bouton_connect=bouton_connect.text
                                        print("119")
                                        if text_bouton_connect.lower().find("connect")!=-1:
                                            time.sleep(1)
                                            bouton_connect.click()
                                            time.sleep(1)
                                            print("120")
                                            #ajout enlever blocage adresse email 20/07/2018
                                            try:
                                                connecter2=driver.find_element_by_xpath("//div[@role='document']/div[@class='ph4']/label[@for='email']/input[@id='email']")
                                                driver.find_element_by_xpath("//header[@class='send-invite__header']/button[@name='cancel']").click()
                                                time.sleep(1)
                                                driver.execute_script("window.scrollTo(0, "+str(scroll_val)+");")
                                                continue
                                            except Exception as inst:
                                                log=open(date_jour.replace("/", "-")+".txt", "a")
                                                traceback.print_exc(file=log)
                                                log.close()

                                                pass
                                            print("121")
                                            button_add_note=driver.find_element_by_xpath("//div[@class='send-invite__actions']/button[@class='button-secondary-large mr1']")
                                            button_add_note.click()
                                            custom_message=driver.find_element_by_xpath("//*[@id='custom-message']")
                                            custom_message.send_keys(u""+texte)
                                            time.sleep(1)
                                            print("122")
                                            button_done=driver.find_element_by_xpath("//div[@class='send-invite__actions']/button[@class='button-primary-large ml1']")
                                            button_done.click()
                                            time.sleep(1)
                                            xx+=1
                                            # nom_acteur=desti1.find_element_by_xpath("//span[@class='name-and-icon']/span[@class='name actor-name']")
                                            print("123")
                                            trace = open("trace.txt", "a")
                                            trace.write("message envoye a {}".format(nom_acteur_text)+"\n")
                                            trace.close()
                                            curlocal.execute("update table_tel set message_envoye='x' where campagne='"+campagne+"' and nom_nettoye='"+nom_nettoye+"'")
                                            local.commit()
                                            print("message envoye")
                                            nbre_traite_encours=nbre_traite_encours+1
                                            nombre_traite = open("nombre_traite.txt", "w")
                                            nombre_traite.write(str(xx))
                                            nombre_traite.close()
##                                        elif text_bouton_connect.lower().find("message")!=-1:
##                                            try:
##                                                bouton_message=desti1.find_element_by_xpath(".//div[@data-control-name='message']/button")
##                                                bouton_message.click()
##                                                time.sleep(3)
##                                                message=driver.find_element_by_xpath("//form[@class='msg-form msg-form--overlay msg-overlay-conversation-bubble__form relative ember-view']/div[@class='msg-form__compose-area relative ember-view']/textarea[@name='message']")
##                                                text_message=texte
##                                                message.send_keys(u""+text_message)
##                                                time.sleep(2)
##                                                driver.find_element_by_xpath("//div[@class='msg-form__right-actions display-flex']/div[@class='ember-view']/button").click()
##                                                time.sleep(2)
##                                                xx+=1
##                                                # print("destinataire: {}".format(nombre_destinataire))
##                                                nombre_traite = open("nombre_traite.txt", "w")
##                                                nombre_traite.write(str(xx))
##                                                nombre_traite.close()
##
##                                                # nom_acteur=desti1.find_element_by_xpath("//span[@class='name-and-icon']/span[@class='name actor-name']")
##                                                # nom_acteur_text=nom_acteur.text
##                                                # text1=desti1.text
##                                                # text2=text1.split("\n")[0]
##                                                # nom_acteur_text=text2
##
##                                                trace = open("trace.txt", "a")
##                                                trace.write("message envoye a {}".format(nom_acteur_text)+"\n")
##                                                trace.close()
##
##                                                fermer_boite_message=driver.find_element_by_xpath("//button[@data-control-name='overlay.close_conversation_window']/li-icon[@type='cancel-icon']")
##                                                fermer_boite_message.click()
##                                            except Exception as inst:
##                                                log=open(date_jour.replace("/", "-")+".txt", "a")
##                                                traceback.print_exc(file=log)
##                                                log.close()
##
##                                                nombre_traite = open("nombre_traite.txt", "w")
##                                                nombre_traite.write(str(xx))
##                                                nombre_traite.close()
                                        else:
                                            print("124")
                                            nombre_traite = open("nombre_traite.txt", "w")
                                            nombre_traite.write(str(xx))
                                            nombre_traite.close()
                                    except Exception as inst:
                                        log=open(date_jour.replace("/", "-")+".txt", "a")
                                        traceback.print_exc(file=log)
                                        log.close()
                                        print("125")
                                        try:
                                            pass
##                                            bouton_message=desti1.find_element_by_xpath(".//div[@data-control-name='message']/button")
##                                            bouton_message.click()
##                                            time.sleep(3)
##                                            print("126")
##                                            message=driver.find_element_by_xpath("//form[@class='msg-form msg-form--overlay msg-overlay-conversation-bubble__form relative ember-view']/div[@class='msg-form__compose-area relative ember-view']/textarea[@name='message']")
##                                            text_message=texte
##                                            message.send_keys(u""+text_message)
##                                            time.sleep(2)
##                                            print("127")
##                                            driver.find_element_by_xpath("//div[@class='msg-form__right-actions display-flex']/div[@class='ember-view']/button").click()
##                                            time.sleep(2)
##                                            # print("destinataire: {}".format(nombre_destinataire))
##                                            nombre_traite = open("nombre_traite.txt", "w")
##                                            nombre_traite.write(str(xx))
##                                            nombre_traite.close()
##                                            print("128")
##                                            # nom_acteur=desti1.find_element_by_xpath("//span[@class='name-and-icon']/span[@class='name actor-name']")
##                                            # nom_acteur_text=nom_acteur.text
##                                            # text1=desti1.text
##                                            # text2=text1.split("\n")[0]
##                                            # nom_acteur_text=text2
##                                            trace = open("trace.txt", "a")
##                                            trace.write("message envoye a {}".format(nom_acteur_text)+"\n")
##                                            trace.close()
##
##                                            fermer_boite_message=driver.find_element_by_xpath("//button[@data-control-name='overlay.close_conversation_window']/li-icon[@type='cancel-icon']")
##                                            fermer_boite_message.click()
                                            print("129")
                                        except Exception as inst:
                                            log=open(date_jour.replace("/", "-")+".txt", "a")
                                            traceback.print_exc(file=log)
                                            log.close()

                                            nombre_traite = open("nombre_traite.txt", "w")
                                            nombre_traite.write(str(xx))
                                            nombre_traite.close()
                                    if str(nbre_traite_encours)==nombre_envoi:
                                        page = open("lien_page.txt", "w")
                                        page.write(driver.current_url)
                                        page.close()
                                        try:
                                            num_compte_en_cours_fichier = open("num_compte_en_cours.txt", "w")
                                            num_compte_en_cours_fichier.write(str(int(num_compte_en_cours)+1))
                                            num_compte_en_cours_fichier.close()
                                        except Exception as inst:
                                            num_compte_en_cours_fichier = open("num_compte_en_cours.txt", "w")
                                            num_compte_en_cours_fichier.write("1")
                                            num_compte_en_cours_fichier.close()

                                        a=1/0
                                    driver.execute_script("window.scrollTo(0, "+str(scroll_val)+");")
                            else:
                                trace = open("trace.txt", "a")
                                trace.write("aucun resultat trouve"+"\n")
                                trace.close()
                            #Next
                            try:
                                bouton_next=driver.find_element_by_xpath("//li/button[@class='next']/div[@class='next-text']")
                            except:
                                try:
                                    bouton_next=driver.find_element_by_xpath("//button[@class='artdeco-pagination__button artdeco-pagination__button--next artdeco-button artdeco-button--muted artdeco-button--icon-right artdeco-button--1 artdeco-button--tertiary ember-view']")
                                except:
                                    trace = open("trace.txt", "a")
                                    trace.write("envoi termine, toutes les pages ont ete parcourues"+"\n")
                                    trace.close()
                                    try:
                                        driver.close()
                                    except:
                                        pass

                                    sys.exit(0)

                            try:
                                url_suivant=""
                                current_url=driver.current_url
                                parse1 = urlparse.parse_qs(urlparse.urlparse(current_url).query)
                                page1=parse1["page"][0]
                                url_suivant=current_url.replace("&page="+str(page1), "&page="+str(int(page1)+1))
                            except:
                                pass
                            bouton_next.click()
                            print("page suivante 2")
                            time.sleep(1)
                            print("130")
                            page = open("lien_page.txt", "w")
                            if url_suivant=="":
                                url_suivant=current_url
                            page.write(url_suivant)
                            page.close()

                            traitement_fichier = open("traitement.txt", "w")
                            traitement_fichier.write("continuer")
                            traitement_fichier.close()
                            print("131")
                            session_url = open("session_url.txt", "w")
                            session_url.write(str(driver.command_executor._url))
                            session_url.close()

                            session_id = open("session_id.txt", "w")
                            session_id.write(str(driver.session_id))
                            session_id.close()

                            #-----test page-------
                            lien_page2=""
                            with open(r"lien_page.txt", "r") as f :
                                lien_page2 = f.read()

                            url = lien_page2
                            par = urlparse.parse_qs(urlparse.urlparse(url).query)
                            page_encours=""
                            try:
                                page_encours=par["page"][0]
                                print("apres page suivante 2, page en cours "+str(page_encours))
                            except:
                                print("apres page suivante 2, page en cours vide")
                                pass
                            if page_encours!="":
                                print("comparaison "+page_encours+" - "+page_fin)
                                if int(page_encours)>=int(page_fin)+1:                                    
                                    trace = open("trace.txt", "a")
                                    trace.write("La page de fin est atteinte" + "\n")
                                    trace.close()
                                    try:
                                        driver.close()
                                    except:
                                        pass
                                    sys.exit(0)
                            #-----------------
                            if page_encours=="3":
                                if int(page_debut)>2:
                                    print("ouverture 2 page debut "+page_debut)
                                    url2=url.replace("&page=3", "&page="+str(page_debut))
                                    driver.get(url2)
                                    time.sleep(1)

                            print("132")
                    except Exception as inst:
                        log=open(date_jour.replace("/", "-")+".txt", "a")
                        traceback.print_exc(file=log)
                        log.close()
                       
                        break
                try:
                    driver.close()
                except:
                    pass

                trace = open("trace.txt", "a")
                trace.write("FIN Traitement envoi message linkedin !"+"\n")
                trace.close()

                #Suppression du fichier .lock
                if os.path.exists('main.lock')==True:
                    os.remove('main.lock')

                sys.exit(0)
                # print("FIN Traitement recuperation donnees !")

            except Exception as inst:
                log=open(date_jour.replace("/", "-")+".txt", "a")
                traceback.print_exc(file=log)
                log.close()
                try:
                    driver.close()
                except:
                    pass
                if os.path.exists('main.lock')==True:
                    os.remove('main.lock')

                traitement_fichier = open("traitement.txt", "w")
                traitement_fichier.write("continuer")
                traitement_fichier.close()

                try:
                    num_compte_en_cours_fichier = open("num_compte_en_cours.txt", "w")
                    num_compte_en_cours_fichier.write(str(int(num_compte_en_cours)+1))
                    num_compte_en_cours_fichier.close()
                except Exception as inst:
                    num_compte_en_cours_fichier = open("num_compte_en_cours.txt", "w")
                    num_compte_en_cours_fichier.write("1")
                    num_compte_en_cours_fichier.close()

                sys.exit(0)

    def insertion(self, table,tzChamp,tzValue,connexion):
        """  Insertion des donnees dans une table;
            parametres:
                table : la table où on veut inserer les données
                tzChamp : les champs concernées par l'insértion (sous forme dde tableau)
                tzValue : les valeurs pour chaque element du tableau champ
                connexion : connexion d'acces à la table

        """
        if(len(tzChamp)==len(tzValue)):
            try:

                i=0
                j=0
                curs = connexion.cursor()
                curs.execute("SET client_encoding = 'WIN1252';")
                connexion.commit()
                sql = ""
                sql += "INSERT INTO \"" + table + "\"("
                while(i<len(tzChamp)):
                    if i == len(tzChamp) - 1:
                        sql+= "\""+tzChamp[i]+"\""
                        i = i+1
                    else:
                        sql+="\""+tzChamp[i]+"\","
                        i = i+1
                sql+=") VALUES("
                while(j<len(tzValue)):
                    if tzValue[j]==None:
                        if j == len(tzValue)-1:
                            sql+=" null "
                            j = j+1
                        else:
                            sql+="null,"
                            j = j+1

                    else:

                        if j == len(tzValue)-1:
                            sql+="'%s'" %(str(tzValue[j]).replace("'","''"),)
                            j = j+1
                        else:
                            sql+="'%s'," %(str(tzValue[j]).replace("'","''"),)
                            j = j+1
                sql+= ")"
                # print sql
                curs.execute(sql.encode("cp1252"))                
                connexion.commit()
                return True
            except Exception as inst:
                msgs =  'type ERREUR78:'+str(type(inst))+'\n'     # the exception instance
                msgs+=  'CONTENU:'+str(inst)+'\n'           # __str__ allows args to printed directly
                print(msgs.encode("utf8"))
                return False

        else:
            print("Nombres des colonnes non identiques")
            return False

    def retour_valeur(self, tchamp, tvaleur, lib_champ):
        for l in range(len(lib_champ)):
            chp=lib_champ[l]
            for c in range(len(tchamp)):
                if tchamp[c].strip()==chp:
                    return u""+tvaleur[c].strip()
        return ""

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
        chaine=chaine.replace(" ","").strip()
        return chaine

    def ReplaceAllDoubleEspace(self, chaine):
        newchaine = chaine
        while newchaine.find('  ') >= 0:
            newchaine = newchaine.replace('  ', ' ')
        return newchaine.lstrip().rstrip().lstrip()

    def nettoye(self, chaine):
        chaine=chaine.replace("\t"," ").replace("\n"," ").replace("  "," ").strip().strip("\t").strip("\n")
        return chaine

    def nz(self, valeur_o,valeur_pardefaut=''):
        if valeur_o=='' or valeur_o==None or valeur_o=='None':
            return valeur_pardefaut
        else:
            return valeur_o

    def date2fr(self, sdateEn,sep="-"):
        a1=sdateEn[0:4]
        m1=sdateEn[5:7]
        d1=sdateEn[8:10]
        return d1+sep+m1+sep+a1

    def retour_lignes_fichier(self, sfichier):
        if os.path.exists(r""+sfichier)==False:
            return ""
        with open(r""+sfichier, "r") as f :
            fichier_entier = f.read()
            if fichier_entier!="":
                lignes = fichier_entier.split("\n")
                return lignes
            else:
                return ""

if __name__ == "__main__":
    app = MainApp()
    app.MainLoop()
