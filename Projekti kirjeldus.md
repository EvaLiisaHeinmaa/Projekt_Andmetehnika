### Läänemere Kalapüük.

Projekt
Andmetehnika Mitteinformaatikutele (LTAT.02.026)
Eva-Liisa Heinmaa
Serle Kirispuu

**Sissejuhatus**

Projekt hõlmab Eesti avaandmete allalaadimist (KA20: Läänemere kalapüük), mis sisaldavad näitajaid, aastaid ja kalaliike. Projekti käigus viidi läbi andmete töötlemine, analüüs ning visualiseerimine.
Olulisel kohal oli töö keskkonna seadistamine.
Projekti keskkonnana kasutati GitHubi repositooriumi. Andmete töötlemine toimus Dockeris ja VSCode'is. Andmete visualiseerimine viidi läbi Superseti keskkonnas.

**Andmete päritolu**

Eesti Avaandmed /Estonian Open Data Portal - KA20: LÄÄNEMERE KALAPÜÜK | Näitaja, Aasta ning Kalaliik 

https://andmed.stat.ee/et/stat/majandus__kalandus/KA20/table/tableViewLayout2

**Andmete sisu**

Läänemere kalapüük tegevusala ja kalaliigi järgi.

Andmed näitavad toorkala püügi hulka tonnides Läänemerel järgnevate näitajate põhjal:

* Avamerepüük traallaevadega
* Rannapüük
* Kalapüük Läänemerel kokku

Välja on toodud nii kogu püütud toorkala kogus kui ka andmed liikide lõikes. Andmestikus on esindatud 20 eristatavat kalaliiki ning üks täiendav veerg pealkirjaga "muu kala".

Selles andmebaasis ei ole avaldatud väliskaubandusstatistika andmetabelid.


**Andmete tüüp**

Andmed on tabulaarsed ja tekst-tüüpi. Alla laetud Avaandmete portaalist .xlsx faili formaadis. Exceli fail on salvestatud viisil, mis säilitab õigesti Unicode-märgistuse, võimaldades erimärkide (sh täpitähtede) korrektset kuvamist ja töötlemist.


**Uuenduste sagedus ja ajalooliste andmete kättesaadavus**

Andmeid uuendatakse iga aasta. Andmestik loodi 01.01.1992.
Viimati muudeti 13:43 12.02.2025. Metaandmed on viimati uuendatud 27/03/2025.
Kodutöö raames vaadeldav andmestik sisaldab andmeid alates 2013.a. (OpenData portaal ei näita üle 10000 kirje ja kontot ei tahtnud hetkel teha.)

**Andmete omandiõigus, litsentsimine ja viitamisnõuded**

Andmed on kogunud  Statistikaamet, autor - Veiko Berendsen
Litsents - Creative Commons Attribution 4.0 International


**Privaatsus, eetilised kaalutlused ja vajalikud sammud nende käsitlemiseks**

Andmete allalaadimisel avanes järgneva infoga aken:
*If open data contains personal data, the re-user of open data is obliged to comply with the conditions of the General Regulation on the Protection of Personal Data, including compliance with the principles of processing personal data and the existence of a legal basis.*
Andmestikus ei ole isikuandmeid. 

**Juurdepääsetavus (nt otsene allalaadimine, API) ja teave API kasutamise kohta**

Andmeid on väiksemas koguses võimalik alla laadida.
Andmestik on API vahendusel saadaval GET-päringutega, kuid 
andmetabelites asuvaid andmeid saab pärida vaid POST-päringutega. POST-päringu sisus on JSON-vormingus kirjeldatud, millist osa tabeli andmetest soovitakse ja millises vormingus vastust soovitakse. 
Andmeformaadid milles on võimalik andmeid alla laadida - px, csv, txt, xlsx

**Andmete maht, skaleeritavus ja kvaliteediga seotud kaalutlused**
Andmed on heas korras. Andmetabelis on 95 rida ja 24 veergu. Faili suurus on 21,3 KB (21 912 bytes)
Ümardamise tõttu võivad väärtuste koondandmed erineda liidetavate väärtuste summast

**Vajalikud sammud andmete analüüsiks**

Eemaldada tühjad read, mis tekivad iga uue püügiviisi järel.
Teisendada tekstiväljad numbrilisteks väärtusteks (kalapüügi kogused tonnides).
Teisendada tekstiväljad ajatelje (timeline) väljadeks.
Asendada nullväärtused puuduvate väärtustega (NaN).

**Andmete töötlemine**

Andmetest on manuaalselt eemaldatud pealkirja ja märkuste read. Samuti kaks rida, kus ainukeseks väärtuseks on näitaja.
Andmete lugemisel on kasutatud UTF-8 kodeeringut. (Eesti keelsed täpitähed)
Andmed on viidud Pandas DataFrame'i, lugemiseks on kasutatud openpyxl mootorit, mis toetab .xlsx faile.
Kaks esimest veergu on nimetatud ümber "Näitaja"-ks (andmeliik) ja "Aasta"-ks (aastaarv).
Veerunimedest on eemaldatud tühikud.
Veerud on teisendatud numbrilisteks (v.a. veerg "Näitaja"). Null või vigased väärtused on muudetud NaN-iks.
"Näitaja" veerg teisendatud kategoorilisteks väärtusteks - astype("category"). Uus veerg Näitaja_ID sisaldab iga unikaalse nime kohta täisarvulist ID-d alates 0. See toiming on tehtud SQL päringute lihtsustamiseks.
Andmetest on loodud kalad.parquet fail.

Vt. koodi transform_kalad.py

**Andmete visualiseerimine**

Andmete visualiseerimine Superseti, DuckDB ja SQL Lab-i abil

Projekti andmed visualiseeriti kasutades Apache Superset keskkonda, kuhu andmestik laaditi DuckDB andmebaasiformaadis. 
DuckDB sobib hästi väikeste ja keskmise suurusega andmestike töötlemiseks, kuna see võimaldab töötada otse failipõhise andmebaasiga ilma eraldi serverita.

Andmete analüüsimiseks ja visualiseerimiseks kasutati Superseti SQL Lab-i, kus koostati SQL-päringud. Päringute abil filtreeriti ja grupeeriti andmestik diagrammide loomiseks. 
SQL-päringute tulemusi kasutati dünaamiliste graafikute ja tabelite loomiseks Superseti kasutajaliideses.

Visualisatsioonid hõlmasid:

Kalapüügi koguste muutumist ajas
Püütud kalade koguhulk püügimeetodi ja aastate lõikes
Eesti rahvuskala räime püügikogused püügimeetodite lõikes
Angerja püük
<<<<<<< HEAD
Top 5 ja 4 min püütud kalaliiki
=======
Top 5 püütud kalaliiki
>>>>>>> d56644d2ee4aaed0df8c122963e9f2979496263a
Kalaliikide osakaalude võrdlust erinevatel aastatel
Konkreetsete näitajate kaupa jaotust

**Ilmnenud probleemid**

Apache Superset ei arvesta Pythoni koodis määratud veergude järjestust — veergude järjekord võib Supersetis kuvatuna erineda lähtekoodis määratust. (Näitaja_ID on pythoni koodiga määratud 1.veeruks, Supersetis on see viimasel kohal)
Apache Superseti jagamise võimaluste lihtsustamiseks kulus päris palju aega. Lõpuks otsustasime ikka Dashboard faili alla laadimise ja seejärel Superseti üleslaadimise kasuks.
Andmestik oli algselt laiformaadis (wide format), kus iga kalaliik oli omaette veerus.
Analüüsi ja visualiseerimise jaoks teisendasime selle piklikku formaati (long format), kus liiginimed ja kogused on ridade kaupa. 

**Kokkuvõte**

Projekti käigus loodi toimiv töökeskkond andmete jagamiseks, töötlemiseks ja visualiseerimiseks. Andmestik salvestati .parquet-vormingus, mida kasutati visualiseeringute loomiseks Apache Superseti keskkonnas. Autorite oskuste areng antud töö keskkondade kasutamises oli märkimisväärse.
