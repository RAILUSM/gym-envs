#Add these registration entries to the existing envs/__init__.py

register(
    id='RLBookGridWorld-v0',
    entry_point='gym-envs.toy_text:GridWorldEnv',
)

register(
    id='BlockDudes-v0',
    entry_point='gym-envs.two_agents:BlockDudes',
    max_episode_steps=200,
    reward_threshold=60.0,
)
