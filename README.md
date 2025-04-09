# Implementing a dynamic programming solution to find the most efficient way to multiply a chain of matrices

## Përshkrimi i Projektit

Ky projekt implementon një algoritëm të **Dynamic Programming** për **Matrix Chain Multiplication**, një problem klasik i optimizimit që kërkon të minimizojë numrin e shumëzimeve skalar që janë të nevojshme për të shumëzuar një zinxhir matricash. Ky problem është shumë i rëndësishëm në fusha si inxhinieria e softuerëve, algoritmat e optimizimit dhe llogaritjet numerike.

### Qëllimi

Qëllimi i këtij projekti është të përdorim një qasje dinamike për të gjetur mënyrën më të shpejtë për të shumëzuar një grup matricash. Për këtë, ne përdorim një tabelë të memories që mban informacionin mbi koston minimale të shumëzimeve dhe renditjen optimale për shumëzimin e matricave.

Përveç llogaritjes së numrit minimal të shumëzimeve, algoritmi gjithashtu përcakton mënyrën optimale të parenthesis-imit (vendosjes se kllapave gjate shumezimit) të matricave, për të parandaluar shumëzime të panevojshme dhe për të arritur performancën më të lartë.

## Algoritmi i Përdorur

Algoritmi që përdorim është **Dynamic Programming**, i cili ndihmon në ndarjen e problemit në nënprobleme më të vogla. Ky është një proces iterativ që e ndihmon sistemin të gjejë zgjidhjen optimale për një problem të ndërlikuar.

### Hapet e Algoritmit

1. **Përcaktimi i Matricave dhe Dimensioneve**: 
   - Inputi i këtij algoritmi janë dimensionet e matricave që do të shumëzohen. Çdo matricë ka dimensionin `p[i-1] x p[i]`.

2. **Tabelat e Memorisë (m dhe s)**:
   - `m[i][j]` mban numrin minimal të shumëzimeve që kërkohen për të shumëzuar matricat A(i)...A(j).
   - `s[i][j]` ruan informacionin për ndarjen optimale që minimizon koston e shumëzimeve.

3. **Llogaritja e Kosit të Shumëzimeve**:
   - Algoritmi e ndan problemin në nënprobleme dhe llogarit koston e shumëzimeve për çdo nënproblem, duke i ruajtur rezultatet në tabelat m dhe s.

4. **Gjetja e Parenthesis-imit Optimal**:
   - Përdorim një funksion për të printuar renditjen optimale të shumëzimit të matricave në formatin e kërkuar.

## Si të Përdorni
### Klononi ose shkarkoni këtë depo:

- git clone https://github.com/username/matrix-chain-multiplication.git

### Instaloni varësitë e nevojshme në backend:

- Navigoni në folderin e backend me komandën:
  _cd backend_
  
- Ky projekt është i shkruar në Python prandaj sigurohuni që keni Python 3 të instaluar. Gjithashtu instaloni libraritë e nevojshme duke pwrdor komandën:
  
  _pip install -r requirements.txt_

### Ekzekutoni programin:

- Pasi të keni instaluar varësitë e nevojshme, ekzekutoni programin me komandën:
  _python main.py_

### Testoni programin:

- Testimi i backend-it të programit mund të bëhet duke përdorur Postman. Vendosni linkun e localhost dhe dërgoni një POST request, duke u siguruar se po dërgoni një listë të dimensioneve në body të kërekesës. Në JSON do të duket kështu:

{
  "dimensions": [10,20,30,40,50]
}

### Pas përfundimit të llogaritjes, programi do të kthej përgjigjie në JSON:

- Numrin minimal të shumëzimeve skalare.

- Renditjen optimale të shumëzimit të matricave.


## Instruksionet për Frontend (React)
- Ky projekt përfshin gjithashtu një ndërfaqe përdoruesi të ndërtuar me React, e cila komunikon me API-në e ndërtuar në Flask.

### Setup për Frontend:

#### Instalimi i frontend
- Instalimi i frontend-it fillon me navigimin në folderin e duhur:
  _cd frontend_
- Vijoni me instalimin e varshmërive pwrmes komandws:
  _npm install_
#### Ekzekutimi i Frontend

- Përdorni komandën:
  _npm run dev_

#### Komunikimi me backend  

- Frontend-i dërgon një listë me dimensione përmes një POST request në http://localhost:5000/matrix-chain
- Backend-i kthen një JSON me min_cost dhe optimal_order

#### Input:

- Një fushë inputi ku përdoruesi vendos dimensionet (p.sh. 10 20 30 40)

- Pas klikimit të butonit "Llogarit", të dhënat dërgohen në backend.

#### Output:

- Shfaqet numri minimal i shumëzimeve

- Shfaqet mënyra optimale e shumëzimit me kllapa, p.sh. ((A1 x A2) x A3)

## Testimi dhe Verifikimi
- Ky projekt është testuar me një sërë rastesh për të verifikuar korrektësinë dhe performancën e algoritmit. Disa nga testet janë:
   - Input i zbrazet: Nëse nuk jepen dimensione matrice, algoritmi duhet të kthejë një mesazh gabimi.
   - Matrica e vetme: Kur jepet si input vetëm një matricë, algoritmi duhet të kthejë zero shumëzime skalare, pasi nuk nevojitet shumëzim.
   - Dy matrica: Algoritmi duhet të kthejë koston e shumëzimit të dy matricave. Nuk duhet të ketë nevojë për llogaritje të ndarjes sepse ekziston vetëm një mënyrë.
   - Vlera negative të dimensioneve: Kur dimensionet janë negative ose zero, algoritmi duhet të kthejë një mesazh gabimi që informon përdoruesin se dimensionet duhet    të       jenë numra pozitivë.

