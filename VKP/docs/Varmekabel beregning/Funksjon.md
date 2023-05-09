
# Beskrivelse
Målet med programmet er at det lett og tilgjengelig går å sette opp en tegning for hvordan varmekabler skal monteres på en plantegning, og som følger kravene til NEK400:2022. Man laster opp et bilde med rikitg målestokk som for eksempel 1:50, og så definerer man rommene ved å lage geometriske former og plasserer dem på tegningen. Det er viktig og også plassere faste plasser der kabler ikke skal ledes, og heller ha en standard avstand fra dem som for eksempel sluk. Programmet må vite hva slags kabel som er oppgitt (fra nexans sine tabeller) og også lengde + forbruk. Ønskelig er å kunne kategorisere hva slags kabel man legger på og tegner inn etter at den er rendered.

## Funksjon 1
Kunne laste opp en plantegning og tegne inn former som er tilpasselig for selve plantegningen (Firkant, Rektangler, Sirkler og Trekanter) og kunne gruppere for å kategorisere for plantegningen (2 rektangler + 1 trekant : Stue, 1 Rektangel : Bad). Også plasser "faste plasser" der det ikke skal gå kabel og som har konstante standardiserte målinger av avstand kablene skal plasseres på (Soner).

## Funksjon 2
Kunne oppgi NEXANS kabel fra tabellene (Lage en database), meter og forbruk, og lage en automatisk tegning av det på de formene som er blitt tegna inn på plantegningen. 

## Funksjon 3
Dokumentasjon for varmekabelanlegg. Dette er det som viser i programmet når man skal tegne og dokumentere. Disse dokumenter gjelder for hver sin kategori (Stue, Bad, Romtyper...):
* "Innstallert av (firma)" - Text Box
* "Innstalleringsadresse" - Text Box
* "Rom" + "Areal" - Text Box + Input Boxes

## Extract all the elements
```python
for page_layout in extract_pages("test.pdf"):
    for element in page_layout:
        print(element)
```

![[Pasted image 20230425145147.png]]
Da får du noe som det her (Hvert element type som bilde, text, og input form)


# Referanser
- https://www.quora.com/How-do-I-create-a-Python-program-that-takes-a-users-input-and-places-it-in-a-PDF-file
- https://stackoverflow.com/questions/17742042/how-to-fill-pdf-form-in-python