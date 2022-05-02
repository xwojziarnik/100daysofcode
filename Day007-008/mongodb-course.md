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

#Przykład:
db.trips.find({ "$expr": { "$and": [ { "$gt": [ "$tripduration", 1200 ]},{ "$eq": [ "$end station id", "$start station id" ]}]}}).count()

-----------------------------------------
#Exercise:
How many companies in the sample_training.companies collection have the same permalink as their twitter_username?

db.companies.find( { $expr:  { $eq: ["$permalink", "$twitter_username"] } } ).count()

#Array Field:

    $push	-> allows us to add an element to an array,
            -> Turns a field into an array field if it was previously a different type
    $all	-> using this operator you can query the documents, where are an array lists to look for some elements from array lists without carring about order of that array list.  
	        Example: {„amenities”: { $all: [ „Shampoo” ] } }

You can also modify upper query, using {$size: value}, like this:
{„amenities”: {$size: 20, $all: [ „Shampoo” ] } }

Let’s find out, if we can query the collection „listingsAndReviews” from „sample_airbnb” database below query:
 db.listingsAndReviews.find( { „amenities”: { „$size”: 20, „$all”: [ „Shampoo” ] } } ).pretty()
Summary:
{ < array field >: { „$size”: < number > } }	-> returns a cursor with all documents where the specified array field is exactly the given length

{ < array field >: { „$all”: < number > } }		-> returns a cursor with all documents in which the specified array field contains all given elements regardless of theif order in the array

#Querying an array field using 
an array					 -> returns only exact array matches
a single document				 -> returns all documents where the specified array field contains this given document
 
#Exercise:
More than 6 people
Has exactly 50 revievs
Db.listingsAndReviews.find({„reviews”: {„size”: 50}, „accommodates”: {„$gt”: 6}}).pretty()

#Exercise2:
Using the sample_airbnb.listingsAndReviews collection find out how many documents have the property type „House” and include „Changing table” as one of the „amenities”?
Db.listingsAndReviews.find( { „property_type”: „House”, „amenities”: „Changing table” } ).count()
Result: 11 -> correct

#Array Operators and Projections:

With projection field you can tell MongoDB, which parts of document you want to see. Like below:
Db.< collection >.find( { < query > }, { < projection > } )
1 – include the field,
0 – exclude the field
#Example:
Db.listingsAndReviews.find( { „amenities”: { „$size”: 20, „$all”: [ „Internet”, „Shampoo” ] } }, { „price”: 1, „adress”: 1 } ).pretty()

The only time, when you can mix ones and zeros is when you query to exclude (with 0) the „_id” field. Otherwise you’ll get an error. 
Db.< collection >.find( { <query> }, { <field1>: 1, „_id”: 0 } )

#$elemMatch:
Matches documents that contain an array field with at least one element that matches the specified query criteria.
{ <field>: { „$elemMatch”: { <field>: <value> } } }
Or
Projects only the array elements with at least one element that matches the specified criteria.
Example: db.grades.find({„scores”: {„$elemMatch”: {„type”: „extra credit”}}})
 
#Exercise:
How many companies in the sample_training.companies collection have offices in the city of Seattle?
Db.companies.find( { „offices”: { „$elemMatch”: { „city”: „Seattle” } } } ).count()

#Dot-notation

MQL uses dot-notation to specify the adress of nested elements in a document.
To use dot-notation in arrays specify the position of the element in the array.
Example: db.< collection >.find( { „field1.other field.also a field”: „value” } ), like below:

Db.companies.find( { „relationships”: { „$elemMatch”: { „is_past”: true, „person.first_name”: „Mark” } } }, { „name”: 1 } ).count()
 
#Exercise:
How many trips in the sample_training.trips collection started at stations that are to the west of the ~74 longtitude coordinate?
< field_name >: [ <longtitude>, <latitude> ]

Db.trips.find( { „start station location.coordinates.0”: { „$lt”: ~74 } } ).count()

#Exercise2:
How many inspections from the sample_training.inspections collection were conducted in the city of NEW YORK?
Db.inspections.find( { „address.city”: „NEW YORK” } ).count()

#Aggregation framework:

In its simpliest form, another way to query data in MongoDB.
#Syntax:
#Example:
Find all documents that have wi-fi as one of the amenities only includes price and address in the resulting cursor.
MQL: db.listingAndReviews.find( { „amenities”: „Wifi” }, { „price”: 1, „address”: 1, „_id”: 0 } ).pretty()
Aggregation framework:
db.listingsAndReviews.aggregate( [ { „$match”: { „amenities”: „Wifi” } }, { „$project”: { „price”: 1, „address”: 1, „_id”: 0 } } ] ).pretty()

In Aggregation framework order matters. It works like a pipeline to action through your documents.
#Why Aggregation?
MQL:
	Filter
	Update
MongoDB Aggregation Framework:
    $group ->	an operator that makes the incoming stream of data, and siphons it into multiple distinct reservoirs
	Syntax: { „$group”: { „_id”: <expression>, //Group By Expression
    <field1>: { <accumulator1>: <expression1> }, … } }
	Compute (obliczać)
	Reshape

#example:
	Which countries are listed in the sample_airbnb.listingsAndReviews collection?
	Db.listingsAndReviews.aggregate( [ { „$project”: { „address”: 1, „_id”: 0 } }, { „$group”: {
    „_id”: „address.country” } } ] )
	Db.listingsAndReviews.aggregate( [ { „$project”: { „address”: 1, „_id”: 0 } }, { „$group”: {
    „_id”: „address.country”, „$count”: { „$sum”: 1 } } } ] )
 
#Exercise:
What room types are present in the sample_airbnb.listingsAndReviews collection?
Db.listingsAndReviews.aggregate( [ { „$project”: { „room type”: 1, „_id”: 0 } }, { „$group”: { „_id”: „room_type” } } ] )

#Cursor methods:

Find():
Db.zips.find().sort( { „pop”: 1, „city”: -1 } )
		Increasing /		\Decreasing
		„pop”: 0-> ∞		„city”: „Z”->”A”

Limit():
Db.zips.find().sort().limit() -> it’s necessary to use sort before limit.
 
#Exercise:
In what year was the youngest bike rider from the sample_training.trips collection born?
Db.trips.find( { „birth year”: { „$ne”: 0 } }, { „birth year”: 1 } ).sort( { „birth year”: -1 } ).limit(1)

#Indexes:

In a database: special data structure that stores a small portion of the collection’s data set in an easy to traverse form.

When to index?:
Support your queries:
Db.trips.createIndex( { „birth year”: 1 } ) -> waaaay much faster than:
Db.trips.find( { „start station id”: 476 } ).sort( „birth year”: 1 )

#Data Modeling:

It’s a way to organize fields in a document to support your application performance and querying capabilities.
Rule:
Data is stored in the way that it is used.
Upsert:

Everything in MQL that is used to locate a document in a collection can also be used to modify this document.
Db.collection.updateOne( { <query to locate> }, { <update> } )

Upsert is a hybrid of update and insert, it should only be used when it is needed.
Db.collection.updateOne( { <query1> }, { <update> }, { „upsert”: true } )

Upsert: true:
	Conditional updates
Upsert: false (default):
	Update an existing document,
	Insert a brand new document