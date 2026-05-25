from setuptools import setup


setup(
    name='si_crowd_nav',
    version='0.0.2',
    # Fork: targets Python 3.10 (ROS 2 Humble). Upstream pinned ==3.8.13;
    # the code runs on 3.10 (validated). Floor only.
    python_requires='>=3.8',
    packages=[
        'sicnav',
        'sicnav.policy',
        'sicnav.utils',
        'sicnav.configs',
        'sicnav_diffusion',
        'sicnav_diffusion.JMID',
        'sicnav_diffusion.policy',
        'sicnav_diffusion.utils',
        'sicnav_diffusion.configs',
        'crowd_sim_plus',
        'crowd_sim_plus.envs',
        'crowd_sim_plus.envs.policy',
        'crowd_sim_plus.envs.utils',
        'RL_nav'
    ],
    install_requires=[
        # Runtime deps, intentionally UNPINNED (floors only). This fork targets
        # Python 3.10 + NumPy 2 + torch 2.x + gym 0.26 (validated). Re-pinning to
        # the original requirements.txt versions (numpy==1.24.4, gym==0.21,
        # torch==1.13.1, ...) would fight the host env and break the validated
        # setup. NOTE: setuptools/pip/wheel were removed from here on purpose —
        # they are build tooling, never runtime install_requires (the old
        # 'pip==21' pin would downgrade pip in the target environment).
        'numpy',
        'scipy',
        'casadi',
        'gymnasium',
        'torch',
        'torchvision',
        'pandas',
        'einops',
        'h5py',
        'easydict',
        'ncls',
        'distinctipy',
        'tensorboardX',
    ],
    extras_require={
        # RL baselines only (the 'SB3' policy). Kept out of the core install
        # because stable-baselines3 drags gym/gymnasium pins that conflict with
        # the validated gym 0.26 + disable_env_checker setup.
        'rl': ['stable-baselines3'],
        'test': ['pylint', 'pytest'],
    },
)
