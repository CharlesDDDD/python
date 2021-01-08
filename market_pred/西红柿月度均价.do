


cd "C:\Users\weiha\Desktop\cif.mofcom.gov.cn\"
set more off

* import
import delimited "批发价格行情_170120_西红柿.txt", delimiter(comma) bindquote(nobind) encoding(UTF-8) clear

* drop duplicate records
duplicates drop

* rename columns
renvars * \ searchDate title AREA COMMDITYNAME COMMDITY_ID COUNTY_ID COUNTY_NAME ENTERID NAME PRICE1 PRICE2 PRICE3 RPT_DATE
renvars PRICE1 PRICE2 PRICE3 \ 当日价格 前一日价格 环比

* sort 
sort searchDate RPT_DATE title AREA COMMDITYNAME COMMDITY_ID COUNTY_ID COUNTY_NAME ENTERID NAME

* ym variable
gen RPT_DATE_date = date(RPT_DATE, "YMD")
format RPT_DATE_date %tdCCYY-NN-DD
gen ym = ym(year(RPT_DATE_date), month(RPT_DATE_date))
format ym %tmCCYY-NN

* keep months: 2015 - 2019
keep if ym >= ym(2015, 1) & ym <= ym(2019, 12)

* daily average
bysort RPT_DATE_date: egen daily_average_price = mean(当日价格)
keep RPT_DATE_date ym daily_average_price
duplicates drop
sort RPT_DATE_date

* monthly average 
bysort ym: egen monthly_average_price = mean(daily_average_price)
keep ym monthly_average_price
duplicates drop
sort ym

twoway scatter monthly_average_price ym, connect(l) sort(ym) msize(vsmall) xlabel(#60, labsize(vsmall) angle(90)) xsize(8) ysize(4)
