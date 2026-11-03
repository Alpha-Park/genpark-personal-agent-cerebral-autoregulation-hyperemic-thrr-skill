"""
Cerebral Autoregulation & Transient Hyperemic Response Ratio (THRR) Engine.
Provides deterministic, zero-dependency modeling of Transcranial Doppler (TCD) MCA velocity,
compression drop ratio, hyperemic overshoot (THRR), and myogenic/metabolic cerebral autoregulatory reserve.
"""

from typing import Dict, Any, List, Optional


class CerebralAutoregulationTHRRClient:
    """
    Deterministic client for calculating Transient Hyperemic Response Ratio (THRR).
    Assesses dynamic cerebral autoregulation (dCA), distal arteriolar vasodilatory reserve,
    and resilience against orthostatic hypoperfusion and ischemic cerebral insults.
    """

    def __init__(self):
        pass

    def evaluate_thrr(
        self,
        baseline_flow_velocity_cm_s: float,
        compression_flow_velocity_cm_s: float,
        hyperemic_peak_flow_velocity_cm_s: float,
        mean_arterial_pressure_mmhg: float = 90.0
    ) -> Dict[str, Any]:
        """
        Calculates THRR = FV3 / FV1 and evaluates autoregulatory compliance.
        Normative values:
        - Baseline MCA Flow Velocity (FV1): 45.0 - 75.0 cm/s
        - Compression Flow Velocity (FV2): 20.0 - 45.0 cm/s (drop >= 25% from baseline)
        - Hyperemic Peak Velocity (FV3): > FV1 during reactive hyperemia
        - THRR (FV3 / FV1): >= 1.10 (normal intact autoregulation: 1.12 - 1.35)
        - THRR < 1.09 indicates impaired dynamic autoregulation
        """
        if baseline_flow_velocity_cm_s <= 0 or compression_flow_velocity_cm_s <= 0 or hyperemic_peak_flow_velocity_cm_s <= 0:
            return {"error": "Flow velocities must be strictly positive"}
        if compression_flow_velocity_cm_s >= baseline_flow_velocity_cm_s:
            return {"error": "Compression flow velocity (FV2) must be less than baseline velocity (FV1)"}

        # 1. Transient Hyperemic Response Ratio (THRR = FV3 / FV1)
        thrr = round(hyperemic_peak_flow_velocity_cm_s / baseline_flow_velocity_cm_s, 3)

        # 2. Compression Drop Percentage
        drop_pct = round(((baseline_flow_velocity_cm_s - compression_flow_velocity_cm_s) / baseline_flow_velocity_cm_s) * 100.0, 1)

        # 3. Hyperemic Overshoot Percentage relative to baseline
        overshoot_pct = round(((hyperemic_peak_flow_velocity_cm_s - baseline_flow_velocity_cm_s) / baseline_flow_velocity_cm_s) * 100.0, 1)

        # 4. Cerebral Autoregulatory Reserve Score (0 - 100)
        score = 80.0
        if thrr >= 1.15:
            score += 15.0
        elif thrr >= 1.10:
            score += 8.0
        elif thrr < 1.02:
            score -= 35.0  # Absent hyperemic reserve
        elif thrr < 1.08:
            score -= 18.0

        if drop_pct >= 30.0:
            score += 5.0
        elif drop_pct < 20.0:
            score -= 10.0  # Inadequate compression challenge

        autoreg_score = round(min(100.0, max(5.0, score)), 1)

        if autoreg_score >= 85.0 and thrr >= 1.12:
            tier = "OPTIMAL_DYNAMIC_CEREBRAL_AUTOREGULATION"
            interp = f"Robust transient hyperemic overshoot (THRR {thrr} >= 1.10, Overshoot {overshoot_pct}%); intact arteriolar vasodilatory capacity."
            guidance = "Superior cerebral hemodynamic resilience. Arterioles respond briskly to transient perfusion drops."
        elif 1.06 <= thrr < 1.10:
            tier = "BORDERLINE_AUTOREGULATORY_RESERVE"
            interp = f"Blunted hyperemic response (THRR {thrr}, Overshoot {overshoot_pct}%); partial depletion of microvascular vasodilatory reserve."
            guidance = "Reduced autoregulatory buffer. Ensure optimal hydration and avoid abrupt postural transitions."
        else:
            tier = "IMPAIRED_CEREBRAL_AUTOREGULATION"
            interp = f"Markedly impaired autoregulation (THRR {thrr} < 1.06, Overshoot {overshoot_pct}%); distal arteriolar bed is fixed or exhausted, predisposing to hypoperfusion."
            guidance = "Critical loss of cerebral autoregulatory protection. Screen for severe carotid stenosis, microvascular disease, or dysautonomia."

        return {
            "baseline_flow_velocity_cm_s": baseline_flow_velocity_cm_s,
            "compression_flow_velocity_cm_s": compression_flow_velocity_cm_s,
            "hyperemic_peak_flow_velocity_cm_s": hyperemic_peak_flow_velocity_cm_s,
            "mean_arterial_pressure_mmhg": mean_arterial_pressure_mmhg,
            "compression_drop_pct": drop_pct,
            "hyperemic_overshoot_pct": overshoot_pct,
            "transient_hyperemic_response_ratio": thrr,
            "autoregulatory_reserve_score": autoreg_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
