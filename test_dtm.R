require(tmcn)
require(tm)

apple <- readLines("./database/apple_final.txt")
liberty <- readLines("./database/liberty_final.txt")
chinatimes <- readLines("./database/chinatimes_final.txt")
newtalk <- readLines("./database/newtalk_final.txt")
people <- readLines("./database/people_final.txt")
storm <- readLines("./database/storm_final.txt")
pre <- readLines("cut_finish")

all <- c(apple,liberty,chinatimes,newtalk,people,storm,pre)

vs <- VectorSource(all)
txt_cor <- Corpus(vs)
ma.corpus <- tm_map(txt_cor,removeWords,stopwordsCN())
dtm <- DocumentTermMatrix(ma.corpus)

freq.terms <- findFreqTerms(dtm, lowfreq = 100)
length(freq.terms)
# inspect(dtm[1:1000,freq.terms])
see <- inspect(dtm[1:length(all),freq.terms])
write.table(see, file = "out_matrix.txt", sep = " ",row.names = FALSE)
print("Document Term Matrix output successfully!")

print(length(apple))
print(length(liberty))
print(length(chinatimes))
print(length(newtalk))
print(length(people))
print(length(storm))
print(length(pre))

