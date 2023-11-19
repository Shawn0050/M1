rm(list=ls())
library(MASS)
library(caret)
library(pROC)
#===============================================================================#

# OLS

# full sample
data <- read.csv('/Users/shawn/Github/M1/金融機構與風險管理/New_/forRegression/SP500_change_V7Final.csv')
data <- data[, -1]
factor_summary <- summary(data[1:35])
# ols_1 <- stargazer(factor_summary, type = "latex")
factor_cov <- cov(data[1:35])
# Train and test data
data_train_df70 <- read.csv("/Users/shawn/Github/M1/金融機構與風險管理/New_/forML/train_df70.csv")
data_train_df70 <- data_train_df70[, -1]
data_train_df70$rating_diff <- factor(data_train_df70$rating_diff, ordered = TRUE)
data_test_df30 <- read.csv("/Users/shawn/Github/M1/金融機構與風險管理/New_/forML/test_df30.csv")
data_test_df30 <- data_test_df30[, -1]

model_ols <- lm(rating_diff ~ .,
                  data = data)
summary(model_ols)
# Backward model selection
model_backward <- step(model_ols,direction="backward", test="F")
bw <- summary(model_backward)
# According to Backward model selection...
model_ols2 <- lm(rating_diff ~ total.debt..total.assets_change + 
                interest..average.total.debt_change +
                price..sales_change +
                interest.coverage.ratio_change +
                gross.profit.margin_change +
                gross.profit..total.assets_change,
                data = data)
summary(model_ols2)
# train 70-30
model_ols_70 <- lm(rating_diff ~ total.debt..total.assets_change + 
                     interest..average.total.debt_change +
                     price..sales_change +
                     interest.coverage.ratio_change +
                     gross.profit.margin_change +
                     gross.profit..total.assets_change,
                     data = data_train_df70)
summary(model_ols_70)
required_columns <- c('total.debt..total.assets_change',
                     'interest..average.total.debt_change',
                     'price..sales_change',
                     'interest.coverage.ratio_change',
                     'gross.profit.margin_change',
                     'gross.profit..total.assets_change')
test_df30 <- data_test_df30[required_columns]
predictors_30 <- predict(model_ols_70, type='response', newdata=test_df30)
plot(predictors_30, data_test_df30$rating_diff)

#===============================================================================#

# Order Logit Model

# full sample
data <- read.csv('/Users/shawn/Github/M1/金融機構與風險管理/New_/forRegression/SP500_change_V7Final.csv')
data <- data[, -1]
factor_summary <- summary(data[1:35])
# ols_1 <- stargazer(factor_summary, type = "latex")
factor_cov <- cov(data[1:35])
# Train and test data
data_train_df70 <- read.csv("/Users/shawn/Github/M1/金融機構與風險管理/New_/forML/train_df70.csv")
data_train_df70 <- data_train_df70[, -1]
data_train_df70$rating_diff <- factor(data_train_df70$rating_diff, ordered = TRUE)
data_test_df30 <- read.csv("/Users/shawn/Github/M1/金融機構與風險管理/New_/forML/test_df30.csv")
data_test_df30 <- data_test_df30[, -1]

data$rating_diff <- factor(data$rating_diff, ordered = TRUE)
# According to Backward model selection with OLS...
model_logit <- polr(rating_diff ~ total.debt..total.assets_change + 
                      interest..average.total.debt_change +
                      price..sales_change +
                      interest.coverage.ratio_change +
                      gross.profit.margin_change +
                      gross.profit..total.assets_change, 
                      data=data, Hess = TRUE)
summary(model_logit)
# 自定義backward
backward_selection <- function(full_model, data) {
  current_model <- full_model
  current_AIC <- AIC(full_model)
  variables <- names(coef(full_model))
  
  for (variable in variables[-1]) { # 略過intercept
    temp_model <- update(current_model, . ~ . - variable)
    temp_AIC <- AIC(temp_model)
    
    if (temp_AIC < current_AIC) {
      current_model <- temp_model
      current_AIC <- temp_AIC
    }
  }
  
  return(current_model)
}
### 解釋變數縮小
"""
model_logit_1 <- polr(rating_diff ~ total.debt..total.assets_change + 
                        interest..average.total.debt_change +
                        gross.profit.margin_change +
                        gross.profit..total.assets_change, data = data, Hess = TRUE)
selected_model <- backward_selection(model_logit_1, data)
summary(selected_model)
"""
# train 70-30
model_logit_70 <- polr(rating_diff ~ interest.coverage.ratio_change + 
                       total.debt..total.assets_change +
                       interest..average.total.debt_change + 
                       price..sales_change + 
                       gross.profit.margin_change + 
                       gross.profit..total.assets_change, 
                       data = data_train_df70, Hess = TRUE)
summary(model_logit_70)
# test 70-30
required_columns <- c("interest.coverage.ratio_change", 
                      "total.debt..total.assets_change", 
                      "interest..average.total.debt_change", 
                      "price..sales_change", 
                      "gross.profit.margin_change", 
                      "gross.profit..total.assets_change")
test_df30 <- data_test_df30[required_columns]
predictors_30 <- predict(model_logit_70, type='class', newdata=test_df30)
plot(predictors_30, data_test_df30$rating_diff)

#===============================================================================#

# Order Probit Model

# full sample
data <- read.csv('/Users/shawn/Github/M1/金融機構與風險管理/New_/forRegression/SP500_change_V7Final.csv')
data <- data[, -1]
factor_summary <- summary(data[1:35])
# ols_1 <- stargazer(factor_summary, type = "latex")
factor_cov <- cov(data[1:35])
# Train and test data
data_train_df70 <- read.csv("/Users/shawn/Github/M1/金融機構與風險管理/New_/forML/train_df70.csv")
data_train_df70 <- data_train_df70[, -1]
data_train_df70$rating_diff <- factor(data_train_df70$rating_diff, ordered = TRUE)
data_test_df30 <- read.csv("/Users/shawn/Github/M1/金融機構與風險管理/New_/forML/test_df30.csv")
data_test_df30 <- data_test_df30[, -1]

data$rating_diff <- factor(data$rating_diff, ordered = TRUE)
model_probit <- polr(rating_diff ~ total.debt..total.assets_change + 
                      interest..average.total.debt_change +
                      price..sales_change +
                      interest.coverage.ratio_change +
                      gross.profit.margin_change +
                      gross.profit..total.assets_change, 
                      method = 'probit', data=data, Hess = TRUE)
summary(model_probit)
# train 70-30
model_probit_70 <- polr(rating_diff ~ interest.coverage.ratio_change + 
                         total.debt..total.assets_change +
                         interest..average.total.debt_change + 
                         price..sales_change + 
                         gross.profit.margin_change + 
                         gross.profit..total.assets_change, 
                         method = 'probit', data=data, Hess = TRUE)
summary(model_probit_70)
# test 70-30
required_columns <- c("interest.coverage.ratio_change", 
                      "total.debt..total.assets_change", 
                      "interest..average.total.debt_change", 
                      "price..sales_change", 
                      "gross.profit.margin_change", 
                      "gross.profit..total.assets_change")
test_df30 <- data_test_df30[required_columns]
predictors_30 <- predict(model_probit_70, type='class', newdata=test_df30)
plot(predictors_30, data_test_df30$rating_diff)

#===============================================================================#
# stargazer(model_probit, type = "latex")

