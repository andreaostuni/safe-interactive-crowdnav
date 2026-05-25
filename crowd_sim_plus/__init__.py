try:
    # Gymnasium renamed the package while keeping a compatible API.
    from gymnasium.envs.registration import register
except ImportError:  # pragma: no cover - fallback for legacy gym installs
    from gym.envs.registration import register

register(
    id='CrowdSimPlus-v0',
    entry_point='crowd_sim_plus.envs:CrowdSimPlus',
)

# JMID/MID is only needed for the diffusion human predictor. Guard so
# crowd_sim_plus (and everything that imports it, e.g. the campc / CVG acados
# paths) loads without the MID Python deps (ncls, distinctipy, einops, ...).
try:
    from sicnav_diffusion.JMID.MID import models  # noqa: F401  (registration side-effect)
except ImportError:
    pass