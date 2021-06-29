# RM1 pitanja
Skripta koja testira tvoje znanje iz predmeta Računarske Mreže 1 na ETF

Postoji mogućnost biranja gradiva koje ti treba, K1/K2/K3 ili celo gradivo

Pitanja su izvučena [odavde](https://drive.google.com/open?id=1--8WGiKMDDu9VxWT_6gr0pNUEGAPPi2K)

Sintaksa ubacivanja novih pitanja nije preterano teška

Ako bi se neko iscimao i nekako našao, ovo bi radilo za sve moodle tip pitalice uz malo parsiranja

## Dodavanje novih pitanja

Pokrenuti extractquestions.py, koji iz iz txt fajla čita pitanja (ako se dodaju nova, obrisati .txt ili samo koristiti neki drugi da se baza ne duplira)


### Pitanja sa jednim tačnim odgovorom
---
```
@[1/2/3]@ <- Iz koje oblasti je pitanje
::Tekst pitanja...::
~Netačno
~Netačno
=Tačno
~Netačno
Prazan red
```
### Pitanja sa više tačnih odgovora
---
```
@[1/2/3]@ <- Iz koje oblasti je pitanje
::Tekst pitanja...::
~%33.333%Tačno
~%-50%Netačno
~%33.333%Tačno
~%33.333%Tačno
~%-100%Netačno
Prazan red
```
### Pitanja sa upisivanjem odgovora
---
```
@[1/2/3]@ <- Iz koje oblasti je pitanje
::Tekst pitanja...::
~%100% Odgovor
Prazan red
```
### True i False pitanja
---
```
@[1/2/3]@ <- Iz koje oblasti je pitanje
::Tekst pitanja...::
=True
~False
ili
~True
=False
```
Takođe, za više pitanja za redom iz iste oblasti, samo prvo mora imati tag za oblast
