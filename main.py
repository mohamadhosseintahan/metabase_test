import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nba.settings')
django.setup()

import pandas as pd

from data.models import MendeleyData

file_path = "Mendeley_data/100_Batches_IndPenSim_V3.csv"

columns_to_read = [
    "Time (h)",
    "Aeration rate(Fg:L/h)",
    "Agitator RPM(RPM:RPM)",
    "Sugar feed rate(Fs:L/h)",
    "Acid flow rate(Fa:L/h)",
    "Base flow rate(Fb:L/h)",
    "Heating/cooling water flow rate(Fc:L/h)",
    "Heating water flow rate(Fh:L/h)",
    "Water for injection/dilution(Fw:L/h)",
    "Air head pressure(pressure:bar)",
    "Dumped broth flow(Fremoved:L/h)",
    "Substrate concentration(S:g/L)",
    "Dissolved oxygen concentration(DO2:mg/L)",
    "Penicillin concentration(P:g/L)",
    "Vessel Volume(V:L)",
    "Vessel Weight(Wt:Kg)",
    "pH(pH:pH)",
    "Temperature(T:K)",
    "Generated heat(Q:kJ)",
    "carbon dioxide percent in off-gas(CO2outgas:%)",
    "PAA flow(Fpaa:PAA flow (L/h))",
    "PAA concentration offline(PAA_offline:PAA (g L^{-1}))",
    "Oil flow(Foil:L/hr)",
    "NH_3 concentration off-line(NH3_offline:NH3 (g L^{-1}))",
    "Oxygen Uptake Rate(OUR:(g min^{-1}))",
    "Offline Penicillin concentration(P_offline:P(g L^{-1}))",
    "Offline Biomass concentratio(X_offline:X(g L^{-1}))",
    "Carbon evolution rate(CER:g/h)",
    "Ammonia shots(NH3_shots:kgs)",
    "Viscosity(Viscosity_offline:centPoise)",
    "Fault reference(Fault_ref:Fault ref)",
    "0 - Recipe driven 1 - Operator controlled(Control_ref:Control ref)",
    "1- No Raman spec",
    " 1-Raman spec recorded",
    "2-PAT control(PAT_ref:PAT ref)",
    "Batch reference(Batch_ref:Batch ref)",
    "Batch ID",
    "Fault flag",
]
# for i in range(2400, 1599, -1):
#     columns_to_read.append(str(i))

chunksize = 10**6

chunks = []

for chunk in pd.read_csv(file_path, chunksize=chunksize, usecols=columns_to_read):
    chunks.append(chunk)

df = pd.concat(chunks, axis=0)

counter = 0
instances = []
for index, row in df.iterrows():
    data = {
    "time" : row["Time (h)"] if pd.notna(row["Time (h)"]) else None,
    "aeration_rate" : row["Aeration rate(Fg:L/h)"] if pd.notna(row["Aeration rate(Fg:L/h)"]) else None,
    "agitator_rpm" : row["Agitator RPM(RPM:RPM)"] if pd.notna(row["Agitator RPM(RPM:RPM)"]) else None,
    "sugar_feed_rate" : row["Sugar feed rate(Fs:L/h)"] if pd.notna(row["Sugar feed rate(Fs:L/h)"]) else None,
    "acid_flow_rate" : row["Acid flow rate(Fa:L/h)"] if pd.notna(row["Acid flow rate(Fa:L/h)"]) else None,
    "base_flow_rate" : row["Base flow rate(Fb:L/h)"] if pd.notna(row["Base flow rate(Fb:L/h)"]) else None,
    "heating_cooling_water_flow_rate" : row["Heating/cooling water flow rate(Fc:L/h)"] if pd.notna(row["Heating/cooling water flow rate(Fc:L/h)"]) else None,
    "heating_water_flow_rate" : row["Heating water flow rate(Fh:L/h)"] if pd.notna(row["Heating water flow rate(Fh:L/h)"]) else None,
    "water_for_injection_dilution" : row["Water for injection/dilution(Fw:L/h)"] if pd.notna(row["Water for injection/dilution(Fw:L/h)"]) else None,
    "air_head_pressure" : row["Air head pressure(pressure:bar)"] if pd.notna(row["Air head pressure(pressure:bar)"]) else None,
    "dumped_broth_flow" : row["Dumped broth flow(Fremoved:L/h)"] if pd.notna(row["Dumped broth flow(Fremoved:L/h)"]) else None,
    "substrate_concentration" : row["Substrate concentration(S:g/L)"] if pd.notna(row["Substrate concentration(S:g/L)"]) else None,
    "dissolved_oxygen_concentration" : row["Dissolved oxygen concentration(DO2:mg/L)"] if pd.notna(row["Dissolved oxygen concentration(DO2:mg/L)"]) else None,
    "penicillin_concentration" : row["Penicillin concentration(P:g/L)"] if pd.notna(row["Penicillin concentration(P:g/L)"]) else None,
    "vessel_volume" : row["Vessel Volume(V:L)"] if pd.notna(row["Vessel Volume(V:L)"]) else None,
    "vessel_weight" : row["Vessel Weight(Wt:Kg)"] if pd.notna(row["Vessel Weight(Wt:Kg)"]) else None,
    "ph" : row["pH(pH:pH)"] if pd.notna(row["pH(pH:pH)"]) else None,
    "temperature" : row["Temperature(T:K)"] if pd.notna(row["Temperature(T:K)"]) else None,
    "generated_heat" : row["Generated heat(Q:kJ)"] if pd.notna(row["Generated heat(Q:kJ)"]) else None,
    "carbon_dioxide_percent_in_off_gas" : row["carbon dioxide percent in off-gas(CO2outgas:%)"] if pd.notna(row["carbon dioxide percent in off-gas(CO2outgas:%)"]) else None,
    "paa_flow" : row["PAA flow(Fpaa:PAA flow (L/h))"] if pd.notna(row["PAA flow(Fpaa:PAA flow (L/h))"]) else None,
    "paa_concentration_offline" : row["PAA concentration offline(PAA_offline:PAA (g L^{-1}))"] if pd.notna(row["PAA concentration offline(PAA_offline:PAA (g L^{-1}))"]) else None,
    "oil_flow" : row["Oil flow(Foil:L/hr)"] if pd.notna(row["Oil flow(Foil:L/hr)"]) else None,
    "nh_3_concentration_off_line" : row["NH_3 concentration off-line(NH3_offline:NH3 (g L^{-1}))"] if pd.notna(row["NH_3 concentration off-line(NH3_offline:NH3 (g L^{-1}))"]) else None,
    "oxygen_uptake_rate" : row["Oxygen Uptake Rate(OUR:(g min^{-1}))"] if pd.notna(row["Oxygen Uptake Rate(OUR:(g min^{-1}))"]) else None,
    "offline_penicillin_concentration" : row["Offline Penicillin concentration(P_offline:P(g L^{-1}))"] if pd.notna(row["Offline Penicillin concentration(P_offline:P(g L^{-1}))"]) else None,
    "offline_biomass_concentration" : row["Offline Biomass concentratio(X_offline:X(g L^{-1}))"] if pd.notna(row["Offline Biomass concentratio(X_offline:X(g L^{-1}))"]) else None,
    "carbon_evolution_rate" : row["Carbon evolution rate(CER:g/h)"] if pd.notna(row["Carbon evolution rate(CER:g/h)"]) else None,
    "ammonia_shots" : row["Ammonia shots(NH3_shots:kgs)"] if pd.notna(row["Ammonia shots(NH3_shots:kgs)"]) else None,
    "viscosity" : row["Viscosity(Viscosity_offline:centPoise)"] if pd.notna(row["Viscosity(Viscosity_offline:centPoise)"]) else None,
    "fault_reference" : row["Fault reference(Fault_ref:Fault ref)"] if pd.notna(row["Fault reference(Fault_ref:Fault ref)"]) else None,
    "control_reference" : row["0 - Recipe driven 1 - Operator controlled(Control_ref:Control ref)"] if pd.notna(row["0 - Recipe driven 1 - Operator controlled(Control_ref:Control ref)"]) else None,
    "raman_spec" : row["1- No Raman spec"] if pd.notna(row["1- No Raman spec"]) else None,
    "pat_control" : row[" 1-Raman spec recorded"] if pd.notna(row[" 1-Raman spec recorded"]) else None,
    "batch_reference" : row["2-PAT control(PAT_ref:PAT ref)"] if pd.notna(row["2-PAT control(PAT_ref:PAT ref)"]) else None,
    "batch_id" : row["Batch reference(Batch_ref:Batch ref)"] if pd.notna(row["Batch reference(Batch_ref:Batch ref)"]) else None,
    "fault_flag" : row["Batch ID"] if pd.notna(row["Batch ID"]) else None,
    }
    # for i in range(2400, 1599, -1):
    #     data[f"f{i}"] = row[str(i)] if pd.notna(row[str(i)]) else None
    instances.append(MendeleyData(**data))
    if index != 0 and index % 1000 == 0:
        MendeleyData.objects.bulk_create(instances)
        instances = []

    print(index)

# remaining data from end of dataframe
MendeleyData.objects.bulk_create(instances)
























