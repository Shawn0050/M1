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
data_test_df30 <- read.csv("/Users/shawn/Github/M1/金融機構與風險管理/New_/forML/test_df30.csv")
data_test_df30 <- data_test_df30[, -1]

model_ols <- lm(rating_diff ~ .,
                  data = data)
summary(model_ols)
# Backward model selection
model_backward <- step(model_ols,direction="backward", test="F")
summary(model_backward)
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
                     data = data_train_df70, type = 'response')
summary(model_ols_70)
required_columns <- c('total.debt..total.assets_change',
                     'interest..average.total.debt_change',
                     'price..sales_change',
                     'interest.coverage.ratio_change',
                     'gross.profit.margin_change',
                     'gross.profit..total.assets_change')
test_df30 <- data_test_df30[required_columns]
predictors_30 <- predict(model_ols_70, type='response', newdata=test_df30)
print(predictors_30-data_test_df30$rating_diff)

#===============================================================================#

# Order Logit Model

# full sample
data <- read.csv('/Users/shawn/Github/M1/金融機構與風險管理/New_/forRegression/SP500_change_V7Final.csv')
data <- data[, -1]
factor_summary <- summary(data[1:35])
factor_cov <- cov(data[1:35])
# Train and test data
data_train_df70 <- read.csv("/Users/shawn/Github/M1/金融機構與風險管理/New_/forML/train_df70.csv")
data_train_df70 <- data_train_df70[, -1]
data_train_df70$rating_diff <- factor(data_train_df70$rating_diff, ordered = TRUE)
data_test_df30 <- read.csv("/Users/shawn/Github/M1/金融機構與風險管理/New_/forML/test_df30.csv")
data_test_df30 <- data_test_df30[, -1]
column_names <- colnames(data)

data$rating_diff <- factor(data$rating_diff, ordered = TRUE)
# According to Backward model selection with OLS...
model_logit <- polr(rating_diff ~ total.debt..total.assets_change + 
                      interest..average.total.debt_change +
                      price..sales_change +
                      interest.coverage.ratio_change +
                      gross.profit.margin_change +
                      gross.profit..total.assets_change 
                      , data=data, Hess = TRUE)
summary(model_logit)

# 向前找因子
data <- read.csv('/Users/shawn/Github/M1/金融機構與風險管理/New_/forRegression/SP500_change_V7Final.csv')
# data <- data[, !(names(data) %in% "asset.turnover_change")]
data <- data[, -1]
data$rating_diff <- factor(data$rating_diff, ordered = TRUE)
column_names <- colnames(data)
# 逐步選擇
stepwise_model_selection <- function(data, column_names, base_formula) {
  best_aic <- Inf
  best_factor <- NA
  best_model <- NULL
  
  for (i in column_names) {
    # 更新公式
    formula <- as.formula(paste(base_formula, i, sep = " + "))
    model_logit_ <- polr(formula, data = data, Hess = TRUE)
    aic <- AIC(model_logit_)
    
    if (aic < best_aic) {
      best_aic <- aic
      best_factor <- i
      best_model <- model_logit_
    }
  }
  return(list(model = best_model, aic = best_aic, factor = best_factor))
}
# 初始化
base_formula <- "rating_diff ~"
# 初始的列名集合
initial_column_names <- column_names[2:35]
# 迭代
for (step in 1:10) {
  result <- stepwise_model_selection(data, initial_column_names, base_formula)
  
  base_formula <- paste(base_formula, result$factor, sep = " + ")
  initial_column_names <- setdiff(initial_column_names, result$factor)
  
  print(paste("步驟", step, ": 最小的AIC:", result$aic, "因子:", result$factor))
}

# According to Backward model selection with AIC Selection(w/o asset.turnover_change, cause we find out that 'asset.turnover_change' will lead to a bigger AIC)...
model_logit <- polr(rating_diff ~ total.debt..total.assets_change + 
                      interest..average.total.debt_change +
                      price..sales_change +
                      interest.coverage.ratio_change +
                      gross.profit.margin_change +
                      gross.profit..total.assets_change +
                      receivables.turnover_change
                    , data=data, Hess = TRUE)
summary(model_logit)

# train 70-30
model_logit_70 <- polr(rating_diff ~ total.debt..total.assets_change + 
                         interest..average.total.debt_change +
                         price..sales_change +
                         interest.coverage.ratio_change +
                         gross.profit.margin_change +
                         gross.profit..total.assets_change +
                         receivables.turnover_change, 
                       data = data_train_df70, Hess = TRUE)
summary(model_logit_70)
# test 70-30
required_columns <- c("interest.coverage.ratio_change", 
                      "total.debt..total.assets_change", 
                      "interest..average.total.debt_change", 
                      "price..sales_change", 
                      "gross.profit.margin_change", 
                      "gross.profit..total.assets_change",
                      "receivables.turnover_change")
test_df30 <- data_test_df30[required_columns]
predictors_30 <- predict(model_logit_70, type='class', newdata=test_df30)
temp_df <- data.frame(predict = predictors_30, actual = data_test_df30$rating_diff, stringsAsFactors = FALSE)
temp_df$predict <- as.numeric(temp_df$predict)
temp_df$actual <- as.numeric(temp_df$actual)
print(temp_df$predict - temp_df$actual)
# 完全不準

#===============================================================================#

# Order Probit Model

# full sample
data <- read.csv('/Users/shawn/Github/M1/金融機構與風險管理/New_/forRegression/SP500_change_V7Final.csv')
data <- data[, -1]
factor_summary <- summary(data[1:35])
factor_cov <- cov(data[1:35])
# Train and test data
data_train_df70 <- read.csv("/Users/shawn/Github/M1/金融機構與風險管理/New_/forML/train_df70.csv")
data_train_df70 <- data_train_df70[, -1]
data_train_df70$rating_diff <- factor(data_train_df70$rating_diff, ordered = TRUE)
data_test_df30 <- read.csv("/Users/shawn/Github/M1/金融機構與風險管理/New_/forML/test_df30.csv")
data_test_df30 <- data_test_df30[, -1]
column_names <- colnames(data)

data$rating_diff <- factor(data$rating_diff, ordered = TRUE)
# According to Backward model selection with OLS...
model_probit <- polr(rating_diff ~ total.debt..total.assets_change + 
                      interest..average.total.debt_change +
                      price..sales_change +
                      interest.coverage.ratio_change +
                      gross.profit.margin_change +
                      gross.profit..total.assets_change 
                    , method = 'probit', data=data, Hess = TRUE)
summary(model_probit)

# 向前找因子
data <- read.csv('/Users/shawn/Github/M1/金融機構與風險管理/New_/forRegression/SP500_change_V7Final.csv')
# data <- data[, !(names(data) %in% "asset.turnover_change")]
data <- data[, -1]
data$rating_diff <- factor(data$rating_diff, ordered = TRUE)
column_names <- colnames(data)
# 逐步選擇(結果發現probit model會出現無法收斂的情況，有鑒於逐步選擇的過程大致與logit相似，故後續直接採用logit選擇出的解釋變數)
stepwise_model_selection <- function(data, column_names, base_formula) {
  best_aic <- Inf
  best_factor <- NA
  best_model <- NULL
  
  for (i in column_names) {
    # 更新公式
    formula <- as.formula(paste(base_formula, i, sep = " + "))
    model_probit_ <- polr(formula, method = 'probit', data = data, Hess = TRUE, 
                          control = list(maxit = 50, reltol = 1e-3))
    aic <- AIC(model_probit_)
    
    if (aic < best_aic) {
      best_aic <- aic
      best_factor <- i
      best_model <- model_probit_
    }
  }
  return(list(model = best_model, aic = best_aic, factor = best_factor))
}
# 初始化
base_formula <- "rating_diff ~"
# 初始的列名集合
initial_column_names <- column_names[2:35]
# 迭代
for (step in 1:10) {
  result <- stepwise_model_selection(data, initial_column_names, base_formula)
  
  base_formula <- paste(base_formula, result$factor, sep = " + ")
  initial_column_names <- setdiff(initial_column_names, result$factor)
  
  print(paste("步驟", step, ": 最小的AIC:", result$aic, "因子:", result$factor))
}

# According to Backward model selection with AIC Selection(w/o asset.turnover_change, cause we find out that 'asset.turnover_change' will lead to a bigger AIC)...
model_probit <- polr(rating_diff ~ total.debt..total.assets_change + 
                      interest..average.total.debt_change +
                      price..sales_change +
                      interest.coverage.ratio_change +
                      gross.profit.margin_change +
                      gross.profit..total.assets_change +
                      receivables.turnover_change
                    , method = 'probit', data=data, Hess = TRUE)
summary(model_probit)

# train 70-30
model_probit_70 <- polr(rating_diff ~ total.debt..total.assets_change + 
                         interest..average.total.debt_change +
                         price..sales_change +
                         interest.coverage.ratio_change +
                         gross.profit.margin_change +
                         gross.profit..total.assets_change +
                         receivables.turnover_change, 
                       method = 'probit', data = data_train_df70, Hess = TRUE)
summary(model_probit_70)
# test 70-30
required_columns <- c("interest.coverage.ratio_change", 
                      "total.debt..total.assets_change", 
                      "interest..average.total.debt_change", 
                      "price..sales_change", 
                      "gross.profit.margin_change", 
                      "gross.profit..total.assets_change",
                      "receivables.turnover_change")
test_df30 <- data_test_df30[required_columns]
predictors_30 <- predict(model_probit_70, type='class', newdata=test_df30)
temp_df <- data.frame(predict = predictors_30, actual = data_test_df30$rating_diff, stringsAsFactors = FALSE)
temp_df$predict <- as.numeric(temp_df$predict)
temp_df$actual <- as.numeric(temp_df$actual)
print(temp_df$predict - temp_df$actual)
# 完全不準

#===============================================================================#
# stargazer(model_probit, type = "latex")

