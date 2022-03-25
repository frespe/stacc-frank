# Stacc code challenge 2021

## Oppgavebeskrivelse
> Oppgaven eg har løst går ut på at man foretar en enkel PEP-sjekk av datasettet som er vedlagt, pep.csv.
>I oppgaven som er levert tar eg utgangspunkt i å teste dataen min på pep_small.csv, ettersom at dette datasettet er svært lite. I tilegg kan eg legge til data, som feks å inkludere high-risk-country personer, og legge til sanksjoner - dette siden ingen i pep.csv-filen hadde noken sanksjoner i heile tatt. 
>Måten dette blir gjort på, er at man gir input i form av navn og vedkommendes ID, og får et ouput som viser til om personen er PEP eller ikkje. 


## Hvordan kjøre prosjektet
>Veldig simpel, men fungerende måte å kjøre prosjektet. Man kjører heile PEP.py, og dermed tar main-funksjonen over, og det eneste du som bruker må gjøre er å gi input i terminalen.
>Ettersom at filen inneholder små og store bokstaver, så har eg gjort det sånn at input kan være alt i små bokstaver, alt i store, eller en blanding, slik at man skal få ett treff på navn uansett.
>Dette gjelder også for personens ID. For at brukeren skal få input, så må navnet og vedkommendes ID stemmer. Viss det ikkje er riktig, så starter metoden på ny, og man må gi nytt input. Dette er berre en enkel feilhåndtering for å sikre at kundens identitet stemmer, som er ett viktig punkt innenfor KYC.
>Output vises i terminalen.

>Så for å vise ett eksempel:
>Du vil først sjekke om personen har sanksjoner tilknyttet seg.
>Du gir input feks: oleg slizhevskiy i fra csv-filen når terminalen spør om navn. 
>Deretter bes det om personens ID, og da legger man inn NK-23wLbkLretoJxTci3VMZwE. <-Denne må stemmer overens med navnet, viss ikkje blir det vist feilmelding, og man må gi input på ny 
>Output blir om personen har sanksjoner

>Videre må man gi nytt input for å sjekke navn i forhold til PEP-sjekk. 
>Akkurat samme framgansmåte som over, men ulik output.
>Nemlig, om personen er PEP - politsk gren og eventuell high risk country.

## Kommentarer
> Slik eg forstod det, så er definisjonen av KYC/PEP svært stor, med mange punkt. Ettersom at eg har best kjennskap til back-end biten, så valgte eg å implementere eit eget program som tok utganspunkt i det utleverte datasettet. For å filtrere ut dataen og bestemme seg for ka som skulle inkluderes denne KYC-sjekken, så kunne eg ved hjelp av litt undersøking på nettet finne ut at PEP-sjekk og sanksjoner var viktige holdepunkt. Det er derfor eg først foretar en sanksjon-sjekk av personen før eg videre foretar en PEP-sjekk. Under en KYC-sjekk, så kom eg over punktet Enhanced Due Diligence, som tar for seg en rekke tillegspunkter. En av disse var "high risk countries" som er merka land i forhold til KYC-sjekker. Derfor valgte eg å inkludere dette i PEP-sjekken min. For å enkelt sjekke dette, så lastet eg ned et datasett som innehold 2-koden for alle land. Deretter fann eg listen over alle high-risk-countries, og sammenlignet koden opp i mot denne listen i en egen metode get_high_risk_countires. Til slutt returnerte eg denne koden i en liste som ble sjekket opp i mot personens "country" i csv-filen inne i pep_check().

Så enkelt forklart: PEP-sjekken og sanksjon-sjekken eg har implementert gir output om du er:
>En PEP-person <- bruk Thomas BLOMQVIST
>En PEP-Person, men også fra et high-risk land <- bruk Abdoulaye Diouf SARR
>Ikkje en PEP-person, men sanksjoner <- Oleg SLIZHEVSKIY
>Minner også på at det er viktig at personens ID stemmer med navnet, viss ikkje får man ikkje output.


>Helst skulle eg ha koplet denne back-end delen opp i mot frontend ved å ta i bruk react og flask, men dette blei ikkje prioritert, ettersom at tidsskjemaet blei knapt, og erfaringen med frontend er minimal, og dette ville tatt en god del tid. 


>Som nevnt tidligere, så kan dette testes på den største csv-filen ved å endre open_file metoden til å åpne pep.csv i stedet for pep_small.csv, men alle personene som er i pep_small.csv er lagt til slik at de skal ta hensyn til alle punktene ovenfor, slik at man kan teste funksjonene på dei.

