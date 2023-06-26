from dwave.system import DWaveSampler, EmbeddingComposite
sampler = EmbeddingComposite(DWaveSampler())

J = -1

spins_l = {('x1', 'x1'): 1, ('x2', 'x2'): 1, ('x3', 'x3'): 1, ('x4', 'x4'): 1}
spins_q = {('x1', 'x2'): J, ('x2', 'x3'): J, ('x3', 'x4'): J, ('x4', 'x1'): J}
sp = {**spins_l, **spins_q}
spins_samples = sampler.sample_ising(spins_l, spins_q, num_reads=500)

print(spins_samples)
