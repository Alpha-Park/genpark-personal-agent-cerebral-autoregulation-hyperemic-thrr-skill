"""
Example Usage: Cerebral Autoregulation & Transient Hyperemic Response Ratio (THRR).
Demonstrates zero-dependency calculation of TCD flow velocities, hyperemic overshoot, THRR ratio, and autoregulatory scoring.
"""

from client import CerebralAutoregulationTHRRClient


def main():
    client = CerebralAutoregulationTHRRClient()
    print("=== Cerebral Autoregulation & THRR Demo ===")

    # Test Case 1: Healthy robust dynamic autoregulatory response
    res1 = client.evaluate_thrr(
        baseline_flow_velocity_cm_s=62.0,
        compression_flow_velocity_cm_s=40.0,
        hyperemic_peak_flow_velocity_cm_s=78.5,
        mean_arterial_pressure_mmhg=92.0
    )
    print("\nTest Case 1: Intact Dynamic Cerebral Autoregulation")
    print(f"  Baseline FV1: {res1['baseline_flow_velocity_cm_s']} cm/s | Compression FV2: {res1['compression_flow_velocity_cm_s']} cm/s (Drop: {res1['compression_drop_pct']}%)")
    print(f"  Hyperemic Peak FV3: {res1['hyperemic_peak_flow_velocity_cm_s']} cm/s (Overshoot: {res1['hyperemic_overshoot_pct']}%)")
    print(f"  THRR Ratio (FV3/FV1): {res1['transient_hyperemic_response_ratio']}")
    print(f"  Autoregulatory Reserve Score: {res1['autoregulatory_reserve_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Physiological Interpretation: {res1['physiological_interpretation']}")
    print(f"  Actionable Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Blunted/exhausted autoregulatory reserve
    res2 = client.evaluate_thrr(
        baseline_flow_velocity_cm_s=58.0,
        compression_flow_velocity_cm_s=41.0,
        hyperemic_peak_flow_velocity_cm_s=59.5,
        mean_arterial_pressure_mmhg=88.0
    )
    print("\nTest Case 2: Impaired Autoregulation / Absent Hyperemia")
    print(f"  THRR Ratio: {res2['transient_hyperemic_response_ratio']} | Overshoot: {res2['hyperemic_overshoot_pct']}%")
    print(f"  Autoregulatory Reserve Score: {res2['autoregulatory_reserve_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Actionable Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
