Poniżej znajduje się kod (wraz z jego zastosowaniem) użyty w kursie "MongoDB M001".

#IMPORT/EXPORT DANYCH W:
JSON:
mongoimport --uri="mongodb+srv://<your username>:<your password>@<your cluster>.mongodb.net/sample_supplies" --drop sales.json
mongoexport --uri="mongodb+srv://<your username>:<your password>@<your cluster>.mongodb.net/sample_supplies" --collection=sales --out=sales.json

BSON (BINARY JSON):
mongorestore --uri "mongodb+srv://<your username>:<your password>@<your cluster>.mongodb.net/sample_supplies"  --drop dump
mongodump --uri "mongodb+srv://<your username>:<your password>@<your cluster>.mongodb.net/sample_supplies"

#ZAPYTANIA DO BAZY DANYCH W MONGODB ATLAS:
FILTER {"city": "NEW YORK"}
       {"state": "NY"}
       {"state": "NY", "city": "ALBANY"}

#ZADANIE:
Używając MongoDB Atlas, z kolekcji sample_training.trips dla osoby urodzonej w 1961 r. oraz startującej wycieczkę ze stacji "Howard St & Centre St" znajdź stację końcową.

Zapytanie: {"birth year": 1961, "start station name": "Howard St & Centre St"}
Rozwiązanie: "South End Ave & Liberty St"

#POŁĄCZENIE Z BAZĄ DANYCH ORAZ PODSTAWOWE ZAPYTANIA UŻYWAJĄC MONGOSHELL (terminal):

Połączenie się z bazą danych:                                mongo "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.lzya6.mongodb.net/admin"

Wskazanie zawartości bazy danych:                            show dbs

Przełączenie się na konkretną bazę danych:                   use sample_training

Wskazanie kolekcji zawartych w bazie danych:                 show collections

Zapytanie: wskaż dokumenty, gdzie "state" jest równy "NY":   db.zips.find({"state": "NY"})

Wskaż kolejną "kartę" (zakładając, że na jedną kartę przypada np. 20 wyników):  it

Zapytanie: Policz ilość dokumentów pasujących do zapytania:  db.zips.find({"state": "NY"}).count()

Zapytanie, dokładając drugi klucz:                           db.zips.find({"state": "NY", "city": "ALBANY"})

Zapytanie + wydrukowanie rozwiązania w bardziej czytelny sposób: db.zips.find({"state": "NY", "city": "ALBANY"}).pretty()

#IMPORTOWANIE PLIKU/OBIEKTU

mongoimport --uri="mongodb+srv://<username>:<password>@<cluster>.mongodb.net/sample_supplies" sales.json    #wraca duplicatekey error, ponieważ taki dokument już istnieje
mongo "mongodb+srv://<username>:<password>@<cluster>.mongodb.net/admin"
use sample_training
db.inspections.findOne();
db.inspections.insert({
      "_id" : ObjectId("56d61033a378eccde8a8354f"),
      "id" : "10021-2015-ENFO",
      "certificate_number" : 9278806,
      "business_name" : "ATLIXCO DELI GROCERY INC.",
      "date" : "Feb 20 2015",
      "result" : "No Violation Issued",
      "sector" : "Cigarette Retail Dealer - 127",
      "address" : {
              "city" : "RIDGEWOOD",
              "zip" : 11385,
              "street" : "MENAHAN ST",
              "number" : 1712
         }
  })

db.inspections.insert({
      "id" : "10021-2015-ENFO",
      "certificate_number" : 9278806,
      "business_name" : "ATLIXCO DELI GROCERY INC.",
      "date" : "Feb 20 2015",
      "result" : "No Violation Issued",
      "sector" : "Cigarette Retail Dealer - 127",
      "address" : {
              "city" : "RIDGEWOOD",
              "zip" : 11385,
              "street" : "MENAHAN ST",
              "number" : 1712
         }
  })

db.inspections.find({"id" : "10021-2015-ENFO", "certificate_number" : 9278806}).pretty()

Przy importowaniu dokumentów do bazy, najważniejsze jest pole _id. Domyślnie, każdy importowany/stworzony dokument otrzymuje _id jako Object (hash, który jest niepowtarzalnym numerem identyfikującym dany plik).

#IMPORTOWANIE DOKUMENTÓW:
db.inspections.insert([ { "test": 1 }, { "test": 2 }, { "test": 3 } ])
db.inspections.insert([{ "_id": 1, "test": 1 },{ "_id": 1, "test": 2 },
                       { "_id": 3, "test": 3 }])
Jeżeli dokumenty zawierają pole "_id", które może się powtórzyć, można zastosować:
db.inspections.insert([{ "_id": 1, "test": 1 },{ "_id": 1, "test": 2 },
                       { "_id": 3, "test": 3 }],{ "ordered": false })
Ponieważ domyślnie dokumenty dodawane są w zadanej w liście kolejności (doc1,doc2...). "Ordered": false sprawia, że nie są dodawane po kolei, dzieki czemu tylko dokumenty o powielonym "_id" nie zostaną dodane.

Kolejną ważną rzeczą jest poprawność nazw baz danych oraz kolekcji. W sytuacji, w której któraś z nazw zostanie wpisana błędnie, zostanie utworzona nowa baza/kolekcja o wpisanej przez nas nazwie.

#UPDATE DOKUMENTÓW:
One:                                                                            Many:
updateOne()                                                                     updateMany()

#operacje update'owania:
{"$inc": {"field": <increment value>, "field2": <increment value>}} => zwiększa podaną wartość o...

{"$set": {"field": <new value>, "field2": <new value>}} => zmienia wartość na podaną

{"$push": {"field": <value>, "field2": <value>}} => dodaje parę klucz:wartość do dokumentu

#USUWANIE DOKUMENTÓW:

One:                                                                            Many:
deleteOne(), warto dodać np. ("_id": 11), aby usunąć konkretny dokument         deleteMany()

db.<collection>.drop() -> usunięcie danej kolekcji w bazie danych


#OPERATORY ZAPYTAŃ
#porównanie:
$eq -> equal to
$ne -> not equal to

$gt -> greater than
$lt -> less than

$gte -> greater than or equal to
$lte -> less than equal to

#Syntax:
{ <field>: { <operator>: <value> } }

#logiczne:
$and
$or
$nor
$not

#Syntax:
In Atlas:
    and,or,nor:
    {<operator>: [{statement1}, {statement2}]}

In MongoDB shell:
    przykład: db.<collection>.find({ "$and": [ { "$or" :[ { "dst_airport": "KZN" }, { "src_airport": "KZN" }]},
                                          { "$or" :[ { "airplane": "CR2" }, { "airplane": "A81" }]}]}).pretty()


------------------------------------------
#Zadanie:
COPY
db.companies.find({ "$and": [{ "$or": [ { "founded_year": 2004 }, { "founded_month": 10 } ] }, { "$or": [ { "category_code": "web" }, { "category_code": "social" }]}]}).count()

#ekspresyjne:
$expr -> pozwala wyszukiwać po kilku wytycznych i łączyć je ze sobą, jak poniżej: { "$eq": [ "$end station id", "$start station id" ]}

#syntax:
Aggregation syntax: { <operator>: { <field>: <value> } }
MQL syntax: { <field>: { <operator>: <value> } }

Przykład:
db.trips.find({ "$expr": { "$and": [ { "$gt": [ "$tripduration", 1200 ]},{ "$eq": [ "$end station id", "$start station id" ]}]}}).count()

-----------------------------------------
#Zadanie:
How many companies in the sample_training.companies collection have the same permalink as their twitter_username?

db.companies.find( { $expr:  { $eq: ["$permalink", "$twitter_username"] } } ).count()