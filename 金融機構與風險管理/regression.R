library(MASS)
library(stargazer)
data <- read.csv("/Users/shawn/Github/M1/金融機構與風險管理/SP500_change_R.csv")
# 處理無窮大的值
data[data == Inf | data == -Inf] <- NA

for(i in 1:ncol(data)) {
  if(is.numeric(data[, i])) {
    data[is.na(data[, i]), i] <- mean(data[, i], na.rm = TRUE)
  }
}
# OLS Method
model_ols <- lm(data$is_upgraded ~ data$CAPEI_change + data$bm_change + data$evm_change + data$pe_op_basic_change + 
                data$pe_op_dil_change + data$pe_exi_change + data$pe_inc_change + data$ps_change + data$pcf_change + 
                data$dpr_change + data$npm_change + data$opmbd_change + data$gpm_change + data$ptpm_change + data$roa_change +
                data$roe_change + data$roce_change + data$efftax_change + data$aftret_eq_change + 
                data$aftret_equity_change + data$cash_lt_change, data = data)
summary(model_ols)
stargazer(model_ols, type = "latex")

# logit mthod
data$is_upgraded <- factor(data$is_upgraded, ordered = TRUE)
model_bin_logit <- glm(is_upgraded ~ CAPEI_change + bm_change + evm_change + 
                         pe_op_basic_change + pe_op_dil_change + pe_exi_change + 
                         pe_inc_change + ps_change + pcf_change + dpr_change + 
                         npm_change + opmbd_change + gpm_change + ptpm_change + 
                         roa_change + roe_change + roce_change + efftax_change + 
                         aftret_eq_change + aftret_equity_change + cash_lt_change, 
                       data = data, family = binomial)
summary(model_bin_logit)
stargazer(model_bin_logit, type = "latex")

# probit method
model_probit <- polr( is_upgraded ~ CAPEI_change + bm_change + evm_change + 
                      pe_op_basic_change + pe_op_dil_change + pe_exi_change + 
                      pe_inc_change + ps_change + pcf_change + dpr_change + 
                      npm_change + opmbd_change + gpm_change + ptpm_change + 
                      roa_change + roe_change + roce_change + efftax_change + 
                      aftret_eq_change + aftret_equity_change + cash_lt_change, 
                     data = data, method = "probit", Hess = TRUE)