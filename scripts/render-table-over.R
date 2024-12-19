library(tidyverse)
library(knitr)
library(kableExtra)
library(readr)


df <- read_csv("read-over-repro.csv") %>% 
  rename_with(~ gsub("_", "", .x, fixed = TRUE)) %>%
  mutate_if(is.numeric, ~case_when(.x == 0 ~ '',
                                   .x == 1 ~ 'X',
                                   TRUE ~ '?'))


to <- df %>% kbl() %>%
  add_header_above(c(" " = 3, "Grade" = 9)) %>%
  row_spec(seq(1,dim(df)[1]), font_size=10) %>%
  column_spec(seq(4,dim(df)[2]), width = "3em") %>%
  column_spec(1, width = "22em", width_min = "22em") %>%
  column_spec(2, width = "20em", width_min = "15em") %>%
  column_spec(3, width = "50em", width_min = "15em") %>%
  kable_paper(full_width = F) %>%
  collapse_rows(columns = 1:2, valign = "middle")
readr::write_file(to, "read-over-repro-0.html")

df %>% kbl() %>%
  add_header_above(c(" " = 3, "Grade" = 9)) %>%
  row_spec(seq(1,dim(df)[1]), font_size=10) %>%
  column_spec(seq(4,dim(df)[2]), width = "3em") %>%
  column_spec(1, width = "22em", width_min = "22em") %>%
  column_spec(2, width = "20em", width_min = "15em") %>%
  column_spec(3, width = "50em", width_min = "15em") %>%
  kable_paper(full_width = F) %>%
  collapse_rows(columns = 1:2, valign = "middle") %>%
  cat(., file = "read-over-repro-1.html")

# Simple script to remove table-striped from: /mnt/c/Users/earll/Documents/fab-carl/_site/posts/demo-graphviz/index.html Shell script to do render then removal.