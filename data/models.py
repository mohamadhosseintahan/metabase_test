from django.db import models

normal_fields = [
    "time",
    "aeration_rate",
    "agitator_rpm",
    "sugar_feed_rate",
    "acid_flow_rate",
    "base_flow_rate",
    "heating_cooling_water_flow_rate",
    "heating_water_flow_rate",
    "water_for_injection_dilution",
    "air_head_pressure",
    "dumped_broth_flow",
    "substrate_concentration",
    "dissolved_oxygen_concentration",
    "penicillin_concentration",
    "vessel_volume",
    "vessel_weight",
    "ph",
    "temperature",
    "generated_heat",
    "carbon_dioxide_percent_in_off_gas",
    "paa_flow",
    "paa_concentration_offline",
    "oil_flow",
    "nh_3_concentration_off_line",
    "oxygen_uptake_rate",
    "offline_penicillin_concentration",
    "offline_biomass_concentration",
    "carbon_evolution_rate",
    "ammonia_shots",
    "viscosity",
    "fault_reference",
    "control_reference",
    "raman_spec",
    "pat_control",
    "batch_reference",
    "batch_id",
    "fault_flag",
]
number_fields = [f"f{i}" for i in range(2400, 1599, -1)]
final_fields = normal_fields + number_fields

# Define a dictionary with the fields from MendeleyData
fields_dict = {
    "time": models.FloatField(null=True, blank=True, db_index=True),
    "aeration_rate": models.IntegerField(null=True, blank=True, help_text="Aeration rate(Fg:L/h)", db_index=True),
    "agitator_rpm": models.IntegerField(null=True, blank=True, help_text="Agitator RPM(RPM:RPM)", db_index=True),
    "sugar_feed_rate": models.IntegerField(null=True, blank=True, help_text="Sugar feed rate(Fs:L/h)", db_index=True),
    "acid_flow_rate": models.FloatField(null=True, blank=True, help_text="Acid flow rate(Fa:L/h)", db_index=True),
    "base_flow_rate": models.FloatField(null=True, blank=True, help_text="Base flow rate(Fb:L/h)", db_index=True),
    "heating_cooling_water_flow_rate": models.FloatField(null=True, blank=True, help_text="Heating/cooling water flow rate(Fc:L/h)", db_index=True),
    "heating_water_flow_rate": models.FloatField(null=True, blank=True, help_text="Heating water flow rate(Fh:L/h)", db_index=True),
    "water_for_injection_dilution": models.IntegerField(null=True, blank=True, help_text="Water for injection/dilution(Fw:L/h)", db_index=True),
    "air_head_pressure": models.FloatField(null=True, blank=True, help_text="Air head pressure(pressure:bar)", db_index=True),
    "dumped_broth_flow": models.IntegerField(null=True, blank=True, help_text="Dumped broth flow(Fremoved:L/h)", db_index=True),
    "substrate_concentration": models.FloatField(null=True, blank=True, help_text="Substrate concentration(S:g/L)", db_index=True),
    "dissolved_oxygen_concentration": models.FloatField(null=True, blank=True, help_text="Dissolved oxygen concentration(DO2:mg/L)", db_index=True),
    "penicillin_concentration": models.FloatField(null=True, blank=True, help_text="Penicillin concentration(P:g/L)", db_index=True),
    "vessel_volume": models.IntegerField(null=True, blank=True, help_text="Vessel Volume(V:L)", db_index=True),
    "vessel_weight": models.FloatField(null=True, blank=True, help_text="Vessel Weight(Wt:Kg)", db_index=True),
    "ph": models.FloatField(null=True, blank=True, help_text="pH(pH:pH)", db_index=True),
    "temperature": models.FloatField(null=True, blank=True, help_text="Temperature(T:K)", db_index=True),
    "generated_heat": models.FloatField(null=True, blank=True, help_text="Generated heat(Q:kJ)", db_index=True),
    "carbon_dioxide_percent_in_off_gas": models.FloatField(null=True, blank=True, help_text="carbon dioxide percent in off-gas(CO2outgas:%)", db_index=True),
    "paa_flow": models.FloatField(null=True, blank=True, help_text="PAA flow(Fpaa:PAA flow (L/h))", db_index=True),
    "paa_concentration_offline": models.FloatField(null=True, blank=True, help_text="PAA concentration offline(PAA_offline:PAA (g L^{-1}))", db_index=True),
    "oil_flow": models.IntegerField(null=True, blank=True, help_text="Oil flow(Foil:L/hr)", db_index=True),
    "nh_3_concentration_off_line": models.FloatField(null=True, blank=True, help_text="NH_3 concentration off-line(NH3_offline:NH3 (g L^{-1}))", db_index=True),
    "oxygen_uptake_rate": models.FloatField(null=True, blank=True, help_text="Oxygen Uptake Rate(OUR:(g min^{-1}))", db_index=True),
    "offline_penicillin_concentration": models.FloatField(null=True, blank=True, help_text="Offline Penicillin concentration(P_offline:P(g L^{-1}))", db_index=True),
    "offline_biomass_concentration": models.FloatField(null=True, blank=True, help_text="Offline Biomass concentratio(X_offline:X(g L^{-1}))", db_index=True),
    "carbon_evolution_rate": models.FloatField(null=True, blank=True, help_text="Carbon evolution rate(CER:g/h)", db_index=True),
    "ammonia_shots": models.IntegerField(null=True, blank=True, help_text="Ammonia shots(NH3_shots:kgs)", db_index=True),
    "viscosity": models.FloatField(null=True, blank=True, help_text="Viscosity(Viscosity_offline:centPoise)", db_index=True),
    "fault_reference": models.IntegerField(null=True, blank=True, help_text="Fault reference(Fault_ref:Fault ref)", db_index=True),
    "control_reference": models.IntegerField(null=True, blank=True, help_text="0 - Recipe driven 1 - Operator controlled(Control_ref:Control ref)", db_index=True),
    "raman_spec": models.IntegerField(null=True, blank=True, help_text="1- No Raman spec 1-Raman spec recorded", db_index=True),
    "pat_control": models.IntegerField(null=True, blank=True, help_text="2-PAT control(PAT_ref:PAT ref)", db_index=True),
    "batch_reference": models.IntegerField(null=True, blank=True, help_text="Batch reference(Batch_ref:Batch ref)", db_index=True),
    "batch_id": models.FloatField(null=True, blank=True, help_text="Batch ID", db_index=True),
    "fault_flag": models.FloatField(null=True, blank=True, help_text="Fault flag", db_index=True),
}

# Add the dynamically generated fields to the dictionary
# dynamic_fields = {f"f{i}": models.FloatField(null=True, blank=True) for i in range(2400, 1599, -1)}
# fields_dict.update(dynamic_fields)

# Add additional attributes to the dictionary if needed
fields_dict.update({
    '__module__': __name__,
    '__str__': lambda self: str(self.time),
    'Meta': type('Meta', (object,), {
        'verbose_name': "Mendeley Datum",
        'verbose_name_plural': "Mendeley Data",
    }),
})
# Use type() to create the model class dynamically
MendeleyData = type('MendeleyData', (models.Model,), fields_dict)