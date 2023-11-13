library(MASS)
data <- read.csv("/Users/shawn/Github/M1/金融機構與風險管理/SP500_change_V2.csv")
data[data == Inf | data == -Inf] <- NA

for(i in 1:ncol(data)) {
  if(is.numeric(data[, i])) {
    data[is.na(data[, i]), i] <- mean(data[, i], na.rm = TRUE)
  }
}

# OLS
model_ols <- lm(data$rating_diff ~ data$CAPEI_change + data$bm_change + data$evm_change + data$pe_op_basic_change + 
                  data$pe_op_dil_change + data$pe_exi_change + data$pe_inc_change + data$ps_change + data$pcf_change + 
                  data$dpr_change + data$npm_change + data$opmbd_change + data$gpm_change + data$ptpm_change + data$roa_change +
                  data$roe_change + data$roce_change + data$efftax_change + data$aftret_eq_change + 
                  data$aftret_equity_change + data$cash_lt_change, data = data)
summary(model_ols)
stargazer(model_ols, type = "latex")

# Logit
data$rating_diff <- factor(data$rating_diff, ordered = TRUE)
model_logit <- polr(data$rating_diff ~ data$CAPEI_change + data$bm_change + data$evm_change + data$pe_op_basic_change + 
                  data$pe_op_dil_change + data$pe_exi_change + data$pe_inc_change + data$ps_change + data$pcf_change + 
                  data$dpr_change + data$npm_change + data$opmbd_change + data$gpm_change + data$ptpm_change + data$roa_change +
                  data$roe_change + data$roce_change + data$efftax_change + data$aftret_eq_change + 
                  data$aftret_equity_change + data$cash_lt_change, data = data, Hess = TRUE)
summary(model_logit)

# Probit
model_probit <- polr(data$rating_diff ~ data$CAPEI_change + data$bm_change + data$evm_change + data$pe_op_basic_change + 
                      data$pe_op_dil_change + data$pe_exi_change + data$pe_inc_change + data$ps_change + data$pcf_change + 
                      data$dpr_change + data$npm_change + data$opmbd_change + data$gpm_change + data$ptpm_change + data$roa_change +
                      data$roe_change + data$roce_change + data$efftax_change + data$aftret_eq_change + 
                      data$aftret_equity_change + data$cash_lt_change, data = data, method = 'probit', Hess = TRUE)
summary(model_probit)