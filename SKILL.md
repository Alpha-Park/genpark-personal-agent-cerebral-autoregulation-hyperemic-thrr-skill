---
name: genpark-personal-agent-cerebral-autoregulation-hyperemic-thrr-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating Transcranial Doppler (TCD) Transient Hyperemic Response Ratio (THRR = FV3/FV1), vasodilatory reserve, and dynamic cerebral autoregulation.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Cerebral Autoregulation & Transient Hyperemic Response Ratio (THRR) Skill

A sovereign personal agent capability for evaluating dynamic cerebral autoregulation (dCA), microvascular arteriolar vasodilatory reserve, Transcranial Doppler (TCD) flow velocity kinetics, and the Transient Hyperemic Response Ratio ($THRR = FV_3 / FV_1$).

## Core Capabilities
- **TCD Hemodynamic Velocity Profiling**: Tracks baseline MCA mean flow velocity ($FV_1$), carotid compression dip velocity ($FV_2$), and release hyperemic overshoot ($FV_3$).
- **Transient Hyperemic Response Ratio (THRR)**: Calculates the physiological metric $THRR = FV_3 / FV_1$ (normative: $\ge 1.10$, representing $\ge 10\%$ hyperemic reserve).
- **Cerebrovascular Autoregulatory Reserve**: Quantifies downstream arteriolar myogenic and metabolic reactivity during transient blood pressure perturbations.
- **Orthostatic & Cognitive Guarding**: Prescribes hydration corridors, gradual postural transitions, and mental pacing during cerebral hypoperfusion risks.

## Fast Invocation
```python
from client import CerebralAutoregulationTHRRClient

client = CerebralAutoregulationTHRRClient()
res = client.evaluate_thrr(
    baseline_flow_velocity_cm_s=62.0,
    compression_flow_velocity_cm_s=40.0,
    hyperemic_peak_flow_velocity_cm_s=78.5
)
print("THRR Ratio:", res["transient_hyperemic_response_ratio"])
print("Autoregulatory Score:", res["autoregulatory_reserve_score"], "/ 100")
```
