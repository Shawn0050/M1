rm(list=ls())
library(plm)
library(tidyverse)
library(cli)
library(tidyr)
library(lmtest)
library(sandwich)
library(BSDA)
# Data preparation
ff3 <- read.csv("/Users/shawn/Github/M1/金融計量/ff3.csv")
etf <- read.csv("/Users/shawn/Github/M1/金融計量/regression_data/etf_transform.csv")
stock_portfolio <- read.csv("/Users/shawn/Github/M1/金融計量/regression_data/merged_stock_portfolios.csv")

# Checking
etf[1:3,1:5]
dim(etf)

# Transfer to long format
long_data = pivot_longer(etf,
                         cols=2:ncol(etf),
                         names_to = 'portf',
                         values_to = 'ExRet')
# Augment the long format data with factor portfolios
long_data = left_join(long_data, ff3, by='date')

# FM regression step1(time-series)
long_pdf = pdata.frame(long_data, index=c('portf','date'))
FM_reg1 = pmg(ExRet~rm+SMB+HML, data = long_pdf)

dim(FM_reg1$indcoef)
t(FM_reg1$indcoef[,1:2])
# Collect the Beta's
Beta = t(FM_reg1$indcoef[-1,])
portf_names = row.names(Beta)
Beta = as_tibble(Beta)
Beta = Beta %>% add_column(portf = portf_names)
Beta

# Data preparation for the second step
long_data2 = long_data %>%
  dplyr::select(date,portf,ExRet) %>%
  left_join(Beta, by = 'portf')
head(long_data2,3)
# FM regression step2(cross-sectional)
long_pdf2 = pdata.frame(long_data2, index=c('date','portf'))
FM_reg2 = pmg(ExRet~rm+SMB+HML, data = long_pdf2)
FM_reg2$indcoef[,1:5]

summary(Beta)
summary(FM_reg2)

# NWSE
Mkt_RP = FM_reg2$indcoef['rm',]
SMB_RP = FM_reg2$indcoef['SMB',]
HML_RP = FM_reg2$indcoef['HML',]

coeftest(lm(Mkt_RP ~ 1), vcov=NeweyWest,lag=3)
coeftest(lm(SMB_RP ~ 1), vcov=NeweyWest,lag=3)
coeftest(lm(HML_RP ~ 1), vcov=NeweyWest,lag=3)

