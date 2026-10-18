## Guidelines

## for writing and grading of theses, i.e. bachelor- and master theses at the Pattern Recognition Lab

## Status 2. Dezember 2024

These guidelines also apply to dissertations, except for sections that are specific to master or bachelor theses. Information about dissertations can be found in Sec. appendix F on page 15. In the following, we will use the term thesis for master and bachelor theses. [URL 🔗](#page-0)


## Inhaltsverzeichnis


## 1 Contents of the thesis

A thesis contains the parts described in Sections 1.1 - 1.9.

## 1.1 Cover letter

The cover letter has to contain the topic of the thesis, its type (e.g. master or bachelor thesis), the name of the author, his or her date and place of birth, the name of the depart- ment and the chair where the thesis has been prepared, the name(s) of the supervisor(s) and the dates where the thesis was started and finished. An example is given on page 21. The LATEXclass lmedoc provides an environment which adheres to these guidelines. Further information can be found in its documentation1. [URL 🔗](#page-0)

## 1.2 Statement personally signed by the author

The following text has to be included in the preface of the thesis. It has to be personally signed by the author and must not be modified.

Ich versichere, dass ich die Arbeit ohne fremde Hilfe und ohne Benutzung anderer als der angegebenen Quellen angefertigt habe und dass die Arbeit in gleicher oder ¨ahnlicher Form noch keiner anderen Pr¨ufungsbeh¨orde vorgelegen hat und von dieser als Teil einer Pr¨ufungsleistung angenommen wurde. Alle Ausf¨uhrungen, die w¨ortlich oder sinngem¨aß ub¨ ernommen wurden, sind als solche gekennzeichnet.

Die Richtlinien des Lehrstuhls f¨ur Examensarbeiten habe ich gelesen und anerkannt, insbesondere die Regelung des Nutzungsrechts in Punkt 2.5 [URL 🔗](#page-0)

Erlangen, den ........

Unterschrift

## 1.3 Abstract

The abstract should contain a brief summary of the thesis in both German and English (max 0.5 pages each).

## 1.4 Table of contents

The table of content should contain the structure of the thesis. It is generated using the LATEX command \tableofcontents.


## 1.5 Introduction

The introduction should verbally describe the motivation of the thesis, as well as the problems addressed in the thesis. It should be comprehensible for readers not familiar with the topic of the thesis. The introduction should describe connections of the thesis to prior work (i.e. the state of the art), as well as to related work, by citing the relevant publications.

## 1.6 Main section

The main section should be approximately equally split into a theoretical and a practical part.

## 1.6.1 Theoretical part

Merits and limitations of the contribution of the thesis should be presented and interpreted

in the context of the state of the art.

Readers of the thesis are experts. Thus, well known facts and methods should only be mentioned or cited, but should not be explained in full detail (e.g. the Sobel operator, the Fourier transform, linear coding, etc.).

## 1.6.2 Practical part

The practical part should fully describe all necessary algorithms and data structures in- dependent of a programming language, e.g. using pseudo code or flow charts. Memory and time complexity should be provided for each algorithm, as well as their runtime and memory consumption.

The structure of this part depends on the topic of the thesis and should be determined with the supervisor.

Descriptions of experiments should be complete and precise.

## 1.6.3 Images

Whenever it is helpful, the text should be augmented with images. Each image contains a number and a caption, it is always referenced from the text. If the image was not created by the author, its source must be listed in the bibliography and must be referenced in the image caption.

## 1.6.4 Mathematics and symbols

All symbols, that do not have a universal meaning (e.g. π) have to be explained in the text. This also applies when the thesis contains a table of notation.

Under certain circumstances, it can be sufficient to reference an image to explain a symbol. Font types and size in images should match those of the main text.


Mathematical symbols should have one (and only one) fixed definition (e.g. I for images). This definition should also be described in a table of notation in the preface of the thesis. Counters or indices such as i and j are exempt from this regulation.

## 1.7 Summary

The summary shoudl contain the most important results of the thesis. It shoudl also clearly state which of these results are original work of the author. The length should be between three and four pages.

## 1.8 Literature

When using TEX/LATEX , BibTEX or BibLATEXshould also be used. All fields in BibTEX should be filled according to the manual. In particular, pages of articles, as well as date, place and editor of conference proceedings are required.

If there is a peer-reviewed version of a paper, please cite this using the bibtex of the publisher and not the google-scholar, arXiv-bibtex, or similar.

## 1.9 Appendix

The following parts should (if applicable) be part of the appendix:

- 1. images of experiments

- 2. technical details

- 3. long derivations

- 4. other details and information required to complete the thesis

A thesis should be self contained and comprehensible without the appendix. Parts of the appendix should be referenced in the text. Also, each part of the appendix should have a reference to the page or section it belongs to.

## 2 Other regulations

## 2.1 Printing

line spacing Text

literature 1 line

The thesis should be printed on a DIN A4 page. The text area should be ca. 16 cm wide, 26 cm high, 2.5 cm left border, 1.5 cm bottom border. Thesis created with resources of the lab should be written using LATEX . Font size: 12pt. This is automatically set up when using the LATEX template (Appendix A). [URL 🔗](#page-0)

Further information on creating the files for the supervisor can be found in Appendix A. [URL 🔗](#page-0)

1.2 lines


## 2.2 Language

§27, Abs. 6 (1) ABMPO/TechFak vom 18.9.2007 and §32, Abs. 6 (1) ABMPO/TechFak vom 18.9.2007 states, that the thesis, Unless stipulated otherwise in the relevant de-

”

gree programme and examination regulations, the thesis shall be written in German, or in English with the permission of the supervisor. With the supervisor’s agreement, the chairperson of the Examinations Committee may permit students to write the thesis in a different language upon request.“ I.e., the thesis can be written either in German or English. We recommend writing the thesis in English.

## 2.3 Syntax and Grammar

Style, correct syntax and punctuation should be given a high priority.

## 2.4 Printed copies

Usually, a printed copy of the thesis has to be submitted. It should be printed double-sided with a spiral binding. This can be done (black and white print) at the Pattern Recognition Lab, however you may need to make an appointment with the technical staff (Sven Gr¨unke).

All data for evaluation, the source code, any binaries and the text sources, as well as a postscript copy of the thesis have to be submitted to the supervisor (or also to the technical staff) for archiving (see Appendix A). [URL 🔗](#page-0)

## 2.5 Rights of use

A thesis has to be registered with a registration form.

Theses are examinations. The right of use of the results and documents is described in a separate agreement. The standard agreement states that the university receives a right of use of results, see Appendix C. For certain theses, it may be necessary to make adjustments to this agreement. [URL 🔗](#page-0)

## 2.6 External theses

The candidate has to confirm that he or she did not receive money for the thesis.

## 2.7 Unauthorized use of computers, programs or data

We refer to Schreiben des Referats I/1 der FAU zitiert: (Nr. I/1-931-23 vom 17.10.1985)

Danach kann man den Studenten mit gutem Recht sagen, dass die unbefug- te Auskundschaftung fremder Programme und Daten, selbst wenn dies nicht mit Vorteils- oder Sch¨adigungsabsichten verbunden ist, strafrechtlich geahndet wird.


Ub¨erdies muss man nat¨urlich auch auf die zivilrechtliche Folge der Schadenser- satzpflicht f¨ur den Fall hinweisen, dass vor allem durch eine unbefugte Verwen- dung von Programmen und Daten Schaden entsteht.

The unauthorized use of computers, programs or data can be punished by criminal

and/or civil law.

## 2.8 Scientific Process

The standards of good scientific practice by G. H. Altenm¨uller (Naturwissenschaften 85 (1998), S. 140-142) should be adhered to2. [URL 🔗](#page-0)

- All results of the thesis should be reproduceable when submitting the thesis. Para- meters required for reproducing experiments have to be listed.

- All input data required for the experiments have to be submitted to the supervisor.

- Experiments and their interpretation should be conducted with utmost diligence, objectivity and honesty.

- Results and works of others should be considered and referenced in the thesis, as they are the state of the art.

## The following additionally applies to dissertations:

Data and scripts for reproducing all results of the dissertation have to be submitted on a storage medium.

## 2.9 Presentation

A 10-min introductory talk should be given to present the topic of the thesis. Before sub- mitting the thesis, its results should be presented in a 30-min final presentation. Depending on the FPO, the final presentation may contribute to the grade of the thesis.

## 2.10 Documentation

Documentation of the source code should be discussed with the supervisor.

## 3 Grading

## 3.1 Style and form

Consistency, completeness, compactness and comprehensibility of the thesis linguistic expression, spelling, punctuation


meaningfulness of illustrations

logical structure

The length of a thesis is not an indicator of its quality (reference: 40 pages for bachelor thesis, 75 pages for master thesis, excluding apendix).

## 3.2 Scientific approach

## Correctness of statements

presentation of the main themes of the thesis (’common thread’)

preciseness of definitions clear presentation of the methods critical discussion of the results limitations of the approach possibility of generalization or extension completness of the work

## 3.3 Program structure (for practical theses)

modularity and structure, comments and documentation of the program(s)

compatibility with existing programs at the lab definition and adherence to interfaces ease of use

choice of test cases

## 3.4 Innovativeness and achievment

## self-relience, own ideas and initative

findings of the author

investigation and consideration of alternative strategies

use of literature

professional level

novelty

collaboration with the supervisor

Remark: Power is work over time!

## 3.5 Presentation

## Presentation of the fundamental results

use of technology


comprehensibility finishing at the correct time

## 4 Dates and deadlines

## 4.1 Bachelor thesis

General Degree Programme and Examination Regulations for the Bachelor’s and Master’s Degree Programmes and other Study Programmes within the meaning of Section 56 (6) BayHSchG at the Faculty of Engineering at FAU from 18.9.2007 states in §27, Absatz 4f.:

(4) The period between being allocated the subject and submitting the Bache- lor’s thesis (standard thesis work period) shall be five months. The scope of the subject must be such that it can be completed within the standard the- sis work period. With the Examinations Committee’s approval, the supervisor may extend the work period by a maximum of one month upon receiving a justified request. If a student submits a doctor’s certificate proving that they are incapable of working on the thesis due to illness, the period for thesis work shall be suspended temporarily.

(5) The subject of the Bachelor’s thesis may only be returned once and within the first three weeks of the thesis work period; returning the subject shall not be permitted for repetitions of the Bachelor’s thesis. If the subject is returned where it is not admissible, the Bachelor’s thesis shall be graded ,,nicht ausrei- chend” (unsatisfactory; 5.0); it shall be regarded as rejected. Sentence 2 shall apply accordingly if the Bachelor’s thesis is not submitted by the deadline.

## 4.2 Master thesis

General Degree Programme and Examination Regulations for the Bachelor’s and Master’s Degree Programmes and other Study Programmes within the meaning of Section 56 (6) BayHSchG at the Faculty of Engineering at FAU from 18.9.2007 states in §32, Absatz 4f.:

(4) The time between the selection of a subject and the submission of the Master’s thesis (standard thesis work period) shall be six months, or twelve months for part-time degree programmes; the scope of the subject must be such that it can be completed within this period. The Examinations Committee shall have the right to extend the period for the Master’s thesis by a maximum of three months upon receiving a justified request. If a student submits a doctor’s certificate proving that they are incapable of working on the Master’s thesis, the period for thesis work shall be suspended temporarily.

(5) The subject may only be returned once and within the first third of the period for working on the thesis. Otherwise the Master’s thesis shall be graded ,,nicht ausreichend” (unsatisfactory; 5.0) if the subject is returned; it shall be regarded as rejected.


For Computational Engineering und IuK, the deadline can - under exception circum- stances - be extended by two month.


## A Guidlines for TEX

- 1. Theses at the lab should be prepared in LATEX ˙LATEX Reference version is the TeTeX version installed at the Lab.

- 2. The table of content uses depth three.

- 3. The thesis can be compiled using:

- (a) latex mt00

- (b) bibtex mt00

- (c) latex mt00

- (d) bibtex mt00

- (e) latex mt00

- (f) latex mt00

- (g) dvips mt00

- 4. Alternative: latexmk -pdf

- 5. Literature is in mt.bib and can be built using “bibtex mt00” . The literature database is described in 12. [URL 🔗](#page-0)

- 6. The LATEX2ϵ class lmedoc should be used, which loads all styles and adjusts the layout. Details can be found in the class documentation3. [URL 🔗](#page-0)

- 7. In mt00.tex, chapter i is included using “\ include{mt0i}”.

- 8. Tables and TikZ images can be outsourced into TEX files. They should be located in subfolders named tables or figures.

- 9. Algorithms should be described with “strukto” or “algorithmic”.

- 10. Literature is included with “\ include{mt-lit}”.

- 11. Images

- Imaged are positioned using either “[tb]” or “[p]”.

- There should be a relationship between the file name of a picture and the section in which it appears.


- EPS images are included with \includegraphics. They have to be scaleable with a correct boundingbox. They are referenced with

- \figurename~\ref{symbolischesLabel} from the text. Tables are referenced with \tablename~\ref{symbolischesLabel} from the text. Referencing by \autoref{symbolischesLabel} is also possible.

- The text area described in. 2.1 should only be accessed via \linewidth , e.g. with [URL 🔗](#page-0)

\includegraphics[width=0.45\linewidth]{bild}

- 12. Citations are entered with \cite{key}. A extended bibliography style for additional fields in Inproceedings is availabel at the lab.

- 13. Appendix (and other stuff) is optional; Appendix j ∈ [a − z] is included with “\include{mt0j}”.

- 14. Standard notation for mathematical symbols is

- scalar: a (or other small (latin, greek) Symbol)

- Vektor: a (or other small (latin, greek) Symbol)

- Matrix: A (or other large (latin, greek) Symbol)

- for other symbols see e.g. Kobka, LATEX, Chap. 5

Using this notation becomes easy when using the styles boldmath und math. They redefine the commands vec und mat to fit the notation above. Both styles are available when using the lmedoc class.

- 15. A few usful remarks: TEX and LATEX are programming languages. Thus it may be helpful to include comments , e. g. when creating images using PicTEX oder with the picture environment. Blocks starting with begin and ending with end shold be indented.

This also applied to equations. Here, indentation can often dramatically increase the readability. (Leading whitespace is ignored by TEX . Linefeeds (that do not cause a empty line) act like a blank character. The math mode even ignores linefeeds and white space).

The names of variables in in program code should reflect their meaning. This also applies to symbols in Text, e.g to labels.

## B About this document

This document and other templates are in the Git-repo: https://git5.cs.fau.de/thesis- guidelines/thesis-guidelines


## C Agreement

## Erklärung

- 1. Ich versichere, dass ich die Studienarbeit/Diplomarbeit/Bachelor Thesis/Master Thesis (im Folgenden Arbeit genannt) ohne fremde Hilfe und ohne Benutzung anderer als der angege- benen Quellen angefertigt habe und dass die Arbeit in gleicher oder ähnlicher Form noch keiner anderen Prüfungsbehörde vorgelegen hat und von dieser als Teil einer Prüfungsleis- tung angenommen wurde. Alle Ausführungen, die wörtlich oder sinngemäß übernommen wurden, sind als solche gekennzeichnet.

- 2. Mir ist ferner bekannt, dass die Friedrich-Alexander-Universität Erlangen-Nürnberg aufgrund der prüfungsrechtlichen Vorschriften einen Anspruch auf das Original der Arbeit hat. Die er- forderlichen Dateien werde ich in LATEX und postscript dem Lehrstuhl für Mustererken- nung zur Verfügung stellen. Dieser Anspruch bezieht sich jedoch nur auf das körperliche Ei- gentum an der Arbeit als solches und auf deren Verwendung zu den in der Prüfungsord- nung festgelegten Zwecken.

………………………………………...….

Unterschrift

Ort, Datum

## Unabhängig von vorstehender Erklärung und in Ergänzung hierzu erkläre ich Folgendes:

Es entspricht meinem ausdrücklichen Wunsch, dass ich vom Lehrstuhl für Mustererkennung eine Arbeit zur Bearbeitung erhalte, für die die nachfolgenden Bedingungen gelten. Ich wurde darauf hingewiesen, dass ich auch ein anderes Thema hätte erhalten können, für das diese Bedingungen nicht gelten würden. Ich erkläre mich mit folgenden Punkten einverstanden:

- 1. Ich bin damit einverstanden, dass meine Arbeit ins Intranet des Lehrstuhls für Mustererken- nung eingestellt und damit der Öffentlichkeit zugänglich gemacht wird.

- 2. Ich räume der Universität für Zwecke der Forschung und Lehre ein einfaches, kostenloses, zeitlich und örtlich unbeschränktes Nutzungsrecht an den Arbeitsergebnissen einschließlich etwaiger Schutzrechte und Urheberrechte ein. Das Nutzungsrecht der Universität umfasst die Befugnis zur Weitergabe der Arbeit an Dritte zur Nutzung in Forschung und Lehre.

- 3. Wegen des Praxisbezugs meiner Arbeit habe ich Informationen erhalten und Einblick in Un- terlagen genommen, die vertraulich zu behandeln sind. Da die Ergebnisse meiner Arbeit auf den vorgenannten Informationen bzw. Unterlagen beruhen, werde ich meine Arbeit nur mit Zustimmung des betreuenden Hochschullehrers Dritten zugänglich machen bzw. veröffentli- chen.

Ort, Datum

Unterschrift


## D Merkblatt Bachelorarbeit

## I. Mit Beginn einer Bachelorarbeit m¨ussen folgende Formulare ausgef¨ullt und zum Unterschreiben vorgelegt werden:

- 1. Das Thema der BA mit Themanummer

- 2. Immatrikulationsbescheinigung

- 3. Erkl¨arung

- 4. Ausgabe einer Bachelorarbeit (Laufzeit max. 6 Monate)

- 5. Laufzettel f¨ur Examensarbeiten

[Die Unterlagen 1-5 bleiben im Sekretariat]

- 6. Beginnanmeldung der Bachelorarbeit an das Pr¨ufungsamt

## II. Nach Abgabe der BA m¨ussen ausgef¨ullt, unterschrieben und an das Pr¨ufungsamt abgesendet werden:

- 7. u.U. Mitteilung, dass die Arbeit mit der Note mindestens mit 4.0 abgeschlossen wird.

- 8. Endg¨ultige Notenmeldung (in der Regel innerhalb eines Monats nach Abgabe)

Das Themenblatt (1) wird vom Betreuer rechtzeitig vor Ausgabe der Arbeit erstellt und zur Genehmigung vorgelegt; der Betreuer gibt die Daten zur Er- stellung von Erkl¨arung (3), Ausgabe (4), Beginnmeldung (5), Notenmeldung (7) an das Sekretariat von LME. Es ist daf¨ur Sorge zu tragen, dass alle Unter- lagen zentral im Sekretariat des LME archiviert werden.


## E Merkblatt Masterarbeit

## I. Mit Beginn einer Masterarbeit m¨ussen folgende Formulare ausgef¨ullt und zum Unterschreiben vorgelegt werden:

- 1. Das Thema der MA mit Themanummer

- 2. Immatrikulationsbescheinigung

- 3. Erkl¨arung

- 4. Ausgabe einer Masterarbeit (Laufzeit 6 Monate)

- 5. Laufzettel f¨ur Examensarbeiten

[Die Unterlagen 1-5 bleiben im Sekretariat]

- 6. Beginnanmeldung der Masterarbeit an das Pr¨ufungsamt

## II. Nach Abgabe der MA m¨ussen ausgef¨ullt, unterschrieben und an das Pr¨ufungsamt abgesendet werden:

- 7. u.U. Mitteilung, dass die Arbeit mit der Note mindestens mit 4.0 abgeschlossen wird.

- 8. Endg¨ultige Notenmeldung (in der Regel innerhalb 3 Monaten nach Abgabe)

Das Themenblatt (1) wird vom Betreuer rechtzeitig vor Ausgabe der Arbeit erstellt und zur Genehmigung vorgelegt; der Betreuer gibt die Daten zur Er- stellung von Erkl¨arung (3), Ausgabe (4), Beginnmeldung (5), Notenmeldung (7) an das Sekretariat des LME. Es ist daf¨ur Sorge zu tragen, dass alle Unter- lagen zentral im Sekretariat des LME archiviert werden.

## F Dissertations

We refer to Sec. 2.8 for dissertations. A digital volume, containing input data, binaries, source code and results has to be created and submitted. Its content should be described in the thesis. [URL 🔗](#page-0)


## G Merkblatt Archivierung

## zur Sicherung der LATEX und sonstigen Dateien:

- Dateien werden an Herrn Gr¨unke ¨ubergeben. (bspw. via Link-Sharing)

- Herr Gr¨unke best¨atigt dass:

- 1. die Vorschriften von Anhang 1 eingehalten sind;

- 2. die gesamte Arbeit fehlerfrei ¨ubersetzbar ist;

- 3. der Text stichprobenartig mit ‘gv mt00.ps’ angesehen wurde und in Ordnung erscheint;

- 4. es keine ‘Warnings’ beim ¨Ubersetzen gab, bzw. welche es gab;

- Eine DA wird abgelegt nach dem Beispiel /net/files/dipl/da-22/studentinnenname/dateien .

- Eine Masterarbeit wird abgelegt nach dem Beispiel /net/files/mt/mt-22/studentinnenname/dateien .

- Eine Bachelorarbeit wird abgelegt nach dem Beispiel /net/files/bt/bt-22/studentinnenname/dateien .


## H Laufzettel f¨ur Examensarbeiten

Laufzettel für Bachelorarbeiten und Masterarbeiten

Bachelorarbeit: [

]

Masterarbeit: [

]

- 1. Adresse und Betreuer [ ]

Student Vorname und Nachname: Matrikelnummer: Geburtsdatum: Anschrift: Email: Zeitraum: Studiengang:

Name der/s Betreuer/s, Kolloquium:

- 2. Themenbeschreibung mit Literaturangaben und Zeitraum der Arbeit liegt zusammen mit Nummer der Arbeit und der Unterschrift von A. Maier im Sekretariat vor: [ ]

- 3. Student hat Anmeldung, Lehrstuhlrichtlinien und Rechnernutzungsanweisungen anerkannt und unterschrieben und ist in den Emailverteiler des Kolloquiums eingetragen: [ ]

- 4. Arbeit wurde auf der Webseite als neuer Post angelegt: [ ]

- 5. Vorträge (Kurzvortrag [ ], Abschlussvortrag [ ]) [ ]

\- BA: 10 Min. KV; 30 Min. AV (benotet, Gewichtung z.B. INF 3/15) Note:

[

]

\- MA: 10 Min. KV; 30 Min. AV (benotet, Gewichtung z.B. INF 3/30) ......................

[

]

Datum des Abschlussvortrags:

[

]

- 6. Teilnahme am Kolloquium wird bestätigt: [ ]

- 7. Ein Exemplar der gedruckten Arbeit wurde im Sekretariat abgegeben: [ ]

- 8. Die Implementierung und Bedienung der Software wurde dem Betreuer vorgeführt: [ ]

- 9. Falls zutreffend: Die Integration in bestehende Systeme wurde dem Betreuer vorgeführt und bspw. auf USB abgegeben. Die Daten und SW wurde dem Betreuer übergeben: [ ]

- 10. Die Latex-Sourcen (Arbeit muss in Latex abgegeben werden!), der Quellcode, Dokumentation wurde bei Sven Grünke abgegeben (bspw. via Google Drive, FAUbox oder USB-Stick): [ ]

11.

Die Latex-Sourcen wurden von Sven geprüft und können am LME kompiliert werden:

[

]

12.

4.0-Schein wird benötigt (ja) (nein) und wurde nach Ansicht der bisherigen Arbeit

ausgestellt:

[

]

13.

Unnötige Daten wurden gelöscht, restliche Daten an den Betreuer übergeben oder

auf's Archiv ausgelagert. Account und Homeverzeichnis wurden zum Löschen freigeben:

[

]

- 14. Student wurde vom Emailverteiler des Kolloquiums entfernt: [ ]

- 15. Note wurde vergeben und an das Sekretariat oder Prüfungsamt weitergeleitet: [ ]

## Sind alle Kästchen abgehakt gilt die Arbeit als abgeschlossen!

Stand: 11.07.24


## I Wissenschaftliches Arbeiten

## Regeln guter wissenschaftlicher Praxis4 [URL 🔗](#page-0)

Bei der Inanspruchnahme von Mitteln der DFG sind die Grunds¨atze zur Sicherung guter wissenschaftlicher Praxis einzuhalten. Diese Grunds¨atze sind von der Mitgliederver- sammlung der DFG am 17. Juni 1998 beschlossen worden. Danach m¨ussen, wenn eine Hochschule oder ein Forschungsinstitut allein oder gleichberechtigt Empf¨anger der Mittel ist, dort die Regeln guter wissenschaftlicher Praxis (Empfehlung 1) und Regeln f¨ur den Umgang mit Vorw¨urfen wissenschaftlichen Fehlverhaltens (Empfehlung 8) etabliert sein. Zur Sicherung guter wissenschaftlicher Praxis sind an Einrichtungen, die sich nicht an die folgenden Empfehlungen 1 bis 8 halten, keine F¨ordermittel zu vergeben. Die Mitgliederver- sammlung der DFG hat ferner beschlossen, dass die Verweigerung von F¨ordermitteln erst nach einer angemessenen ¨Ubergangsfrist m¨oglich sein soll. Das Ende dieser Frist ist noch nicht bestimmt. Nach Ablauf der Frist m¨ussen vor einer Inanspruchnahme von Mitteln der DFG die folgenden Empfehlungen umgesetzt sein:

## Empfehlung 1:

Regeln guter wissenschaftlicher Praxis m¨ussen - allgemein und nach Bedarf spezifi- ziert f¨ur die einzelnen Disziplinen - Grunds¨atze, insbesondere f¨ur die folgenden Themen,

umfassen:

- allgemeine Prinzipien wissenschaftlicher Arbeit, zum Beispiel:

- lege artis zu arbeiten,

- Resultate zu dokumentieren,

- alle Ergebnisse konsequent selbst anzuzweifeln,

- strikte Ehrlichkeit im Hinblick auf die Beitr¨age von Partnern, Konkurrenten und Vorg¨angern zu wahren,

- Zusammenarbeit und Leitungsverantwortung in Arbeitsgruppen,

- die Betreuung des wissenschaftlichen Nachwuchses,

- die Sicherung und Aufbewahrung von Prim¨ardaten,

- wissenschaftliche Ver¨offentlichungen.

## Empfehlung 2:

Hochschulen und außeruniversit¨are Forschungsinstitute m¨ussen unter Beteiligung ihrer wissenschaftlichen Mitglieder Regeln guter wissenschaftlicher Praxis formulieren, sie allen ihren Mitgliedern bekanntgeben und diese darauf verpflichten. Diese Regeln sollen fester Bestandteil der Lehre und der Ausbildung des wissenschaftlichen Nachwuchses sein.


## Empfehlung 3:

Die Leitung jeder Hochschule und jeder Forschungseinrichtung tr¨agt die Verantwortung f¨ur eine angemessene Organisation, die sichert, dass in Abh¨angigkeit von der Gr¨osse der einzelnen wissenschaftlichen Arbeitseinheiten der Leitung, Aufsicht, Konfliktregelung und Qualit¨atssicherung eindeutig zugewiesen sind und gew¨ahrleistet ist, dass sie tats¨achlich wahrgenommen werden.

## Empfehlung 4:

Der Ausbildung und F¨orderung des wissenschaftlichen Nachwuchses muss besondere Aufmerksamkeit gelten. Hochschulen und Forschungseinrichtungen sollen Grunds¨atze f¨ur seine Betreuung entwickeln und die Leitungen der einzelnen wissenschaftlichen Arbeitsein- heiten darauf verpflichten.

## Empfehlung 5:

Hochschulen und Forschungseinrichtungen m¨ussen unabh¨angige Vertrauensperso- nen/Ansprechpartner vorsehen, an die sich ihre Mitglieder in Konfliktf¨allen, auch in Fragen vermuteten wissenschaftlichen Fehlverhaltens, wenden k¨onnen.

## Empfehlung 6:

Hochschulen und Forschungseinrichtungen sollen bei Pr¨ufungen, bei der Verleihung aka- demischer Grade, Einstellungen und Berufungen Originalit¨at und Qualit¨at stets Vorrang zur Quantit¨at zumessen. Dies soll vorrangig auch f¨ur die leistungs- und belastungsorien- tierte Mittelzuweisung in der Forschung gelten.

## Empfehlung 7:

Prim¨ardaten als Grundlagen f¨ur Ver¨offentlichungen m¨ussen auf haltbaren und gesicher- ten Tr¨agern in der Institution, wo sie entstanden, f¨ur zehn Jahre aufbewahrt werden.

## Empfehlung 8:

Hochschulen und Forschungseinrichtungen m¨ussen Verfahren zum Umgang mit Vorw¨urfen wissenschaftlichen Fehlverhaltens vorsehen. Diese m¨ussen von dem daf¨ur le- gitimierten Organ beschlossen sein und unter Ber¨ucksichtigung einschl¨agiger rechtlicher Regelungen einschliesslich Disziplinarrechts folgendes umfassen:

- eine Definition von Tatbest¨anden, die in Abgrenzung zu guter wissenschaftlicher Pra- xis (Empfehlung 1) als wissenschaftliches Fehlverhalten gelten, beispielsweise Erfin- dung und F¨alschung

von Daten, Plagiat, Vertrauensbruch als Gutachter oder Vorgesetzter,

- Zust¨andigkeit, Verfahren (einschliesslich Beweislastregeln) und Fristen f¨ur Ermitt- lungen zur Feststellung des Sachverhalts,

- Regeln zur Anh¨orung Beteiligter oder Betroffener, zur Wahrung der Vertraulichkeit und zum Ausschluss von Befangenheit,


- Sanktionen in Abh¨angigkeit vom Schweregrad nachgewiesenen Fehlverhaltens,

- Zust¨andigkeit f¨ur die Festlegung von Sanktionen.


## Topic of the thesis in German, or in German and English

## Bachelor’s/Master’s thesis in degree program

submitted by

first name, last name

born MM/DD/YYY in XXX

Written at

Lehrstuhl f¨ur Mustererkennung (Informatik 5)

Department f¨ur Informatik

Friedrich-Alexander-Universit¨at Erlangen-N¨urnberg

Advisors:

Started:

Finished:
