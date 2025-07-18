import numpy as np

data=np.genfromtxt("dirty_cafe_sales.csv" , delimiter="," , skip_header=1)
print(data.shape)
quantity=data[:,2]
price_per_unit=data[:,3]
total_spent=data[:,4]
missing_quantity=np.isnan(quantity)

quantity[missing_quantity]=total_spent[missing_quantity]/price_per_unit[missing_quantity]
data[:,2]=quantity

missing_total=np.isnan(total_spent)

total_spent[missing_total]=quantity[missing_total]*price_per_unit[missing_total]
data[:,4] = total_spent
missing_price=np.isnan(price_per_unit)
price_per_unit[missing_price]=total_spent[missing_price]/quantity[missing_price]
data[:,3]=price_per_unit
print(data[:20])
np.savetxt("cleaned_numeric_data.csv",data,delimiter="," ,fmt="%.2f")

data_str=np.genfromtxt("dirty_cafe_sales.csv",delimiter=",",dtype=str,skip_header=1)
print(data[:5])
data_str[:,5]=np.where((data_str[:,5]=="UNKNOWN" )| (data_str[:,5]=="ERROR") |(data_str[:,5]==""),"missing",data_str[:,5])
data_str[:,6]=np.where((data_str[:,6]=="UNKNOWN" )| (data_str[:,6]=="ERROR")| (data_str[:,6]==""),"missing",data_str[:,6])
item_column = data_str[:, 1]
data_str[:, 1] = np.where(
    (item_column == "UNKNOWN") | (item_column == "ERROR") | (item_column == "") | (item_column == "nan"),
    "Missing",
    item_column
)
print(data[:20])
np.savetxt("cleaned_cafe_sales_text.csv", data_str, delimiter=",", fmt="%s")
data_numeric_str=data.astype(str)
# Assuming column order: txn_id, item, quantity, price, total, payment, location, date
final_data = np.column_stack((
    data_str[:, 0],   # txn_id
    data_str[:, 1],   # item
    data_numeric_str[:, 2],  # quantity
    data_numeric_str[:, 3],  # price
    data_numeric_str[:, 4],  # total
    data_str[:, 5],   # payment method
    data_str[:, 6],   # location
    data_str[:, 7],   # date
))
np.savetxt("final_cleaned_data.csv", final_data, delimiter=",", fmt="%s", header="TransactionID,Item,Quantity,PricePerUnit,TotalSpent,PaymentMethod,Location,Date", comments="")

