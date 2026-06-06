from astroquery.mast import Observations

obs_table = Observations.query_criteria(
    obs_collection="JWST",
    proposal_id="1366",
    instrument_name="NIRSPEC*",
    target_name="WASP-39"
)

print("\n=== Observation Table ===")
print(obs_table)

products = Observations.get_product_list(obs_table)
print("\n=== Products Table ===")
print(products)

print("\n=== Unique Product Types ===")
print(set(products['productType']))

print("\n=== Available Columns ===")
print(products.colnames)

print("\n=== Unique Descriptions ===")
print(set(products['description']))