library(readxl)
library(tidyverse)
library(lme4)
library(lmerTest)

raw_data <- read_excel("C:/Users/19146/Desktop/cleanerdata.xlsx")

filtered_data <- raw_data %>% filter(!is.na(response), `word type` == "r",
                                     `user correct?` == "incorrect",
                                     `correct response` == "f", !(`word` == "rided"),
                                     !(`word` == "swinged"))
                                    
