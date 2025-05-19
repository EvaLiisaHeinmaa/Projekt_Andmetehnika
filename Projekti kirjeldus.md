Läänemere Kalapüük.

Andmete päritolu:

Eesti Avaandmed /Estonian Open Data Portal - KA20: LÄÄNEMERE KALAPÜÜK | Näitaja, Aasta ning Kalaliik 

https://andmed.stat.ee/et/stat/majandus__kalandus/KA20/table/tableViewLayout2

Andmete sisu:

Andmed näitavad toorkkala püügi hulka tonnides Läänemerel järgneva näitaja põhjal:

* Avamerepüük traallaevadega
* Kalapüük Läänemerel kokku
* Rannapüük

Välja on toodud nii kogu püütud toorkala hulk, kui erinevate liigite kaupa. 20 eristatatavat kalaliiki ja üks veerg pealkirjaga "muu kala" .

Selles andmebaasis ei ole avaldatud väliskaubandusstatistika andmetabelid.



Andmete tüüp:

Andmed on tabulaarsed ja tekst-tüüpi. Alla laetud Avaandmete portaalist .xcxl faili formaadis. 

Andmete töötlemine:

Andmetest on manuaalselt eemaldatud pealkirja, märkuste read ja kaks rida, kus ainukesek väärtuseks on näitaja.
Andmed on viidud Pandas DataFrame'i, lugemiseks on kasutatud openpyxl mootorit, mis toetab .xlsx faile.
Kaks esimest veergu on nimetatud ümber "Näitaja"-ks (andmeliik) ja "Aasta"-ks (aastaarv).
Veerunimedest on eemaldatud tühikud
Veerud teisendatud numbrilisteks (v.a. veerg "Näitaja"). Vigased väärtused muudetud NaN-iks.
"Näitaja" veerg teisendatud kategoorilisteks väärtusteks - astype("category"). Uus veerg Näitaja_ID sisaldab iga unikaalse nime kohta täisarvulist ID alates 0. 
Andmetest on loodud kalad.parquet fail.

Vt. koodi transform_kalad.py


Andmeid uuendatakse iga aasta. Andmestik loodi 01.01.1992.
Viimati muudeti 13:43 12.02.2025.
Kodutöö raames vaadeldav andmestik sisaldab andmeid alates 2013.a. (OpenData portaal ei näita üle 10000 kirje ja kontot ei tahtnud hetkel teha.)

**Data ownership, licensing, and attribution requirements**
Andmed on kogunud  Statistikaamet, autor - Veiko Berendsen
Litsents - Creative Commons Attribution 4.0 International


**Privacy, ethical concerns, and necessary steps to address them**
Andmete allalaadimisel avanes järgneva infoga aken:
*If open data contains personal data, the re-user of open data is obliged to comply with the conditions of the General Regulation on the Protection of Personal Data, including compliance with the principles of processing personal data and the existence of a legal basis.*
Andmestikus ei ole isikuandmeid. 

**Accessibility (e.g., direct download, API) and any API usage information**
Andmeid on väiksemas koguses võimalik alla laadida. (kasutasin OpenDatast otse allalaadimise võimalust)
Andmestik on API vahendusel saadaval GET-päringutega, kuid 
andmetabelites asuvaid andmeid saab pärida vaid POST-päringutega. POST-päringu sisus on JSON-vormingus kirjeldatud, millist osa tabeli andmetest soovitakse ja millises vormingus vastust soovitakse. 
Andmeformaadid - px, csv, txt, xlsx

**Data size, scalability, and quality considerations**
Andmed on heas korras. Andmetabelis on 95 rida ja 24 veergu. Faili suurus on 21,3 KB (21 912 bytes)
Ümardamise tõttu võivad väärtuste koondandmed erineda liidetavate väärtuste summast

**Preprocessing and cleaning tasks required before analysis**
* Eemaldada tühjad read - iga uue püüdmisviisiga kaasneb tühi rida.
* Muuta tekstiväljad numbrilisteks (kalapüügi hulgad tonnides)
* Muuta tekstiväljad *timeline* väljadeks
* Muuta nullväärtustega väljad Nanideks

