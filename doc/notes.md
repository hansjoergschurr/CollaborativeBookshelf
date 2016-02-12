# Gedanken und Notizen zu ToDos und möglichen Issues

## Grundlegendes

Was wollen wir mit diesem Programm denn eigentlich machen? Wollen wir ein "Host your own Goodreads?", wollen wir was anderes?

Wie gehen wir mit der Tatsache um, daß welche Bücher eine Person besitzt/liest/gutfindet bzw. wer wem welche Bücher borgt teils sehr sensible, persönliche Daten sind, die nicht *leichfertig* gesammelt oder abgreifbar sein sollten.

Warum sollten Menschen dieses Tool verwenden? Wozu?

---
Grundlegender Gedanke war: Oh Freunde haben tolle Bücher, ich hab tolle Bücher; Menschen wären bereit das sich gegenseitig zu leihen, aber das ist irgendwie zach zu handeln. 

Weiters will ich eigentlich nicht noch einem weiteren kommerziellen Unternehmen meine Daten auf dem Silbertablet darbieten. Gerade eben wegen der Sensibilität der Daten.

Dachte das ganze erst mal sehr minimalistisch zu machen. Der pragmatische Gedanke dabei ist, dass dadruch die Wahrscheinlichkeit steigt, dass das ganze auch fertig wird. Da das ganze auch self hosted/beschränkt auf kleineren Personenkreis genutzt wird, ist es auch nicht nötig hunderttausend Funktionen zu implementieren. Statdessen könnte es einfach im normalen Online-Umgang miteinander eingebaut werden. So ala "Ich hab grad das `Link auf dstrbooks` neue Buch gelesen, das könntest du auch toll finden." "Ich hab gesehen du hast `Link auf dstrbook`, könnt ich mir das mal ausleihen" (im Jabber/Twitter DM/Facebook).

## Notwendige Funktionalität

### User Management
Vieles hier wird vermutlich Django für uns übernehmen, sollte aber dennoch mitgedacht werden.

- Login
- Passwortmanagement
- Sessionhandling
- Angelegte User löschen
- kontaktdaten/Benachrichtigungen?

### BookCatalogue Exporte importieren
- Export parsen
- Import
- Wie mit Dublikaten umgehen?
- User Input in Import? ("Dieses Buch nicht importieren, ...")

---
Weitere Gedanken:

 - Solle es ein Invitesystem geben?
 - Wie Dublikate erkennen, ist das überhaupt wichtig?
 - In wieweit von der BookCataloge Datenstruktur abweichen?

### Bookshelves

Buchsammlungen sind sensible Daten!

- Einzelne Bücher nicht importieren/private schalten
- Evt. konfigurierbar machen das Bücher mit gew. UUIDs auch bei späteren Import nicht übernommen werden?
- Datensicherheit!
- Anzeige einzelner Datenfelder konfigurierbar machen
- Sinnvolle Defaults (Alle Bücher private? ...)

### Bookshelves anderer User ansehen

- Wie public?
- Sortierbar

### Social Stuff

- User wegen Leihwunsch kontaktieren? Wie? (Mail durch Tool? oder einfach Kontaktdaten auf user page?)
- Verleihstatus sichtbar machen?
- Wie konfigurierbar? (Nur über reimport abändern, also Konfig über BC app? Oder in dstrbooks änderbar, dadurch aber out-of-sync mit app?)

---

BookCataloge ist das Verleihfeld nur ein Textfeld. Eine Möglichkeit das Verleihen mit zu importieren währe ala Twitter ein besonderes Zeichen ein zu führen um Usernamen zu makieren. Ein @alice könnte bedeuten, dass das Buch an dstrbooks User_in alice verliehen wurde. 

Kontaktdaten hängt imho ein wenig mit der Frage zusamen: Wie sehr soll es Userprofile geben. Reicht bspw. ein toller Freitext mit Avatar?

### Import/Export

- Sync?!? (Änderungen nur über App/reimport wär einfach aber unfreundlich. Andersrum ist benutzbarer, aber macht sync/mergeprobleme. Und Arbeit.)
- Export als druckbares Inventarverzeichnis? Oder statisches html für's blog?
- Wie Duplikate oder zwischenzeitliche Änderung in App-DB handhaben?

---

Eine technisch saubere Lösung währe, glaube ich, den BookCatalog Code zu forken und eine gute Sync Option zu bauen. Das währe, aber auch am aufwendigsten. Es wirft aber auch eine weitere Frage auf: Soll das Ding eine API haben?

Spannende Export optionen sind spannend.

### Extras

- Statistiken? (Pro User? über alle user? Public?)
- Soziales Netzwerkfoo? ("User -- Buch", "User -- User", "Buch -- Buch", ...)
- Buchvorschlagszeugs?

---

Würde private persönliche Statistiken cool finden, Globale nur wenn sie sehr allgemein sind (Wieviele Bücher gibts im System?)

Re.: Privacy: Eine Option das zu implementieren währe über die Bookshelves. in BookCataloge kann ein Buch in meheren Shelves stehen. Ich könnte also ein Buch in den Private Shelve stelle, dann seh nur ichs online, ein anderer Shelve könnte Bücher makieren die nicht importiert werden. Das könnte eine Abfrage während des Importvorgangs sein. Fraglich ist wie ein nicht-import technisch implementiert wird. Die einzig wirklich zuverlässige Funktion währe den Importer komplett in JavaScript auf der Userseite zu implementieren. Ich weisz nicht wie aufwendig das ist. Eine andere option währe das Tar File in ein RAM Filesystem zu laden, zu parsen und dann wieder raus zu löschen. Das könnte zwar einen bösartigen Serveradmin nicht stoppen, aber würde verhindern, dass die Bücher jemals im Admininterface/der Datenbank zu sehen sind.
