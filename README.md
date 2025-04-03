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

### Instaloni varësitë e nevojshme:

- Ky projekt është i shkruar në Python dhe nuk ka varësi të jashtme të nevojshme, përveç Python 3. Sigurohuni që keni Python 3 të instaluar.

### Ekzekutoni programin:

- Pasi të keni shkarkuar skedarët, ekzekutoni programin me komandën:
  _python main.py_

  
### Pasi të ekzekutohet, programi do t'ju kërkojë:
- **Numrin e matricave**
- **Dimensionet e secilës matricë**

### Pas përfundimit të llogaritjes, programi do të shfaqë:

-**Numrin minimal të shumëzimeve skalare.**

- **Renditjen optimale të shumëzimit të matricave.**

### Inputi dhe Outputi
#### Input:

- Lista p[] ku p[i] përfaqëson dimensionin e matricës A(i), që ka dimensionet p[i-1] x p[i].
- Përdoruesi duhet të futë numrin e matricave dhe dimensionet e tyre.

#### Output:

- m[][]: Tabela që përmban koston minimale të shumëzimeve për secilin grup matricash.

- s[][]: Tabela që përmban informacion për ndarjen optimale të matricave.

Shembuj të Inputeve dhe Outputeve

## Testimi dhe Verifikimi
- Ky projekt është testuar me një sërë rastesh për të verifikuar korrektësinë dhe performancën e algoritmit. Disa nga rezultatet e testeve janë:
