library(tabulizer)

f <- "gpf/GPF-Reading-Final.pdf"
coordinates <- c("top", "left", "bottom", "right")

# 🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛🚛
# Page 112 🚀
# Table 23: Grade 2, Example 1—Information (Description): Van
# Table 24: Grade 2, Example 2—Information (Description): Maya
# Table 25: Grade 2, Example 3—Information: The Pippi
page <- rep(112,3)
table <- seq(23,25)
part <- rep("a",3)
areas <- list(c(90.83774, 44.96604, 185.52453, 742.41509),
               c(224.7849,  42.6566, 329.8642, 738.9509),
               c(379.5170,  42.6566, 489.2151, 738.9509))
legendTable <- seq(23, 25)
legendGrade <- c(2,2,2)
legendExample <- seq(1,3)
legendType <- c("Information (Description)",
                "Information (Description)",
                "Information")
legendTitle <- c("Van","Maya","The Pippi")

# Page 113 🚀
# Table 26: Grade 3, Example 1—Story: The Mango
# Table 27: Grade 3, Example 2—Story: Tadala’s Deed
#   continues 1 item next page (114)
page <- c(page, c(113, 113))
table <- c(table, c(26,27))
part <- c(part, rep("a",2))
areas <- append(areas, list(c(89.68302,  43.81132, 346.03019, 744.72453)))
areas <- append(areas, list(c(381.82642,  44.96604, 561.96226, 742.41509)))

legendTable <- c(legendTable, seq(26, 27))
legendGrade <- c(legendGrade, c(3,3))
legendExample <- c(legendExample, seq(1,2))
legendType <- c(legendType, c("Story", "Story"))
legendTitle <- c(legendTitle, c("The Mango","Tadala's Deed"))


# Page 114
# Table 28: Grade 3, Example 3—Story: The Fox and the Grapes
page <- c(page, c(114, 114))
table <- c(table, c(27,28))
part <- c(part, c("b", "a"))
areas <- append(areas, list(c(51.57736,  43.81132, 126.63396, 736.64151)))
areas <- append(areas, list(c(165.89434,  46.12075, 424.55094, 743.56981)))

legendTable <- c(legendTable, seq(28, 28))
legendGrade <- c(legendGrade, c(3))
legendExample <- c(legendExample, seq(3,3))
legendType <- c(legendType, c("Story"))
legendTitle <- c(legendTitle, c("The Fox and the Grapes"))

# Page 115
# Table 29: Grade 3, Example 4—Information (Description): Grass
# Table 30: Grade 3, Example 5—Information (Description): Aliyah
#   continues 2 items next page (116)
page <- c(page, c(115, 115))
table <- c(table, c(29,30))
part <- c(part, c("a", "a"))
areas <- append(areas, list(c(71.20755,  44.96604, 337.94717, 744.72453)))
areas <- append(areas, list(c(377.20755,  43.81132, 540.02264, 745.87925)))

legendTable <- c(legendTable, seq(29, 30))
legendGrade <- c(legendGrade, c(3, 3))
legendExample <- c(legendExample, seq(4,5))
legendType <- c(legendType, c("Information (Description)",
                              "Information (Description)"))
legendTitle <- c(legendTitle, c("Grass","Aliyah"))


# Page 116
# Table 31: Grade 4, Example 1—Story: The Accident
page <- c(page, c(116, 116))
table <- c(table, c(30,31))
part <- c(part, c("b", "a"))
areas <- append(areas, list(c(51.57736,  46.12075, 135.87170, 745.87925)))
areas <- append(areas, list(c(191.29811,  44.96604, 513.46415, 745.87925)))

legendTable <- c(legendTable, seq(31, 31))
legendGrade <- c(legendGrade, c(4))
legendExample <- c(legendExample, seq(1,1))
legendType <- c(legendType, c("Story"))
legendTitle <- c(legendTitle, c("The Accident"))

# Page 117
# Table 32: Grade 4, Example 2—Story: Noga the Small Girl
page <- c(page, 117)
table <- c(table, 32)
part <- c(part, "a")
areas <- append(areas, list(c(70.05283,  44.96604, 541.17736, 745.87925)))

legendTable <- c(legendTable, seq(32, 32))
legendGrade <- c(legendGrade, c(4))
legendExample <- c(legendExample, seq(2,2))
legendType <- c(legendType, c("Story"))
legendTitle <- c(legendTitle, c("Noga the Small Girl"))

# Page 118
# Table 33: Grade 4, Example 3—Information: The Dwarf Lantern Shark
#   continues 1 item on next page (119)
page <- c(page, 118)
table <- c(table, 33)
part <- c(part, "a")
areas <- append(areas, list(c(70.05283,  44.96604, 503.07170, 747.03396)))

legendTable <- c(legendTable, seq(33, 33))
legendGrade <- c(legendGrade, c(4))
legendExample <- c(legendExample, seq(3,3))
legendType <- c(legendType, c("Information"))
legendTitle <- c(legendTitle, c("The Dwarf Lantern Shark"))

# 119
# Table 34: Grade 4, Example 4—Information: Animals in Nature
page <- c(page, c(119, 119))
table <- c(table, c(33, 34))
part <- c(part, c("b", "a"))
areas <- append(areas, list(c(49.26792,  43.81132, 152.03774, 733.17736)))
areas <- append(areas, list(c(188.98868,  44.96604, 526.16604, 747.03396)))

legendTable <- c(legendTable, seq(34, 34))
legendGrade <- c(legendGrade, c(4))
legendExample <- c(legendExample, seq(4,4))
legendType <- c(legendType, c("Information"))
legendTitle <- c(legendTitle, c("Animals in Nature"))

# 120
# Table 35: Grade 5, Example 1—Information: The Giant Coconut Crab
page <- c(page, 120)
table <- c(table, 35)
part <- c(part, "a")
areas <- append(areas, list(c(89.68302,  44.96604, 367.96981, 743.56981)))

legendTable <- c(legendTable, c(35))
legendGrade <- c(legendGrade, c(5))
legendExample <- c(legendExample, c(1))
legendType <- c(legendType, c("Information"))
legendTitle <- c(legendTitle, c("The Giant Coconut Crab"))

# 121
# Table 36: Grade 5, Example 2—Information: Salt
page <- c(page, 121)
table <- c(table, 36)
part <- c(part, "a")
areas <- append(areas, list(c(70.05283,  43.81132, 494.98868, 745.87925)))

legendTable <- c(legendTable, c(36))
legendGrade <- c(legendGrade, c(5))
legendExample <- c(legendExample, c(2))
legendType <- c(legendType, c("Information"))
legendTitle <- c(legendTitle, c("Salt"))

# 122
# Table 37: Grade 5, Example 3—Story: Chiumbo and the Goats
page <- c(page, 122)
table <- c(table, 37)
part <- c(part, "a")
areas <- append(areas, list(c(70.05283,  43.81132, 462.65660, 745.87925)))

legendTable <- c(legendTable, c(37))
legendGrade <- c(legendGrade, c(5))
legendExample <- c(legendExample, c(3))
legendType <- c(legendType, c("Story"))
legendTitle <- c(legendTitle, c("Chiumbo and the Goats"))

# 123
# Table 38: Grade 5, Example 4—Procedural: Orange and Cardamom Fruit Salad
page <- c(page, 123)
table <- c(table, 38)
part <- c(part, "a")
areas <- append(areas, list(c(71.20755,  44.96604, 396.83774, 741.26038)))

legendTable <- c(legendTable, c(38))
legendGrade <- c(legendGrade, c(5))
legendExample <- c(legendExample, c(4))
legendType <- c(legendType, c("Procedural"))
legendTitle <- c(legendTitle, c("Orange and Cardamom Fruit Salad"))

# 124 - 127
# Table 39: Example 1—Information: Sevan Trout
page <- c(page, seq(124,127))
table <- c(table, rep(39,4))
part <- c(part, letters[1:4])
areas <- append(areas, list(c(90.83774,  44.96604, 536.55849, 745.87925)))
areas <- append(areas, list(c(49.26792,  44.96604, 463.81132, 744.72453)))
areas <- append(areas, list(c(49.26792,  44.96604, 505.38113, 744.72453)))
areas <- append(areas, list(c(50.42264,  44.96604, 190.14340, 740.10566)))

legendTable <- c(legendTable, c(39))
legendGrade <- c(legendGrade, c(6))
legendExample <- c(legendExample, c(1))
legendType <- c(legendType, c("Information"))
legendTitle <- c(legendTitle, c("Sevan Trout"))


# 128 - 131
# Table 40: Grade 6, Example 2—Story: The Old House
page <- c(page, seq(128,131))
table <- c(table, rep(40,4))
part <- c(part, letters[1:4])
areas <- append(areas, list(c(71.20755,  44.96604, 510.00000, 745.87925)))
areas <- append(areas, list(c(50.42264,  44.96604, 545.79623, 744.72453)))
areas <- append(areas, list(c(49.26792,  44.96604, 520.39245, 747.03396)))
areas <- append(areas, list(c(49.26792,  44.96604, 475.35849, 745.87925)))

legendTable <- c(legendTable, c(40))
legendGrade <- c(legendGrade, c(6))
legendExample <- c(legendExample, c(2))
legendType <- c(legendType, c("Story"))
legendTitle <- c(legendTitle, c("The Old House"))


# 132 - 133
# Table 41: Grade 6, Example 3—Information (Non-continuous): Seb’s Delivery Schedule
page <- c(page, c(132,133))
table <- c(table, rep(41,2))
part <- c(part, letters[1:2])
areas <- append(areas, list(c(68.89811,  46.12075, 518.08302, 747.03396)))
areas <- append(areas, list(c(49.26792,  43.81132, 329.86415, 745.87925)))

legendTable <- c(legendTable, c(41))
legendGrade <- c(legendGrade, c(6))
legendExample <- c(legendExample, c(3))
legendType <- c(legendType, c("Information (Non-continuous)"))
legendTitle <- c(legendTitle, c("Seb’s Delivery Schedule"))

# 134 - 135
# Table 42: Grade 7, Example 1—Story: The Hole
page <- c(page, c(134,135))
table <- c(table, rep(42,2))
part <- c(part, letters[1:2])
areas <- append(areas, list(c(90.83774,  44.96604, 525.01132, 745.87925)))
areas <- append(areas, list(c(49.26792,  44.96604, 541.17736, 747.03396)))

legendTable <- c(legendTable, c(42))
legendGrade <- c(legendGrade, c(7))
legendExample <- c(legendExample, c(1))
legendType <- c(legendType, c("Story"))
legendTitle <- c(legendTitle, c("The Hole"))

# 136, 137, first 2 items 138
# Table 43: Grade 7, Example 2—Information: How Shells Climb Mountains
page <- c(page, c(136,137,138))
table <- c(table, rep(43,3))
part <- c(part, letters[1:3])
areas <- append(areas, list(c(70.05283,  43.81132, 540.02264, 745.87925)))
areas <- append(areas, list(c(49.26792,  44.96604, 548.10566, 744.72453)))
areas <- append(areas, list(c(51.57736,  44.96604, 259.42642, 744.72453)))

legendTable <- c(legendTable, c(43))
legendGrade <- c(legendGrade, c(7))
legendExample <- c(legendExample, c(2))
legendType <- c(legendType, c("Information"))
legendTitle <- c(legendTitle, c("How Shells Climb Mountains"))

# 138, first 3 items 139
# Table 44: Grade 7, Example 3—Persuasive: Dear Uncle and Aunty
page <- c(page, c(138,139))
table <- c(table, rep(44,2))
part <- c(part, letters[1:2])
areas <- append(areas, list(c(298.68679,  43.81132, 527.32075, 747.03396)))
areas <- append(areas, list(c(48.11321,  44.96604, 277.90189, 747.03396)))

legendTable <- c(legendTable, c(44))
legendGrade <- c(legendGrade, c(7))
legendExample <- c(legendExample, c(3))
legendType <- c(legendType, c("Persuasive"))
legendTitle <- c(legendTitle, c("Dear Uncle and Aunty"))


# 139 - 141
# Table 45: Grade 8, Example 1—Information: Brushing Your Teeth
page <- c(page, seq(139,141))
table <- c(table, rep(45,3))
part <- c(part, letters[1:3])
areas <- append(areas, list(c(334.48302,  43.81132, 491.52453, 745.87925)))
areas <- append(areas, list(c(44.64906,  43.81132, 563.11698, 745.87925)))
areas <- append(areas, list(c(50.42264,  44.96604, 363.35094, 745.87925)))

legendTable <- c(legendTable, c(45))
legendGrade <- c(legendGrade, c(8))
legendExample <- c(legendExample, c(1))
legendType <- c(legendType, c("Information"))
legendTitle <- c(legendTitle, c("Brushing Your Teeth"))


# 142 - first 3 items 143
# Table 46: Grade 8, Example 2—Information (Non-continuous Text—Table): Country Fact File
page <- c(page, seq(142,143))
table <- c(table, rep(46,2))
part <- c(part, letters[1:2])
areas <- append(areas, list(c(71.20755,  44.96604, 493.83396, 745.87925)))
areas <- append(areas, list(c(50.42264,  43.81132, 365.66038, 745.87925)))

legendTable <- c(legendTable, c(46))
legendGrade <- c(legendGrade, c(8))
legendExample <- c(legendExample, c(2))
legendType <- c(legendType, c("Information (Non-continuous Text—Table)"))
legendTitle <- c(legendTitle, c("Country Fact File"))

# 143 - 145
# Table 47: Grade 8, Example 3—Story: Lazy Rabbit
page <- c(page, seq(143,145))
table <- c(table, rep(47,3))
part <- c(part, letters[1:3])
areas <- append(areas, list(c(407.23019,  43.81132, 553.87925, 745.87925)))
areas <- append(areas, list(c(51.57736,  44.96604, 446.49057, 745.87925)))
areas <- append(areas, list(c(51.57736,  43.81132, 333.32830, 747.03396)))

legendTable <- c(legendTable, c(47))
legendGrade <- c(legendGrade, c(8))
legendExample <- c(legendExample, c(3))
legendType <- c(legendType, c("Story"))
legendTitle <- c(legendTitle, c("Lazy Rabbit"))

# 146 - 147
# Table 48: Grade 9, Example—Information (Non-continuous Text—Labeled Diagrams): Balloon
page <- c(page, seq(146,147))
table <- c(table, rep(48,2))
part <- c(part, letters[1:2])
areas <- append(areas, list(c(90.83774,  44.96604, 486.90566, 745.87925)))
areas <- append(areas, list(c(48.11321,  46.12075, 555.03396, 744.72453)))

legendTable <- c(legendTable, c(48))
legendGrade <- c(legendGrade, c(9))
legendExample <- c(legendExample, c(1))
legendType <- c(legendType, c("Information (Non-continuous Text—Labeled Diagrams)"))
legendTitle <- c(legendTitle, c("Balloon"))

# 148 - 149
# Table 49: Grade 9, Example 2—Story: Miser
page <- c(page, seq(148,149))
table <- c(table, rep(49,2))
part <- c(part, letters[1:2])
areas <- append(areas, list(c(72.22599,  44.93054, 529.78531, 742.45771)))
areas <- append(areas, list(c(50.32768,  46.08347, 441.03955, 745.91653)))

legendTable <- c(legendTable, c(49))
legendGrade <- c(legendGrade, c(9))
legendExample <- c(legendExample, c(2))
legendType <- c(legendType, c("Story"))
legendTitle <- c(legendTitle, c("Miser"))

# 150 - 151
# Table 50: Grade 9, Example 3—Information (Mixed Continuous and Non-continuous): First Car
page <- c(page, seq(150,151))
table <- c(table, rep(50,2))
part <- c(part, letters[1:2])
areas <- append(areas, list(c(68.76836,  43.77760, 475.61582, 745.91653)))
areas <- append(areas, list(c(51.48023,  44.93054, 460.63277, 747.06946)))

legendTable <- c(legendTable, c(50))
legendGrade <- c(legendGrade, c(9))
legendExample <- c(legendExample, c(3))
legendType <- c(legendType, c("Information (Mixed Continuous and Non-continuous)"))
legendTitle <- c(legendTitle, c("First Car"))

# 152 - 153
# Table 51: Grade 9, Example 4—Persuasive: Clever or Hardworking?
page <- c(page, seq(152,153))
table <- c(table, rep(51,2))
part <- c(part, letters[1:2])
areas <- append(areas, list(c(68.76836,  46.08347, 540.15819, 747.06946)))
areas <- append(areas, list(c(48.02260,  44.93054, 406.46328, 745.91653)))  

legendTable <- c(legendTable, c(51))
legendGrade <- c(legendGrade, c(9))
legendExample <- c(legendExample, c(4))
legendType <- c(legendType, c("Persuasive"))
legendTitle <- c(legendTitle, c("Clever or Hardworking?"))

# as <- locate_areas(f, pages=152)
# as <- locate_areas(f, pages=153)

TOC <- data.frame(table=legendTable, grade=legendGrade,
                  example=legendExample, type=legendType,
                  title=legendTitle)

write.csv(TOC, "gpf/csv/toc.csv", row.names=FALSE)
# 🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧
# 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
# Extract each table/table-part and write CSV to gpf/csv/
# Remember to write as csv data.frame with table-to-info table
n.files <- length(page)
for (i in 1:n.files) {
  av <- setNames(areas[[i]], coordinates)
  a <- list(av)
  file.out <- paste("gpf/csv/table-", 
                    as.character(table[i]), "-",part[i],".csv", sep = "")
  df <- extract_tables(f, pages = page[i], area = a, guess = FALSE,
                       method = "lattice", output = "data.frame")
  write.csv(df, file = file.out, row.names = FALSE)
}


# 🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧
# PROBLEM TABLES

# Table 39 Part b
#   page 125
# 
# Strategy
#   - extract each column separately
#   - combine into single frame with appropriate names
#   - write to csv
# as <- locate_areas(f, pages=125)
areas <- list(c(46.08889,  44.66667, 465.42222,  99.06667),
              c(46.08889, 104.73333, 459.75556, 253.20000),
              c(48.35556, 257.73333, 462.02222, 355.20000),
              c(48.35556, 359.73333, 462.02222, 746.20000))

av <- setNames(areas[[1]], coordinates); a <- list(av)
c1 <- extract_tables(f, pages = 125, area = a, guess = FALSE,
                     method = "lattice", output = "data.frame")
c1 <- c1[[1]]

av <- setNames(areas[[2]], coordinates); a <- list(av)
c2 <- extract_tables(f, pages = 125, area = a, guess = FALSE,
                     method = "lattice", output = "data.frame")
c2 <- c2[[1]]; View(c2)
c2 <- c(c2[1,1],
        paste(c2[2:6,1], collapse=" "),
        paste(c2[7:16,1], collapse=" "),
        paste(c2[17:26,1], collapse=" "),
        paste(c2[27:33,1], collapse=" "))

av <- setNames(areas[[3]], coordinates); a <- list(av)
c3 <- extract_tables(f, pages = 125, area = a, guess = FALSE,
                     method = "lattice", output = "data.frame")
c3 <- c3[[1]]; View(c3)
c3 <- c(c3[1,1],
        paste(c3[2:5,1], collapse=" "),
        paste(c3[6:15,1], collapse=" "),
        paste(c3[16:18,1], collapse=" "),
        paste(c3[19:20,1], collapse=" "))

av <- setNames(areas[[4]], coordinates); a <- list(av)
c4 <- extract_tables(f, pages = 125, area = a, guess = FALSE,
                     method = "lattice", output = "data.frame")
c4 <- c4[[1]]; View(c4)
c4 <- c(paste(c4[1:3,1], collapse=" "),
        paste(c4[4:13,1], collapse=" "),
        paste(c4[14:18,1], collapse=" "),
        paste(c4[19:22,1], collapse=" "),
        paste(c4[23:29,1], collapse=" "))

fdf <- data.frame("Ref.." = c1,
                  "Items" = c2,
                  "Acceptable.Key.s" = c3,
                  "Notes" = c4)
file.out <- "gpf/csv/table-39-b.csv"
write.csv(fdf, file = file.out, row.names = FALSE)

# Table 39 Part c
# Page 126
# c(TOP,       LEFT,     BOTTOM,    RIGHT)
# c(49.26792,  44.96604, 505.38113, 744.72453)
# as <- locate_areas(f, pages=126)
areas <- list(c(49.26792,  44.66667, 505.38113,  99.06667),
              c(49.26792, 104.73333, 505.38113, 253.20000),
              c(49.26792, 257.73333, 505.38113, 355.20000),
              c(49.26792, 359.73333, 505.38113, 746.20000))

av <- setNames(areas[[1]], coordinates); a <- list(av)
c1 <- extract_tables(f, pages = 126, area = a, guess = FALSE,
                     method = "lattice", output = "data.frame")
c1 <- c1[[1]]; View(c1)


av <- setNames(areas[[2]], coordinates); a <- list(av)
c2 <- extract_tables(f, pages = 126, area = a, guess = FALSE,
                     method = "lattice", output = "data.frame")
c2 <- c2[[1]]; View(c2)
c2 <- c(paste(c2[1:9,1], collapse=" "),
        paste(c2[10:14,1], collapse=" "),
        paste(c2[15:28,1], collapse=" "),
        paste(c2[29:31,1], collapse=" "))


av <- setNames(areas[[3]], coordinates); a <- list(av)
c3 <- extract_tables(f, pages = 126, area = a, guess = FALSE,
                     method = "lattice", output = "data.frame")
c3 <- c3[[1]]; View(c3)
c3 <- c(paste(c3[1:3,1], collapse=" "),
        paste(c3[4,1], collapse=" "),
        paste(c3[5:18,1], collapse=" "),
        paste(c3[19:22,1], collapse=" "))


av <- setNames(areas[[4]], coordinates); a <- list(av)
c4 <- extract_tables(f, pages = 126, area = a, guess = FALSE,
                     method = "lattice", output = "data.frame")
c4 <- c4[[1]]; View(c4)
c4 <- c(paste(c4[1:3,1], collapse=" "),
        paste(c4[4:9,1], collapse=" "),
        paste(c4[10:12,1], collapse=" "),
        paste(c4[13:19,1], collapse=" "))

fdf <- data.frame("Ref.." = c1,
                  "Items" = c2,
                  "Acceptable.Key.s" = c3,
                  "Notes" = c4)
file.out <- "gpf/csv/table-39-c.csv"
write.csv(fdf, file = file.out, row.names = FALSE)


# Table 40 a to d ---------------------------------------------
pages <- data.frame(page = seq(128,131),
                    letter = letters[1:4])
print(pages)

areas <- list(c(71.20755,  44.96604, 510.00000, 745.87925),
              c(50.42264,  44.96604, 545.79623, 744.72453),
              c(49.26792,  44.96604, 520.39245, 747.03396),
              c(49.26792,  44.96604, 475.35849, 745.87925))

# 40-a
av <- setNames(areas[[1]], coordinates); a <- list(av)
tf <- extract_tables(f, pages = pages[1,1], area = a, guess = FALSE,
                     method = "lattice", output = "data.frame")
tf <- tf[[1]]
View(tf)

c1 <- tf[,1]
c2 <- tf[,2]
c3 <- tf[,3]
c4 <- tf[,4]

c1 <- c1[c1!=""]

c2 <- c(paste(c2[1], collapse = " "),
        paste(c2[4:5], collapse = " "),
        paste(c2[8], collapse = " "),
        paste(c2[11:16], collapse = " "),
        paste(c2[17:18], collapse = " "),
        paste(c2[23:26], collapse = " "),
        paste(c2[29:31], collapse = " "),
        paste(c2[33:39], collapse = " "))

c3<- c(paste(c3[1], collapse = " "),
       paste(c3[4:6], collapse = " "),
       paste(c3[8:10], collapse = " "),
       paste(c3[11:12], collapse = " "),
       paste(c3[17:19], collapse = " "),
       paste(c3[23:27], collapse = " "),
       paste(c3[29:30], collapse = " "),
       paste(c3[33], collapse = " "))

c4<- c(paste(c4[1:3], collapse = " "),
       paste(c4[4:7], collapse = " "),
       paste(c4[8:10], collapse = " "),
       paste(c4[11:14], collapse = " "),
       paste(c4[17:22], collapse = " "),
       paste(c4[23:28], collapse = " "),
       paste(c4[29:32], collapse = " "),
       paste(c4[33:39], collapse = " "))

fdf <- data.frame("Ref.." = c1,
                  "Items" = c2,
                  "Acceptable.Key.s" = c3,
                  "Notes" = c4)
file.out <- "gpf/csv/table-40-a.csv"
write.csv(fdf, file = file.out, row.names = FALSE)


# 40-b
whichTable <- "40"
whichPart <- 2
av <- setNames(areas[[whichPart]], coordinates); a <- list(av)
tf <- extract_tables(f, pages = pages[whichPart,1], area = a, guess = FALSE,
                     method = "lattice", output = "data.frame")
tf <- tf[[1]]
View(tf)

c1 <- tf[,1]
c2 <- tf[,2]
c3 <- tf[,3]
c4 <- tf[,4]

c1 <- c1[c1!=""]

c2 <- c(paste(c2[1:2], collapse = " "),
        paste(c2[6:11], collapse = " "),
        paste(c2[12:17], collapse = " "),
        paste(c2[18:19], collapse = " "),
        paste(c2[21:22], collapse = " "),
        paste(c2[24:25], collapse = " "),
        paste(c2[29:31], collapse = " "),
        paste(c2[33:34], collapse = " "),
        paste(c2[38:38], collapse = " "))

c3<- c(paste(c3[1:3], collapse = " "),
       paste(c3[6:6], collapse = " "),
       paste(c3[12:16], collapse = " "),
       paste(c3[18:19], collapse = " "),
       paste(c3[21:23], collapse = " "),
       paste(c3[24:27], collapse = " "),
       paste(c3[29:31], collapse = " "),
       paste(c3[33:35], collapse = " "),
       paste(c3[38:38], collapse = " "))

c4<- c(paste(c4[1:5], collapse = " "),
       paste(c4[6:7], collapse = " "),
       paste(c4[12:12], collapse = " "),
       paste(c4[18:20], collapse = " "),
       paste(c4[21:22], collapse = " "),
       paste(c4[24:28], collapse = " "),
       paste(c4[29:32], collapse = " "),
       paste(c4[33:37], collapse = " "),
       paste(c4[38:39], collapse = " "))

fdf <- data.frame("Ref.." = c1,
                  "Items" = c2,
                  "Acceptable.Key.s" = c3,
                  "Notes" = c4)

file.out <- paste("gpf/csv/table-",
                  whichTable, "-", 
                  pages[whichPart,2], 
                  ".csv", sep = "")

write.csv(fdf, file = file.out, row.names = FALSE)


# 40-c
whichTable <- "40"
whichPart <- 3
av <- setNames(areas[[whichPart]], coordinates); a <- list(av)
tf <- extract_tables(f, pages = pages[whichPart,1], area = a, guess = FALSE,
                     method = "lattice", output = "data.frame")
tf <- tf[[1]]
View(tf)

c1 <- tf[,1]
c2 <- tf[,2]
c3 <- tf[,3]
c4 <- tf[,4]

c1 <- c1[c1!=""]

c2 <- c(paste(c2[1:3], collapse = " "),
        paste(c2[14:19], collapse = " "),
        paste(c2[20:24], collapse = " "),
        paste(c2[27:30], collapse = " "),
        paste(c2[32:36], collapse = " "),
        paste(c2[37:41], collapse = " "))

c3<- c(paste(c3[1:13], collapse = " "),
       paste(c3[14:15], collapse = " "),
       paste(c3[20:20], collapse = " "),
       paste(c3[27:31], collapse = " "),
       paste(c3[32:34], collapse = " "),
       paste(c3[37:39], collapse = " "))

c4<- c(paste(c4[1:5], collapse = " "),
       paste(c4[14:19], collapse = " "),
       paste(c4[20:26], collapse = " "),
       paste(c4[27:30], collapse = " "),
       paste(c4[32:34], collapse = " "),
       paste(c4[37:41], collapse = " "))

fdf <- data.frame("Ref.." = c1,
                  "Items" = c2,
                  "Acceptable.Key.s" = c3,
                  "Notes" = c4)

file.out <- paste("gpf/csv/table-",
                  whichTable, "-", 
                  pages[whichPart,2], 
                  ".csv", sep = "")

write.csv(fdf, file = file.out, row.names = FALSE)


# 40-d
whichTable <- "40"
whichPart <- 4
av <- setNames(areas[[whichPart]], coordinates); a <- list(av)
tf <- extract_tables(f, pages = pages[whichPart,1], area = a, guess = FALSE,
                     method = "lattice", output = "data.frame")
tf <- tf[[1]]
View(tf)

c1 <- tf[,1]
c2 <- tf[,2]
c3 <- tf[,3]
c4 <- tf[,4]

c1 <- c1[c1!=""]

c2 <- c(paste(c2[1:3], collapse = " "),
        paste(c2[8:11], collapse = " "),
        paste(c2[14:17], collapse = " "),
        paste(c2[19:23], collapse = " "),
        paste(c2[27:32], collapse = " "),
        paste(c2[33:37], collapse = " "))

c3<- c(paste(c3[1:7], collapse = " "),
       paste(c3[8:9], collapse = " "),
       paste(c3[14:18], collapse = " "),
       paste(c3[19:22], collapse = " "),
       paste(c3[27:28], collapse = " "),
       paste(c3[33:37], collapse = " "))

c4<- c(paste(c4[1:6], collapse = " "),
       paste(c4[8:13], collapse = " "),
       paste(c4[14:17], collapse = " "),
       paste(c4[19:26], collapse = " "),
       paste(c4[27:30], collapse = " "),
       paste(c4[33:36], collapse = " "))

fdf <- data.frame("Ref.." = c1,
                  "Items" = c2,
                  "Acceptable.Key.s" = c3,
                  "Notes" = c4)

file.out <- paste("gpf/csv/table-",
                  whichTable, "-", 
                  pages[whichPart,2], 
                  ".csv", sep = "")


write.csv(fdf, file = file.out, row.names = FALSE)


# 🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧
# # Table 42

# copy from Earll folder (manual copy to Excel/CSV)
# table-42-a.csv
# table-42-b.csv
# table-43-c.csv
# table-49-a.csv
# filestocopy <- c("table-42-a.csv",
#                  "table-42-b.csv",
#                  "table-43-c.csv",
#                  "table-49-a.csv")
# files.from <- paste("/mnt/c/Users/earll/", filestocopy, sep="")
# files.to <- paste("./gpf/csv/", filestocopy, sep="")
# file.copy(from=files.from, to=files.to, 
#           overwrite = TRUE, recursive = FALSE, 
#           copy.mode = TRUE)

# CURRENT 🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧
#   Created from manually copy-paste into Excel sheets
#   Transfer these to fab-data-try/project-2/gpf and push legion pull macbook

df <- read.csv("/mnt/c/Users/earll/table-42-a.csv")
names(df) <- c("Ref..","Items","Acceptable.Key.s","Notes")
write.csv(df, "./gpf/csv/table-42-a.csv", row.names = FALSE)

df <- read.csv("/mnt/c/Users/earll/table-42-b.csv")
names(df) <- c("Ref..","Items","Acceptable.Key.s","Notes")
write.csv(df, "./gpf/csv/table-42-b.csv", row.names = FALSE)

df <- read.csv("/mnt/c/Users/earll/table-43-c.csv")
names(df) <- c("Ref..","Items","Acceptable.Key.s","Notes")
write.csv(df, "./gpf/csv/table-43-c.csv", row.names = FALSE)

df <- read.csv("/mnt/c/Users/earll/table-49-a.csv")
names(df) <- c("Ref..","Items","Acceptable.Key.s","Notes")
write.csv(df, "./gpf/csv/table-49-a.csv", row.names = FALSE)
# pages <- data.frame(page = seq(134,135),
#                     letter = letters[1:2])
# print(pages)
# 
# areas <- list(c(90.83774,  44.96604, 525.01132, 745.87925),
#               c(49.26792,  44.96604, 541.17736, 747.03396))

# # 42-a (8 items)
# whichTable <- "42"
# whichPart <- 1
# 
# av <- setNames(areas[[whichPart]], coordinates); a <- list(av)
# tf <- extract_tables(f, pages = pages[whichPart,1], area = a, guess = FALSE,
#                      method = "lattice", output = "data.frame")
# tf <- tf[[1]]
# View(tf)
# 
# pat <- "[RDC][1-3]\\.[1-4]\\.\\d{1}\\_[PME]"
# c1 <- array()
# c2 <- array()
# for (i in 1 : nrow(tf)) {
#   ind <- grep(pattern = pat, tf[i,1])
#   if (length(ind)>0){
#     # c1 <- append(c1, substr(tf[i,1], ind, ind+7))
#     # # remove from tf[i,1]
#     # nc <- nchar(tf[i,1])
#     # locs <- setdiff(seq(1,nc), seq(ind,ind+7))
#     m <- regexpr(pattern=pat, tf[i,1])
#     this.ref <- regmatches(tf[i,1], m) # matching reference ID!
#     this.rest <- regmatches(tf[i,1], m, invert=TRUE)
#     n.parts <- length(this.rest[[1]])
#     if (i==20) {
#       this.item <- this.rest[[1]][2]
#       sx.in.item.5 <- this.rest[[1]][1]
#     } else {
#       this.item<- paste(this.rest[[1]], collapse="")
#     }
#     c1 <- append(c1, this.ref)
#     c2 <- append(c2, this.item)
#   }
# }
# ref.id <- c1[2:length(c1)]
# items <- c2[2:length(c2)]

# Only getting R2.2.1 (not R2.2.1_M)

# i <- 20
# m <- regexpr(pattern=pat, tf[i,1])
# this.ref <- regmatches(tf[i,1], m) # matching reference ID!
# this.rest <- regmatches(tf[i,1], m, invert=TRUE)
# n.parts <- length(this.rest[[1]])
# if (i==20) {
#   this.item <- this.rest[[1]][2]
#   sx.in.item.5 <- this.rest[[1]][1]
# } else {
#   this.item<- paste(this.rest[[1]], collapse="")
# }
# Skipped with check on grep (nevermind)
# i <- 9
# m <- regexpr(pattern=pat, tf[i,1])
# regmatches(tf[i,1], m)
# regmatches(tf[i,1], m, invert=TRUE)

# c1 <- tf[,1]
# c2 <- tf[,2]
# c3 <- tf[,3]
# c4 <- tf[,4]
# 
# c1 <- c1[c1!=""]
# 
# c2 <- c(paste(c2[1], collapse = " "),
#         paste(c2[4:5], collapse = " "),
#         paste(c2[8], collapse = " "),
#         paste(c2[11:16], collapse = " "),
#         paste(c2[17:18], collapse = " "),
#         paste(c2[23:26], collapse = " "),
#         paste(c2[29:31], collapse = " "),
#         paste(c2[33:39], collapse = " "))

# End
# -----------------------------------------------------------------------