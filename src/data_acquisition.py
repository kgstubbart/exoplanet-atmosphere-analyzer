from astroquery.mast import Observations

obs_table = Observations.query_criteria(
    obs_collection="JWST",
    proposal_id="1366",
    instrument_name="NIRSPEC*",
    target_name="WASP-39"
)

print("\n=== Observation Table ===")
print(obs_table)