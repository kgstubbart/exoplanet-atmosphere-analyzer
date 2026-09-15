from pathlib import Path

import h5py
import numpy as np
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

def load_transmission_spectrum():
    path = Path(__file__).parent.parent / "data" / "raw" / "FIREFLy_transit_spec.h5"
    with h5py.File(path, "r") as f:
        wavelength = np.array(f["wavelength"])
        depth      = np.array(f["transit_depth"])
        uncertainty = np.array(f["transit_depth_uncertainty"])
    return wavelength, depth, uncertainty

if __name__ == "__main__":
    wavelength, depth, uncertainty = load_transmission_spectrum()
    print("\n=== Transmission Spectrum ===")
    print(f"shapes:           {wavelength.shape}, {depth.shape}, {uncertainty.shape}")
    print(f"wavelength range: {wavelength.min():.4f} – {wavelength.max():.4f} µm")
    print(f"transit depth:    {depth.min():.6f} – {depth.max():.6f}")