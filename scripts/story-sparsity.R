library(tidyverse)
library(ggtext)

df <- read_csv("data-extract/sparsity-stories-meets-long.csv")
skill.levels <- unique(df["Skill"])
text.levels <- unique(df["Text"])

df <- df %>% 
  mutate(Skill = factor(Skill)) %>% 
  mutate(Text = factor(Text))

df["Skill"] <- substr(df$Skill, 1, 6)  # remove performance level; constant M

# color code domain in x-axis tick labels
domain <- substr(df$Skill, 2, 2)
tick_color <- case_when(domain=="1" ~ "red",
                        domain=="2" ~ "green",
                        domain=="3" ~ "blue")
df["tick_color"] <- tick_color

h.in <- 7.0
w.in <- 8.5
colours = c("white", "black", "blue")
df <- df %>% rename(Grade = grade)
ggplot(df, aes(Skill, Text)) +
  geom_tile(aes(fill = as.factor(Check)), colour = "grey50") +
  scale_fill_manual(values = colours, name = "Items") +
  facet_grid(rows=vars(Grade), 
             scales="free_y",
             space="free",
             labeller = labeller(Grade = label_both)) + 
  theme(axis.text.x = element_markdown(angle = 90, color = tick_color),
        axis.ticks.x = element_blank(),
        axis.title.x = element_text(size = 16),
        axis.title.y = element_text(size = 16),
        strip.text.y.right = element_text(angle = 0)) +
  scale_x_discrete(position = "top")
ggsave("plots/story-sparsity-meets-grade.svg", width=w.in, height=h.in, units="in")

# Also save (Text) Genre and make alternate facets
h.in <- 7.0
w.in <- 11.5
df <- df %>% rename(Genre = type)
ggplot(df, aes(Skill, Text)) +
  geom_tile(aes(fill = as.factor(Check)), colour = "grey50") +
  scale_fill_manual(values = colours, name = "Items") +
  facet_grid(rows=vars(Genre), 
             scales="free_y",
             space="free",
             labeller = labeller(Genre = label_both)) + 
  theme(axis.text.x = element_text(angle = 90),
        axis.ticks.x = element_blank(),
        axis.title.x = element_text(size = 16),
        axis.title.y = element_text(size = 16),
        strip.text.y.right = element_text(angle = 0)) +
  scale_x_discrete(position = "top")
ggsave("plots/story-sparsity-meets-genre.svg", width=w.in, height=h.in, units="in")


# End
# ---------------------------------------------------------