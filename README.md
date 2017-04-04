## DOKUMENTÁCIA

Terinálové človeče. Druhá domáca úloha na predmet Prcinípy a tvorby softwaru. Účelom je využiť immutable design pri vytváraní programu.

## Terminálové človeče

Oproti klasickej hre Človeče nehnevaj sa má Terminálove človeče mnoho zjednodušení ale na druhej strane a možnosti navyše.

**Pravidlá hry:**
Na cyklyckej ploche je rozostavených n políčok niekoľko z nich sú štartovacíe políčka jednotlivých hráčov.
Políčka na hernej ploche sú očíslované od 0 po n-1.
Hráč môže mať svoje figúrky na ľubovoľnom z týchto políčok, pokojne aj všetky na jednom, avšak akonáhle sa pokúsi súper vstúpiť na toto políčko, všetky figúrky tam nachádzajúce vyhodí (teda ak sa tam nenachdázajú jeho vlastné).
Každý hráč má **4 figúrky**. Všetky začínajú na pozícií **-1** nazvime v domčeku, z domčeka sa nevyhadzuje, ak je figúrka vyhodená, poputuje do domčeka.
Najmenší počet hráčov je **2**. Hráči sú očíslovaný od 0 po počet hráčov - 1.
Každý hráč má svoje štartovacie políčko nachádzajúce sa na políčku (číslo hráča)*OFFSET.
**OFFSET** je vzdialenosť medzi jednotlivými štartovacími políčkami.
Vypočíta sa ako **BOARD_SIZE** deleno **MAX_PLAYERS**, pročom BOARD_SIZE je počet políčok na hernej ploche a MAX_PLAYERS je maximálny počet hráčov. Tieto koštanty je možné si zvoliť v súbore constants.py.
Každý hráč hádže kockov na ktorej sú čísla od 1 po 6 vrátane. Po padnutí kocky, hráč sa toto číslo dozvie, si hráč volí ktorou figúrkou sa chce pohnúť. Ak sa chce pohnúť figúrkou nachádzajúcou sa v domčeku, figúrka sa presunie na pozíciu štartovacie políčko hráča + výsledok hodu kockov - 1.
Hráči sa striedajú v hádzaní kocky postupne podľa ich čísiel, začínajúci hráč je vybraný náhodne.
Každý hráč ktorému sa podarí prejsť figúrkou cez svoju štartovaciu pozíciu získa 1 bod. Hra je nekonečná.

## Immutable desing

Hra je uložená v stave. Ak sa niečo v hre zmení, napríklad hráč presunie figúrku, vytvorí sa nový stav ktorý je kópiou predchádzajúceho až na vykonanú zmenu. Jednotlivé stavy hry sú ukladané.

## Príkazy

**throw** - hod kockou

**undo** - vrátenie sa do predchádzajúceho stavu hry

**quit** - ukončenie hry s výpisom výslednej tabuľky dosiahnutých bodov

