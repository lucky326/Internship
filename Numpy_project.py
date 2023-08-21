import csv
import numpy as np
data=[]
with open(r"C:\Users\Lokesh\Downloads\MER_T07_02A-2020-02-03.csv",'r') as csvfile:
    file_read=csv.reader(csvfile,delimiter=',')
    for row in file_read:
        data.append(row)

data=np.array(data)#convert the list to array

##
dimension=print(data.ndim,data.shape,data.dtype)

##
print(data[:10,3])

##
print(data[0])

##
print(data[1:20,[1,2]])

##
print(data[:3],data[-3:])

##
sort=data[data[:,2].argsort()]
print(sort)

##
alldata=data[1:,:]
r_rows=(alldata[:,1]>='194901') & (alldata[:,1]<'199013')
r_source=(alldata[:,0]=='CLETPUS') | (alldata[:,0]=='NUETPUS')

r_sources= r_rows & r_source
electricity=alldata[r_sources,2].astype(float)
total_electricity=np.sum(electricity)
print("total electricity",total_electricity)

##
unique_sources = np.unique(data[1:, 0])
for source in unique_sources:
    print(source)

##
mask = data[1:, 0] == 'WYETPUS'
wind_energy_data = data[1:][mask]
for row in wind_energy_data:
    print(row)

##

mask = data[1:, 4] == 'Electricity Net Generation Total (including from sources not shown), All Sectors'
usa_total_energy_data = data[1:][mask]
total_energy_generated = np.sum(usa_total_energy_data[:, 2].astype(float))
print("Total energy generated in the USA till date:", total_energy_generated)

##
wind_energy_mask = data[1:, 0] == 'WYETPUS'
wind_energy_data = data[1:][wind_energy_mask]
valid_wind_energy_data = wind_energy_data[wind_energy_data[:, 2] != 'Not Available']
wind_energy_values = valid_wind_energy_data[:, 2].astype(float)
average_wind_energy = np.mean(wind_energy_values)
std_dev_wind_energy = np.std(wind_energy_values)
print("Average annual energy generated from wind in the USA:", average_wind_energy)

##
valid_rows = data[1:][data[1:, 2] != 'Not Available']
years = valid_rows[:, 1].astype(int) // 100
values = valid_rows[:, 2].astype(float)
max_energy_index = np.argmax(values)
max_energy_year = years[max_energy_index]
max_energy_value = values[max_energy_index]

print("Maximum annual energy generated:", max_energy_value, "Million Kilowatthours")
print("Year when the maximum annual energy was generated:", max_energy_year)

##
years = data[1:, 1].astype(int) // 100
values = data[1:, 2]

values[values == 'Not Available'] = np.nan
values = values.astype(float)

wind_energy_mask = data[1:, 0] == 'WYETPUS'
wind_years = years[wind_energy_mask]
wind_values = values[wind_energy_mask]

avg_wind_energy = np.nanmean(wind_values)

max_source_index = np.nanargmax(values)
max_source = data[max_source_index + 1, 0]

print("Average wind energy production:", avg_wind_energy, "Million Kilowatthours")
print("Source with the largest annual electricity production:", max_source)

##
sources = data[1:, 0]
values = data[1:, 2].astype(float)

wind_mask = sources == 'WYETPUS'
solar_mask = sources == 'SOTEPUS'

wind_energy = np.sum(values[wind_mask])
solar_energy = np.sum(values[solar_mask])

total_energy = np.sum(values)

combined_energy = wind_energy + solar_energy

wind_contribution = (wind_energy / total_energy) * 100
solar_contribution = (solar_energy / total_energy) * 100
combined_contribution = (combined_energy / total_energy) * 100

print("Wind Energy Contribution:", wind_contribution, "%")
print("Solar Energy Contribution:", solar_contribution, "%")
print("Combined Wind and Solar Contribution:", combined_contribution, "%")

if wind_contribution > combined_contribution:
    print("The national grid is shifting toward wind energy.")
else:
    print("The national grid is not fundamentally shifting toward wind energy.")
