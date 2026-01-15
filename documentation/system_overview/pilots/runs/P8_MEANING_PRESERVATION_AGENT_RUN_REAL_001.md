# P8_MEANING_PRESERVATION_AGENT_RUN_REAL_001

## 1. Source Fragment (verbatim, with page/section if known)

Source: data/source_imports/sayur_groente_001/sayur_groente_excerpt_v1.txt (lines 118–146)

```
Sajuran dimakan muda dan mentah sebagai lalab atau direbus

sebagai seupan. Pada galibnja sajuran itu adalah sumber vitamin

A dan €, seperti buah2an, akan tetapi ada djuga diantaranja jang

banjak mengandung protein, seperti daun ubi kaju, daun katuk,

daun lamtoro, daun melindjo, dan dengan begitu merupakan bahan

makan jang sangat berharga. Sajuran banjak mengandung cellulosa

jang sukar ditjernakan, karena itu ia menjempurnakan pembentukan

faccalia dan ikut menimbulkan rasa kenjang.



Djika memasak sajuran djangan memakai suhu jang terlampau

tinggi, sebab vitamin2 tersebut diatas tidak tahan panas.



Kalau mentjutji sajuran supaja dilakukan sebelum di-potong?2,

djangan sesudahnja, untuk mendjaga supaja vitamin C tidak larut

dan hilang.
```

## 2. Step: Translation (agent output)

Groenten worden jong en rauw gegeten als lalab of gekookt als seupan.
In het algemeen zijn groenten een bron van vitamine A en €, zoals fruit,
maar er zijn er ook onder die veel eiwit bevatten, zoals daun ubi kaju,
daun katuk, daun lamtoro, daun melindjo, en daarmee vormen zij een zeer
waardevol voedingsmiddel. Groenten bevatten veel cellulose die moeilijk
te verteren is, daarom vervolmaken zij de vorming van faccalia en dragen
zij bij aan een gevoel van verzadiging.

Als men groenten kookt, gebruik dan geen te hoge temperatuur, want de
bovengenoemde vitaminen zijn niet hittebestendig.

Als men groenten wast, laat het dan gebeuren vóór het di-potong?2, niet
erna, om te voorkomen dat vitamine C oplost en verloren gaat.

Ambiguity notes:
- "A dan €" is onduidelijk; het teken "€" lijkt een OCR-fout.
- "lalab" en "seupan" zijn niet vertaald; de betekenis blijft impliciet.
- "faccalia" is onduidelijk; mogelijk OCR of verouderde term.
- "di-potong?2" is onduidelijk; OCR-artefact in de handeling.

## 3. Step: Readability (agent output + risk notes)

Groenten worden jong en rauw gegeten als lalab, of gekookt als bijgerecht.
In het algemeen zijn groenten een bron van vitamine A en €, net als fruit,
maar sommige bevatten veel eiwit, zoals daun ubi kaju, daun katuk, daun
lamtoro en daun melindjo; daardoor vormen ze een zeer waardevolle
voedselbron. Groenten bevatten veel cellulose die moeilijk te verteren is;
daarom helpen ze de vorming van faccalia en geven ze een vol gevoel.

Kook groenten niet op een te hoge temperatuur, want de bovengenoemde
vitaminen zijn niet hittebestendig.

Was groenten bij voorkeur vóór het di-potong?2, niet erna, om te
voorkomen dat vitamine C oplost en verloren gaat.

Risk notes:
- "seupan" → "bijgerecht": vloeiender, maar betekenisverschuiving mogelijk.
- "zoals fruit" → "net als fruit": lichte herformulering; betekenis vermoedelijk gelijk.
- "daarom vervolmaken zij" → "daarom helpen ze": nuance kan afzwakken.
- "een gevoel van verzadiging" → "een vol gevoel": eenvoudiger, maar nuance kan verschuiven.
- "Als men groenten kookt" → "Kook groenten": directer, maar blijft instructief.
- "laat het dan gebeuren" → "bij voorkeur": voeg voorkeur toe die niet expliciet is.

## 4. Step: Fidelity (agent analysis)

### A) Potential Drift
- "seupan" is vervangen door "bijgerecht", wat mogelijk een specifieke invulling geeft.
- "vervolmaken" is vervangen door "helpen", wat de sterkte van de claim kan verzwakken.
- "een gevoel van verzadiging" is vervangen door "een vol gevoel", wat informeler en minder technisch is.
- "laat het dan gebeuren" is vervangen door "bij voorkeur", wat een voorkeur suggereert in plaats van een aanwijzing.

### B) Why it matters
- Een term als "seupan" kan een specifieke culturele categorie aanduiden; "bijgerecht" kan te modern of te smal zijn.
- De sterkte van voedingsclaims kan inhoudelijk relevant zijn voor historische context.
- Informatieverlies over de mate van verzadiging kan de voedingskundige toon veranderen.
- Een voorkeur in plaats van een instructie kan de praktische waarschuwing verzwakken.

### C) Safer Alternatives (suggestions only)
- "...als lalab of gekookt als seupan" behouden, eventueel met korte toelichting in noot.
- "...daarom vervullen zij de vorming van faccalia" als middenweg tussen letterlijk en leesbaar.
- "...en dragen bij aan een gevoel van verzadiging" behouden voor precisie.
- "Was groenten vóór het di-potong?2" zonder "bij voorkeur" om de instructie te behouden.

## 5. Observed Drift Patterns (short bullets)

- Culturele termen worden snel vervangen door moderne, bredere termen.
- Versterkende woorden (zoals "vervolmaken") worden afgezwakt voor soepelheid.
- Waarschuwende instructies verschuiven naar voorkeurstaal.

## 6. Notes for Future Editors (what to watch out for next time)

- Let op OCR-tekens ("€", "di-potong?2", "faccalia") voordat je parafraseert.
- Bewaak dat waarschuwingen en instructies niet worden afgezwakt in leesbare versie.
- Culturele termen eerst als term behandelen; pas later eventueel toelichten.
